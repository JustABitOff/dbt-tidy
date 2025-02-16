from typing import Literal

from pydantic import BaseModel, ConfigDict


class Owner(BaseModel):
    email: str
    name: str

    model_config = ConfigDict(
        extra="allow",
    )


class Group(BaseModel):
    name: str
    resource_type: Literal["group"] = "group"
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    owner: Owner
