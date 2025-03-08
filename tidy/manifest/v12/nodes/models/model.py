from typing import Optional, Literal, List, Dict, Any, Union

from pydantic import BaseModel, ConfigDict, Field, computed_field

from tidy.manifest.v12.bases.file_hash import FileHash
from tidy.manifest.v12.bases.column_info import ColumnInfo
from tidy.manifest.v12.bases.docs import Docs
from tidy.manifest.v12.bases.ref_args import RefArgs
from tidy.manifest.v12.bases.depends_on import DependsOn
from tidy.manifest.v12.bases.injected_cte import InjectedCTE
from tidy.manifest.v12.bases.contract import Contract
from tidy.manifest.v12.bases.defer_relation import DeferRelation
from tidy.manifest.v12.bases.enums import Access
from tidy.manifest.v12.nodes.models.model_config import ModelConfig
from tidy.manifest.v12.nodes.models.model_level_constraint import ModelLevelConstraint
from tidy.manifest.v12.nodes.models.time_spine import TimeSpine
from tidy.manifest.v12.nodes.models.model_freshness import ModelFreshness
from tidy.manifest.utils.config_block import get_config_block


class Model(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    database: Optional[str] = None
    schema_: str = Field(..., alias="schema")
    name: str
    resource_type: Literal["model"]
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: List[str]
    alias: str
    checksum: FileHash = Field(..., title="FileHash")
    config: Optional[ModelConfig] = Field(None, title="ModelConfig")
    tags: Optional[List[str]] = None
    description: Optional[str] = ""
    columns: Optional[Dict[str, ColumnInfo]] = None
    meta: Optional[Dict[str, Any]] = None
    group: Optional[str] = None
    docs: Optional[Docs] = Field(None, title="Docs")
    patch_path: Optional[str] = None
    build_path: Optional[str] = None
    unrendered_config: Optional[Dict[str, Any]] = None
    created_at: Optional[float] = None
    config_call_dict: Optional[Dict[str, Any]] = None
    unrendered_config_call_dict: Optional[Dict[str, Any]] = None
    relation_name: Optional[str] = None
    raw_code: Optional[str] = ""
    doc_blocks: Optional[List[str]] = None
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
    access: Optional[Access] = Access.protected
    constraints: Optional[List[ModelLevelConstraint]] = None
    version: Optional[Union[str, float]] = None
    latest_version: Optional[Union[str, float]] = None
    deprecation_date: Optional[str] = None
    defer_relation: Optional[DeferRelation] = None
    primary_key: Optional[List[str]] = None
    time_spine: Optional[TimeSpine] = None
    freshness: Optional[ModelFreshness] = None

    @computed_field
    @property
    def config_block(self) -> Optional[Dict[str, Any]]:
        return get_config_block(self.raw_code)
