from typing import Optional
from pydantic import BaseModel, ConfigDict


class Docs(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    show: Optional[bool] = True
    node_color: Optional[str] = None
