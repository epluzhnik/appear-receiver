import collections
import json
import pathlib

from app.data_models.prediction import Prediction


class StatisticsCollector:
    def __init__(self, statistics_path: pathlib.Path) -> None:
        self.path = statistics_path
        self.path.mkdir(parents=True, exist_ok=True)
        self._load()

    def _load(self) -> None:
        self.theme_counts = collections.Counter()
        self.theme_group_counts = collections.Counter()
        self.executor_counts = collections.Counter()

        with open(self.path, 'r') as file:
            data = json.load(file)
            self.theme_counts.update(data.get('theme_counts', {}))
            self.theme_group_counts.update(data.get('theme_group_counts', {}))
            self.executor_counts.update(data.get('executor_counts', {}))

    def _save(self) -> None:
        data = {
            'theme_counts': self.theme_counts,
            'theme_group_counts': self.theme_group_counts,
            'executor_counts': self.executor_counts
        }
        with open(self.path, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def collect(self, text: str, prediction: Prediction) -> None:
        self.theme_counts[prediction.theme] += 1
        self.theme_group_counts[prediction.theme_group] += 1
        self.executor_counts[prediction.executor] += 1

        self._save()
