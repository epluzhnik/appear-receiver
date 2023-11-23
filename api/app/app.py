from fastapi import FastAPI

from app.classifier.tfidf import TfidfClassifier
from app.data_models.prediction import Prediction
from resources import RESOURCES_PATH


def build_app() -> FastAPI:
    app_ = FastAPI()

    tfidf_path = RESOURCES_PATH / 'baseline_tfidf.pt'
    classifier = TfidfClassifier(tfidf_path)

    @app_.post('/predict', response_model=Prediction)
    async def predict_single(texts: list[str]) -> list[Prediction]:
        return classifier.predict(texts)

    return app_


app = build_app()
