from typing import Literal, Union, Any

from pydantic import BaseModel, ConfigDict


class Owner(BaseModel):
    email: str | None = None
    name: str | None = None

    model_config = ConfigDict(
        extra="allow",
    )


class ExposureConfig(BaseModel):
    enabled: bool = True

    model_config = ConfigDict(
        extra="allow",
    )


class DependsOn(BaseModel):
    macros: list[str] = []
    nodes: list[str] = []


class RefArgs(BaseModel):
    name: str = ""
    package: str | None = None
    version: Union[str, int, None] = None


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
