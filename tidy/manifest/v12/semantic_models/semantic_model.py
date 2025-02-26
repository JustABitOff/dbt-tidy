from typing import List, Optional, Dict, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v12.bases.source_file_metadata import SourceFileMetadata
from tidy.manifest.v12.bases.depends_on import DependsOn
from tidy.manifest.v12.bases.ref_args import RefArgs
from tidy.manifest.v12.semantic_models.node_relation import NodeRelation
from tidy.manifest.v12.semantic_models.defaults import Defaults
from tidy.manifest.v12.semantic_models.entity import Entity
from tidy.manifest.v12.semantic_models.measure import Measure
from tidy.manifest.v12.semantic_models.dimension import Dimension
from tidy.manifest.v12.semantic_models.semantic_model_config import SemanticModelConfig


class SemanticModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    resource_type: Literal["semantic_model"]
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: List[str]
    model: str
    node_relation: Optional[NodeRelation] = None
    description: Optional[str] = None
    label: Optional[str] = None
    defaults: Optional[Defaults] = None
    entities: Optional[List[Entity]] = None
    measures: Optional[List[Measure]] = None
    dimensions: Optional[List[Dimension]] = None
    metadata: Optional[SourceFileMetadata] = None
    depends_on: Optional[DependsOn] = Field(None, title="DependsOn")
    refs: Optional[List[RefArgs]] = None
    created_at: Optional[float] = None
    config: Optional[SemanticModelConfig] = Field(None, title="SemanticModelConfig")
    unrendered_config: Optional[Dict[str, Any]] = None
    primary_entity: Optional[str] = None
    group: Optional[str] = None
