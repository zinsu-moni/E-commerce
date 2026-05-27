from fastapi import APIRouter, Depends, HTTPException, Header, Request
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.api.auth import get_current_user
from app.models.models import Cart, Product, User
from app.schema.schema import CheckoutRequest
from app.services.payment import initialize_payment, verify_payment, get_bridge, FRONTEND_URL  # type: ignore
import time

router = APIRouter()


@router.post("/checkout")
async def checkout(
    payload: CheckoutRequest | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a payment session for the current user's cart."""
    cart_items = db.query(Cart).filter(Cart.user_id == current_user.id).all()
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total = 0.0
    for item in cart_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")
        total += float(product.price) * item.quantity

    reference = f"order_{current_user.id}_{int(time.time())}"
    callback_url = f"{FRONTEND_URL}/payments/callback"

    checkout_metadata = {
        "user_id": current_user.id,
        "full_name": payload.address.full_name if payload else current_user.full_name,
        "phone": payload.address.phone if payload else None,
        "address": payload.address.model_dump() if payload else None,
        "save_address": payload.save_address if payload else False,
        "delivery_notes": payload.delivery_notes if payload else None,
    }

    # Remove empty values before sending to the gateway.
    checkout_metadata = {key: value for key, value in checkout_metadata.items() if value is not None}

    try:
        payment = await initialize_payment(
            amount=total,
            email=current_user.email,
            reference=reference,
            callback_url=callback_url,
            metadata=checkout_metadata,
        )
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))

    return payment


@router.post("/verify")
async def verify(
    reference: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Verify a payment reference and fulfill the order on success."""
    try:
        verification = await verify_payment(reference)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))

    if getattr(verification, "status", None) != "successful":
        return {"verified": False, "verification": verification}

    # decrement stock and clear cart
    cart_items = db.query(Cart).filter(Cart.user_id == current_user.id).all()
    for item in cart_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if product:
            product.stock = max(0, product.stock - item.quantity)
            db.delete(item)
    db.commit()

    return {"verified": True, "verification": verification}


@router.post("/webhooks/paystack")
async def paystack_webhook(request: Request, x_paystack_signature: str = Header(...)):
    raw_body = await request.body()
    try:
        bridge = get_bridge()
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc))
    try:
        is_valid = bridge.get_provider().validate_webhook(raw_body.decode("utf-8"), x_paystack_signature)
    except Exception:
        is_valid = False

    if not is_valid:
        raise HTTPException(status_code=400, detail="Invalid webhook signature")

    event = await request.json()
    # Basic acknowledgement. Extend to handle events (charge.success, refund, etc.)
    return {"ok": True, "event": event.get("event")}
