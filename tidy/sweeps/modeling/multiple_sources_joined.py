from collections import Counter

from tidy.sweeps.base import sweep
from tidy.manifest.utils.types import ManifestType


@sweep(
    name="Multiple Sources Joined",
    resolution="Ensure that each source has it's own staging model, and that down stream models reference the staging model instead of the source.",
)
def multiple_sources_joined(manifest: ManifestType) -> list:
    failures = []

    for node in manifest.nodes.values():
        if (
            node.resource_type == "model"
            and Counter(s.startswith("source.") for s in node.depends_on.nodes)[True]
            > 1
        ):
            failures.append(f"{node.unique_id}")

    return failures
