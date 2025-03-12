from pathlib import Path
import click.testing
from unittest.mock import MagicMock, patch

from tidy.sweeps.base import sweep
from tidy.cli.cli import cli


@sweep("Passing Custom Sweep")
def passing_custom_sweep(manifest):
    return []


class TestSweepCommand:
    def test_manifestv10(self, manifestv10_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv10_fixture, tidy_config_fixture=tidy_config_fixture
        )

    def test_manifestv11(self, manifestv11_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv11_fixture, tidy_config_fixture=tidy_config_fixture
        )

    def test_manifestv12(self, manifestv12_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv12_fixture, tidy_config_fixture=tidy_config_fixture
        )

    @patch.object(
        Path, "rglob", lambda self, pattern: [(self / "mock_user_sweep_one.py")]
    )
    @patch.object(Path, "exists", lambda self: self == Path(".mock_tidy"))
    @patch("tidy.cli.commands.sweep.importlib.util.spec_from_file_location")
    @patch("importlib.util.module_from_spec")
    @patch("tidy.cli.commands.sweep.TidyConfig")
    @patch("tidy.manifest.ManifestWrapper.load", autospec=True)
    def _run_cli(
        self,
        mock_load_manifest,
        mock_tidy_config,
        mock_module_from_spec,
        mock_spec_from_file_location,
        mocked_manifest,
        tidy_config_fixture,
    ):
        runner = click.testing.CliRunner()

        mock_load_manifest.return_value = mocked_manifest

        result = runner.invoke(cli, ["sweep"])

        assert result.exit_code == 0


class TestIncludeOption:
    def test_manifestv10(self, manifestv10_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv10_fixture, tidy_config_fixture=tidy_config_fixture
        )

    def test_manifestv11(self, manifestv11_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv11_fixture, tidy_config_fixture=tidy_config_fixture
        )

    def test_manifestv12(self, manifestv12_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv12_fixture, tidy_config_fixture=tidy_config_fixture
        )

    @patch.object(
        Path, "rglob", lambda self, pattern: [(self / "mock_user_sweep_one.py")]
    )
    @patch.object(Path, "exists", lambda self: self == Path(".mock_tidy"))
    @patch("tidy.cli.commands.sweep.importlib.util.spec_from_file_location")
    @patch("importlib.util.module_from_spec")
    @patch("tidy.cli.commands.sweep.TidyConfig")
    @patch("tidy.manifest.ManifestWrapper.load", autospec=True)
    def _run_cli(
        self,
        mock_load_manifest,
        mock_tidy_config,
        mock_module_from_spec,
        mock_spec_from_file_location,
        mocked_manifest,
        tidy_config_fixture,
    ):
        runner = click.testing.CliRunner()

        mock_load_manifest.return_value = mocked_manifest

        result = runner.invoke(cli, ["sweep", "--include", "root_models"])

        assert result.exit_code == 0
        assert result.output == "Sweeping...\n\nRoot Models\nStatus: pass\n"


class TestExcludeOption:
    def test_manifestv10(self, manifestv10_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv10_fixture, tidy_config_fixture=tidy_config_fixture
        )

    def test_manifestv11(self, manifestv11_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv11_fixture, tidy_config_fixture=tidy_config_fixture
        )

    def test_manifestv12(self, manifestv12_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv12_fixture, tidy_config_fixture=tidy_config_fixture
        )

    @patch.object(
        Path, "rglob", lambda self, pattern: [(self / "mock_user_sweep_one.py")]
    )
    @patch.object(Path, "exists", lambda self: self == Path(".mock_tidy"))
    @patch("tidy.cli.commands.sweep.importlib.util.spec_from_file_location")
    @patch("importlib.util.module_from_spec")
    @patch("tidy.cli.commands.sweep.TidyConfig")
    @patch("tidy.manifest.ManifestWrapper.load", autospec=True)
    def _run_cli(
        self,
        mock_load_manifest,
        mock_tidy_config,
        mock_module_from_spec,
        mock_spec_from_file_location,
        mocked_manifest,
        tidy_config_fixture,
    ):
        runner = click.testing.CliRunner()

        mock_load_manifest.return_value = mocked_manifest

        result = runner.invoke(cli, ["sweep", "--exclude", "root_models"])

        assert result.exit_code == 0
        assert "Root Models" not in result.output


class TestManifestOption:
    def test_manifestv10(self, manifestv10_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv10_fixture, tidy_config_fixture=tidy_config_fixture
        )

    def test_manifestv11(self, manifestv11_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv11_fixture, tidy_config_fixture=tidy_config_fixture
        )

    def test_manifestv12(self, manifestv12_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv12_fixture, tidy_config_fixture=tidy_config_fixture
        )

    @patch.object(
        Path, "rglob", lambda self, pattern: [(self / "mock_user_sweep_one.py")]
    )
    @patch.object(Path, "exists", lambda self: self == Path(".mock_tidy"))
    @patch("tidy.cli.commands.sweep.importlib.util.spec_from_file_location")
    @patch("importlib.util.module_from_spec")
    @patch("tidy.cli.commands.sweep.TidyConfig")
    @patch("tidy.manifest.ManifestWrapper.load", autospec=True)
    def _run_cli(
        self,
        mock_load_manifest,
        mock_tidy_config,
        mock_module_from_spec,
        mock_spec_from_file_location,
        mocked_manifest,
        tidy_config_fixture,
    ):
        runner = click.testing.CliRunner()

        mock_load_manifest.return_value = mocked_manifest

        result = runner.invoke(
            cli, ["sweep", "--manifest-path", "./some/folder/manifest.json"]
        )

        assert result.exit_code == 0


class TestUserSweeps:
    def test_manifestv10(self, manifestv10_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv10_fixture, tidy_config_fixture=tidy_config_fixture
        )

    def test_manifestv11(self, manifestv11_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv11_fixture, tidy_config_fixture=tidy_config_fixture
        )

    def test_manifestv12(self, manifestv12_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv12_fixture, tidy_config_fixture=tidy_config_fixture
        )

    @patch.object(
        Path, "rglob", lambda self, pattern: [(self / "mock_user_sweep_one.py")]
    )
    @patch.object(Path, "exists", lambda self: self == Path(".mock_tidy"))
    @patch("tidy.cli.commands.sweep.importlib.util.spec_from_file_location")
    @patch("importlib.util.module_from_spec")
    @patch("tidy.cli.commands.sweep.TidyConfig")
    @patch("tidy.manifest.ManifestWrapper.load", autospec=True)
    def _run_cli(
        self,
        mock_load_manifest,
        mock_tidy_config,
        mock_module_from_spec,
        mock_spec_from_file_location,
        mocked_manifest,
        tidy_config_fixture,
    ):
        runner = click.testing.CliRunner()

        mock_spec = mock_spec_from_file_location.return_value
        mock_spec.loader.exec_module = MagicMock()
        mock_module = mock_module_from_spec.return_value
        setattr(mock_module, "passing_custom_sweep", passing_custom_sweep)

        mock_load_manifest.return_value = mocked_manifest
        mock_tidy_config.return_value = tidy_config_fixture

        result = runner.invoke(cli, ["sweep", "--include", "passing_custom_sweep"])

        assert result.exit_code == 0
        assert "Passing Custom Sweep" in result.output


class TestUserSweepsBadPath:
    def test_manifestv10(self, manifestv10_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv10_fixture, tidy_config_fixture=tidy_config_fixture
        )

    def test_manifestv11(self, manifestv11_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv11_fixture, tidy_config_fixture=tidy_config_fixture
        )

    def test_manifestv12(self, manifestv12_fixture, tidy_config_fixture):
        self._run_cli(
            mocked_manifest=manifestv12_fixture, tidy_config_fixture=tidy_config_fixture
        )

    @patch.object(Path, "exists", lambda self: False)
    @patch("tidy.cli.commands.sweep._import_module_from_path")
    @patch("tidy.cli.commands.sweep.importlib.util.spec_from_file_location")
    @patch("importlib.util.module_from_spec")
    @patch("tidy.cli.commands.sweep.TidyConfig")
    @patch("tidy.manifest.ManifestWrapper.load", autospec=True)
    def _run_cli(
        self,
        mock_load_manifest,
        mock_tidy_config,
        mock_module_from_spec,
        mock_spec_from_file_location,
        mock_import_module_from_path,
        mocked_manifest,
        tidy_config_fixture,
    ):
        runner = click.testing.CliRunner()

        mock_spec = mock_spec_from_file_location.return_value
        mock_spec.loader.exec_module = MagicMock()
        mock_module = mock_module_from_spec.return_value
        setattr(mock_module, "passing_custom_sweep", passing_custom_sweep)

        mock_load_manifest.return_value = mocked_manifest
        mock_tidy_config.return_value = tidy_config_fixture

        result = runner.invoke(cli, ["sweep", "--include", "passing_custom_sweep"])

        assert result.exit_code == 0
        mock_import_module_from_path.assert_not_called()
