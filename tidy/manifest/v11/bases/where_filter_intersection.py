from typing import List

from pydantic import BaseModel, ConfigDict


class WhereFilter(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    where_sql_template: str


class WhereFilterIntersection(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    where_filters: List[WhereFilter]
