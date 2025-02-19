from typing import Literal

from pydantic import BaseModel, ConfigDict

from tidy.manifest.bases import Owner


class Group(BaseModel):
    name: str
    resource_type: Literal["group"] = "group"
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    owner: Owner
