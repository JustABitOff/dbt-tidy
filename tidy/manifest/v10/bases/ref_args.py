from typing import Optional, Union

from pydantic import BaseModel, ConfigDict


class RefArgs(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    package: Optional[str] = None
    version: Optional[Union[str, float]] = None
