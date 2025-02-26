from typing import Optional, Dict, List, Any

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v12.bases.node_config import NodeConfig
from tidy.manifest.v12.bases.enums import ResourceType


class DeferRelation(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    database: Optional[str] = None
    schema_: str = Field(..., alias="schema")
    alias: str
    relation_name: Optional[str] = None
    resource_type: ResourceType
    name: str
    description: str
    compiled_code: Optional[str] = None
    meta: Dict[str, Any]
    tags: List[str]
    config: Optional[NodeConfig] = None
