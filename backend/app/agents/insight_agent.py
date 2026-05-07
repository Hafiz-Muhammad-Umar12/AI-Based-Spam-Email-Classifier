from typing import Dict, Any

class InsightAgent:
    @staticmethod
    def generate_insights(metrics: Dict[str, Any]) -> str:
        accuracy = metrics.get('accuracy', 0)
        if accuracy > 0.9:
            return "The model is performing exceptionally well with high accuracy. It's ready for production use."
        elif accuracy > 0.7:
            return "The model has good performance, but there is room for improvement. Consider adding more diverse data."
        else:
            return "The model performance is currently low. Please check the dataset quality and ensure balanced classes."

    @staticmethod
    def summarize_dataset(stats: Dict[str, int]) -> str:
        total = stats.get('total', 0)
        spam = stats.get('spam', 0)
        ham = stats.get('ham', 0)
        return f"Dataset contains {total} emails, with {spam} spam and {ham} ham messages."

insight_agent = InsightAgent()
