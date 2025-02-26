from typing import Optional, Dict, Any

from pydantic import BaseModel, ConfigDict, Field


class Owner(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    field_extra: Optional[Dict[str, Any]] = Field(None, alias="_extra")
    email: Optional[str] = None
    name: Optional[str] = None
