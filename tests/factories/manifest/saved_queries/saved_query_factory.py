import factory

from tests.factories.manifest.bases.source_file_metadata_factory import (
    SourceFileMetadataFactory,
)
from tests.factories.manifest.bases.depends_on_factory import DependsOnFactory
from tests.factories.manifest.bases.ref_args_factory import RefArgsFactory
from tidy.manifest.saved_queries.saved_query import (
    QueryParams,
    ExportConfig,
    Export,
    SavedQueryCache,
    SavedQueryConfig,
    SavedQuery,
)


class QueryParamsFactory(factory.Factory):
    class Meta:
        model = QueryParams

    metrics = factory.List([factory.Faker("word") for _ in range(2)])


class ExportConfigFactory(factory.Factory):
    class Meta:
        model = ExportConfig

    export_as = factory.Faker("random_element", elements=["table", "view"])
    schema_name = factory.Faker("word")
    alias = factory.Faker("word")
    database = factory.Faker("word")


class ExportFactory(factory.Factory):
    class Meta:
        model = Export

    name = factory.Faker("word")
    config = factory.SubFactory(ExportConfigFactory)
    unrendered_config = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(
                None, None, {"locale": "en_US"}
            ): factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
            for _ in range(2)
        }
    )


class SavedQueryCacheFactory(factory.Factory):
    class Meta:
        model = SavedQueryCache

    enabled = factory.Faker("boolean")


class SavedQueryConfigFactory(factory.Factory):
    class Meta:
        model = SavedQueryConfig

    enabled = factory.Faker("boolean")
    group = factory.Faker("word")
    meta = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(
                None, None, {"locale": "en_US"}
            ): factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
            for _ in range(2)
        }
    )
    export_as = factory.Faker("random_element", elements=["table", "view"])
    schema_name = factory.Faker("word")
    cache = factory.SubFactory(SavedQueryCacheFactory)


class SavedQueryFactory(factory.Factory):
    class Meta:
        model = SavedQuery

    name = factory.Faker("word")
    package_name = factory.Faker("word")
    path = factory.Faker("file_path")
    original_file_path = factory.Faker("file_path")
    unique_id = factory.Faker("word")
    fqn = factory.List([package_name, name])
    query_params = factory.SubFactory(QueryParamsFactory)
    exports = factory.List([factory.SubFactory(ExportFactory) for _ in range(2)])
    description = factory.Faker("sentence")
    label = factory.Faker("word")
    metadata = factory.SubFactory(SourceFileMetadataFactory)
    config = factory.SubFactory(SavedQueryConfigFactory)
    unrendered_config = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(
                None, None, {"locale": "en_US"}
            ): factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
            for _ in range(2)
        }
    )
    group = factory.Faker("word")
    depends_on = factory.SubFactory(DependsOnFactory)
    created_at = factory.Faker("unix_time")
    refs = factory.List([factory.SubFactory(RefArgsFactory) for _ in range(2)])
    tags = factory.List([factory.Faker("word") for _ in range(3)])
