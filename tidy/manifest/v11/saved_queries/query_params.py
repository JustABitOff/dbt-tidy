from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from tidy.manifest.v11.bases.where_filter_intersection import WhereFilterIntersection


class QueryParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    metrics: List[str]
    group_by: List[str]
    where: Optional[WhereFilterIntersection] = None
