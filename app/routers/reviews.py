from fastapi import APIRouter, status
from app.schemas.review import ReviewCreate, ReviewResponse, ReviewListResponse
from app.database import db

router = APIRouter(prefix="/api/reviews", tags=["Rəy və Təkliflər (Feedback)"])

@router.get("", response_model=ReviewListResponse, summary="Bütün rəylər və orta reytinq")
def get_all_reviews():
    """İstifadəçilər və tələbələr tərəfindən göndərilmiş bütün rəyləri, ümumi sayı və orta reytinqi qaytarır."""
    reviews = db.get_reviews()
    total = len(reviews)
    avg = round(sum(r["rating"] for r in reviews) / total, 1) if total > 0 else 0.0
    return {
        "total": total,
        "average_rating": avg,
        "reviews": reviews
    }

@router.post("", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED, summary="Yeni rəy göndər")
def submit_review(payload: ReviewCreate):
    """Sayt və tibb məntəqəsi haqqında yeni rəy və reytinq əlavə edir (Anonim və ya ad ilə)."""
    return db.create_review(
        author=payload.author,
        topic=payload.topic,
        rating=payload.rating,
        comment=payload.comment
    )
