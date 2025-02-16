from typing import Dict, List, Any, Annotated, Union, Literal
from pydantic import BaseModel, Field, ConfigDict


class Checksum(BaseModel):
    name: str | None = None
    checksum: str | None = None


class Hook(BaseModel):
    sql: str
    transaction: bool = True
    index: int | None = None


class DocsConfig(BaseModel):
    show: bool = True
    node_color: str | None = None


class ContractConfig(BaseModel):
    enforced: bool = False
    alias_types: bool = True
    checksum: str | None = None


class ColumnLevelConstraint(BaseModel):
    type: Literal["check", "not_null", "unique", "primary_key", "foreign_key", "custom"]
    name: str | None = None
    expression: str | None = None
    warn_unenforced: bool = True
    warn_unsupported: bool = True
    to: str | None = None
    to_columns: List[str] = []


class ColumnInfo(BaseModel):
    name: str
    description: str = ""
    meta: Dict[str, Any] = {}
    data_type: str | None = None
    constraints: List[ColumnLevelConstraint] = []
    quote: bool | None = None
    tags: List[str] = []
    granularity: (
        Literal[
            "nanosecond",
            "microsecond",
            "millisecond",
            "second",
            "minute",
            "hour",
            "day",
            "week",
            "month",
            "quarter",
            "year",
        ]
        | None
    ) = None

    model_config = ConfigDict(
        extra="allow",
    )


class RefArgs(BaseModel):
    name: str = ""
    package: str | None = None
    version: Union[str, int, None] = None


class DependsOn(BaseModel):
    macros: List[str] = []
    nodes: List[str] = []


class InjectedCte(BaseModel):
    id: str
    sql: str


class CustomGranularity(BaseModel):
    name: str
    column_name: str | None = None


class TimeSpine(BaseModel):
    standard_granularity_column: str
    custom_granularities: List[CustomGranularity] = []


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
    post_hook: List[Hook] = Field([], alias="post-hook")
    pre_hook: List[Hook] = Field([], alias="pre-hook")
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
    )


class NodeConfig(BaseConfig):
    access: Literal["private", "protected", "public"] = "public"


class DeferRelation(BaseModel):
    database: str | None = None
    schema_name: str | None = Field(None, alias="schema")
    alias: str | None = None
    relation_name: str | None = None
    resource_type: str | None = None
    name: str | None = None
    description: str = ""
    compiled_code: str | None = None
    meta: Dict[str, Any] = {}
    tags: List[Any] = []
    config: NodeConfig | None = None
