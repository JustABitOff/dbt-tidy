from typing import Optional, List

from pydantic import BaseModel, ConfigDict

from tidy.manifest.v12.bases.enums import Agg
from tidy.manifest.v12.semantic_models.semantic_layer_element_config import (
    SemanticLayerElementConfig,
)


class MeasureAggregationParameters(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    percentile: Optional[float] = None
    use_discrete_percentile: Optional[bool] = False
    use_approximate_percentile: Optional[bool] = False


class NonAdditiveDimension(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    window_choice: Agg
    window_groupings: List[str]


class Measure(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    agg: Agg
    description: Optional[str] = None
    label: Optional[str] = None
    create_metric: Optional[bool] = False
    expr: Optional[str] = None
    agg_params: Optional[MeasureAggregationParameters] = None
    non_additive_dimension: Optional[NonAdditiveDimension] = None
    agg_time_dimension: Optional[str] = None
    config: Optional[SemanticLayerElementConfig] = None
