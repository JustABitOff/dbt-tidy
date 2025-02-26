from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v11.bases.owner import Owner


class Group(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    resource_type: Literal["group"]
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    owner: Owner = Field(..., title="Owner")
