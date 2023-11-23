import pathlib

import joblib
import sklearn.pipeline

from app.classifier.base import BaseClassifier
from app.data_models.prediction import Prediction


class TfidfClassifier(BaseClassifier):
    def __init__(self, pipeline_path: pathlib.Path) -> None:
        self._pipeline: sklearn.pipeline.Pipeline = joblib.load(str(pipeline_path))

    def predict(self, texts: list[str]) -> list[Prediction]:
        raw_predictions = self._pipeline.predict(texts)
        return [Prediction(theme=pred) for pred in raw_predictions]
