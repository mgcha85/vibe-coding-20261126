import pytest
from pydantic import ValidationError

from src.domain.models import OrderItem, OrderRequest


def test_order_item_validation_success():
    item = OrderItem(name="Token Pack", price=10.5, quantity=3)
    assert item.name == "Token Pack"
    assert item.price == 10.5
    assert item.quantity == 3


def test_order_item_negative_price_fails():
    with pytest.raises(ValidationError) as exc_info:
        OrderItem(name="Invalid Pack", price=-5.0, quantity=1)
    errors = exc_info.value.errors()
    assert any("greater than 0" in e["msg"] for e in errors)


def test_order_item_zero_quantity_fails():
    with pytest.raises(ValidationError):
        OrderItem(name="Zero Quantity", price=10.0, quantity=0)


def test_order_request_invalid_currency_fails():
    with pytest.raises(ValidationError) as exc_info:
        OrderRequest(
            order_id="ORD-001",
            user_id="user-123",
            items=[OrderItem(name="Item", price=10.0, quantity=1)],
            currency="JPY",  # pyright: ignore[reportArgumentType]
        )
    assert "Input should be 'KRW' or 'USD'" in str(exc_info.value)


def test_order_request_empty_items_fails():
    with pytest.raises(ValidationError):
        OrderRequest(
            order_id="ORD-001",
            user_id="user-123",
            items=[],
            currency="KRW",
        )
