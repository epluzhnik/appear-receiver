from fastapi import FastAPI

from app.classifier.tfidf import TfidfClassifier
from app.data_models.prediction import Prediction
from app.theme_mapping import THEME_TO_GROUP
from resources import RESOURCES_PATH


def enrich_theme_group(prediction: Prediction) -> None:
    if prediction.theme_group is None:
        prediction.theme_group = THEME_TO_GROUP.get(prediction.theme)


def build_app() -> FastAPI:
    app_ = FastAPI()

    tfidf_path = RESOURCES_PATH / 'baseline_tfidf.pt'
    classifier = TfidfClassifier(tfidf_path)

    @app_.post('/predict', response_model=list[Prediction])
    async def predict_single(texts: list[str]) -> list[Prediction]:
        preds = classifier.predict(texts)
        for pred in preds:
            enrich_theme_group(pred)

        return preds

    return app_


app = build_app()
