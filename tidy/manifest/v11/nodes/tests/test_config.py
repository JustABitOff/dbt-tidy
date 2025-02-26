from typing import Optional, Dict, Any, Union, List

from pydantic import BaseModel, ConfigDict, Field


class TestConfig(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    field_extra: Optional[Dict[str, Any]] = Field(None, alias="_extra")
    enabled: Optional[bool] = True
    alias: Optional[str] = None
    schema_: Optional[str] = Field("dbt_test__audit", alias="schema")
    database: Optional[str] = None
    tags: Optional[Union[List[str], str]] = None
    meta: Optional[Dict[str, Any]] = None
    group: Optional[str] = None
    materialized: Optional[str] = "test"
    severity: Optional[str] = Field(
        "ERROR", pattern=r"^([Ww][Aa][Rr][Nn]|[Ee][Rr][Rr][Oo][Rr])$"
    )
    store_failures: Optional[bool] = None
    store_failures_as: Optional[str] = None
    where: Optional[str] = None
    limit: Optional[int] = None
    fail_calc: Optional[str] = "count(*)"
    warn_if: Optional[str] = "!= 0"
    error_if: Optional[str] = "!= 0"
