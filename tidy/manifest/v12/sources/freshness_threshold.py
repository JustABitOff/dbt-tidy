from typing import Optional

from pydantic import BaseModel, ConfigDict

from tidy.manifest.v12.bases.enums import Period


class Time(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    count: Optional[int] = None
    period: Optional[Period] = None


class FreshnessThreshold(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    warn_after: Optional[Time] = None
    error_after: Optional[Time] = None
    filter: Optional[str] = None
