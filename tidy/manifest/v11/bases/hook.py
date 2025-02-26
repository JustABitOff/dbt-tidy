from typing import Optional
from pydantic import BaseModel, ConfigDict


class Hook(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    sql: str
    transaction: Optional[bool] = True
    index: Optional[int] = None
