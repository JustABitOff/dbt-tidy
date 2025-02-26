from typing import Optional

from pydantic import BaseModel, ConfigDict

from tidy.manifest.v12.bases.source_file_metadata import SourceFileMetadata
from tidy.manifest.v12.bases.enums import Granularity, DimensionType
from tidy.manifest.v12.semantic_models.semantic_layer_element_config import (
    SemanticLayerElementConfig,
)


class DimensionValidityParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    is_start: Optional[bool] = False
    is_end: Optional[bool] = False


class DimensionTypeParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    time_granularity: Granularity
    validity_params: Optional[DimensionValidityParams] = None


class Dimension(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    type: DimensionType
    description: Optional[str] = None
    label: Optional[str] = None
    is_partition: Optional[bool] = False
    type_params: Optional[DimensionTypeParams] = None
    expr: Optional[str] = None
    metadata: Optional[SourceFileMetadata] = None
    config: Optional[SemanticLayerElementConfig] = None
