from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class MacroDependsOn(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    macros: Optional[List[str]] = None
