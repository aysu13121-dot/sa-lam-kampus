from pydantic import BaseModel, Field

class OrderItem(BaseModel):
    product_id: int = Field(..., example=1)
    quantity: int = Field(..., ge=1, example=2)
    name: str = Field(default="", example="Paracetamol tabletləri")
    icon: str = Field(default="💊", example="💊")

class OrderCreate(BaseModel):
    items: list[OrderItem]
    ordered_by: str = Field(default="Məntəqə nümayəndəsi", example="Aysu Məmmədova")

class OrderResponse(BaseModel):
    id: str
    items: list[OrderItem]
    total_items: int
    status: str
    ordered_by: str
    created_at: str
