import pathlib
from typing import Optional

from fastapi import FastAPI

from app.classifier.sklearn_pipeline import MultiPipelineClassifier
from app.data_models import PredictionResponse, Statistics, Prediction
from app.incidents.tracker import GroupIncidentTracker
from app.mappings import THEME_TO_GROUP, THEME_TO_THEME
from app.statistics.stats_collector import StatisticsCollector
from app.statistics.stats_exporter import export_to_dict
from resources import RESOURCES_PATH


def get_theme_group(prediction: Prediction) -> Optional[str]:
    if prediction.theme_group is None:
        return THEME_TO_GROUP.get(prediction.theme)
    return prediction.theme_group


def build_app() -> FastAPI:
    app_ = FastAPI()

    data_path = pathlib.Path('data')
    theme_classifier_path = RESOURCES_PATH / 'theme_tfidf_baseline.pt'
    executor_classifier_path = RESOURCES_PATH / 'executor_tfidf_baseline.pt'
    classifier = MultiPipelineClassifier(
        theme_classifier_path,
        executor_classifier_path,
    )
    stats_collector = StatisticsCollector(data_path / 'statistics.json')
    incident_tracker = GroupIncidentTracker()

    @app_.post('/predict', response_model=list[PredictionResponse])
    async def predict_single(texts: list[str]) -> list[PredictionResponse]:
        preds: list[Prediction] = classifier.predict(texts)
        for pred in preds:
            pred.theme_group = get_theme_group(pred)
            pred.theme = THEME_TO_THEME.get(pred.theme, pred.theme)

        for text, pred in zip(texts, preds):
            stats_collector.collect(text, pred)

        scales = incident_tracker.track(preds)
        return [PredictionResponse(**pred.model_dump(), incident_scale=scale) for pred, scale in zip(preds, scales)]

    @app_.get('/export_stats', response_model=Statistics)
    async def export_stats() -> dict:
        return export_to_dict(stats_collector)

    return app_


app = build_app()
