from typing import Literal, Any

from pydantic import BaseModel, Field, ConfigDict

from tidy.manifest.bases.ref_args import RefArgs
from tidy.manifest.bases.depends_on import DependsOn
from tidy.manifest.bases.source_file_metadata import SourceFileMetadata


class QueryParams(BaseModel):
    metrics: list[str] = []


class ExportConfig(BaseModel):
    export_as: Literal["table", "view"]
    schema_name: str | None = None
    alias: str | None = None
    database: str | None = None


class Export(BaseModel):
    name: str
    config: ExportConfig
    unrendered_config: dict[str, Any] = {}


class SavedQueryCache(BaseModel):
    enabled: bool = False


class SavedQueryConfig(BaseModel):
    enabled: bool = True
    group: str | None = None
    meta: dict[str, Any] = {}
    export_as: Literal["table", "view"] | None = None
    schema_name: str | None = Field(None, alias="schema")
    cache: SavedQueryCache = SavedQueryCache()

    model_config = ConfigDict(
        extra="allow",
    )


class SavedQuery(BaseModel):
    name: str
    resource_type: Literal["saved_query"] = "saved_query"
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: list[str]
    query_params: QueryParams
    exports: list[Export] = []
    description: str | None = None
    label: str | None = None
    metadata: SourceFileMetadata | None = None
    config: SavedQueryConfig = SavedQueryConfig()
    unrendered_config: dict[str, Any] = {}
    group: str | None = None
    depends_on: DependsOn = DependsOn()
    created_at: float
    refs: list[RefArgs] = []
    tags: list[str] | str | None = None
