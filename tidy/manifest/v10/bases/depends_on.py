from typing import Optional, List

from pydantic import BaseModel, ConfigDict


class DependsOn(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    macros: Optional[List[str]] = []
    nodes: Optional[List[str]] = []
