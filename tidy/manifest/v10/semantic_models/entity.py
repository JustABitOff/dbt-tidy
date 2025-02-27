from typing import Optional

from pydantic import BaseModel, ConfigDict

from tidy.manifest.v10.bases.enums import EntityType


class Entity(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    type: EntityType
    description: Optional[str] = None
    label: Optional[str] = None
    role: Optional[str] = None
    expr: Optional[str] = None
