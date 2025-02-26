from typing import Optional, Dict, Any, List, Union

from pydantic import BaseModel, ConfigDict, Field


class UnitTestConfig(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    field_extra: Optional[Dict[str, Any]] = Field(None, alias="_extra")
    tags: Optional[Union[str, List[str]]] = None
    meta: Optional[Dict[str, Any]] = None
    enabled: Optional[bool] = True
