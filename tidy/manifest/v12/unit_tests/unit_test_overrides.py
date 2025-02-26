from typing import Optional, Dict, Any

from pydantic import BaseModel, ConfigDict


class UnitTestOverrides(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    macros: Optional[Dict[str, Any]] = None
    vars: Optional[Dict[str, Any]] = None
    env_vars: Optional[Dict[str, Any]] = None
