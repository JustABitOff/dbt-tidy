from factory import Factory

from tidy.manifest.metrics.metric import Metric


class MetricFactory(Factory):
    class Meta:
        model = Metric
