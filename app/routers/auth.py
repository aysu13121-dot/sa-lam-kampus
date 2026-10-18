from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.schemas.auth import SignUpRequest, LoginRequest, TokenResponse, UserResponse
from app.database import db
from app.security import hash_password, verify_password, create_access_token, decode_access_token

router = APIRouter(prefix="/api/auth", tags=["Autentifikasiya"])
security = HTTPBearer(auto_error=False)

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Aktiv istifadəçini token əsasında əldə edir."""
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Giriş icazəsi yoxdur: Bearer Token tələb olunur."
        )
    token = credentials.credentials
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Keçərsiz və ya müddəti bitmiş token."
        )
    user_id = payload.get("id")
    user = db.find_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="İstifadəçi tapılmadı."
        )
    return user

@router.post("/signup", response_model=TokenResponse, status_code=status.HTTP_201_CREATED, summary="Yeni istifadəçi qeydiyyatı")
def signup(payload: SignUpRequest):
    """Yeni istifadəçi (tələbə və ya tibb heyəti) qeydiyyatdan keçirir və dərhal JWT token qaytarır."""
    existing_user = db.find_user_by_email(payload.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Bu email ünvanı ilə artıq qeydiyyat mövcuddur."
        )
    
    hashed_pwd = hash_password(payload.password)
    user = db.create_user(
        full_name=payload.full_name,
        email=payload.email,
        password_hash=hashed_pwd,
        role="student"
    )

    token = create_access_token({"id": user["id"], "email": user["email"], "role": user["role"]})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": user
    }

@router.post("/login", response_model=TokenResponse, summary="Sistemə daxil olmaq")
def login(payload: LoginRequest):
    """Mövcud istifadəçinin email və şifrəsini yoxlayır, uğurlu olduqda JWT qaytarır."""
    user = db.find_user_by_email(payload.email)
    if not user or not verify_password(payload.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email və ya şifrə yanlışdır."
        )

    token = create_access_token({"id": user["id"], "email": user["email"], "role": user["role"]})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": user
    }

@router.get("/me", response_model=UserResponse, summary="Cari daxil olmuş istifadəçi")
def get_me(current_user: dict = Depends(get_current_user)):
    """Token vasitəsilə cari daxil olmuş istifadəçinin profil məlumatlarını qaytarır."""
    return current_user
