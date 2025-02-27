from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Quoting(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    database: Optional[bool] = None
    schema_: Optional[bool] = Field(None, alias="schema")
    identifier: Optional[bool] = None
    column: Optional[bool] = None
