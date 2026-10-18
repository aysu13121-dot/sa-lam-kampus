from pydantic import BaseModel, Field

class CategoryResponse(BaseModel):
    id: int
    name: str
    icon: str

class ProductResponse(BaseModel):
    id: int
    name: str
    icon: str
    category_id: int
    category_name: str
    stock: int
    monthly_demand: int
    status: str
    status_level: str
    meter_percent: int

class ProductCreate(BaseModel):
    name: str = Field(..., example="Paracetamol tabletləri")
    icon: str = Field(default="💊", example="💊")
    category_id: int = Field(default=1, example=1)
    stock: int = Field(default=40, ge=0, example=40)
    monthly_demand: int = Field(default=60, gt=0, example=60)

class StockUpdate(BaseModel):
    stock: int = Field(..., ge=0, example=50)
