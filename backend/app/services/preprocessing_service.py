import pandas as pd
from app.agents.preprocessing_agent import preprocessing_agent
from app.utils.file_handler import file_handler

class PreprocessingService:
    def __init__(self):
        self.agent = preprocessing_agent

    async def prepare_dataset(self, filename: str) -> pd.DataFrame:
        """
        Load, clean and prepare the dataset for training.
        """
        df = file_handler.load_dataset(filename)
        df = self.agent.clean_dataset(df)
        return df

    def clean_text(self, text: str) -> str:
        return self.agent.clean_single_message(text)

preprocessing_service = PreprocessingService()
