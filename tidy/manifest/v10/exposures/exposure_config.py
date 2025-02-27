from typing import Optional

from pydantic import BaseModel, ConfigDict


class ExposureConfig(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    enabled: Optional[bool] = True
