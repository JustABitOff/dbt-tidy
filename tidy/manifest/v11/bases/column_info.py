from typing import Optional, List, Dict, Any

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v11.bases.enums import ConstraintType


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
    meta: Optional[Dict[str, Any]] = None
    data_type: Optional[str] = None
    constraints: Optional[List[ColumnLevelConstraint]] = None
    quote: Optional[bool] = None
    tags: Optional[List[str]] = None
    field_extra: Optional[Dict[str, Any]] = Field(None, alias="_extra")
