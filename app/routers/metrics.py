from fastapi import APIRouter

router = APIRouter(prefix="/metrics", tags=["Metrics"])


@router.post("/calculate")
def calculate_transaction(unit_price: float, quantity: int, currency: str):
    total = unit_price * quantity

    return {
        "transaction_total": round(total, 2),
        "formatted_summary": f"Total amount is {total:.2f} {currency}"
    }


@router.get("/store/{store_id}")
def store_profile(store_id: str, filter_type: str = "all"):
    if store_id == "main-hub":
        performance_tier = "High Volume Profile"
    else:
        performance_tier = "Standard Volume Profile"

    return {
        "store_id": store_id,
        "active_filter": filter_type,
        "performance_tier": performance_tier
    }