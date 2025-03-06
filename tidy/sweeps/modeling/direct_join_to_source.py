from tidy.sweeps.base import sweep
from tidy.manifest.utils.types import ManifestType


@sweep(
    name="Direct Join to Source",
    resolution="Read from the staging model instead of the source.",
)
def direct_join_to_source(manifest: ManifestType) -> list:
    failures = []

    for node in manifest.nodes.values():
        if node.resource_type == "model" and {"source", "model"}.issubset(
            {i.split(".")[0] for i in node.depends_on.nodes}
        ):
            failures.append(f"{node.unique_id}")

    return failures
