from typing import Optional, List

from pydantic import BaseModel, ConfigDict

from tidy.manifest.v11.bases.enums import ConstraintType


class ModelLevelConstraint(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: ConstraintType
    name: Optional[str] = None
    expression: Optional[str] = None
    warn_unenforced: Optional[bool] = True
    warn_unsupported: Optional[bool] = True
    columns: Optional[List[str]] = []
