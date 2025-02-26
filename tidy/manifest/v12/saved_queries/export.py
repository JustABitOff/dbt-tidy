from typing import Optional, Dict

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v12.bases.enums import ExportAs


class ExportConfig(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    export_as: ExportAs
    schema_name: Optional[str] = None
    alias: Optional[str] = None
    database: Optional[str] = None


class Export(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    config: ExportConfig = Field(..., title="ExportConfig")
    unrendered_config: Optional[Dict[str, str]] = None
