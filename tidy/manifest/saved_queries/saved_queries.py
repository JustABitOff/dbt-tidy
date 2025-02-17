from typing import Literal, Any, Union

from pydantic import BaseModel, Field, ConfigDict


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


class FileSlice(BaseModel):
    filename: str
    content: str
    start_line_number: int
    end_line_number: int


class SourceFileMetadata(BaseModel):
    repo_file_path: str
    file_slice: FileSlice


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


class DependsOn(BaseModel):
    macros: list[str] = []
    nodes: list[str] = []


class RefArgs(BaseModel):
    name: str = ""
    package: str | None = None
    version: Union[str, int, None] = None


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
