from pydantic import BaseModel, ConfigDict


class InjectedCTE(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: str
    sql: str
