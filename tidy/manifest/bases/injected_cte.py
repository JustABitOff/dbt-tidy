from pydantic import BaseModel


class InjectedCte(BaseModel):
    id: str
    sql: str
