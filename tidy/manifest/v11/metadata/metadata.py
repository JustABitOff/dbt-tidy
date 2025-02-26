from typing import Dict, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ManifestMetadata(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    dbt_schema_version: Optional[str] = None
    dbt_version: Optional[str] = "1.7.14"
    generated_at: Optional[str] = None
    invocation_id: Optional[str] = None
    env: Optional[Dict[str, str]] = None
    project_name: Optional[str] = Field(None, description="Name of the root project")
    project_id: Optional[str] = Field(
        None,
        description="A unique identifier for the project, hashed from the project name",
    )
    user_id: Optional[UUID] = Field(
        None, description="A unique identifier for the user"
    )
    send_anonymous_usage_stats: Optional[bool] = Field(
        None, description="Whether dbt is configured to send anonymous usage statistics"
    )
    adapter_type: Optional[str] = Field(
        None, description="The type name of the adapter"
    )
