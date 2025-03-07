import pytest
import pathlib
import types
import click.testing
from unittest.mock import MagicMock, patch, mock_open

from tidy.manifest import ManifestWrapper
from tidy.sweeps.base import CheckResult, CheckStatus, sweep
from tidy.cli.cli import discover_and_run_checks, import_module_from_path, cli


@pytest.fixture
def mock_manifest():
    return MagicMock(spec=ManifestWrapper)


@pytest.fixture
def mock_check_result():
    return CheckResult(
        name="test_check",
        status=CheckStatus.FAIL,
        nodes=["node_1"],
        resolution="resolve this.",
    )


@patch("tidy.cli.cli.importlib.util.spec_from_file_location")
@patch("tidy.cli.cli.importlib.util.module_from_spec")
def test_import_module_from_path(mock_module_from_spec, mock_spec_from_file_location):
    mock_spec = mock_spec_from_file_location.return_value
    mock_spec.loader.exec_module = MagicMock()
    mock_module = mock_module_from_spec.return_value

    module = import_module_from_path("test_module", "/path/to/module.py")

    assert mock_spec_from_file_location.called
    assert mock_module_from_spec.called
    assert module is mock_module


@patch("importlib.import_module")
@patch("pkgutil.walk_packages")
@patch("importlib.resources.files")
def test_discover_and_run_checks(mock_files, mock_walk_packages, mock_import_module):
    fake_path = pathlib.Path("/mock/sweeps")
    mock_files.return_value = fake_path

    mock_walk_packages.return_value = [(None, "tidy.sweeps", False)]

    @sweep("Builtin Check")
    def builtin_check(manifest):
        return ["node_1"]

    @sweep("Builtin Check Two")
    def builtin_check_two(manifest):
        return ["node_1"]

    mock_module = types.ModuleType("mock_builtin_module")
    setattr(mock_module, "builtin_check", builtin_check)
    setattr(mock_module, "builtin_check_two", builtin_check_two)

    mock_import_module.return_value = mock_module

    results = discover_and_run_checks(
        mock_manifest, check_names=["builtin_check", "builtin_check_two"]
    )

    mock_import_module.assert_called_with("tidy.sweeps")

    assert len(results) == 2
    assert results[0].name == "Builtin Check"
    assert results[0].status == CheckStatus.FAIL
    assert results[0].nodes == ["node_1"]
    assert results[1].name == "Builtin Check Two"
    assert results[1].status == CheckStatus.FAIL
    assert results[1].nodes == ["node_1"]


@patch("tidy.cli.cli.USER_CHECKS_PATH", new=pathlib.Path("/mocked/path/.tidy"))
@patch("tidy.cli.cli.pathlib.Path.exists", return_value=True)
@patch("tidy.cli.cli.pathlib.Path.rglob")
@patch("tidy.cli.cli.import_module_from_path")
def test_discover_and_run_checks_with_user_checks(
    mock_import_module_from_path, mock_rglob, mock_user_check_path
):
    mock_rglob.return_value = iter([pathlib.Path("/mocked/path/.tidy/user_check.py")])

    @sweep("user_check")
    def mock_sweep(manifest):
        return ["node_1"]

    mock_module = types.ModuleType("mock_module")
    setattr(mock_module, "user_check", mock_sweep)
    mock_import_module_from_path.return_value = mock_module

    results = discover_and_run_checks(mock_manifest, check_names=["mock_sweep"])
    
    mock_import_module_from_path.assert_called_with(
        "user_check", pathlib.Path("/mocked/path/.tidy/user_check.py")
    )
    assert len(results) == 1
    assert results[0].name == "user_check"
    assert results[0].status == CheckStatus.FAIL
    assert results[0].nodes == ["node_1"]


@patch("tidy.cli.cli.discover_and_run_checks")
@patch("tidy.cli.cli.ManifestWrapper.load")
def test_cli_sweep_command(
    mock_manifest_load,
    mock_discover_and_run_checks,
    mock_manifest,
    mock_check_result,
):
    runner = click.testing.CliRunner()
    mock_manifest_load.return_value = mock_manifest
    mock_discover_and_run_checks.return_value = [mock_check_result]

    result = runner.invoke(
        cli, ["sweep", "--manifest-path", "target/manifest.json"]
    )

    assert result.exit_code == 1
    assert "Sweeping..." in result.output
    assert "test_check" in result.output
    assert "Status: fail" in result.output
    assert "Nodes:" in result.output
    assert "node_1" in result.output
    assert "Resolution: " in result.output


@patch("pathlib.Path.open", new_callable=mock_open)
@patch("tidy.cli.cli.discover_and_run_checks")
@patch("tidy.cli.cli.ManifestWrapper.load")
def test_cli_sweep_command_output_file(
    mock_manifest_load,
    mock_discover_and_run_checks,
    mock_json_write,
    mock_manifest,
    mock_check_result,
):
    runner = click.testing.CliRunner()
    mock_manifest_load.return_value = mock_manifest
    mock_discover_and_run_checks.return_value = [mock_check_result]

    result = runner.invoke(cli, ["sweep", "--output-failures", "./test_fails.json"])

    mock_json_write.assert_called_once()
    assert result.exit_code == 1
