import pathlib

import pandas as pd

from app.statistics.stats_collector import StatisticsCollector


def export_to_dict(collector: StatisticsCollector) -> dict:
    return {
        'theme_counts': collector.theme_counts,
        'theme_group_counts': collector.theme_group_counts,
        'executor_counts': collector.executor_counts
    }


def export_to_excel(collector: StatisticsCollector, path: pathlib.Path) -> None:
    theme_df = pd.DataFrame.from_dict(
        collector.theme_counts, orient='index',
        columns=['Тема', 'Количество обращений']
    ).reset_index()
    theme_group_df = pd.DataFrame.from_dict(
        collector.theme_group_counts, orient='index',
        columns=['Группа тем', 'Количество обращений']
    ).reset_index()
    executor_df = pd.DataFrame.from_dict(
        collector.executor_counts, orient='index',
        columns=['Исполнитель', 'Количество обращений']
    )

    with pd.ExcelWriter(path) as writer:
        theme_df.to_excel(writer, sheet_name="Количество обращений по темам", index=False)
        theme_group_df.to_excel(writer, sheet_name="Количество обращений по группам тем", index=False)
        executor_df.to_excel(writer, sheet_name="Количество обращений по исполнителям", index=False)
