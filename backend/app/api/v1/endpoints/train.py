from fastapi import APIRouter, HTTPException
from app.models.schemas import TrainingResponse
from app.services.training_service import training_service
from app.core.config import settings
from urllib.parse import unquote
import os

router = APIRouter()


@router.post("/train", response_model=TrainingResponse)
async def train_model(filename: str):
    """
    Train the spam classification model using uploaded dataset.
    """

    # 🔥 FIX 1: decode URL-encoded filename
    filename = unquote(filename)

    file_path = os.path.join(settings.UPLOAD_DIR, filename)

    # 🔥 FIX 2: safer file validation
    if not os.path.isfile(file_path):
        raise HTTPException(
            status_code=404,
            detail=f"Dataset file not found: {filename}. Please upload it first."
        )

    try:
        # 🔥 FIX 3: training call
        metrics = await training_service.run_training(filename)

        return {
            "message": "Model trained and evaluated successfully.",
            "metrics": metrics
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Training failed: {str(e)}"
        )