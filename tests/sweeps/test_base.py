from tidy.manifest.utils.types import ManifestType
from tidy.sweeps.base import sweep, CheckResult, CheckStatus


# def test_sweep_decorator_pass():
#     @sweep("test_sweep")
#     def mock_sweep(manifest: ManifestType):
#         return []

#     result = mock_sweep(None)

#     assert isinstance(result, CheckResult)
#     assert result.name == "test_sweep"
#     assert result.status == CheckStatus.PASS
#     assert result.nodes == []


# def test_sweep_decorator_fail():
#     @sweep("test_sweep_fail")
#     def mock_sweep_fail(manifest: ManifestType):
#         return ["mode.package_name.node_1", "node_2"]

#     result = mock_sweep_fail(None)

#     assert isinstance(result, CheckResult)
#     assert result.name == "test_sweep_fail"
#     assert result.status == CheckStatus.FAIL
#     assert result.nodes == ["node_1", "node_2"]


# def test_sweep_decorator_metadata():
#     @sweep("metadata_sweep")
#     def mock_sweep(manifest: ManifestType):
#         return []

#     assert hasattr(mock_sweep, "__is_sweep__")
#     assert hasattr(mock_sweep, "__sweep_name__")
#     assert mock_sweep.__is_sweep__ is True
#     assert mock_sweep.__sweep_name__ == "metadata_sweep"


class TestSweepDecoratorPass:
    def test_manifestv10(self, manifestv10_fixture):
        self._sweep_decorator_pass(mocked_manifest=manifestv10_fixture)

    def test_manifestv11(self, manifestv11_fixture):
        self._sweep_decorator_pass(mocked_manifest=manifestv11_fixture)

    def test_manifestv12(self, manifestv12_fixture):
        self._sweep_decorator_pass(mocked_manifest=manifestv12_fixture)

    def _sweep_decorator_pass(self, mocked_manifest):
        @sweep("test_sweep")
        def mock_sweep(manifest: ManifestType):
            return []

        result = mock_sweep(mocked_manifest)

        assert isinstance(result, CheckResult)
        assert result.name == "test_sweep"
        assert result.status == CheckStatus.PASS
        assert result.nodes == []
        assert hasattr(mock_sweep, "__is_sweep__")
        assert hasattr(mock_sweep, "__sweep_name__")
        assert mock_sweep.__is_sweep__ is True
        assert mock_sweep.__sweep_name__ == "test_sweep"

class TestSweepDecoratorFail:
    def test_manifestv10(self, manifestv10_fixture):
        self._sweep_decorator_fail(mocked_manifest=manifestv10_fixture)

    def test_manifestv11(self, manifestv11_fixture):
        self._sweep_decorator_fail(mocked_manifest=manifestv11_fixture)

    def test_manifestv12(self, manifestv12_fixture):
        self._sweep_decorator_fail(mocked_manifest=manifestv12_fixture)

    def _sweep_decorator_fail(self, mocked_manifest):
        @sweep("test_sweep_fail")
        def mock_sweep_fail(manifest: ManifestType):
            return [
                f"model.{manifest.metadata.project_name}.node_1",
                f"model.{manifest.metadata.project_name}.node_2",
            ]

        result = mock_sweep_fail(mocked_manifest)

        assert isinstance(result, CheckResult)
        assert result.name == "test_sweep_fail"
        assert result.status == CheckStatus.FAIL
        assert result.nodes == [
            f"model.{mocked_manifest.metadata.project_name}.node_1",
            f"model.{mocked_manifest.metadata.project_name}.node_2",
        ]
        assert hasattr(mock_sweep_fail, "__is_sweep__")
        assert hasattr(mock_sweep_fail, "__sweep_name__")
        assert mock_sweep_fail.__is_sweep__ is True
        assert mock_sweep_fail.__sweep_name__ == "test_sweep_fail"