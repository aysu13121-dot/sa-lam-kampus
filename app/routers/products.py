from fastapi import APIRouter, HTTPException, status, Depends, Query
from app.schemas.product import ProductResponse, CategoryResponse, ProductCreate, StockUpdate
from app.database import db
from app.routers.auth import get_current_user

router = APIRouter(prefix="/api", tags=["Tibb Məntəqəsi Kataloqu"])

@router.get("/categories", response_model=list[CategoryResponse], summary="Kateqoriyalar siyahısı")
def get_categories():
    """Tibb məntəqəsi kataloqundakı bütün kateqoriyaları (ikonları ilə) qaytarır."""
    return db.get_categories()

@router.get("/products", response_model=list[ProductResponse], summary="Məhsullar və ehtiyat statusu")
def get_products(
    category_id: int | None = Query(default=None, description="Kateqoriya ID (0 = Hamısı)"),
    search: str | None = Query(default=None, description="Məhsul adı və ya kateqoriya üzrə axtarış")
):
    """Bütün dərman və tibbi ləvazimatların siyahısını, onların ehtiyat və aylıq tələbat göstəricilərini qaytarır."""
    return db.get_products(category_id=category_id, search=search)

@router.get("/products/{product_id}", response_model=ProductResponse, summary="ID ilə tək məhsul")
def get_product_by_id(product_id: int):
    """Müəyyən bir məhsulun detallarını qaytarır."""
    prod = db.get_product_by_id(product_id)
    if not prod:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Məhsul tapılmadı.")
    return prod

@router.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED, summary="Yeni məhsul əlavə et (Admin)")
def add_product(payload: ProductCreate, current_user: dict = Depends(get_current_user)):
    """Kataloqa yeni məhsul əlavə edir (Autentifikasiya tələb olunur)."""
    return db.create_product(
        name=payload.name,
        icon=payload.icon,
        category_id=payload.category_id,
        stock=payload.stock,
        monthly_demand=payload.monthly_demand
    )

@router.patch("/products/{product_id}/stock", response_model=ProductResponse, summary="Ehtiyat miqdarını yenilə")
def update_stock(product_id: int, payload: StockUpdate, current_user: dict = Depends(get_current_user)):
    """Məhsulun mövcud ehtiyat sayını yeniləyir və statusu avtomatik yenidən hesablayır."""
    updated = db.update_stock(product_id, payload.stock)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Məhsul tapılmadı.")
    return updated
