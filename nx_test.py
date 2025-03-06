import json

import networkx as nx
from tidy.manifest import ManifestWrapper


def build_dbt_graph_from_manifest(manifest) -> nx.DiGraph:
    """Constructs a DAG from dbt manifest.json using the depends_on field."""
    
    G = nx.DiGraph()

    # Add nodes
    for unique_id, node in manifest.nodes.items():
        G.add_node(unique_id, name=node.name)

    # Add edges based on `depends_on.nodes` (parent → child)
    for unique_id, node in manifest.nodes.items():
        # breakpoint()
        if hasattr(node.depends_on, "nodes"):
            for parent_id in node.depends_on.nodes:
                if parent_id in manifest.nodes:  # Ensure parent exists in manifest
                    G.add_edge(parent_id, unique_id)

    return G


# with open("target/graph_summary.json", "r") as f:
#     graph_input = json.loads(f.read())["linked"]


# DG = nx.DiGraph()

# for node_id, node_data in graph_input.items():
#     DG.add_node(node_id, name=node_data["name"], type=node_data["type"])
#     for successor in node_data.get("succ", []):
#         DG.add_edge(node_id, str(successor)) 

manifest = ManifestWrapper.load("target/manifest.json")
graph = build_dbt_graph_from_manifest(manifest)

test_me = nx.descendants(graph, "model.supply_chain_target_state_data_model.pla_eopd_smry")
breakpoint()
counter = 0
for i in test_me:
    # breakpoint()
    if i.split(".")[0] == "model":
        print(graph.nodes[i])
        counter += 1

# print(f"final count: {counter}")


breakpoint()