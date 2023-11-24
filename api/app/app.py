import pathlib

from fastapi import FastAPI

from app.classifier.tfidf import TfidfClassifier
from app.data_models.prediction import Prediction, Statistics
from app.statistics.stats_collector import StatisticsCollector
from app.statistics.stats_exporter import export_to_dict
from app.theme_mapping import THEME_TO_GROUP
from resources import RESOURCES_PATH


def enrich_theme_group(prediction: Prediction) -> None:
    if prediction.theme_group is None:
        prediction.theme_group = THEME_TO_GROUP.get(prediction.theme)


def build_app() -> FastAPI:
    app_ = FastAPI()

    data_path = pathlib.Path('data')
    tfidf_path = RESOURCES_PATH / 'baseline_tfidf.pt'
    classifier = TfidfClassifier(tfidf_path)
    stats_collector = StatisticsCollector(data_path / 'statistics.json')

    @app_.post('/predict', response_model=list[Prediction])
    async def predict_single(texts: list[str]) -> list[Prediction]:
        preds = classifier.predict(texts)
        for pred in preds:
            enrich_theme_group(pred)

        for pred in preds:
            stats_collector.collect(pred.text, pred)
        return preds

    @app_.post('/export_stats', response_model=Statistics)
    async def export_stats() -> dict:
        return export_to_dict(stats_collector)

    return app_


app = build_app()
