from typing import Optional

from pydantic import BaseModel, ConfigDict

from tidy.manifest.v12.bases.enums import EntityType
from tidy.manifest.v12.semantic_models.semantic_layer_element_config import (
    SemanticLayerElementConfig,
)


class Entity(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    type: EntityType
    description: Optional[str] = None
    label: Optional[str] = None
    role: Optional[str] = None
    expr: Optional[str] = None
    config: Optional[SemanticLayerElementConfig] = None
