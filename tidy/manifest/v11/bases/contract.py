from typing import Optional
from pydantic import BaseModel, ConfigDict


class Contract(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    enforced: Optional[bool] = False
    alias_types: Optional[bool] = True
    checksum: Optional[str] = None
