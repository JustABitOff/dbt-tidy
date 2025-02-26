from typing import Optional

from pydantic import BaseModel, ConfigDict


class SnapshotMetaColumnNames(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    dbt_valid_to: Optional[str] = None
    dbt_valid_from: Optional[str] = None
    dbt_scd_id: Optional[str] = None
    dbt_updated_at: Optional[str] = None
    dbt_is_deleted: Optional[str] = None
