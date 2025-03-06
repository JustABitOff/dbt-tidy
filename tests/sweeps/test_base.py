from tidy.manifest.utils.types import ManifestType
from tidy.sweeps.base import sweep, CheckResult, CheckStatus


def test_sweep_decorator_pass():
    @sweep("test_sweep")
    def mock_sweep(manifest: ManifestType):
        return []

    result = mock_sweep(None)

    assert isinstance(result, CheckResult)
    assert result.name == "test_sweep"
    assert result.status == CheckStatus.PASS
    assert result.nodes == []


def test_sweep_decorator_fail():
    @sweep("test_sweep_fail")
    def mock_sweep_fail(manifest: ManifestType):
        return ["node_1", "node_2"]

    result = mock_sweep_fail(None)

    assert isinstance(result, CheckResult)
    assert result.name == "test_sweep_fail"
    assert result.status == CheckStatus.FAIL
    assert result.nodes == ["node_1", "node_2"]


def test_sweep_decorator_metadata():
    @sweep("metadata_sweep")
    def mock_sweep(manifest: ManifestType):
        return []

    assert hasattr(mock_sweep, "__is_sweep__")
    assert hasattr(mock_sweep, "__sweep_name__")
    assert mock_sweep.__is_sweep__ is True
    assert mock_sweep.__sweep_name__ == "metadata_sweep"
