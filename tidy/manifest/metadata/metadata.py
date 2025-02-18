from typing import Dict, Any
from pydantic import BaseModel


class Metadata(BaseModel):
    dbt_schema_version: str | None = None
    dbt_version: str | None = None
    generated_at: str | None = None
    invocation_id: str | None = None
    env: Dict[str, Any] = {}
    project_name: str | None = None
    project_id: str | None = None
    user_id: str | None = None
    send_anonymous_usage_stats: bool | None = None
    adapter_type: str | None = None
