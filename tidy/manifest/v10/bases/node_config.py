from typing import Optional, Dict, Any, Union, List

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v10.bases.hook import Hook
from tidy.manifest.v10.bases.docs import Docs
from tidy.manifest.v10.bases.contract import Contract
from tidy.manifest.v10.bases.enums import OnConfigurationChange


class NodeConfig(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    enabled: Optional[bool] = True
    alias: Optional[str] = None
    schema_: Optional[str] = Field(None, alias="schema")
    database: Optional[str] = None
    tags: Optional[Union[List[str], str]] = []
    meta: Optional[Dict[str, Any]] = {}
    group: Optional[str] = None
    materialized: Optional[str] = "view"
    incremental_strategy: Optional[str] = None
    persist_docs: Optional[Dict[str, Any]] = {}
    post_hook: Optional[List[Hook]] = Field([], alias="post-hook")
    pre_hook: Optional[List[Hook]] = Field([], alias="pre-hook")
    quoting: Optional[Dict[str, Any]] = {}
    column_types: Optional[Dict[str, Any]] = {}
    full_refresh: Optional[bool] = None
    unique_key: Optional[Union[str, List[str]]] = None
    on_schema_change: Optional[str] = "ignore"
    on_configuration_change: Optional[OnConfigurationChange] = "apply"
    grants: Optional[Dict[str, Any]] = {}
    packages: Optional[List[str]] = []
    docs: Optional[Docs] = Field(
        default_factory=lambda: Docs.model_validate({"show": True, "node_color": None})
    )
    contract: Optional[Contract] = Field(
        default_factory=lambda: Contract.model_validate({"enforced": False})
    )
