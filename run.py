import uvicorn
from app.config import settings

if __name__ == "__main__":
    print("==================================================================")
    print("💊 Sağlam Kampus - FastAPI Backend Server işə salınır...")
    print(f"🌐 Server:        http://127.0.0.1:{settings.PORT}")
    print(f"📄 Swagger UI:    http://127.0.0.1:{settings.PORT}/docs")
    print(f"📚 ReDoc Docs:    http://127.0.0.1:{settings.PORT}/redoc")
    print("==================================================================")
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
