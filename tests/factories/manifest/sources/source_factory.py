import factory

from tests.factories.manifest.bases.column_info_factory import ColumnInfoFactory
from tidy.manifest.sources.source import (
    Quoting,
    Time,
    FreshnessThreshold,
    ExternalPartition,
    ExternalTable,
    SourceConfig,
    Source,
)


class QuotingFactory(factory.Factory):
    class Meta:
        model = Quoting

    database = True
    schema_name = True
    identifier = True
    column = True


class TimeFactory(factory.Factory):
    class Meta:
        model = Time

    count = 1
    period = factory.Faker("random_element", elements=["minute", "hour", "day"])


class FreshnessThresholdFactory(factory.Factory):
    class Meta:
        model = FreshnessThreshold

    warn_after = TimeFactory(count=1, period="hour")
    error_after = TimeFactory(count=2, period="hour")
    filter = "1 = 1"


class ExternalPartitionFactory(factory.Factory):
    class Meta:
        model = ExternalPartition

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    data_type = factory.Faker("word")
    meta = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(
                None, None, {"locale": "en_US"}
            ): factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
            for _ in range(2)
        }
    )


class ExternalTableFactory(factory.Factory):
    class Meta:
        model = ExternalTable

    location = factory.Faker("word")
    file_format = factory.Faker("word")
    row_format = factory.Faker("word")
    tbl_properties = factory.Faker("word")
    partitions = factory.List(
        [factory.SubFactory(ExternalPartitionFactory) for _ in range(2)]
    )


class SourceConfigFactory(factory.Factory):
    class Meta:
        model = SourceConfig

    enabled = factory.Faker("boolean")
    event_time = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(
                None, None, {"locale": "en_US"}
            ): factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
            for _ in range(2)
        }
    )


class SourceFactory(factory.Factory):
    class Meta:
        model = Source

    database = factory.Faker("word")
    schema_name = factory.Faker("word")
    name = factory.Faker("word")
    package_name = factory.Faker("word")
    path = factory.Faker("file_path")
    original_file_path = factory.Faker("file_path")
    unique_id = factory.Faker("word")
    fqn = factory.List([package_name, name])
    source_name = factory.Faker("word")
    source_description = factory.Faker("sentence")
    loader = factory.Faker("word")
    identifier = factory.Faker("word")
    quoting = factory.SubFactory(QuotingFactory)
    loaded_at_field = factory.Faker("word")
    loaded_at_query = "1 = 1"
    freshness = factory.SubFactory(FreshnessThresholdFactory)
    external = factory.SubFactory(ExternalTableFactory)
    description = factory.Faker("sentence")
    columns = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(
                None, None, {"locale": "en_US"}
            ): ColumnInfoFactory.build()
            for _ in range(2)
        }
    )
    meta = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(
                None, None, {"locale": "en_US"}
            ): factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
            for _ in range(2)
        }
    )
    source_meta = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(
                None, None, {"locale": "en_US"}
            ): factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
            for _ in range(2)
        }
    )
    tags = factory.List([factory.Faker("word") for _ in range(3)])
    config = factory.SubFactory(SourceConfigFactory)
    patch_path = factory.Faker("file_path")
    unrendered_config = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(
                None, None, {"locale": "en_US"}
            ): factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
            for _ in range(2)
        }
    )
    relation_name = factory.Faker("word")
    created_at = factory.Faker("unix_time")
    unrendered_database = factory.Faker("word")
    unrendered_schema = factory.Faker("word")
