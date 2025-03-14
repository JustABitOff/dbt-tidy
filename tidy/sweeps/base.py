from enum import StrEnum
from typing import Optional, List
from functools import wraps
from typing import Callable

import click
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
        @click.pass_context
        @wraps(func)
        def wrapped_sweep(
            ctx, 
            manifest: ManifestType,
        ) -> CheckResult:
            failures = func(manifest)
            
            # TODO: Instead of post-filtering, we could filter the manifest before the sweep is run.
            if not ctx.params["dbt_unique_ids"]:
                return CheckResult(
                    name=name,
                    status=CheckStatus.PASS if not failures else CheckStatus.FAIL,
                    nodes=failures,
                    resolution=resolution if failures else None,
                )

            filtered_failures = [
                failure
                for failure in failures
                if (
                    failure.split(".")[1] == manifest.metadata.project_name
                    and failure in ctx.params["dbt_unique_ids"]
                )
            ]
            
            return CheckResult(
                name=name,
                status=CheckStatus.PASS if not filtered_failures else CheckStatus.FAIL,
                nodes=filtered_failures,
                resolution=resolution if filtered_failures else None,
            )

        wrapped_sweep.__is_sweep__ = True
        wrapped_sweep.__sweep_name__ = name
        wrapped_sweep.__resolution__ = resolution

        return wrapped_sweep

    return decorator
