from src.domain.models import OrderItem, OrderRequest
from src.services.order_service import OrderService


def test_calculate_total():
    service = OrderService()
    items = [
        OrderItem(name="Item A", price=10.50, quantity=2),
        OrderItem(name="Item B", price=5.25, quantity=4),
    ]
    # 21.00 + 21.00 = 42.00
    assert service.calculate_total(items) == 42.00


def test_process_order_success():
    service = OrderService()
    req = OrderRequest(
        order_id="ORD-999",
        user_id="vip_user",
        items=[
            OrderItem(name="Enterprise License", price=100.0, quantity=2),
        ],
        currency="KRW",
    )
    res = service.process_order(req)
    assert res.order_id == "ORD-999"
    assert res.user_id == "vip_user"
    assert res.total_amount == 200.0
    assert res.currency == "KRW"
    assert res.status == "CONFIRMED"
