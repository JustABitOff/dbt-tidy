from typing import Optional, Dict, Any, Union, List

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v11.bases.hook import Hook
from tidy.manifest.v11.bases.docs import Docs
from tidy.manifest.v11.bases.contract import Contract
from tidy.manifest.v11.bases.enums import OnConfigurationChange


class NodeConfig(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    field_extra: Optional[Dict[str, Any]] = Field(None, alias="_extra")
    enabled: Optional[bool] = True
    alias: Optional[str] = None
    schema_: Optional[str] = Field(None, alias="schema")
    database: Optional[str] = None
    tags: Optional[Union[List[str], str]] = None
    meta: Optional[Dict[str, Any]] = None
    group: Optional[str] = None
    materialized: Optional[str] = "view"
    incremental_strategy: Optional[str] = None
    persist_docs: Optional[Dict[str, Any]] = None
    post_hook: Optional[List[Hook]] = Field(None, alias="post-hook")
    pre_hook: Optional[List[Hook]] = Field(None, alias="pre-hook")
    quoting: Optional[Dict[str, Any]] = None
    column_types: Optional[Dict[str, Any]] = None
    full_refresh: Optional[bool] = None
    unique_key: Optional[Union[str, List[str]]] = None
    on_schema_change: Optional[str] = "ignore"
    on_configuration_change: Optional[OnConfigurationChange] = None
    grants: Optional[Dict[str, Any]] = None
    packages: Optional[List[str]] = None
    docs: Optional[Docs] = Field(None, title="Docs")
    contract: Optional[Contract] = Field(None, title="Contract")
