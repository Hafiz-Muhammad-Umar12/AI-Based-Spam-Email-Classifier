import os
import shutil
import pandas as pd
from fastapi import UploadFile, HTTPException
from app.core.config import settings

class FileHandler:
    @staticmethod
    async def save_upload(file: UploadFile) -> str:
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="Only CSV files are allowed.")
        
        file_path = os.path.join(settings.UPLOAD_DIR, file.filename)
        
        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Could not save file: {str(e)}")
            
        return file_path

    @staticmethod
    def load_dataset(filename: str) -> pd.DataFrame:
        file_path = os.path.join(settings.UPLOAD_DIR, filename)
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="Dataset file not found.")
        
        try:
            df = pd.read_csv(file_path)
            if 'text' not in df.columns or 'label' not in df.columns:
                raise HTTPException(status_code=400, detail="CSV must contain 'text' and 'label' columns.")
            return df
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading CSV: {str(e)}")

file_handler = FileHandler()
