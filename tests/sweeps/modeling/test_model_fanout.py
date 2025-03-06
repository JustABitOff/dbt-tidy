from unittest.mock import MagicMock

from tidy.sweeps.base import CheckResult, CheckStatus
from tidy.sweeps.modeling.model_fanout import model_fanout


def test_model_fanout_fail():
    mock_manifest = MagicMock(
        child_map={
            "model.mock_package.mock_parent_node": [
                "test.child_one",
                "test.child_two",
                "test.child_three",
                "model.child_one",
                "model.child_two",
                "model.child_three",
                "model.child_four",
            ]
        }
    )

    result = model_fanout(mock_manifest)

    expected = CheckResult(
        name=model_fanout.__sweep_name__,
        status=CheckStatus.FAIL,
        nodes=["model.mock_package.mock_parent_node"],
    )

    assert result == expected


def test_model_fanout_pass():
    mock_manifest = MagicMock(
        child_map={
            "model.mock_package.mock_parent_node": [
                "test.child_one",
                "test.child_two",
                "test.child_three",
                "model.child_one",
                "model.child_two",
            ]
        }
    )

    result = model_fanout(mock_manifest)

    expected = CheckResult(
        name=model_fanout.__sweep_name__,
        status=CheckStatus.PASS,
        nodes=[],
    )

    assert result == expected
