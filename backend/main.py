from fastapi import FastAPI
from app.api import auth, product, cart
from app.db.database import init_db
from app.models import models  # noqa: F401


app = FastAPI()

init_db()


app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])

app.include_router(product.router, prefix="/api/v1/products", tags=["products"])

app.include_router(cart.router, prefix="/api/v1/cart", tags=["cart"])