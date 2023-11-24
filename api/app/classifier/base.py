import abc

from app.data_models import Prediction


class BaseClassifier(abc.ABC):
    @abc.abstractmethod
    def predict(self, texts: list[str]) -> list[Prediction]:
        ...
