from pydantic import BaseModel, ConfigDict


class WhereFilter(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    where_sql_template: str
