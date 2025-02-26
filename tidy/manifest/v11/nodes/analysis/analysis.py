from typing import Optional, Literal, List, Dict, Any

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v11.bases.file_hash import FileHash
from tidy.manifest.v11.bases.node_config import NodeConfig
from tidy.manifest.v11.bases.column_info import ColumnInfo
from tidy.manifest.v11.bases.docs import Docs
from tidy.manifest.v11.bases.ref_args import RefArgs
from tidy.manifest.v11.bases.depends_on import DependsOn
from tidy.manifest.v11.bases.contract import Contract
from tidy.manifest.v11.bases.injected_cte import InjectedCTE


class Analysis(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    database: Optional[str] = None
    schema_: str = Field(..., alias="schema")
    name: str
    resource_type: Literal["analysis"]
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: List[str]
    alias: str
    checksum: FileHash = Field(..., title="FileHash")
    config: Optional[NodeConfig] = Field(None, title="NodeConfig")
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
    language: Optional[str] = "sql"
    refs: Optional[List[RefArgs]] = None
    sources: Optional[List[List[str]]] = None
    metrics: Optional[List[List[str]]] = None
    depends_on: Optional[DependsOn] = Field(None, title="DependsOn")
    compiled_path: Optional[str] = None
    compiled: Optional[bool] = False
    compiled_code: Optional[str] = None
    extra_ctes_injected: Optional[bool] = False
    extra_ctes: Optional[List[InjectedCTE]] = None
    field_pre_injected_sql: Optional[str] = Field(None, alias="_pre_injected_sql")
    contract: Optional[Contract] = Field(None, title="Contract")
