import redis
from dotenv import load_dotenv
import os


load_dotenv()

redis_url = os.getenv("REDIS_URL")


def get_redis():
    if not redis_url:
        raise RuntimeError("REDIS_URL is not configured")
    return redis.from_url(redis_url, decode_responses=True)