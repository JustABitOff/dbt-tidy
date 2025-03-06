from enum import StrEnum
from typing import Optional, List
from functools import wraps
from typing import Callable

from pydantic import BaseModel

from tidy.manifest.utils.types import ManifestType


class CheckStatus(StrEnum):
    PASS = "pass"
    FAIL = "fail"
    WARNING = "warning"


class CheckResult(BaseModel):
    name: str
    status: CheckStatus
    nodes: Optional[List[str]] = None


def sweep(name: str):
    """
    Decorator to standardize sweep functions.

    Args:
        name (str): The name of the check.

    Returns:
        Callable[[Callable[[ManifestType], list]], Callable[[ManifestType], CheckResult]]
    """

    def decorator(
        func: Callable[
            [ManifestType],
            list,
        ],
    ):
        @wraps(func)
        def wrapped_sweep(
            manifest: ManifestType,
        ) -> CheckResult:
            failures = func(manifest)
            return CheckResult(
                name=name,
                status=CheckStatus.PASS if not failures else CheckStatus.FAIL,
                nodes=failures,
            )

        wrapped_sweep.__is_sweep__ = True
        wrapped_sweep.__sweep_name__ = name

        return wrapped_sweep

    return decorator
