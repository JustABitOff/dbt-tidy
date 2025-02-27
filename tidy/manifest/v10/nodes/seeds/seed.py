from typing import Optional, List, Dict, Any

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v10.bases.file_hash import FileHash
from tidy.manifest.v10.bases.column_info import ColumnInfo
from tidy.manifest.v10.bases.docs import Docs
from tidy.manifest.v10.bases.defer_relation import DeferRelation
from tidy.manifest.v10.bases.enums import ResourceType
from tidy.manifest.v10.macros.macro_depends_on import MacroDependsOn
from tidy.manifest.v10.nodes.seeds.seed_config import SeedConfig


class SeedNode(BaseModel):
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
    alias: str
    checksum: FileHash
    config: Optional[SeedConfig] = Field(
        default_factory=lambda: SeedConfig.model_validate(
            {
                "enabled": True,
                "alias": None,
                "schema": None,
                "database": None,
                "tags": [],
                "meta": {},
                "group": None,
                "materialized": "seed",
                "incremental_strategy": None,
                "persist_docs": {},
                "quoting": {},
                "column_types": {},
                "full_refresh": None,
                "unique_key": None,
                "on_schema_change": "ignore",
                "on_configuration_change": "apply",
                "grants": {},
                "packages": [],
                "docs": {"show": True, "node_color": None},
                "contract": {"enforced": False},
                "quote_columns": None,
                "post-hook": [],
                "pre-hook": [],
            }
        )
    )
    tags: Optional[List[str]] = []
    description: Optional[str] = ""
    columns: Optional[Dict[str, ColumnInfo]] = {}
    meta: Optional[Dict[str, Any]] = {}
    group: Optional[str] = None
    docs: Optional[Docs] = Field(
        default_factory=lambda: Docs.model_validate({"show": True, "node_color": None})
    )
    patch_path: Optional[str] = None
    build_path: Optional[str] = None
    deferred: Optional[bool] = False
    unrendered_config: Optional[Dict[str, Any]] = {}
    created_at: Optional[float] = 1696465994.420199
    config_call_dict: Optional[Dict[str, Any]] = {}
    relation_name: Optional[str] = None
    raw_code: Optional[str] = ""
    root_path: Optional[str] = None
    depends_on: Optional[MacroDependsOn] = Field(
        default_factory=lambda: MacroDependsOn.model_validate({"macros": []})
    )
    defer_relation: Optional[DeferRelation] = None
