from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class DeferRelation(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    database: Optional[str] = None
    schema_: str = Field(..., alias="schema")
    alias: str
    relation_name: Optional[str] = None
