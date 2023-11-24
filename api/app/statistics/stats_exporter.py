from app.statistics.stats_collector import StatisticsCollector


def export_to_dict(collector: StatisticsCollector) -> dict:
    return {
        'theme_counts': collector.theme_counts,
        'theme_group_counts': collector.theme_group_counts,
        'executor_counts': collector.executor_counts
    }
