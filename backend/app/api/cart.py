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
    cart_item: CartItem,
    db: Session =Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    pass

@router.get("/cart", response_model=List[CartItemResponse])
async def def_cart(
    db: Session =Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    pass

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