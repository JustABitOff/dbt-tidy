from pathlib import Path
import click.testing
from unittest.mock import patch

from tidy.cli.cli import cli


class TestRootModelsPass:
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


class TestRootModelsFail:
    def test_manifestv10(
        self, manifestv10_root_models_fixture, tidy_config_fixture
    ):
        self._run_cli(
            mocked_manifest=manifestv10_root_models_fixture,
            tidy_config_fixture=tidy_config_fixture,
        )

    def test_manifestv11(
        self, manifestv11_root_models_fixture, tidy_config_fixture
    ):
        self._run_cli(
            mocked_manifest=manifestv11_root_models_fixture,
            tidy_config_fixture=tidy_config_fixture,
        )

    def test_manifestv12(
        self, manifestv12_root_models_fixture, tidy_config_fixture
    ):
        self._run_cli(
            mocked_manifest=manifestv12_root_models_fixture,
            tidy_config_fixture=tidy_config_fixture,
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
        
        assert result.exit_code == 1
