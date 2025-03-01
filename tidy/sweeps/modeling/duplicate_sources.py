from collections import Counter

from tidy.manifest.v12.manifest import WritableManifest
from tidy.sweeps.base import CheckResult, CheckStatus


def sweep(manifest: WritableManifest) -> CheckResult:
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

    return CheckResult(
        name="Duplicates Sources",
        status=CheckStatus.PASS if not failures else CheckStatus.FAIL,
        nodes=failures,
    )
