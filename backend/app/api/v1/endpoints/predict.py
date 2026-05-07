from fastapi import APIRouter, HTTPException
from app.models.schemas import PredictionRequest, PredictionResponse
from app.services.prediction_service import prediction_service
from app.services.analytics_service import analytics_service

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict_spam(request: PredictionRequest):
    """
    Predict whether a given email message is spam or ham.
    """
    try:
        result = await prediction_service.predict_message(request.message)
        
        # Track analytics
        analytics_service.increment_stats(result["prediction"])
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
