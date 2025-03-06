from collections import Counter

from tidy.sweeps.base import sweep
from tidy.manifest.utils.types import ManifestType


@sweep(
    name="Model Fanout",
    resolution="Ensure that models do not have more than 3 direct children.",
)
def model_fanout(manifest: ManifestType) -> list:
    failures = []

    for key, value in manifest.child_map.items():
        if (
            key.startswith("model.")
            and Counter(s.startswith("model.") for s in value)[True] > 3
        ):
            failures.append(f"{key}")

    return failures
