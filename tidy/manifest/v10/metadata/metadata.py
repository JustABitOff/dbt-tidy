from datetime import datetime
from typing import Dict, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ManifestMetadata(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    dbt_schema_version: Optional[str] = (
        "https://schemas.getdbt.com/dbt/manifest/v10.json"
    )
    dbt_version: Optional[str] = "1.6.5"
    generated_at: Optional[datetime] = "2023-10-05T00:33:14.410024Z"
    invocation_id: Optional[UUID] = "603e2fae-9c7d-4d17-8530-7d28c9875263"
    env: Optional[Dict[str, str]] = {}
    project_name: Optional[str] = Field(None, description="Name of the root project")
    project_id: Optional[str] = Field(
        None,
        description="A unique identifier for the project, hashed from the project name",
    )
    user_id: Optional[UUID] = Field(
        None,
        pattern=r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
        description="A unique identifier for the user",
    )
    send_anonymous_usage_stats: Optional[bool] = Field(
        None, description="Whether dbt is configured to send anonymous usage statistics"
    )
    adapter_type: Optional[str] = Field(
        None, description="The type name of the adapter"
    )
