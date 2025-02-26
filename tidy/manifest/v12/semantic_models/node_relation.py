from typing import Optional

from pydantic import BaseModel, ConfigDict


class NodeRelation(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    alias: str
    schema_name: str
    database: Optional[str] = None
    relation_name: Optional[str] = ""
