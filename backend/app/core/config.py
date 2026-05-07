import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application configuration settings
    """

    PROJECT_NAME: str = "Intelligent AI-Powered Spam Email Detection System"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True

    # Base directory (project root)
    BASE_DIR: str = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    # Storage paths
    MODEL_DIR: str = os.path.join(BASE_DIR, "trained_models")
    UPLOAD_DIR: str = os.path.join(BASE_DIR, "uploads")
    DATASET_DIR: str = os.path.join(BASE_DIR, "datasets")

    # Model files
    MODEL_FILENAME: str = "spam_classifier_model.joblib"
    VECTORIZER_FILENAME: str = "tfidf_vectorizer.joblib"
    METRICS_FILENAME: str = "model_metrics.json"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()


# ✅ Ensure required directories exist at startup
def init_directories():
    paths = [
        settings.MODEL_DIR,
        settings.UPLOAD_DIR,
        settings.DATASET_DIR,
    ]

    for path in paths:
        os.makedirs(path, exist_ok=True)


init_directories()