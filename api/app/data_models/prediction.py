from typing import Optional

from pydantic import BaseModel


class Prediction(BaseModel):
    theme: str
    theme_group: Optional[str] = None
    executor: Optional[str] = None
