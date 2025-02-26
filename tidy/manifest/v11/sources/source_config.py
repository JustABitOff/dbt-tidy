from typing import Optional, Dict, Any

from pydantic import BaseModel, ConfigDict, Field


class SourceConfig(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    field_extra: Optional[Dict[str, Any]] = Field(None, alias="_extra")
    enabled: Optional[bool] = True
