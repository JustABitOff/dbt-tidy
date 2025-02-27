from typing import Optional

from pydantic import BaseModel, ConfigDict


class Owner(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    email: Optional[str] = None
    name: Optional[str] = None
