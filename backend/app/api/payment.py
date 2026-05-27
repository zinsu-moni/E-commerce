from fastapi import APIRouter, Depends, HTTPException, Header, Request
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.api.auth import get_current_user
from app.models.models import Cart, Product, User, Order, OrderItem
from app.schema.schema import CheckoutRequest
from app.services.payment import initialize_payment, verify_payment, get_bridge, FRONTEND_URL, DEFAULT_CURRENCY
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
        # persist an order record before initializing payment
        order = Order(
            user_id=current_user.id,
            reference=reference,
            status="pending",
            amount=total,
            currency=DEFAULT_CURRENCY,
            shipping_address=checkout_metadata.get("address"),
            delivery_notes=checkout_metadata.get("delivery_notes"),
            save_address=checkout_metadata.get("save_address", False),
        )
        db.add(order)
        db.flush()

        for item in cart_items:
            product = db.query(Product).filter(Product.id == item.product_id).first()
            if not product:
                raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")
            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=item.quantity,
                unit_price=float(product.price),
            )
            db.add(order_item)

        db.commit()

        payment = await initialize_payment(
            amount=total,
            email=current_user.email,
            reference=reference,
            callback_url=callback_url,
            metadata={**checkout_metadata, "order_id": order.id},
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

    # find associated order and mark successful, decrement stock, clear cart
    order = db.query(Order).filter(Order.reference == reference).first()
    if order:
        # idempotent: don't reprocess successful orders
        if order.status == "successful":
            return {"verified": True, "verification": verification}

        # store provider info if available
        order.status = "successful"
        order.provider = getattr(verification, "provider", None) or order.provider
        order.provider_transaction_id = getattr(verification, "transaction_id", None) or getattr(verification, "reference", None)

        # decrement stock for items on the order
        for oi in order.items:
            product = db.query(Product).filter(Product.id == oi.product_id).first()
            if product:
                product.stock = max(0, product.stock - oi.quantity)

        # remove cart items for this user
        db.query(Cart).filter(Cart.user_id == current_user.id).delete()
        db.commit()

        return {"verified": True, "verification": verification, "order_id": order.id}

    # fallback: no order found — preserve previous behavior
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
