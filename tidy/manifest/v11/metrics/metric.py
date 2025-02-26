from typing import Literal, List, Optional, Dict, Any

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v11.bases.source_file_metadata import SourceFileMetadata
from tidy.manifest.v11.bases.depends_on import DependsOn
from tidy.manifest.v11.bases.ref_args import RefArgs
from tidy.manifest.v11.bases.enums import MetricType
from tidy.manifest.v11.metrics.metric_type_params import MetricTypeParams
from tidy.manifest.v11.bases.where_filter_intersection import WhereFilterIntersection
from tidy.manifest.v11.metrics.metric_config import MetricConfig


class Metric(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    resource_type: Literal["metric"]
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: List[str]
    description: str
    label: str
    type: MetricType
    type_params: MetricTypeParams = Field(..., title="MetricTypeParams")
    filter: Optional[WhereFilterIntersection] = None
    metadata: Optional[SourceFileMetadata] = None
    meta: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None
    config: Optional[MetricConfig] = Field(None, title="MetricConfig")
    unrendered_config: Optional[Dict[str, Any]] = None
    sources: Optional[List[List[str]]] = None
    depends_on: Optional[DependsOn] = Field(None, title="DependsOn")
    refs: Optional[List[RefArgs]] = None
    metrics: Optional[List[List[str]]] = None
    created_at: Optional[float] = None
    group: Optional[str] = None
