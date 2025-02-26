from typing import Optional, Dict, Any

from pydantic import BaseModel, ConfigDict


class TestMetadata(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: Optional[str] = "test"
    kwargs: Optional[Dict[str, Any]] = None
    namespace: Optional[str] = None
