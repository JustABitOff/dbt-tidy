from typing import Optional, List, Dict, Any

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v10.bases.column_info import ColumnInfo
from tidy.manifest.v10.bases.enums import ResourceType
from tidy.manifest.v10.sources.quoting import Quoting
from tidy.manifest.v10.sources.freshness_threshold import FreshnessThreshold
from tidy.manifest.v10.sources.external_table import ExternalTable
from tidy.manifest.v10.sources.source_config import SourceConfig


class SourceDefinition(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    database: Optional[str] = None
    schema_: str = Field(..., alias="schema")
    name: str
    resource_type: ResourceType
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: List[str]
    source_name: str
    source_description: str
    loader: str
    identifier: str
    quoting: Optional[Quoting] = Field(
        default_factory=lambda: Quoting.model_validate(
            {"database": None, "schema": None, "identifier": None, "column": None}
        )
    )
    loaded_at_field: Optional[str] = None
    freshness: Optional[FreshnessThreshold] = None
    external: Optional[ExternalTable] = None
    description: Optional[str] = ""
    columns: Optional[Dict[str, ColumnInfo]] = {}
    meta: Optional[Dict[str, Any]] = {}
    source_meta: Optional[Dict[str, Any]] = {}
    tags: Optional[List[str]] = []
    config: Optional[SourceConfig] = Field(
        default_factory=lambda: SourceConfig.model_validate({"enabled": True})
    )
    patch_path: Optional[str] = None
    unrendered_config: Optional[Dict[str, Any]] = {}
    relation_name: Optional[str] = None
    created_at: Optional[float] = 1696465994.421661
