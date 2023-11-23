import abc

from app.data_models.prediction import Prediction


class BaseClassifier(abc.ABC):
    @abc.abstractmethod
    def predict(self, texts: list[str]) -> list[Prediction]:
        ...
