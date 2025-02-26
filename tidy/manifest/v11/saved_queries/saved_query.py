from typing import List, Optional, Dict, Any

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v11.saved_queries.query_params import QueryParams
from tidy.manifest.v11.saved_queries.saved_query_config import SavedQueryConfig
from tidy.manifest.v11.saved_queries.export import Export
from tidy.manifest.v11.bases.source_file_metadata import SourceFileMetadata
from tidy.manifest.v11.bases.depends_on import DependsOn
from tidy.manifest.v11.bases.ref_args import RefArgs
from tidy.manifest.v11.bases.enums import ResourceType


class SavedQuery(BaseModel):
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
    query_params: QueryParams = Field(..., title="QueryParams")
    exports: List[Export]
    field_event_status: Optional[Dict[str, Any]] = Field(None, alias="_event_status")
    description: Optional[str] = None
    label: Optional[str] = None
    metadata: Optional[SourceFileMetadata] = None
    config: Optional[SavedQueryConfig] = Field(None, title="SavedQueryConfig")
    unrendered_config: Optional[Dict[str, Any]] = None
    group: Optional[str] = None
    depends_on: Optional[DependsOn] = Field(None, title="DependsOn")
    created_at: Optional[float] = None
    refs: Optional[List[RefArgs]] = None
