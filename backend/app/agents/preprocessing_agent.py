import pandas as pd
from app.utils.text_cleaner import text_cleaner

class PreprocessingAgent:
    def __init__(self):
        self.cleaner = text_cleaner

    def clean_dataset(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean the 'text' column of the dataframe.
        """
        df['cleaned_text'] = df['text'].apply(self.cleaner.clean_text)
        return df

    def clean_single_message(self, message: str) -> str:
        """
        Clean a single string message.
        """
        return self.cleaner.clean_text(message)

preprocessing_agent = PreprocessingAgent()
