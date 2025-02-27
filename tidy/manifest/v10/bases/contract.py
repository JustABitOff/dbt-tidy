from typing import Optional
from pydantic import BaseModel, ConfigDict


class Contract(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    enforced: Optional[bool] = False
    checksum: Optional[str] = None
