from typing import Optional

from pydantic import BaseModel, ConfigDict


class SourceConfig(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    enabled: Optional[bool] = True
