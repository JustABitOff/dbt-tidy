from typing import Optional, List, Union

from pydantic import BaseModel, ConfigDict


class UnitTestNodeVersions(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    include: Optional[List[Union[str, float]]] = None
    exclude: Optional[List[Union[str, float]]] = None
