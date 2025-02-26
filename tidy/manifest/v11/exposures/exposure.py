from typing import Literal, List, Optional, Dict, Any

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v11.bases.depends_on import DependsOn
from tidy.manifest.v11.bases.ref_args import RefArgs
from tidy.manifest.v11.bases.enums import ExposureType, Maturity
from tidy.manifest.v11.exposures.exposure_config import ExposureConfig
from tidy.manifest.v11.bases.owner import Owner


class Exposure(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    resource_type: Literal["exposure"]
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: List[str]
    type: ExposureType
    owner: Owner = Field(..., title="Owner")
    description: Optional[str] = ""
    label: Optional[str] = None
    maturity: Optional[Maturity] = None
    meta: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None
    config: Optional[ExposureConfig] = Field(None, title="ExposureConfig")
    unrendered_config: Optional[Dict[str, Any]] = None
    url: Optional[str] = None
    depends_on: Optional[DependsOn] = Field(None, title="DependsOn")
    refs: Optional[List[RefArgs]] = None
    sources: Optional[List[List[str]]] = None
    metrics: Optional[List[List[str]]] = None
    created_at: Optional[float] = None
