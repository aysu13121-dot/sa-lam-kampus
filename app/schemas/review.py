from pydantic import BaseModel, Field

class ReviewCreate(BaseModel):
    author: str = Field(default="Anonim", example="Aysel K.")
    topic: str = Field(default="Ümumi", example="Tibb məntəqəsi ideyası")
    rating: int = Field(default=5, ge=1, le=5, example=5)
    comment: str = Field(..., min_length=2, max_length=500, example="Çox faydalı layihədir!")

class ReviewResponse(BaseModel):
    id: str
    author: str
    topic: str
    rating: int
    comment: str
    created_at: str

class ReviewListResponse(BaseModel):
    total: int
    average_rating: float
    reviews: list[ReviewResponse]
