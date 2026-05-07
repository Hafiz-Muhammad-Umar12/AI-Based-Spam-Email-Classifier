from app.agents.prediction_agent import prediction_agent
from app.services.preprocessing_service import preprocessing_service

class PredictionService:
    def __init__(self):
        self.agent = prediction_agent

    async def predict_message(self, message: str):
        """
        Prediction pipeline: Preprocess -> Predict
        """
        # Reload model if it was just trained (simple mechanism)
        self.agent.load_model()
        
        cleaned_text = preprocessing_service.clean_text(message)
        result = self.agent.predict(cleaned_text)
        return result

prediction_service = PredictionService()
