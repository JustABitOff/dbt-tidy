from typing import Dict, List, Any
from pydantic import BaseModel, Field, ConfigDict

from tidy.manifest.nodes.base import (
    Checksum,
    ColumnInfo,
    DocsConfig,
    RefArgs,
    DependsOn,
    InjectedCte,
    ContractConfig,
    BaseConfig,
)


class TestMetadata(BaseModel):
    name: str = "test"
    kwargs: Dict[str, Any] = {}
    namespace: str | None = None

    
class TestConfig(BaseConfig):
    enabled: bool = True
    alias: str | None = None
    schema_name: str | None = Field(None, alias="schema")
    database: str | None = None
    tags: List[str] | None = None
    meta: Dict[str, Any] | None = None
    group: str | None = None
    materialized: str = "test"
    severity: str = Field("ERROR", pattern="^([Ww][Aa][Rr][Nn]|[Ee][Rr][Rr][Oo][Rr])$")
    store_errors: bool | None = None
    store_failures_as: str | None = None
    where: str | None = None
    limit: int | None = None
    fail_calc: str = "count(*)"
    warn_if: str = "!=0"
    error_if: str = "!=0"


class GenericTest(BaseModel):
    database: str | None = None
    schema_name: str | None = Field(None, alias="schema")
    name: str | None = None
    resource_type: str | None = None
    package_name: str | None = None
    path: str | None = None
    original_file_path: str | None = None
    unique_id: str | None = None
    fqn: List[str] | None = None
    alias: str | None = None
    checksum: Checksum | None = None
    config: TestConfig | None = None
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
    column_name: str | None = None
    file_key_name: str | None = None
    attached_node: str | None = None
    test_metadata: TestMetadata | None = None
