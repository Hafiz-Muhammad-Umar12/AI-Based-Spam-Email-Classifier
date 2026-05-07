from pydantic import BaseModel, Field
from typing import Dict, Optional, List

class PredictionRequest(BaseModel):
    message: str = Field(..., example="Congratulations! You won a lottery.")

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float

class UploadResponse(BaseModel):
    filename: str
    message: str
    status: str

class TrainingMetrics(BaseModel):
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    confusion_matrix: List[List[int]]

class TrainingResponse(BaseModel):
    message: str
    metrics: TrainingMetrics

class AnalyticsResponse(BaseModel):
    total_predictions: int
    spam_count: int
    ham_count: int
    model_accuracy: Optional[float]
    dataset_statistics: Dict[str, int]

class HealthCheck(BaseModel):
    status: str
    version: str
