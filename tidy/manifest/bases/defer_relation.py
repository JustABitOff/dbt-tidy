from typing import Any

from pydantic import BaseModel, Field

from tidy.manifest.bases.node_config import NodeConfig


class DeferRelation(BaseModel):
    database: str | None = None
    schema_name: str | None = Field(None, alias="schema")
    alias: str | None = None
    relation_name: str | None = None
    resource_type: str | None = None
    name: str | None = None
    description: str = ""
    compiled_code: str | None = None
    meta: dict[str, Any] = {}
    tags: list[Any] = []
    config: NodeConfig | None = None