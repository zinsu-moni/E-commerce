from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.auth.auth import create_acccess_token
from app.db.database import get_db
from app.models.models import User
from app.schema.schema import CreateUser, UserLogin, VerifyOTP
from app.utils.email import send_otp_email
from app.utils.otp import (
    delete_otp,
    delete_pending_user,
    generate_otp,
    get_otp,
    get_pending_user,
    store_otp,
    store_pending_user,
)
from app.utils.utils import hash_password, verify_password

router = APIRouter()


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
    store_pending_user(user.email, user.full_name, hashed_password)

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

    return {
        "message": "OTP verified and user registered successfully",
        "user": {
            "id": new_user.id,
            "full_name": new_user.full_name,
            "email": new_user.email,
        },
    }


@router.post("/login")
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not verify_password(user.password, existing_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_acccess_token({"user_id": existing_user.id})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": existing_user.id,
            "full_name": existing_user.full_name,
            "email": existing_user.email,
        },
    }

@router.post("/logout")
def logout_user():
    pass
    return {"message": "Successfully logged out"}


