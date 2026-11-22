from typing import Literal

from pydantic import BaseModel, Field


class OrderItem(BaseModel):
    name: str = Field(..., min_length=1, description="상품 이름")
    price: float = Field(..., gt=0, description="상품 단가 (양수)")
    quantity: int = Field(..., gt=0, description="수량 (1 이상)")


class OrderRequest(BaseModel):
    order_id: str = Field(..., min_length=3, description="주문 식별자")
    user_id: str = Field(..., min_length=3, description="사용자 식별자")
    items: list[OrderItem] = Field(..., min_length=1, description="주문 항목 목록")
    currency: Literal["KRW", "USD"] = Field(..., description="결제 통화")


class OrderResponse(BaseModel):
    order_id: str
    user_id: str
    total_amount: float
    currency: Literal["KRW", "USD"]
    status: Literal["PENDING", "CONFIRMED", "CANCELLED"]
