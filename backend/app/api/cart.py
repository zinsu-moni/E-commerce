import os
from typing import List
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
from app.models.models import Product, User, Cart
from app.db.database import get_db
from app.schema.schema import CartItem, CartItemResponse,CartItemUpdate
from app.api.auth import get_current_user


router = APIRouter()


@router.post("/add-to-cart", response_model=CartItemResponse)
async def add_to_cart(
    payload: CartItem,
    db: Session =Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == payload.product_id).first()
 
    if not product:
        raise HTTPException(
            status_code=403,
            detail="Not in product"
        )
    
    if product.stock < payload.quantity:
        raise HTTPException(
            status_code=401,
            detail="insuffient product"
        )
    exiting_item = db.query(Cart).filter(
        Cart.user_id == current_user.id,
        Cart.product_id == payload.product_id,
    ).first()

    if exiting_item:
        exiting_item.quantity += payload.quantity
        db.commit()
        db.refresh(exiting_item)
        return exiting_item
    
    
    cart_item = Cart(
        user_id=current_user.id,
        product_id=payload.product_id,
        quantity=payload.quantity
    )
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item




@router.get("/cart-user", response_model=List[CartItemResponse])
async def def_cart(
    db: Session =Depends(get_db),
    current_user: User = Depends(get_current_user)
):
     cart = db.query(Cart).filter(Cart.user_id == current_user.id).all()
     return cart

@router.get("/cart", response_model=List[CartItemResponse])
async def def_cart(
    db: Session =Depends(get_db),
    current_user: User = Depends(get_current_user)
):
     if not current_user.is_admin:
         raise HTTPException(
             status_code=403,
             detail="Access denied"
         )
     cart = db.query(Cart).all()
     return cart

@router.put("/update-cart/{cart_item_id}", response_model=CartItemResponse)
async def update_cart(
    cart_item_id: int,
    cart_item: CartItemUpdate,
    db: Session =Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    pass

@router.delete("/delete-cart/{cart_item_id}")
async def delete_cart(
    cart_item_id: int,
    db: Session =Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    pass