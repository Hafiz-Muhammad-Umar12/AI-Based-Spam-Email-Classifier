import os
import joblib
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from app.core.config import settings

class TrainingAgent:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000)
        self.models = {
            'logistic_regression': LogisticRegression(),
            'naive_bayes': MultinomialNB()
        }

    def train(self, df: pd.DataFrame):
        X = df['cleaned_text']
        y = df['label']

        # Vectorization
        X_tfidf = self.vectorizer.fit_transform(X)

        # Train/Test Split
        X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

        # We will use Naive Bayes as the primary model for now, but could be configurable
        model = self.models['naive_bayes']
        model.fit(X_train, y_train)

        # Evaluation
        y_pred = model.predict(X_test)
        
        metrics = {
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "precision": float(precision_score(y_test, y_pred, pos_label='spam', average='binary')),
            "recall": float(recall_score(y_test, y_pred, pos_label='spam', average='binary')),
            "f1_score": float(f1_score(y_test, y_pred, pos_label='spam', average='binary')),
            "confusion_matrix": confusion_matrix(y_test, y_pred).tolist()
        }

        # Save model, vectorizer and metrics
        joblib.dump(model, os.path.join(settings.MODEL_DIR, settings.MODEL_FILENAME))
        joblib.dump(self.vectorizer, os.path.join(settings.MODEL_DIR, settings.VECTORIZER_FILENAME))
        
        with open(os.path.join(settings.MODEL_DIR, settings.METRICS_FILENAME), 'w') as f:
            json.dump(metrics, f)

        return metrics

training_agent = TrainingAgent()
