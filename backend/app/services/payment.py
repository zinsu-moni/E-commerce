from paybridge import PayBridge
from paybridge.gateway.router import RoutingStrategy
from dotenv import load_dotenv
import os

load_dotenv()

PROVIDER = os.getenv("PAYBRIDGE_PROVIDER", os.getenv("PAYSTACK_PROVIDER", "paystack")).lower()
PAYSTACK_SECRET = os.getenv("PAYSTACK_SECRET_KEY", "")
FLUTTERWAVE_SECRET = os.getenv("FLUTTERWAVE_SECRET_KEY", "")
ENABLE_MULTI = os.getenv("ENABLE_MULTI_GATEWAY", "false").lower() in ("1", "true", "yes")
STRATEGY = os.getenv("GATEWAY_STRATEGY", "PRIORITY").upper()
DEFAULT_CURRENCY = os.getenv("DEFAULT_CURRENCY", "NGN")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

# Lazily initialize the PayBridge client so the app can start without a master secret
bridge: PayBridge | None = None


def _resolve_strategy(value: str) -> RoutingStrategy:
    # Accept common aliases from env while mapping to SDK enum names.
    alias = {
        "LOAD": "LEAST_LOADED",
        "LEAST": "LEAST_LOADED",
        "ROUNDROBIN": "ROUND_ROBIN",
        "ROUND-ROBIN": "ROUND_ROBIN",
        "WEIGHT": "WEIGHTED",
    }
    normalized = alias.get(value.upper(), value.upper())
    try:
        return getattr(RoutingStrategy, normalized)
    except Exception:
        return RoutingStrategy.PRIORITY


def _init_bridge() -> PayBridge:
    global bridge
    if bridge is not None:
        return bridge

    available_providers = {
        "paystack": PAYSTACK_SECRET,
        "flutterwave": FLUTTERWAVE_SECRET,
    }
    configured = {name: secret for name, secret in available_providers.items() if secret}

    if ENABLE_MULTI and len(configured) >= 2:
        bridge = PayBridge()
        paystack_default = PROVIDER == "paystack"
        bridge.use_provider_by_name("paystack", secret_key=PAYSTACK_SECRET, set_as_default=paystack_default)
        bridge.use_provider_by_name("flutterwave", secret_key=FLUTTERWAVE_SECRET, set_as_default=not paystack_default)

        strat = _resolve_strategy(STRATEGY)

        bridge.enable_multi_gateway(strategy=strat, max_retries=2)
        return bridge

    if not configured:
        raise RuntimeError("Configure PAYSTACK_SECRET_KEY or FLUTTERWAVE_SECRET_KEY in .env")

    if len(configured) == 1:
        provider_name, secret_key = next(iter(configured.items()))
        bridge = PayBridge(provider=provider_name, secret_key=secret_key)
        return bridge

    if PROVIDER == "paystack":
        if not PAYSTACK_SECRET:
            raise RuntimeError("PAYBRIDGE_PROVIDER=paystack requires PAYSTACK_SECRET_KEY")
        bridge = PayBridge(provider="paystack", secret_key=PAYSTACK_SECRET)
        return bridge

    if PROVIDER == "flutterwave":
        if not FLUTTERWAVE_SECRET:
            raise RuntimeError("PAYBRIDGE_PROVIDER=flutterwave requires FLUTTERWAVE_SECRET_KEY")
        bridge = PayBridge(provider="flutterwave", secret_key=FLUTTERWAVE_SECRET)
        return bridge

    raise RuntimeError("Set PAYBRIDGE_PROVIDER to paystack or flutterwave")


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
