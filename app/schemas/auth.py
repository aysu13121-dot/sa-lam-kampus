from pydantic import BaseModel, EmailStr, Field

class SignUpRequest(BaseModel):
    full_name: str = Field(..., example="Aysu Məmmədova", min_length=2)
    email: EmailStr = Field(..., example="aysu@saglamkampus.az")
    password: str = Field(..., example="kampus123", min_length=6)

class LoginRequest(BaseModel):
    email: EmailStr = Field(..., example="aysu@saglamkampus.az")
    password: str = Field(..., example="kampus123")

class UserResponse(BaseModel):
    id: str
    full_name: str
    email: str
    role: str
    created_at: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
