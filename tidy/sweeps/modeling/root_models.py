from collections import Counter

from tidy.sweeps.base import sweep
from tidy.manifest.utils.types import ManifestType


@sweep("Root Models")
def root_models(manifest: ManifestType) -> list:
    failures = []
    for node in manifest.nodes.values():
        if (
            node.resource_type == "model" 
            and not node.depends_on.nodes
        ):
            failures.append(f"{node.unique_id}")

    return failures
