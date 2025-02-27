from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


class CheckStatus(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    WARNING = "warning"


class CheckResult(BaseModel):
    name: str
    status: CheckStatus
    details: Optional[List[str]] = None
    severity: Optional[str] = "info"