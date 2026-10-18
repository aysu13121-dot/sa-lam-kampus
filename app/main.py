from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import auth, products, reviews, orders, analysis, health

app = FastAPI(
    title="Sağlam Kampus API",
    description="""
# 💊 Sağlam Kampus - Tibb Məntəqəsi və Ehtiyat İdarəetmə Sistemi

Sprint 1 - **Initial MVP Setup** çərçivəsində hazırlanmış Python (FastAPI) Backend REST API.

### 🌟 Əsas Xüsusiyyətlər:
* **Autentifikasiya:** Qeydiyyat (Sign Up), Giriş (Login) və JWT Token əsaslı qorunan endpoint-lər (`/api/auth/*`).
* **Kataloq & Ehtiyat:** Dərman və ləvazimatların ehtiyat statusu və kateqoriyalar (`/api/products`, `/api/categories`).
* **Rəylər (Feedback):** Tələbə və istifadəçi rəylərinin toplanması və orta reytinq (`/api/reviews`).
* **Ehtiyat Sifariş Siyahısı:** Tibb məntəqəsinin növbəti ehtiyat sifarişlərinin idarəsi (`/api/orders`).
* **Müalicə Analizi:** Sorğu və statistik göstəricilər (`/api/analysis`).
* **Canlı Test:** Bütün endpoint-lər bu Swagger UI səhifəsindən birbaşa test edilə bilər!
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware (Frontend inteqrasiyası üçün tam açıqdır)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router-lərin qoşulması
app.include_router(health.router)
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(reviews.router)
app.include_router(orders.router)
app.include_router(analysis.router)

@app.get("/", tags=["Kök Endpoint"])
def root():
    return {
        "message": "Sağlam Kampus REST API uğurla işləyir!",
        "documentation": "/docs",
        "redoc": "/redoc",
        "health_check": "/api/health"
    }
