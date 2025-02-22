import factory

from tests.factories.manifest.bases.source_file_metadata_factory import (
    SourceFileMetadataFactory,
)
from tests.factories.manifest.bases.depends_on_factory import DependsOnFactory
from tests.factories.manifest.bases.ref_args_factory import RefArgsFactory
from tidy.manifest.metrics.metric import (
    WhereFilter,
    WhereFilterIntersection,
    MetricInputMeasure,
    MetricTimeWindow,
    MetricInput,
    ConstantPropertyInput,
    ConversionTypeParams,
    CumulativeTypeParams,
    MetricTypeParams,
    MetricConfig,
    Metric,
)


class WhereFilterFactory(factory.Factory):
    class Meta:
        model = WhereFilter

    where_sql_template = "1=1"


class WhereFilterIntersectionFactory(factory.Factory):
    class Meta:
        model = WhereFilterIntersection

    where_filters = factory.List([factory.SubFactory(WhereFilterFactory)])


class MetricInputMeasureFactory(factory.Factory):
    class Meta:
        model = MetricInputMeasure

    name = factory.Faker("word")
    filter = factory.SubFactory(WhereFilterFactory)
    alias = name


class MetricTimeWindowFactory(factory.Factory):
    class Meta:
        model = MetricTimeWindow

    count = 1
    granularity = "day"


class MetricInputFactory(factory.Factory):
    class Meta:
        model = MetricInput

    name = factory.Faker("word")
    filter = factory.SubFactory(WhereFilterFactory)
    alias = name
    offset_window = factory.SubFactory(MetricTimeWindowFactory)
    offset_to_grain = "30"


class ConstantPropertyInputFactory(factory.Factory):
    class Meta:
        model = ConstantPropertyInput

    base_property = factory.Faker("word")
    conversion_property = factory.Faker("word")


class ConversionTypeParamsFactory(factory.Factory):
    class Meta:
        model = ConversionTypeParams

    base_measure = factory.SubFactory(MetricInputMeasureFactory)
    conversion_measure = factory.SubFactory(MetricInputMeasureFactory)
    entity = factory.Faker("word")
    calculation = factory.Faker(
        "random_element", elements=["conversions", "conversion_rate"]
    )
    window = factory.SubFactory(MetricTimeWindowFactory)
    constant_properties = factory.List(
        [factory.SubFactory(ConstantPropertyInputFactory) for _ in range(2)]
    )


class CumulativeTypeParamsFactory(factory.Factory):
    class Meta:
        model = CumulativeTypeParams

    window = factory.SubFactory(MetricTimeWindowFactory)
    grain_to_date = factory.Faker("word")
    period_agg = factory.Faker("random_element", elements=["first", "last", "average"])


class MetricTypeParamsFactory(factory.Factory):
    class Meta:
        model = MetricTypeParams

    measure = factory.SubFactory(MetricInputMeasureFactory)
    input_measures = factory.List(
        [factory.SubFactory(MetricInputMeasureFactory) for _ in range(2)]
    )
    numerator = factory.SubFactory(MetricInputFactory)
    denominator = factory.SubFactory(MetricInputFactory)
    expr = factory.Faker("word")
    window = factory.SubFactory(MetricTimeWindowFactory)
    grain_to_date = factory.Faker(
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
    metrics = factory.List([factory.SubFactory(MetricInputFactory) for _ in range(2)])
    conversion_type_params = factory.SubFactory(ConversionTypeParamsFactory)
    cumulative_type_params = factory.SubFactory(CumulativeTypeParamsFactory)


class MetricConfigFactory(factory.Factory):
    class Meta:
        model = MetricConfig

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


class MetricFactory(factory.Factory):
    class Meta:
        model = Metric

    name = factory.Faker("word")
    package_name = factory.Faker("word")
    path = factory.Faker("file_path")
    original_file_path = factory.Faker("file_path")
    unique_id = factory.Faker("word")
    fqn = factory.List([package_name, name])
    description = factory.Faker("sentence")
    label = factory.Faker("word")
    type = factory.Faker(
        "random_element",
        elements=[
            "simple",
            "ratio",
            "cumulative",
            "derived",
            "conversion",
        ],
    )
    type_params = factory.SubFactory(MetricTypeParamsFactory)
    filter = factory.SubFactory(WhereFilterIntersectionFactory)
    metadata = factory.SubFactory(SourceFileMetadataFactory)
    time_granularity = "day"
    meta = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(
                None, None, {"locale": "en_US"}
            ): factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
            for _ in range(2)
        }
    )
    tags = factory.List(
        [
            factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
            for _ in range(2)
        ]
    )
    config = factory.SubFactory(MetricConfigFactory)
    unrendered_config = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(
                None, None, {"locale": "en_US"}
            ): factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
            for _ in range(2)
        }
    )
    sources = factory.List(
        [
            factory.List(
                [
                    factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
                    for _ in range(3)
                ]
            )
        ]
    )
    depends_on = factory.SubFactory(DependsOnFactory)
    refs = factory.List([factory.SubFactory(RefArgsFactory) for _ in range(2)])
    metrics = factory.List(
        [
            factory.List(
                [
                    factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
                    for _ in range(3)
                ]
            )
        ]
    )
    created_at = factory.Faker("unix_time")
    group = factory.Faker("word")
