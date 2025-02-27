from typing import Optional

from pydantic import BaseModel, ConfigDict


class MetricConfig(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    enabled: Optional[bool] = True
    group: Optional[str] = None
