from pydantic import BaseModel


class DocsConfig(BaseModel):
    show: bool = True
    node_color: str | None = None
    