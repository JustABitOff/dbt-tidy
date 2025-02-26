from typing import Optional, Dict, Any, Union, List

from pydantic import BaseModel, ConfigDict, Field


class Owner(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    field_extra: Optional[Dict[str, Any]] = Field(None, alias="_extra")
    email: Optional[Union[str, List[str]]] = None
    name: Optional[str] = None
