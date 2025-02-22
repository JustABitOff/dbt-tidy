import random

import factory

from tests.factories.manifest.bases.source_file_metadata_factory import (
    SourceFileMetadataFactory,
)
from tests.factories.manifest.bases.depends_on_factory import DependsOnFactory
from tests.factories.manifest.bases.ref_args_factory import RefArgsFactory
from tidy.manifest.semantic_models.semantic_model import (
    NodeRelation,
    Defaults,
    SemanticLayerElementConfig,
    Entity,
    MeasureAggregationParameters,
    NonAdditiveDimension,
    Measure,
    DimensionValidityParams,
    DimensionTypeParams,
    Dimension,
    SemanticModelConfig,
    SemanticModel,
)


class NodeRelationFactory(factory.Factory):
    class Meta:
        model = NodeRelation

    alias = factory.Faker("word")
    schema_name = factory.Faker("word")
    database = factory.Faker("word")
    relation_name = factory.Faker("word")


class DefaultsFactory(factory.Factory):
    class Meta:
        model = Defaults

    agg_time_dimension = factory.Faker("word")


class SemanticLayerElementConfigFactory(factory.Factory):
    class Meta:
        model = SemanticLayerElementConfig

    meta = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(
                None, None, {"locale": "en_US"}
            ): factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
            for _ in range(2)
        }
    )


class EntityFactory(factory.Factory):
    class Meta:
        model = Entity

    name = factory.Faker("word")
    type = factory.Faker(
        "random_element", elements=["foreign", "natural", "primary", "unique"]
    )
    description = factory.Faker("sentence")
    label = factory.Faker("word")
    role = factory.Faker("word")
    expr = "1 = 1"
    config = factory.SubFactory(SemanticLayerElementConfigFactory)


class MeasureAggregationParametersFactory(factory.Factory):
    class Meta:
        model = MeasureAggregationParameters

    percentile = float(random.randint(0, 100))
    use_discrete_percentile = factory.Faker("boolean")
    use_approxiate_percentile = factory.Faker("boolean")


class NonAdditiveDimensionFactory(factory.Factory):
    class Meta:
        model = NonAdditiveDimension

    name = factory.Faker("word")
    window_choice = factory.Faker(
        "random_element",
        elements=[
            "sum",
            "min",
            "max",
            "count_distinct",
            "sum_boolean",
            "average",
            "percentile",
            "median",
            "count",
        ],
    )
    window_groupings = factory.List([factory.Faker("word") for _ in range(2)])


class MeasureFactory(factory.Factory):
    class Meta:
        model = Measure

    name = factory.Faker("word")
    agg = factory.Faker(
        "random_element",
        elements=[
            "sum",
            "min",
            "max",
            "count_distinct",
            "sum_boolean",
            "average",
            "percentile",
            "median",
            "count",
        ],
    )
    description = factory.Faker("sentence")
    label = factory.Faker("word")
    create_metric = factory.Faker("boolean")
    expr = "1 = 1"
    agg_params = factory.SubFactory(MeasureAggregationParametersFactory)
    non_additive_dimension = factory.SubFactory(NonAdditiveDimensionFactory)
    agg_time_dimension = "day"
    config = factory.SubFactory(SemanticLayerElementConfigFactory)


class DimensionValidityParamsFactory(factory.Factory):
    class Meta:
        model = DimensionValidityParams

    is_start = factory.Faker("boolean")
    is_end = factory.Faker("boolean")


class DimensionTypeParamsFactory(factory.Factory):
    class Meta:
        model = DimensionTypeParams

    time_granularity = factory.Faker(
        "random_element",
        elements=[
            "nanosecond",
            "microsecond",
            "millisecond",
            "second",
            "minute",
            "hour",
            "day",
            "week",
            "month",
            "quarter",
            "year",
        ],
    )
    validity_params = factory.SubFactory(DimensionValidityParamsFactory)


class DimensionFactory(factory.Factory):
    class Meta:
        model = Dimension

    name = factory.Faker("word")
    type = factory.Faker("random_element", elements=["categorical", "time"])
    description = factory.Faker("sentence")
    label = factory.Faker("word")
    is_partition = factory.Faker("boolean")
    type_params = factory.SubFactory(DimensionTypeParamsFactory)


class SemanticModelConfigFactory(factory.Factory):
    class Meta:
        model = SemanticModelConfig

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


class SemanticModelFactory(factory.Factory):
    class Meta:
        model = SemanticModel

    name = factory.Faker("word")
    package_name = factory.Faker("word")
    path = factory.Faker("file_path")
    original_file_path = factory.Faker("file_path")
    unique_id = factory.Faker("word")
    fqn = factory.List([package_name, name])
    model = factory.Faker("word")
    node_relation = factory.SubFactory(NodeRelationFactory)
    description = factory.Faker("sentence")
    label = factory.Faker("word")
    defaults = factory.SubFactory(DefaultsFactory)
    entities = factory.List([factory.SubFactory(EntityFactory) for _ in range(2)])
    measures = factory.List([factory.SubFactory(MeasureFactory) for _ in range(2)])
    dimensions = factory.List([factory.SubFactory(DimensionFactory) for _ in range(2)])
    metadata = factory.SubFactory(SourceFileMetadataFactory)
    depends_on = factory.SubFactory(DependsOnFactory)
    refs = factory.List([factory.SubFactory(RefArgsFactory) for _ in range(2)])
    created_at = factory.Faker("unix_time")
    config = factory.SubFactory(SemanticModelConfigFactory)
    unrendered_config = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(
                None, None, {"locale": "en_US"}
            ): factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
            for _ in range(2)
        }
    )
    primary_entity = factory.Faker("word")
    group = factory.Faker("word")
