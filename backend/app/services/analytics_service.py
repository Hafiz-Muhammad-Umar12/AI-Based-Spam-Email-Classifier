import os
import json
import pandas as pd
from app.core.config import settings
from app.agents.insight_agent import insight_agent

class AnalyticsService:
    def __init__(self):
        # In a real app, these would come from a database. 
        # For this demo, we'll simulate or read from files.
        self.stats = {
            "total_predictions": 0,
            "spam_count": 0,
            "ham_count": 0
        }

    def increment_stats(self, prediction: str):
        self.stats["total_predictions"] += 1
        if prediction == "spam":
            self.stats["spam_count"] += 1
        else:
            self.stats["ham_count"] += 1

    def get_analytics(self):
        metrics_path = os.path.join(settings.MODEL_DIR, settings.METRICS_FILENAME)
        model_accuracy = None
        if os.path.exists(metrics_path):
            with open(metrics_path, 'r') as f:
                metrics = json.load(f)
                model_accuracy = metrics.get('accuracy')

        # Simulate dataset stats from the last uploaded file if available
        dataset_stats = {"total": 0, "spam": 0, "ham": 0}
        uploads = os.listdir(settings.UPLOAD_DIR)
        if uploads:
            last_file = os.path.join(settings.UPLOAD_DIR, uploads[-1])
            try:
                df = pd.read_csv(last_file)
                dataset_stats["total"] = len(df)
                dataset_stats["spam"] = len(df[df['label'] == 'spam'])
                dataset_stats["ham"] = len(df[df['label'] == 'ham'])
            except:
                pass

        return {
            "total_predictions": self.stats["total_predictions"],
            "spam_count": self.stats["spam_count"],
            "ham_count": self.stats["ham_count"],
            "model_accuracy": model_accuracy,
            "dataset_statistics": dataset_stats,
            "ai_insight": insight_agent.generate_insights({"accuracy": model_accuracy}) if model_accuracy else "No model trained yet."
        }

analytics_service = AnalyticsService()
