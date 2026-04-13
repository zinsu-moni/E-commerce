from fastapi import FastAPI
from app.api import auth, product
from app.db.database import init_db
from app.models import models  # noqa: F401


app = FastAPI()

init_db()


app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])

app.include_router(product.router, prefix="/api/v1/products", tags=["products"])