from typing import Optional

from pydantic import BaseModel, ConfigDict


class MacroArgument(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    type: Optional[str] = None
    description: Optional[str] = ""
