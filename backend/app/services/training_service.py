from app.agents.training_agent import training_agent
from app.services.preprocessing_service import preprocessing_service


class TrainingService:
    def __init__(self):
        self.agent = training_agent

    async def run_training(self, filename: str):
        df = await preprocessing_service.prepare_dataset(filename)
        metrics = self.agent.train(df)
        return metrics


# 🔥 THIS LINE WAS MISSING (CAUSE OF ERROR)
training_service = TrainingService()