from pydantic import BaseModel, ConfigDict

from tidy.manifest.v10.bases.owner import Owner
from tidy.manifest.v10.bases.enums import ResourceType


class Group(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    resource_type: ResourceType
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    owner: Owner
