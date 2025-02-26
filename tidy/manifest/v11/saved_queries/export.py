from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v11.bases.enums import ExportAs


class ExportConfig(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    export_as: ExportAs
    schema_name: Optional[str] = None
    alias: Optional[str] = None


class Export(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    config: ExportConfig = Field(..., title="ExportConfig")
