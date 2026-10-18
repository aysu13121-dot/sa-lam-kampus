from fastapi import APIRouter, status, HTTPException
from app.schemas.order import OrderCreate, OrderResponse
from app.database import db

router = APIRouter(prefix="/api/orders", tags=["Ehtiyat Sifariş Siyahısı (Cart/Orders)"])

@router.post("", response_model=OrderResponse, status_code=status.HTTP_201_CREATED, summary="Ehtiyat sifarişi göndər")
def create_order(payload: OrderCreate):
    """Məntəqənin növbəti ehtiyat sifarişi üçün seçilmiş məhsulların siyahısını qeydə alır."""
    if not payload.items:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Sifariş siyahısı boş ola bilməz."
        )
    
    # Məhsul adlarını və ikonlarını doldururuq əgər boşdursa
    formatted_items = []
    for item in payload.items:
        prod = db.get_product_by_id(item.product_id)
        formatted_items.append({
            "product_id": item.product_id,
            "quantity": item.quantity,
            "name": prod["name"] if prod else item.name,
            "icon": prod["icon"] if prod else item.icon
        })

    new_order = db.create_order(
        items=formatted_items,
        ordered_by=payload.ordered_by
    )
    return new_order

@router.get("", response_model=list[OrderResponse], summary="Bütün ehtiyat sifarişləri")
def get_orders():
    """Planlaşdırılmış bütün ehtiyat sifarişlərinin siyahısını qaytarır."""
    return db.get_orders()
