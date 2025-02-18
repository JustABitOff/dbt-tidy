from typing import Literal, Any

from pydantic import BaseModel, ConfigDict

from tidy.manifest.bases import (
    DependsOn,
    RefArgs,
    SourceFileMetadata,
)


class NodeRelation(BaseModel):
    alias: str
    schema_name: str
    database: str | None = None
    relation_name: str | None = ""


class Defaults(BaseModel):
    agg_time_dimension: str | None = None


class SemanticLayerElementConfig(BaseModel):
    meta: dict[str, Any] = {}


class Entity(BaseModel):
    name: str
    type: Literal["foreign", "natural", "primary", "unique"]
    description: str | None = None
    label: str | None = None
    role: str | None = None
    expr: str | None = None
    config: SemanticLayerElementConfig | None = None


class MeasureAggregationParameters(BaseModel):
    percentile: float | None = None
    use_discrete_percentile: bool = False
    use_approxiate_percentile: bool = False


class NonAdditiveDimension(BaseModel):
    name: str
    window_choice: Literal[
        "sum",
        "min",
        "max",
        "count_distinct",
        "sum_boolean",
        "average",
        "percentile",
        "median",
        "count",
    ]
    window_groupings: list[str] = []


class Measure(BaseModel):
    name: str
    agg: Literal[
        "sum",
        "min",
        "max",
        "count_distinct",
        "sum_boolean",
        "average",
        "percentile",
        "median",
        "count",
    ]
    description: str | None = None
    label: str | None = None
    create_metric: bool = False
    expr: str | None = None
    agg_params: MeasureAggregationParameters | None = None
    non_additive_dimension: NonAdditiveDimension | None = None
    agg_time_dimension: str | None = None
    config: SemanticLayerElementConfig | None = None


class DimensionValidityParams(BaseModel):
    is_start: bool = False
    is_end: bool = False


class DimensionTypeParams(BaseModel):
    time_granularity: Literal[
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
    validity_params: DimensionValidityParams | None = None


class Dimension(BaseModel):
    name: str
    type: Literal[
        "categorical",
        "time",
    ]
    description: str | None = None
    label: str | None = None
    is_partition: bool = False
    type_params: DimensionTypeParams | None = None


class SemanticModelConfig(BaseModel):
    enabled: bool = True
    group: str | None = None
    meta: dict[str, Any] = {}

    model_config = ConfigDict(
        extra="allow",
    )


class SemanticModel(BaseModel):
    name: str
    resource_type: Literal["semantic_model"] = "semantic_model"
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: list[str]
    model: str
    node_relation: NodeRelation | None = None
    description: str | None = None
    label: str | None = None
    defaults: Defaults | None = None
    entities: list[Entity] = []
    measures: list[Measure] = []
    dimensions: list[Dimension] = []
    metadata: SourceFileMetadata | None = None
    depends_on: DependsOn = DependsOn()
    refs: list[RefArgs] = []
    created_at: float
    config: SemanticModelConfig = SemanticModelConfig()
    unrendered_config: dict[str, Any] = {}
    primary_entity: str | None = None
    group: str | None = None
