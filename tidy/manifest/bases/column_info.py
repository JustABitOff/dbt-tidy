from typing import Literal, List, Dict, Any

from pydantic import BaseModel, ConfigDict

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