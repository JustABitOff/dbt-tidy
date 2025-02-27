from typing import Optional, List, Dict, Any

from pydantic import BaseModel, ConfigDict

from tidy.manifest.v10.bases.enums import ConstraintType


class ColumnLevelConstraint(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: ConstraintType
    name: Optional[str] = None
    expression: Optional[str] = None
    warn_unenforced: Optional[bool] = True
    warn_unsupported: Optional[bool] = True


class ColumnInfo(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    name: str
    description: Optional[str] = ""
    meta: Optional[Dict[str, Any]] = {}
    data_type: Optional[str] = None
    constraints: Optional[List[ColumnLevelConstraint]] = []
    quote: Optional[bool] = None
    tags: Optional[List[str]] = []
