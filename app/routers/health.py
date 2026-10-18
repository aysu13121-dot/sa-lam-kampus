from datetime import datetime
from fastapi import APIRouter
from app.config import settings

router = APIRouter(prefix="/api/health", tags=["Health Check"])

@router.get("", summary="Server sağlamlıq yoxlanışı")
def check_health():
    """Serverin və API xidmətlərinin aktivliyini yoxlayır."""
    return {
        "status": "UP",
        "app_name": settings.APP_NAME,
        "timestamp": datetime.utcnow().isoformat(),
        "environment": "development" if settings.DEBUG else "production"
    }
