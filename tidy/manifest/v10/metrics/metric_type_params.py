from typing import Optional, List

from pydantic import BaseModel, ConfigDict

from tidy.manifest.v10.bases.enums import GrainToDate
from tidy.manifest.v10.metrics.where_filter import WhereFilter


class MetricTimeWindow(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    count: int
    granularity: GrainToDate


class MetricInputMeasure(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    filter: Optional[WhereFilter] = None
    alias: Optional[str] = None
    join_to_timespine: Optional[bool] = False
    fill_nulls_with: Optional[int] = None


class MetricInput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    filter: Optional[WhereFilter] = None
    alias: Optional[str] = None
    offset_window: Optional[MetricTimeWindow] = None
    offset_to_grain: Optional[GrainToDate] = None


class MetricTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    measure: Optional[MetricInputMeasure] = None
    input_measures: Optional[List[MetricInputMeasure]] = []
    numerator: Optional[MetricInput] = None
    denominator: Optional[MetricInput] = None
    expr: Optional[str] = None
    window: Optional[MetricTimeWindow] = None
    grain_to_date: Optional[GrainToDate] = None
    metrics: Optional[List[MetricInput]] = None
