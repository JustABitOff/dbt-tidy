from typing import Optional, List, Dict, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v11.bases.file_hash import FileHash
from tidy.manifest.v11.bases.column_info import ColumnInfo
from tidy.manifest.v11.bases.docs import Docs
from tidy.manifest.v11.bases.defer_relation import DeferRelation
from tidy.manifest.v11.macros.macro_depends_on import MacroDependsOn
from tidy.manifest.v11.nodes.seeds.seed_config import SeedConfig


class SeedNode(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    database: Optional[str] = None
    schema_: str = Field(..., alias="schema")
    name: str
    resource_type: Literal["seed"]
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: List[str]
    alias: str
    checksum: FileHash = Field(..., title="FileHash")
    config: Optional[SeedConfig] = Field(None, title="SeedConfig")
    field_event_status: Optional[Dict[str, Any]] = Field(None, alias="_event_status")
    tags: Optional[List[str]] = None
    description: Optional[str] = ""
    columns: Optional[Dict[str, ColumnInfo]] = None
    meta: Optional[Dict[str, Any]] = None
    group: Optional[str] = None
    docs: Optional[Docs] = Field(None, title="Docs")
    patch_path: Optional[str] = None
    build_path: Optional[str] = None
    deferred: Optional[bool] = False
    unrendered_config: Optional[Dict[str, Any]] = None
    created_at: Optional[float] = None
    config_call_dict: Optional[Dict[str, Any]] = None
    relation_name: Optional[str] = None
    raw_code: Optional[str] = ""
    root_path: Optional[str] = None
    depends_on: Optional[MacroDependsOn] = Field(None, title="MacroDependsOn")
    defer_relation: Optional[DeferRelation] = None
