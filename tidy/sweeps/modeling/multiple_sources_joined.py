from collections import Counter

from tidy.sweeps.base import sweep
from tidy.manifest.utils.types import ManifestType


@sweep("Multiple Sources Joined")
def multiple_sources_joined(manifest: ManifestType) -> list:
    failures = []

    for node in manifest.nodes.values():
        if (
            node.resource_type == "model" 
            and Counter(s.startswith("source.") for s in node.depends_on.nodes)[True] > 1
        ):
            failures.append(f"{node.unique_id}")

    return failures
