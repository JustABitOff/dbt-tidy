from typing import Dict, List, Any, Literal, Union
from pydantic import BaseModel, Field, ConfigDict


class Quoting(BaseModel):
    database: bool | None = None
    schema_name: bool | None = Field(None, alias="schema")
    identifier: bool | None = None
    column: bool | None = None


class Time(BaseModel):
    count: int | None = None
    period: Literal["minute", "hour", "day"] | None = None


class FreshnessThreshold(BaseModel):
    warn_after: Time | None = None
    error_after: Time | None = None
    filter: str | None = None


class ExternalPartition(BaseModel):
    name: str = ""
    description: str = ""
    data_type: str = ""
    meta: Dict[str, Any] = {}

    model_config = ConfigDict(
        extra='allow',
    )


class ExternalTable(BaseModel):
    location: str | None = None
    file_format: str | None = None
    row_format: str | None = None
    tbl_properties: str | None = None
    partitions: Union[List[str], List[ExternalPartition], None] = None

    model_config = ConfigDict(
        extra='allow',
    )


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
    granularity: Literal[
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

    model_config = ConfigDict(
        extra='allow',
    )


class SourceConfig(BaseModel):
    enabled: bool = True
    event_time: Dict[str, Any] | None = None

    model_config = ConfigDict(
        extra='allow',
    )


class Source(BaseModel):
    database: str | None = None
    schema_name: str | None = Field(None, alias="schema")
    name: str | None = None
    #TODO: Update resource type enum
    resource_type: str | None = None
    package_name: str | None = None
    path: str | None = None
    original_file_path: str | None = None
    unique_id: str | None = None
    fqn: List[str] | None = None
    source_name: str
    source_description: str
    loader: str
    identifier: str
    quoting: Quoting
    loaded_at_field: str | None = None
    loaded_at_query: str | None = None
    freshness: FreshnessThreshold | None = None
    external: ExternalTable | None = None
    description: str | None = None
    columns: ColumnInfo | None = None
    meta: Dict[str, Any] = {}
    source_meta: Dict[str, Any] = {}
    tags: List[str] = []
    config: SourceConfig | None = None
    patch_path: str | None = None
    unrendered_config: Dict[str, Any] = {}
    relation_name: str | None = None
    created_at: int
    unrendered_database: str | None = None
    unrendered_schema: str | None = None
