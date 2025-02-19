from pydantic import BaseModel


class Hook(BaseModel):
    sql: str
    transaction: bool = True
    index: int | None = None