from typing import List, Optional, Dict, Any

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v11.bases.depends_on import DependsOn
from tidy.manifest.v11.bases.ref_args import RefArgs
from tidy.manifest.v11.bases.enums import ExposureType, Maturity, ResourceType
from tidy.manifest.v11.exposures.exposure_config import ExposureConfig
from tidy.manifest.v11.bases.owner import Owner


class Exposure(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    resource_type: ResourceType
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: List[str]
    type: ExposureType
    owner: Owner
    description: Optional[str] = ""
    label: Optional[str] = None
    maturity: Optional[Maturity] = None
    meta: Optional[Dict[str, Any]] = {}
    tags: Optional[List[str]] = []
    config: Optional[ExposureConfig] = Field(
        default_factory=lambda: ExposureConfig.model_validate({"enabled": True})
    )
    unrendered_config: Optional[Dict[str, Any]] = {}
    url: Optional[str] = None
    depends_on: Optional[DependsOn] = Field(
        default_factory=lambda: DependsOn.model_validate({"macros": [], "nodes": []})
    )
    refs: Optional[List[RefArgs]] = []
    sources: Optional[List[List[str]]] = []
    metrics: Optional[List[List[str]]] = []
    created_at: Optional[float] = 1696465994.422623
