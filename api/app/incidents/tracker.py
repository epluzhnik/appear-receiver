import collections
import dataclasses
import datetime
from typing import Optional

from app.data_models import Prediction


@dataclasses.dataclass
class IncidentData:
    dttm: datetime.datetime
    group: str


class GroupIncidentTracker:
    def __init__(
            self,
            lifespan=datetime.timedelta(minutes=10),
            threshold=5,
    ):
        self.lifespan = lifespan
        self.threshold = threshold

        self._records: collections.deque[IncidentData] = collections.deque()
        self._group_counts = collections.Counter()

    def _remove_old_records(self):
        now = datetime.datetime.now()
        while self._records and (now - self._records[0].dttm) > self.lifespan:
            data = self._records.popleft()
            self._group_counts[data.group] -= 1

    def track(self, predictions: list[Prediction]) -> list[Optional[int]]:
        self._remove_old_records()
        for pred in predictions:
            if pred.theme_group is None:
                continue

            data = IncidentData(dttm=datetime.datetime.now(), group=pred.theme_group)
            self._group_counts[data.group] += 1
            self._records.append(data)

        output = []
        for pred in predictions:
            if pred.theme_group is None:
                output.append(None)
                continue

            scale = self._group_counts.get(pred.theme_group, 0)
            if scale >= self.threshold:
                output.append(scale)
            else:
                output.append(None)

        return output
