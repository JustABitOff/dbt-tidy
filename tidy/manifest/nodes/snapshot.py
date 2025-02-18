from typing import Dict, List, Any, Union, Literal
from pydantic import BaseModel, Field

from tidy.manifest.bases import (
    Checksum,
    ColumnInfo,
    DocsConfig,
    RefArgs,
    DependsOn,
    InjectedCte,
    ContractConfig,
    DeferRelation,
    BaseConfig,
)


class SnapshotMetaColumnNames(BaseModel):
    dbt_valid_to: str | None = None
    dbt_valid_from: str | None = None
    dbt_scd_id: str | None = None
    dbt_updated_at: str | None = None
    dbt_is_deleted: str | None = None


class SnapshotConfig(BaseConfig):
    materialized: str = "snapshot"
    strategy: str | None = None
    target_schema: str | None = None
    target_database: str | None = None
    updated_at: str | None = None
    check_cols: Union[str, List[str], None] = None
    snapshot_meta_column_names: SnapshotMetaColumnNames | None = None
    dbt_valid_to_current: str | None = None


class Snapshot(BaseModel):
    database: str | None = None
    schema_name: str | None = Field(None, alias="schema")
    name: str | None = None
    resource_type: Literal["snapshot"] = "snapshot"
    package_name: str | None = None
    path: str | None = None
    original_file_path: str | None = None
    unique_id: str | None = None
    fqn: List[str] | None = None
    alias: str | None = None
    checksum: Checksum | None = None
    config: SnapshotConfig | None = None
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
    defer_relation: DeferRelation | None = None
