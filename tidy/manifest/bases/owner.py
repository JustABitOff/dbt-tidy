from pydantic import BaseModel, ConfigDict


class Owner(BaseModel):
    email: str | None = None
    name: str | None = None

    model_config = ConfigDict(
        extra="allow",
    )
