from typing import Literal, Any, Union

from pydantic import BaseModel, ConfigDict

from tidy.manifest.bases import(
    DependsOn,
    RefArgs,
    SourceFileMetadata,
)


class WhereFilter(BaseModel):
    where_sql_template: str


class WhereFilterIntersection(BaseModel):
    where_filters: list[WhereFilter] = []


class MetricInputMeasure(BaseModel):
    name: str
    filter: WhereFilter | None = None
    alias: str | None = None
    join_to_timespine: bool = False
    fill_nulls_with: int | None = None


class MetricTimeWindow(BaseModel):
    count: int
    granularity: str


class MetricInput(BaseModel):
    name: str
    filter: WhereFilter | None = None
    alias: str | None = None
    offset_window: MetricTimeWindow | None = None
    offset_to_grain: str | None = None


class ConstantPropertyInput(BaseModel):
    base_property: str
    conversion_property: str


class ConversionTypeParams(BaseModel):
    base_measure: MetricInputMeasure
    conversion_measure: MetricInputMeasure
    entity: str
    calculation: Literal["conversions", "conversion_rate"] = "conversion_rate"
    window: MetricTimeWindow | None = None
    constant_properties: list[ConstantPropertyInput] | None = None


class CumulativeTypeParams(BaseModel):
    window: MetricTimeWindow | None = None
    grain_to_date: str | None = None
    period_agg: Literal[
        "first",
        "last",
        "average",
    ] = "first"


class MetricTypeParams(BaseModel):
    measure: MetricInputMeasure
    input_measures: list[MetricInputMeasure]
    numerator: MetricInput | None = None
    denominator: MetricInput | None = None
    expr: str | None = None
    window: MetricTimeWindow | None
    grain_to_date: (
        Literal[
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
        ]
        | None
    ) = None
    metrics: list[MetricInput] | None = None
    conversion_type_params: ConversionTypeParams | None = None
    cumulative_type_params: CumulativeTypeParams | None = None


class MetricConfig(BaseModel):
    enabled: bool = True
    group: str | None = None
    meta: dict[str, Any] = {}

    model_config = ConfigDict(
        extra="allow",
    )


class Metric(BaseModel):
    name: str
    resource_type: Literal["metric"] = "metric"
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: list[str]
    description: str
    label: str
    type: Literal[
        "simple",
        "ratio",
        "cumulative",
        "derived",
        "conversion",
    ]
    type_params: MetricTypeParams
    filter: WhereFilterIntersection | None = None
    metadata: SourceFileMetadata | None = None
    time_granularity: str | None = None
    meta: dict[str, Any] = {}
    tags: list[str] = []
    config: MetricConfig
    unrendered_config: dict[str, Any] = {}
    sources: list[list[str]] = []
    depends_on: DependsOn = DependsOn()
    refs: list[RefArgs] = []
    metrics: list[list[str]] = []
    created_at: float
    group: str | None = None
