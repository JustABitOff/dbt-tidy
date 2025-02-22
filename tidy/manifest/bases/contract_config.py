from pydantic import BaseModel


class ContractConfig(BaseModel):
    enforced: bool = False
    alias_types: bool = True
    checksum: str | None = None
