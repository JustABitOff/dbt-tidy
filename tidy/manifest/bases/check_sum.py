from pydantic import BaseModel


class Checksum(BaseModel):
    name: str | None = None
    checksum: str | None = None