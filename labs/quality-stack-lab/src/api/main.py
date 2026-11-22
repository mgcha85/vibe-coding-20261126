import sys

from src.domain.models import OrderItem, OrderRequest
from src.services.order_service import OrderService


def run_demo() -> None:
    service = OrderService()
    req = OrderRequest(
        order_id="ORD-2026-001",
        user_id="user_vibe",
        items=[
            OrderItem(name="AI Coding Assistant Subscription", price=29.99, quantity=2),
            OrderItem(name="GPU Cloud Tokens (1M)", price=15.00, quantity=1),
        ],
        currency="USD",
    )
    res = service.process_order(req)
    print(
        f"✅ 주문 처리 성공: {res.order_id} | "
        f"총액: {res.total_amount} {res.currency} | "
        f"상태: {res.status}"
    )


if __name__ == "__main__":
    run_demo()
    sys.exit(0)
