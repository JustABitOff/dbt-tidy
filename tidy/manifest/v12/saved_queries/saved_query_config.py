from typing import Optional, Dict, Any

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v12.bases.enums import ExportAs


class SavedQueryCache(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    enabled: Optional[bool] = False


class SavedQueryConfig(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    field_extra: Optional[Dict[str, Any]] = Field(None, alias="_extra")
    enabled: Optional[bool] = True
    group: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
    export_as: Optional[ExportAs] = None
    schema_: Optional[str] = Field(None, alias="schema")
    cache: Optional[SavedQueryCache] = Field(None, title="SavedQueryCache")
