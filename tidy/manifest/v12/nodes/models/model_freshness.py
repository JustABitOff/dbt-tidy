from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v12.bases.enums import Period, DependsOn


class ModelBuildAfter(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    depends_on: Optional[DependsOn] = DependsOn.any
    count: Optional[int] = 0
    period: Optional[Period] = Period.hour


class ModelFreshness(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    build_after: Optional[ModelBuildAfter] = Field(None, title="ModelBuildAfter")
