from typing import Optional, Dict, Any, Union, List

from pydantic import BaseModel, ConfigDict, Field


class ExternalPartition(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    field_extra: Optional[Dict[str, Any]] = Field(None, alias="_extra")
    name: Optional[str] = ""
    description: Optional[str] = ""
    data_type: Optional[str] = ""
    meta: Optional[Dict[str, Any]] = None


class ExternalTable(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    field_extra: Optional[Dict[str, Any]] = Field(None, alias="_extra")
    location: Optional[str] = None
    file_format: Optional[str] = None
    row_format: Optional[str] = None
    tbl_properties: Optional[str] = None
    partitions: Optional[Union[List[str], List[ExternalPartition]]] = None
