from pydantic import BaseModel


class CustomGranularity(BaseModel):
    name: str
    column_name: str | None = None


class TimeSpine(BaseModel):
    standard_granularity_column: str
    custom_granularities: list[CustomGranularity] = []
