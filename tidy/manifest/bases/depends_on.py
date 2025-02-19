from pydantic import BaseModel


class DependsOn(BaseModel):
    macros: list[str] = []
    nodes: list[str] = []
    