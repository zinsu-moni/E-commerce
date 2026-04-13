from app.db.cache import get_redis
import random
import json
import secrets

def generate_otp() -> str:
    return str(random.randint(100000, 999999))


def store_otp(email: str, otp: str, ttl: int = 300):
    get_redis().setex(f"otp:{email}", ttl, otp)


def get_otp(email: str) -> str | None:
    return get_redis().get(f"otp:{email}")


def delete_otp(email: str):
    get_redis().delete(f"otp:{email}")


def store_pending_user(email: str, full_name: str, hashed_password: str, role: str = "User", ttl: int = 300):
    payload = json.dumps({
        "full_name": full_name,
        "hashed_password": hashed_password,
        "role": role,
    })
    get_redis().setex(f"pending_user:{email}", ttl, payload)


def get_pending_user(email: str) -> dict | None:
    payload = get_redis().get(f"pending_user:{email}")
    if not payload:
        return None
    return json.loads(payload)


def delete_pending_user(email: str):
    get_redis().delete(f"pending_user:{email}")


def generate_reset_token() -> str:
    return secrets.token_urlsafe(32)

def store_reset_token(email: str, token: str, ttl: int = 900): 
    get_redis().setex(f"password_reset:{token}", ttl, email)

def get_reset_token(token: str) -> str | None:
    return get_redis().get(f"password_reset:{token}")

def delete_reset_token(token: str):
    get_redis().delete(f"password_reset:{token}")