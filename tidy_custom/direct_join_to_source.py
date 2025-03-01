from tidy.manifest.v12.manifest import WritableManifest
from tidy.sweeps.base import CheckResult, CheckStatus


def sweep(manifest: WritableManifest) -> CheckResult:
    failures = []

    for node in manifest.nodes.values():
        if node.resource_type == "model" and {"source", "model"}.issubset(
            {i.split(".")[0] for i in node.depends_on.nodes}
        ):
            failures.append(f"{node.unique_id}")

    return CheckResult(
        name="Direct Join to Source",
        status=CheckStatus.PASS if not failures else CheckStatus.FAIL,
        nodes=failures,
    )
