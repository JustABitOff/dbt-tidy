from tidy.sweeps.base import sweep
from tidy.manifest.utils.types import ManifestType


@sweep(
    name="Source Fanout",
    resolution="Ensure that sources do not have more than 1 direct child.",
)
def source_fanout(manifest: ManifestType) -> list:
    failures = []

    for key, value in manifest.child_map.items():
        if (
            key.startswith("source.")
            and sum(s.startswith(("model.", "snapshot.")) for s in value) > 1
        ):
            failures.append(f"{key}")

    return failures
