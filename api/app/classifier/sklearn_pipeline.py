import pathlib

import joblib
import numpy as np
import sklearn.pipeline

from app.classifier.base import BaseClassifier
from app.data_models import Prediction


class MultiPipelineClassifier(BaseClassifier):
    def __init__(
            self,
            theme_path: pathlib.Path,
            executor_path: pathlib.Path,
            theme_threshold: float = 0.3,
            executor_threshold: float = 0.5,
    ) -> None:
        self._theme_pipeline: sklearn.pipeline.Pipeline = joblib.load(str(theme_path))
        self._executor_pipeline: sklearn.pipeline.Pipeline = joblib.load(str(executor_path))
        self.theme_threshold: float = theme_threshold
        self.executor_threshold: float = executor_threshold

    def predict(self, texts: list[str]) -> list[Prediction]:
        theme_probas = self._theme_pipeline.predict_proba(texts)
        executor_probas = self._executor_pipeline.predict_proba(texts)
        return [
            self._make_prediction(theme_proba, executor_proba) for theme_proba, executor_proba in
            zip(theme_probas, executor_probas)
        ]

    def _make_prediction(self, theme_proba, executor_proba) -> Prediction:
        theme_label = np.argmax(theme_proba)
        if theme_proba[theme_label] < self.theme_threshold:
            theme_label = None
        else:
            theme_label = self._theme_pipeline.classes_[theme_label]
        executor_label = np.argmax(executor_proba)
        if executor_proba[executor_label] < self.executor_threshold:
            executor_label = None
        else:
            executor_label = self._executor_pipeline.classes_[executor_label]

        return Prediction(
            theme=theme_label,
            executor=executor_label,
        )
