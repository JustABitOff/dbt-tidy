from typing import Dict, List, Any, Annotated, Union, Literal

from pydantic import BaseModel, Field, ConfigDict

from tidy.manifest.bases.hook import Hook
from tidy.manifest.bases.docs_config import DocsConfig
from tidy.manifest.bases.contract_config import ContractConfig


class BaseConfig(BaseModel):
    enabled: bool = True
    alias: str | None = None
    schema_name: str | None = Field(None, alias="schema")
    database: str | None = None
    tags: List[str] | None = None
    meta: Dict[str, Any] | None = None
    group: str | None = None
    materialized: str = "view"
    incremental_strategy: str | None = None
    batch_size: str | None = None
    lookback: Annotated[int, Field(strict=True, gt=0)] = 1
    begin: Any | None = None
    persist_docs: Dict[str, Any] | None = None
    post_hook: List[Hook] = Field(default_factory=list, alias="post-hook")
    pre_hook: List[Hook] = Field(default_factory=list, alias="pre-hook")
    quoting: Dict[str, Any] = {}
    column_types: Dict[str, Any] = {}
    full_refresh: bool | None = None
    unique_key: Union[None, str, List[str]] = None
    on_schema_change: str | None = "ignore"
    on_configuration_change: Literal["apply", "continue", "fail"] = "apply"
    grants: Dict[str, Any] = {}
    packages: List[str] = []
    docs: DocsConfig = DocsConfig()
    contract: ContractConfig = ContractConfig()
    event_time: Any | None = None
    concurrent_batches: bool = True

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
