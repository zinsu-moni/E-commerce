import os
from fastapi import APIRouter, Body, Depends, Form, HTTPException, Request, Response, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError
from app.services.auth import (
    blacklist_token,
    create_acccess_token,
    get_token_ttl,
    oauth2_scheme,
    verify_access_token,
)
from app.models.models import User
from app.db.database import get_db
from app.models.models import User
from app.schema.schema import AdminLogin, CreateUser, ForgotPassword, ResetPassword, UserLogin, VerifyOTP
from app.utils.email import send_otp_email, send_password_reset_email, welcome_message, password_changed_successfully
from app.utils.otp import (
    delete_otp,
    delete_pending_user,
    delete_reset_token,
    generate_otp,
    generate_reset_token,
    get_otp,
    get_pending_user,
    get_reset_token,
    store_otp,
    store_pending_user,
    store_reset_token,
)
from app.utils.utils import hash_password, verify_password

router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token", auto_error=False)



def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = verify_access_token(token)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user



@router.post("/register")
async def register_user(user: CreateUser, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    otp = generate_otp()
    try:
        store_otp(user.email, otp)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="OTP service is unavailable",
        )

    try:
        send_otp_email(user.email, otp)
    except Exception:
        delete_otp(user.email)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send OTP email",
        )

    hashed_password = hash_password(user.password)
    store_pending_user(user.email, user.full_name, hashed_password, user.role)
    


    return {
        "message": "OTP sent to email. Verify OTP to complete registration.",
        "email": user.email,
    }


@router.post("/send-otp")
def send_otp(email: str):
    otp = generate_otp()
    try:
        store_otp(email, otp)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="OTP service is unavailable",
        )
    try:
        send_otp_email(email, otp)
    except Exception:
        delete_otp(email)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send OTP email",
        )
    return {"message": "OTP sent", "email": email}


@router.post("/verify-otp")
def verify_otp(payload: VerifyOTP, db: Session = Depends(get_db)):
    stored_otp = get_otp(payload.email)
    pending_user = get_pending_user(payload.email)

    if not stored_otp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="OTP expired or not found. Please request a new OTP.",
        )

    if stored_otp != payload.otp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid OTP",
        )

    if not pending_user:
        existing_user = db.query(User).filter(User.email == payload.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User is already registered. Please login.",
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No pending registration found. Start with /api/v1/auth/register.",
        )

    new_user = User(
        username=payload.email,
        full_name=pending_user["full_name"],
        email=payload.email,
        password=pending_user["hashed_password"],
        role=pending_user.get("role", "User"),
    )

    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User registration failed due to a duplicate value",
        )

    delete_otp(payload.email)
    delete_pending_user(payload.email)
    welcome_message(new_user.email)

    return {
        "message": "OTP verified and user registered successfully",
        "user": {
            "id": new_user.id,
            "full_name": new_user.full_name,
            "email": new_user.email,
            "role": new_user.role,
        },
    }

@router.post("/token", include_in_schema=False)
def login_for_swagger(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.email == form_data.username).first()
    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    access_token = create_acccess_token({"user_id": db_user.id})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post("/login")
async def login(payload: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == payload.email).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid credentials"
        )
    if not verify_password(payload.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid credentials"
        )
    access_token = create_acccess_token({"user_id": db_user.id})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": db_user.id,
            "full_name": db_user.full_name,
            "email": db_user.email,
            "role": db_user.role,
        }
    }


@router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)):
    try:
        ttl = get_token_ttl(token)
        if ttl:
            blacklist_token(token, ttl)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    return {"message": "Logged out successfully"}



@router.post("/forgot-password")
async def forgot_password(payload: ForgotPassword, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()

    if not user:
        return {"message": "If this email is registered, a reset link has been sent."}

    token = generate_reset_token()
    store_reset_token(payload.email, token)
    reset_link =f"{os.getenv('FRONTEND_URL')}/reset-password?token={token}"

    try:
        send_password_reset_email(payload.email, reset_link)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send reset email"
        )

    return {"message": "If this email is registered, a reset link has been sent."}


@router.post("/reset-password")
async def reset_password(payload: ResetPassword, db: Session = Depends(get_db)):
    email = get_reset_token(payload.token)

    if not email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Reset link is invalid or has expired"
        )

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    user.password = hash_password(payload.new_password)
    db.commit()

    delete_reset_token(payload.token)

    return {"message": "Password reset successful. You can now log in."}

@router.post("/change-password")
async def change_password(
    current_password: str = Body(...),
    new_password: str = Body(...),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not verify_password(current_password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect"
        )

    user.password = hash_password(new_password)
    db.commit()
    password_changed_successfully(user.email)

    return {"message": "Password changed successfully."}


@router.post("/admin/login")
def login_admin(admin: AdminLogin, request: Request, response: Response, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == admin.email).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    if db_user.is_admin != 1 and db_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    if not verify_password(admin.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    access_token = create_acccess_token({"user_id": db_user.id})

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite="lax",
        secure=False,
        max_age=60 * 60 * 24 * 7,
        path="/"
    )
    

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": db_user.id,
            "full_name": db_user.full_name,
            "email": db_user.email,
            "role": db_user.role,
            "is_admin": db_user.is_admin,
        },
    }
    