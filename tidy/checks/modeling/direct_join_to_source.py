from tidy.manifest.v12.manifest import WritableManifest
from tidy.checks.base import CheckResult, CheckStatus


def check_direct_join_to_source(manifest: WritableManifest) -> CheckResult:
    failures = []

    for node in manifest.nodes.values():
        if (
            node.resource_type == 'model'
            and 'model' and 'source' in set([i.split(".")[0] for i in node.depends_on.nodes])
        ):
            failures.append(f"Model '{node.name}' joins to both a source and another model.")

    return CheckResult(
        name="Direct Join to Source",
        status=CheckStatus.PASS if not failures else CheckStatus.FAIL,
        details=failures,
        severity="critical" if failures else "info"
    )