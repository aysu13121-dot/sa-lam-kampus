from fastapi import APIRouter
from app.schemas.analysis import AnalysisResponse
from app.database import db

router = APIRouter(prefix="/api/analysis", tags=["Müalicə Analizi və Statistika"])

@router.get("", response_model=AnalysisResponse, summary="Müalicə nəticələrinin analizi")
def get_treatment_analysis():
    """Sorğu nəticələrinə əsasən xəstəliklər, yaş qrupları və nəticələr üzrə analitik məlumatları təqdim edir."""
    results = db.get_analysis()
    total_samples = sum(item["sample_size"] for item in results)
    return {
        "title": "Müalicə nəticələrinin analizi",
        "description": "Anonim sorğu və təcrübə məlumatlarına əsaslanan qruplar üzrə sağalma və yan təsir statistikası.",
        "total_samples": total_samples,
        "results": results
    }
