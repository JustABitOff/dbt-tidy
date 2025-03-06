import pytest
import networkx as nx
from unittest.mock import MagicMock

from tidy.manifest.utils.dag import (
    build_dbt_graph_from_manifest,
    get_ancestors,
    get_descendants,
)


@pytest.fixture
def mock_manifest():
    manifest = MagicMock()

    manifest.parent_map = {
        "model_1": ["source_1", "source_2"],
        "model_2": ["source_3"],
        "model_3": ["model_1", "model_2"],
    }

    return manifest


@pytest.fixture
def graph():
    graph = nx.DiGraph()

    graph.add_edges_from(
        [
            ("source_1", "model_1"),
            ("source_2", "model_1"),
            ("source_3", "model_2"),
            ("model_1", "model_3"),
            ("model_2", "model_3"),
        ]
    )

    return graph


def test_build_dbt_graph_from_manifest(mock_manifest):
    graph = build_dbt_graph_from_manifest(mock_manifest)

    expected_nodes = {
        "model_1",
        "model_2",
        "model_3",
        "source_1",
        "source_2",
        "source_3",
    }

    expected_edges = {
        ("source_1", "model_1"),
        ("source_2", "model_1"),
        ("source_3", "model_2"),
        ("model_1", "model_3"),
        ("model_2", "model_3"),
    }

    assert isinstance(graph, nx.DiGraph)
    assert set(graph.nodes) == expected_nodes
    assert set(graph.edges) == expected_edges


def test_get_ancestors(graph):
    ancestors = get_ancestors(graph, "model_3")

    expected_ancestors = [
        ("source_1", 2),
        ("source_2", 2),
        ("source_3", 2),
        ("model_1", 1),
        ("model_2", 1),
    ]

    ancestors_sorted = sorted(ancestors, key=lambda x: x[0])
    expected_sorted = sorted(expected_ancestors, key=lambda x: x[0])

    assert ancestors_sorted == expected_sorted


def test_get_ancestors_no_ancestors(graph):
    ancestors = get_ancestors(graph, "source_1")

    assert ancestors == []


def test_get_descendants(graph):
    descendants = get_descendants(graph, "source_1")

    expected_descendants = [("model_1", 1), ("model_3", 2)]

    descendants_sorted = sorted(descendants, key=lambda x: x[0])
    expected_sorted = sorted(expected_descendants, key=lambda x: x[0])

    assert descendants_sorted == expected_sorted


def test_get_descendants_no_descendants(graph):
    descendants = get_descendants(graph, "model_3")

    assert descendants == []
