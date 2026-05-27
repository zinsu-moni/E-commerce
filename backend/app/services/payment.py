from paybridge import PayBridge
from paybridge.gateway.router import RoutingStrategy
from dotenv import load_dotenv
import os

load_dotenv()

PROVIDER = os.getenv("PAYBRIDGE_PROVIDER", os.getenv("PAYSTACK_PROVIDER", "paystack"))
PAYSTACK_SECRET = os.getenv("PAYSTACK_SECRET_KEY", "")
FLUTTERWAVE_SECRET = os.getenv("FLUTTERWAVE_SECRET_KEY", "")
ENABLE_MULTI = os.getenv("ENABLE_MULTI_GATEWAY", "false").lower() in ("1", "true", "yes")
STRATEGY = os.getenv("GATEWAY_STRATEGY", "PRIORITY").upper()
DEFAULT_CURRENCY = os.getenv("DEFAULT_CURRENCY", "NGN")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

# Lazily initialize the PayBridge client so the app can start without a master secret
bridge: PayBridge | None = None


def _init_bridge() -> PayBridge:
    global bridge
    if bridge is not None:
        return bridge

    if not PAYSTACK_SECRET and not FLUTTERWAVE_SECRET:
        raise RuntimeError("Configure PAYSTACK_SECRET_KEY and/or FLUTTERWAVE_SECRET_KEY in .env")

    bridge = PayBridge()

    if PAYSTACK_SECRET:
        bridge.use_provider_by_name("paystack", secret_key=PAYSTACK_SECRET, set_as_default=True)
    if FLUTTERWAVE_SECRET:
        bridge.use_provider_by_name("flutterwave", secret_key=FLUTTERWAVE_SECRET)

    if ENABLE_MULTI and PAYSTACK_SECRET and FLUTTERWAVE_SECRET:
        try:
            strat = getattr(RoutingStrategy, STRATEGY)
        except Exception:
            strat = RoutingStrategy.PRIORITY

        bridge.enable_multi_gateway(strategy=strat, max_retries=2)

    return bridge


async def initialize_payment(*, amount: float, email: str, reference: str | None = None, callback_url: str | None = None, metadata: dict | None = None, currency: str | None = None):
    currency = (currency or DEFAULT_CURRENCY).upper()
    br = _init_bridge()
    return await br.initialize_payment(
        amount=amount,
        email=email,
        reference=reference,
        callback_url=callback_url,
        metadata=metadata or {},
        currency=currency,
    )


async def verify_payment(reference: str):
    br = _init_bridge()
    return await br.verify_payment(reference)


def get_bridge():
    return _init_bridge()
