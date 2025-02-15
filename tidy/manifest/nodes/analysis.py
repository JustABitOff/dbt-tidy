from typing import Dict, List, Any, Literal
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
)


class Analysis(BaseModel):
    database: str | None = None
    schema_name: str | None = Field(None, alias="schema")
    name: str | None = None
    #TODO: Update resource type enum
    resource_type: Literal["analysis"] = "analysis"
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