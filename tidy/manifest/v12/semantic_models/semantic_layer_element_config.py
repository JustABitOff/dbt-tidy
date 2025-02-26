from typing import Optional, Dict, Any

from pydantic import BaseModel, ConfigDict


class SemanticLayerElementConfig(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    meta: Optional[Dict[str, Any]] = None
