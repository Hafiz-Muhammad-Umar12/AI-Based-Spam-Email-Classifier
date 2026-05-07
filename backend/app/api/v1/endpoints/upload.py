from fastapi import APIRouter, UploadFile, File
from app.models.schemas import UploadResponse
from app.utils.file_handler import file_handler

router = APIRouter()

@router.post("/upload", response_model=UploadResponse)
async def upload_dataset(file: UploadFile = File(...)):
    """
    Upload a CSV dataset for training.
    Expected format: text,label
    """
    file_path = await file_handler.save_upload(file)
    return {
        "filename": file.filename,
        "message": "Dataset uploaded successfully.",
        "status": "success"
    }
