from tidy.sweeps.base import sweep

@sweep("Direct Join to Source")
def direct_join_to_source(manifest) -> list:
    failures = []

    for node in manifest.nodes.values():
        if node.resource_type == "model" and {"source", "model"}.issubset(
            {i.split(".")[0] for i in node.depends_on.nodes}
        ):
            failures.append(f"{node.unique_id}")

    return failures
