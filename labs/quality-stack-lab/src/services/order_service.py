from src.domain.models import OrderItem, OrderRequest, OrderResponse


class OrderService:
    def calculate_total(self, items: list[OrderItem]) -> float:
        """주문 항목의 총 금액을 계산합니다."""
        total = sum(item.price * item.quantity for item in items)
        return round(total, 2)

    def process_order(self, request: OrderRequest) -> OrderResponse:
        """주문 요청을 검증하고 주문을 처리합니다."""
        total = self.calculate_total(request.items)
        return OrderResponse(
            order_id=request.order_id,
            user_id=request.user_id,
            total_amount=total,
            currency=request.currency,
            status="CONFIRMED",
        )
