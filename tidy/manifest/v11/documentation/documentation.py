from typing import Literal

from pydantic import BaseModel, ConfigDict


class Documentation(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    resource_type: Literal["doc"]
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    block_contents: str
