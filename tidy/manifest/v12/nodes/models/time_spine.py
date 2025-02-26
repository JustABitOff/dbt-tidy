from typing import Optional, List

from pydantic import BaseModel, ConfigDict


class CustomGranularity(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    column_name: Optional[str] = None


class TimeSpine(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    standard_granularity_column: str
    custom_granularities: Optional[List[CustomGranularity]] = None
