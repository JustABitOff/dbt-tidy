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
    resolution: Optional[str] = None


def sweep(name: str, resolution: Optional[str] = None):
    """
    Decorator to standardize sweep functions.

    Args:
        name (str): The name of the check.
        resolution (Optional[str]): The common resolution path for the failed sweep. Default is None.

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

            # TODO: Instead of post-filtering, we could filter the manifest before the sweep is run.
            failures = [
                failure 
                for failure in failures 
                if len(failure.split(".")) == 3
                and failure.split(".")[1] == manifest.metadata.project_name
            ]

            return CheckResult(
                name=name,
                status=CheckStatus.PASS if not failures else CheckStatus.FAIL,
                nodes=failures,
                resolution=resolution if failures else None,
            )

        wrapped_sweep.__is_sweep__ = True
        wrapped_sweep.__sweep_name__ = name
        wrapped_sweep.__resolution__ = resolution

        return wrapped_sweep

    return decorator
