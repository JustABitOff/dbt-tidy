import pytest
from unittest.mock import MagicMock

from tidy.manifest import ManifestWrapper
from tidy.manifest.v12.nodes.models.model import Model
from tidy.sweeps.base import CheckResult, CheckStatus, sweep
from tidy.sweeps.modeling.direct_join_to_source import direct_join_to_source


def test_direct_join_to_source_fail():
    mock_manifest = MagicMock(
        nodes={
            "node_one": MagicMock(
                resource_type="model",
                unique_id="package.node_one",
                depends_on=MagicMock(
                    nodes=[
                        "source.source",
                        "model.model",
                    ]
                )
            )
        }
    )

    result = direct_join_to_source(mock_manifest)

    expected = CheckResult(
        name=direct_join_to_source.__sweep_name__,
        status=CheckStatus.FAIL,
        nodes=[mock_manifest.nodes.get("node_one").unique_id],
    )
    
    assert result == expected


def test_direct_join_to_source_pass():
    mock_manifest = MagicMock(
        nodes={
            "node_one": MagicMock(
                resource_type="model",
                unique_id="package.node_one",
                depends_on=MagicMock(
                    nodes=[
                        "model.model_two",
                        "model.model",
                    ]
                )
            )
        }
    )

    result = direct_join_to_source(mock_manifest)

    expected = CheckResult(
        name=direct_join_to_source.__sweep_name__,
        status=CheckStatus.PASS,
        nodes=[],
    )
    
    assert result == expected