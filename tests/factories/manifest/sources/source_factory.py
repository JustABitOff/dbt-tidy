from factory import Factory

from tidy.manifest.sources.source import (
    Quoting,
    Time,
    FreshnessThreshold,
    ExternalPartition,
    ExternalTable,
    SourceConfig,
    Source,
)


class QuotingFactory(Factory):
    class Meta:
        model = Quoting


class TimeFactory(Factory):
    class Meta:
        model = Time


class FreshnessThresholdFactory(Factory):
    class Meta:
        model = FreshnessThreshold


class ExternalPartitionFactory(Factory):
    class Meta:
        model = ExternalPartition


class ExternalTableFactory(Factory):
    class Meta:
        model = ExternalTable


class SourceConfigFactory(Factory):
    class Meta:
        model = SourceConfig


class SourceFactory(Factory):
    class Meta:
        model = Source
