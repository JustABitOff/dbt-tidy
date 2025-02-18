from typing import Dict, List, Any, Union, Literal
from pydantic import BaseModel, Field

from tidy.manifest.nodes.base import (
    Checksum,
    NodeConfig,
    ColumnInfo,
    DocsConfig,
    RefArgs,
    DependsOn,
    InjectedCte,
    ContractConfig,
    DeferRelation,
    TimeSpine,
)


class ModelLevelConstraint(BaseModel):
    type: Literal["check", "not_null", "unique", "primary_key", "foreign_key", "custom"]
    name: str | None = None
    expression: str | None = None
    warn_unenforced: bool = True
    warn_unsupported: bool = True
    to: str | None = None
    to_columns: List[str] = []
    columns: List[str] = []


class ModelBuildAfter(BaseModel):
    count: int = 0
    period: Literal["minute", "hour", "day"] = "hour"
    depends_on: Literal["all", "any"] = "any"


class ModelFreshness(BaseModel):
    build_after: ModelBuildAfter | None = None


class Model(BaseModel):
    database: str | None = None
    schema_name: str | None = Field(None, alias="schema")
    name: str | None = None
    resource_type: Literal["model"] = "model"
    package_name: str | None = None
    path: str | None = None
    original_file_path: str | None = None
    unique_id: str | None = None
    fqn: List[str] | None = None
    alias: str | None = None
    checksum: Checksum | None = None
    config: NodeConfig | None = None
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
    language: str = "sql"
    ref: List[RefArgs] = []
    sources: List[List[str]] = []
    metrics: List[List[str]] = []
    depends_on: DependsOn = DependsOn()
    compiled_path: str | None = None
    compiled: bool = False
    compiled_code: str | None = None
    extra_ctes_injected: bool = False
    extra_ctes: List[InjectedCte] = []
    contract: ContractConfig = {}
    access: Literal["private", "protected", "public"] = "public"
    constraints: List[ModelLevelConstraint] = []
    version: Union[str, int, None] = None
    latest_version: Union[str, int, None] = None
    deprecation_date: str | None = None
    defer_relation: DeferRelation | None = None
    primary_key: List[str] = []
    time_spine: TimeSpine | None = None
    freshness: ModelFreshness | None = None
