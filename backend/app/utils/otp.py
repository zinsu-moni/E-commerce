from app.db.cache import get_redis
import random
import json

def generate_otp() -> str:
    return str(random.randint(100000, 999999))


def store_otp(email: str, otp: str, ttl: int = 300):
    get_redis().setex(f"otp:{email}", ttl, otp)


def get_otp(email: str) -> str | None:
    return get_redis().get(f"otp:{email}")


def delete_otp(email: str):
    get_redis().delete(f"otp:{email}")


def store_pending_user(email: str, full_name: str, hashed_password: str, ttl: int = 300):
    payload = json.dumps({
        "full_name": full_name,
        "hashed_password": hashed_password,
    })
    get_redis().setex(f"pending_user:{email}", ttl, payload)


def get_pending_user(email: str) -> dict | None:
    payload = get_redis().get(f"pending_user:{email}")
    if not payload:
        return None
    return json.loads(payload)


def delete_pending_user(email: str):
    get_redis().delete(f"pending_user:{email}")
