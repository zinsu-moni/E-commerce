from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.models import Product, User, Cart
from app.db.database import get_db
from app.schema.schema import CartItem, CartItemResponse, CartItemUpdate
from app.api.auth import get_current_user
 
router = APIRouter()
 
 
@router.post("/add-to-cart", response_model=CartItemResponse)
async def add_to_cart(
    payload: CartItem,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    
    product = db.query(Product).filter(Product.id == payload.product_id).first()
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
 

    if product.stock < payload.quantity:
        raise HTTPException(
            status_code=400,
            detail=f"Only {product.stock} units available"
        )
 
    
    existing_item = db.query(Cart).filter(
        Cart.user_id == current_user.id,
        Cart.product_id == payload.product_id,
    ).first()
 
    if existing_item:
        new_quantity = existing_item.quantity + payload.quantity
        if product.stock < new_quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Only {product.stock} units available (you already have {existing_item.quantity} in cart)"
            )
        existing_item.quantity = new_quantity
        db.commit()
        db.refresh(existing_item)
        return CartItemResponse.model_validate(existing_item)
 
    
    cart_item = Cart(
        user_id=current_user.id,
        product_id=payload.product_id,
        quantity=payload.quantity
    )
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return CartItemResponse.model_validate(cart_item)
 
 
@router.get("/cart-user", response_model=List[CartItemResponse])
async def get_my_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    cart = db.query(Cart).filter(Cart.user_id == current_user.id).all()
    return [CartItemResponse.model_validate(item) for item in cart]
 
 
@router.get("/cart", response_model=List[CartItemResponse])
async def get_all_carts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )
    cart = db.query(Cart).all()
    return [CartItemResponse.model_validate(item) for item in cart]
 
 
@router.put("/update-cart/{cart_item_id}", response_model=CartItemResponse)
async def update_cart(
    cart_item_id: int,
    cart_item: CartItemUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    cart_item_db = db.query(Cart).filter(Cart.id == cart_item_id).first()
    if not cart_item_db:
        raise HTTPException(status_code=404, detail="Cart item not found")

    if cart_item_db.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Access denied")

    product = db.query(Product).filter(Product.id == cart_item_db.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.stock < cart_item.quantity:
        raise HTTPException(
            status_code=400,
            detail=f"Only {product.stock} units available"
        )

    cart_item_db.quantity = cart_item.quantity
    db.commit()

    db.refresh(cart_item_db)
    return CartItemResponse.from_orm(cart_item_db)
 
@router.delete("/delete-cart/{cart_item_id}")
async def delete_cart(
    cart_item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    cart_item_db = db.query(Cart).filter(Cart.id == cart_item_id).first()
    if not cart_item_db:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found"
        )
 
    if cart_item_db.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )
 
    db.delete(cart_item_db)
    db.commit()
    return {"detail": "Cart item deleted successfully"}
 
 
@router.delete("/clear-cart")
async def clear_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db.query(Cart).filter(Cart.user_id == current_user.id).delete()
    db.commit()
    return {"detail": "Cart cleared successfully"}
 