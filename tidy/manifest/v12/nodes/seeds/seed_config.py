from typing import Optional, Dict, Any, Union, List

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v12.bases.hook import Hook
from tidy.manifest.v12.bases.docs import Docs
from tidy.manifest.v12.bases.contract import Contract
from tidy.manifest.v12.bases.enums import OnConfigurationChange


class SeedConfig(BaseModel):
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
    materialized: Optional[str] = "seed"
    incremental_strategy: Optional[str] = None
    batch_size: Optional[Any] = None
    lookback: Optional[Any] = 1
    begin: Optional[Any] = None
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
    event_time: Optional[Any] = None
    concurrent_batches: Optional[Any] = None
    delimiter: Optional[str] = ","
    quote_columns: Optional[bool] = None
