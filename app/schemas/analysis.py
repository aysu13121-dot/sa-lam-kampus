from pydantic import BaseModel

class AnalysisItem(BaseModel):
    disease: str
    patient_group: str
    sample_size: int
    healed_percent: int
    improved_percent: int
    side_effect_percent: int
    summary: str

class AnalysisResponse(BaseModel):
    title: str
    description: str
    total_samples: int
    results: list[AnalysisItem]
