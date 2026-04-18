from jose import JWTError, jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer

from app.db.cache import get_redis

load_dotenv()

secret_key = os.getenv("SECRET_KEY", "your-super-secret-key-change-in-production-12345")
algorithm = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))  
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def create_acccess_token(data: dict):
    encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    encode.update({"exp": expire})
    return jwt.encode(encode, secret_key, algorithm=algorithm)


def verify_access_token(token: str | None):
    if not secret_key or not algorithm:
        return None
    if not token:
        return None
    if is_token_blacklisted(token):
        return None
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        user_id: int = payload.get("user_id")
        if user_id is None:
            return None
        return user_id
    except (JWTError, AttributeError, TypeError):
        return None


def is_token_blacklisted(token: str | None) -> bool:
    if not token:
        return False
    try:
        return get_redis().exists(f"blacklist:{token}") == 1
    except Exception:
        return False


def blacklist_token(token: str, ttl: int):
    if ttl <= 0:
        return
    get_redis().setex(f"blacklist:{token}", ttl, "1")


def get_token_ttl(token: str | None) -> int | None:
    if not token:
        return None
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
    except (JWTError, AttributeError, TypeError):
        return None

    exp = payload.get("exp")
    if exp is None:
        return None
    ttl = int(exp) - int(datetime.utcnow().timestamp())
    return ttl if ttl > 0 else None