from passlib.context import CryptContext

pss_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def hash_password(password:str):
    return pss_context.hash(password)

def verify_password(plain, hashed):
    try:
        return pss_context.verify(plain, hashed)
    except Exception:
        return False