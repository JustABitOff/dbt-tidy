from typing import Literal, Any

from pydantic import BaseModel, ConfigDict

from tidy.manifest.bases import (
    RefArgs,
    DependsOn,
    Owner,
)


class ExposureConfig(BaseModel):
    enabled: bool = True

    model_config = ConfigDict(
        extra="allow",
    )


class Exposure(BaseModel):
    name: str
    resource_type: Literal["exposure"] = "exposure"
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: list[str]
    type: Literal[
        "dashboard",
        "notebook",
        "analysis",
        "ml",
        "application",
    ]
    owner: Owner = Owner()
    description: str = ""
    label: str | None = None
    maturity: (
        Literal[
            "low",
            "medium",
            "high",
        ]
        | None
    ) = None
    meta: dict[str, Any] = {}
    tags: list[str] = []
    config: ExposureConfig = ExposureConfig()
    unrendered_config: dict[str, Any] = {}
    url: str | None = None
    depends_on: DependsOn = DependsOn()
    refs: list[RefArgs] = []
    sources: list[list[str]] = []
    metrics: list[list[str]] = []
    created_at: float
