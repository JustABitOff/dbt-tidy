import networkx as nx

from tidy.manifest.utils.types import ManifestType


def build_dbt_graph_from_manifest(manifest: "ManifestType") -> nx.DiGraph:
    """Constructs a DAG from dbt manifest.json using the parent_map field."""

    DG = nx.DiGraph()

    all_nodes = set(manifest.parent_map.keys())
    for parents in manifest.parent_map.values():
        all_nodes.update(parents)

    DG.add_nodes_from(all_nodes)

    for child_id, parents in manifest.parent_map.items():
        DG.add_edges_from((parent_id, child_id) for parent_id in parents)

    return DG


def get_ancestors(graph: nx.DiGraph, node: str) -> list[tuple[str, int]]:
    """
    Returns a list of tuples where each tuple contains an ancestor node and
    the level of separation (shortest path length) from the ancestor to the given node.
    """
    return [
        (ancestor, nx.shortest_path_length(graph, ancestor, node))
        for ancestor in nx.ancestors(graph, node)
    ]


def get_descendants(graph: nx.DiGraph, node: str) -> list[tuple[str, int]]:
    """
    Returns a list of tuples where each tuple contains an ancestor node and
    the level of separation (shortest path length) from the ancestor to the given node.
    """
    return [
        (descendant, nx.shortest_path_length(graph, node, descendant))
        for descendant in nx.descendants(graph, node)
    ]
