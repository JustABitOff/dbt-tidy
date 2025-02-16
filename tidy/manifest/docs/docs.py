from typing import Dict, List, Any, Literal
from pydantic import BaseModel


class Documentation(BaseModel):
    name: str
    resource_type: Literal["doc"] = "doc"
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    block_contents: str
