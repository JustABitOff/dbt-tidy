from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v10.bases.source_file_metadata import SourceFileMetadata
from tidy.manifest.v10.bases.depends_on import DependsOn
from tidy.manifest.v10.bases.ref_args import RefArgs
from tidy.manifest.v10.bases.enums import ResourceType
from tidy.manifest.v10.semantic_models.node_relation import NodeRelation
from tidy.manifest.v10.semantic_models.defaults import Defaults
from tidy.manifest.v10.semantic_models.entity import Entity
from tidy.manifest.v10.semantic_models.measure import Measure
from tidy.manifest.v10.semantic_models.dimension import Dimension
from tidy.manifest.v10.semantic_models.semantic_model_config import SemanticModelConfig


class SemanticModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    resource_type: ResourceType
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
    entities: Optional[List[Entity]] = []
    measures: Optional[List[Measure]] = []
    dimensions: Optional[List[Dimension]] = []
    metadata: Optional[SourceFileMetadata] = None
    depends_on: Optional[DependsOn] = Field(
        default_factory=lambda: DependsOn.model_validate({"macros": [], "nodes": []})
    )
    refs: Optional[List[RefArgs]] = []
    created_at: Optional[float] = 1696465994.425479
    config: Optional[SemanticModelConfig] = Field(
        default_factory=lambda: SemanticModelConfig.model_validate({"enabled": True})
    )
    primary_entity: Optional[str] = None
