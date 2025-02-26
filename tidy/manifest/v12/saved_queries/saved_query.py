from typing import Literal, List, Optional, Dict, Any, Union

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v12.saved_queries.query_params import QueryParams
from tidy.manifest.v12.saved_queries.saved_query_config import SavedQueryConfig
from tidy.manifest.v12.saved_queries.export import Export
from tidy.manifest.v12.bases.source_file_metadata import SourceFileMetadata
from tidy.manifest.v12.bases.depends_on import DependsOn
from tidy.manifest.v12.bases.ref_args import RefArgs


class SavedQuery(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    resource_type: Literal["saved_query"]
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: List[str]
    query_params: QueryParams = Field(..., title="QueryParams")
    exports: List[Export]
    description: Optional[str] = None
    label: Optional[str] = None
    metadata: Optional[SourceFileMetadata] = None
    config: Optional[SavedQueryConfig] = Field(None, title="SavedQueryConfig")
    unrendered_config: Optional[Dict[str, Any]] = None
    group: Optional[str] = None
    depends_on: Optional[DependsOn] = Field(None, title="DependsOn")
    created_at: Optional[float] = None
    refs: Optional[List[RefArgs]] = None
    tags: Optional[Union[List[str], str]] = None
