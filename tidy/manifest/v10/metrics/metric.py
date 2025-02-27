from typing import List, Optional, Dict, Any

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v10.bases.source_file_metadata import SourceFileMetadata
from tidy.manifest.v10.bases.depends_on import DependsOn
from tidy.manifest.v10.bases.ref_args import RefArgs
from tidy.manifest.v10.bases.enums import MetricType, ResourceType
from tidy.manifest.v10.metrics.metric_type_params import MetricTypeParams
from tidy.manifest.v10.metrics.metric_config import MetricConfig
from tidy.manifest.v10.metrics.where_filter import WhereFilter


class Metric(BaseModel):
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
    description: str
    label: str
    type: MetricType
    type_params: MetricTypeParams
    filter: Optional[WhereFilter] = None
    metadata: Optional[SourceFileMetadata] = None
    meta: Optional[Dict[str, Any]] = {}
    tags: Optional[List[str]] = []
    config: Optional[MetricConfig] = Field(
        default_factory=lambda: MetricConfig.model_validate(
            {"enabled": True, "group": None}
        )
    )
    unrendered_config: Optional[Dict[str, Any]] = {}
    sources: Optional[List[List[str]]] = []
    depends_on: Optional[DependsOn] = Field(
        default_factory=lambda: DependsOn.model_validate({"macros": [], "nodes": []})
    )
    refs: Optional[List[RefArgs]] = []
    metrics: Optional[List[List[str]]] = []
    created_at: Optional[float] = 1696465994.4238322
    group: Optional[str] = None
