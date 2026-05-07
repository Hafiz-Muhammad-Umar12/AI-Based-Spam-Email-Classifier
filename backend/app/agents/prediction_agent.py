import os
import joblib
from app.core.config import settings
from fastapi import HTTPException

class PredictionAgent:
    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.load_model()

    def load_model(self):
        model_path = os.path.join(settings.MODEL_DIR, settings.MODEL_FILENAME)
        vec_path = os.path.join(settings.MODEL_DIR, settings.VECTORIZER_FILENAME)
        
        if os.path.exists(model_path) and os.path.exists(vec_path):
            self.model = joblib.load(model_path)
            self.vectorizer = joblib.load(vec_path)

    def predict(self, cleaned_text: str):
        if not self.model or not self.vectorizer:
            raise HTTPException(status_code=400, detail="Model not trained yet.")
        
        vectorized_text = self.vectorizer.transform([cleaned_text])
        prediction_idx = self.model.predict(vectorized_text)[0]
        confidence = self.model.predict_proba(vectorized_text).max()
        
        return {
            "prediction": str(prediction_idx),
            "confidence": float(confidence)
        }

prediction_agent = PredictionAgent()
