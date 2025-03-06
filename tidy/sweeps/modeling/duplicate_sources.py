from collections import Counter

from tidy.sweeps.base import sweep
from tidy.manifest.utils.types import ManifestType


@sweep(
    name="Duplicate Sources",
    resolution="Ensure that no more than one source definition points to an object in your database.",
)
def duplicate_sources(manifest: ManifestType) -> list:
    failures = []

    sources = [
        (source.unique_id, (source.database + "." + source.schema_ + "." + source.name))
        for source in manifest.sources.values()
    ]

    duplicate_sources = [
        source for source in sources if Counter(i[1] for i in sources)[source[1]] > 1
    ]

    for source in duplicate_sources:
        failures.append(f"{source[0]}")

    return failures
