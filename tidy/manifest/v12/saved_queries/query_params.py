from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from tidy.manifest.v12.bases.where_filter_intersection import WhereFilterIntersection


class QueryParams(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    metrics: List[str]
    group_by: List[str]
    where: Optional[WhereFilterIntersection] = None
    order_by: Optional[List[str]] = None
    limit: Optional[int] = None
