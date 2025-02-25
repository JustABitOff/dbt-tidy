from typing import Dict, List, Any, Literal
from pydantic import BaseModel, Field

from tidy.manifest.bases.base_config import BaseConfig
from tidy.manifest.bases.check_sum import Checksum
from tidy.manifest.bases.column_info import ColumnInfo
from tidy.manifest.bases.docs_config import DocsConfig
from tidy.manifest.bases.depends_on import DependsOn
from tidy.manifest.bases.defer_relation import DeferRelation


class SeedConfig(BaseConfig):
    materialized: str = "seed"
    delimiter: str = ","
    quote_columns: bool | None = None


class Seed(BaseModel):
    database: str | None = None
    schema_name: str | None = Field(None, alias="schema")
    name: str | None = None
    resource_type: Literal["seed"] = "seed"
    package_name: str | None = None
    path: str | None = None
    original_file_path: str | None = None
    unique_id: str | None = None
    fqn: List[str] | None = None
    alias: str | None = None
    checksum: Checksum | None = None
    config: SeedConfig | None = None
    tags: List[Any] = []
    description: str = ""
    columns: Dict[str, ColumnInfo] | None = None
    meta: Dict[str, Any] = {}
    group: str | None = None
    docs: DocsConfig = DocsConfig()
    patch_path: str | None = None
    build_path: str | None = None
    unrendered_config: Dict[str, Any] = {}
    created_at: float
    config_call_dict: Dict[str, Any] = {}
    unrendered_config_call_dict: Dict[str, Any] = {}
    relation_name: str | None = None
    raw_code: str = ""
    root_path: str | None = None
    depends_on: DependsOn = DependsOn()
    defer_relation: DeferRelation | None = None
