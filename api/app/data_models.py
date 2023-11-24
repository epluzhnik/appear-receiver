from typing import Optional

from pydantic import BaseModel


class Prediction(BaseModel):
    theme: Optional[str]
    theme_group: Optional[str] = None
    executor: Optional[str] = None


class Statistics(BaseModel):
    theme_counts: dict[str, int]
    theme_group_counts: dict[str, int]
    executor_counts: dict[str, int]


class PredictionResponse(Prediction):
    incident_scale: Optional[int] = None
