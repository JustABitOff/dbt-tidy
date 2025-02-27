from typing import Optional, Dict, Any, Union, List

from pydantic import BaseModel, ConfigDict


class ExternalPartition(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    name: Optional[str] = ""
    description: Optional[str] = ""
    data_type: Optional[str] = ""
    meta: Optional[Dict[str, Any]] = {}


class ExternalTable(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    location: Optional[str] = None
    file_format: Optional[str] = None
    row_format: Optional[str] = None
    tbl_properties: Optional[str] = None
    partitions: Optional[Union[List[str], List[ExternalPartition]]] = None
