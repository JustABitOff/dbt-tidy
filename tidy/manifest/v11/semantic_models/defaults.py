from typing import Optional

from pydantic import BaseModel, ConfigDict


class Defaults(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    agg_time_dimension: Optional[str] = None
