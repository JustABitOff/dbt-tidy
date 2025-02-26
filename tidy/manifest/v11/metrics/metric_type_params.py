from typing import Optional, List

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v11.bases.enums import MetricCalculation, Granularity
from tidy.manifest.v11.bases.where_filter_intersection import WhereFilterIntersection


class MetricInputMeasure(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    filter: Optional[WhereFilterIntersection] = None
    alias: Optional[str] = None
    join_to_timespine: Optional[bool] = False
    fill_nulls_with: Optional[int] = None


class MetricTimeWindow(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    count: int
    granularity: Granularity


class MetricInput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    filter: Optional[WhereFilterIntersection] = None
    alias: Optional[str] = None
    offset_window: Optional[MetricTimeWindow] = None
    offset_to_grain: Optional[Granularity] = None


class ConstantPropertyInput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    base_property: str
    conversion_property: str


class ConversionTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    base_measure: MetricInputMeasure = Field(..., title="MetricInputMeasure")
    conversion_measure: MetricInputMeasure = Field(..., title="MetricInputMeasure")
    entity: str
    calculation: Optional[MetricCalculation] = "conversion_rate"
    window: Optional[MetricTimeWindow] = None
    constant_properties: Optional[List[ConstantPropertyInput]] = None


class MetricTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    measure: Optional[MetricInputMeasure] = None
    input_measures: Optional[List[MetricInputMeasure]] = None
    numerator: Optional[MetricInput] = None
    denominator: Optional[MetricInput] = None
    expr: Optional[str] = None
    window: Optional[MetricTimeWindow] = None
    grain_to_date: Optional[Granularity] = None
    metrics: Optional[List[MetricInput]] = None
    conversion_type_params: Optional[ConversionTypeParams] = None
