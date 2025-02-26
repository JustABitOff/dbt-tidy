from typing import Optional, Literal, List, Dict, Any

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v11.bases.column_info import ColumnInfo
from tidy.manifest.v11.sources.quoting import Quoting
from tidy.manifest.v11.sources.freshness_threshold import FreshnessThreshold
from tidy.manifest.v11.sources.external_table import ExternalTable
from tidy.manifest.v11.sources.source_config import SourceConfig


class SourceDefinition(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    database: Optional[str] = None
    schema_: str = Field(..., alias="schema")
    name: str
    resource_type: Literal["source"]
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: List[str]
    source_name: str
    source_description: str
    loader: str
    identifier: str
    field_event_status: Optional[Dict[str, Any]] = Field(None, alias="_event_status")
    quoting: Optional[Quoting] = Field(None, title="Quoting")
    loaded_at_field: Optional[str] = None
    freshness: Optional[FreshnessThreshold] = None
    external: Optional[ExternalTable] = None
    description: Optional[str] = ""
    columns: Optional[Dict[str, ColumnInfo]] = None
    meta: Optional[Dict[str, Any]] = None
    source_meta: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None
    config: Optional[SourceConfig] = Field(None, title="SourceConfig")
    patch_path: Optional[str] = None
    unrendered_config: Optional[Dict[str, Any]] = None
    relation_name: Optional[str] = None
    created_at: Optional[float] = None
