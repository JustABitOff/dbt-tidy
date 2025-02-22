from typing import Union

from pydantic import BaseModel


class RefArgs(BaseModel):
    name: str = ""
    package: str | None = None
    version: Union[str, int, None] = None
