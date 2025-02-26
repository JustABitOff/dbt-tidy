from pydantic import BaseModel, ConfigDict


class FileHash(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    checksum: str
