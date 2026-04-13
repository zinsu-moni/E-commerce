import os
from fastapi import APIRouter, Body, Depends, Form, HTTPException, Request, Response, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.services.auth import (
    blacklist_token,
    create_acccess_token,
    get_token_ttl,
    oauth2_scheme,
    verify_access_token,
)
from app.models.models import Product, User
from app.db.database import get_db
from app.schema.schema import ProductCreate, ProductResponse, ProductUpdate
from app.api.auth import get_current_user
# from app.utils.email import


router = APIRouter()


@router.post("/upload-products", response_model=ProductResponse)
async def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Access denied")

    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock,
        category=product.category,
        image_url=product.image_url,
        image_public_id=product.image_public_id,
        images=product.images or [],
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return ProductResponse.model_validate(new_product)



@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.id == Product.id).first()

    if not Product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return products


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    payload: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Access denied")

    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    db_product.name = payload.name
    db_product.category = payload.category
    db_product.description = payload.description
    db_product.image_public_id = payload.image_public_id
    db_product.image_url = payload.image_url
    db_product.stock = payload.stock
    db_product.price = payload.price
    db_product.images = payload.images or []

    db.commit()
    db.refresh(db_product)
    return ProductResponse.model_validate(db_product)


@router.delete("/{product_id}")
def delete_product(product_id: int, db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not current_user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="Access Denied"
        )
    
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Not a product"
        )
    db.delete(product)
    db.commit()
