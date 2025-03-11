import pytest
from pathlib import Path
import types
import click.testing
from unittest.mock import MagicMock, patch, mock_open

from tidy.sweeps.base import CheckResult, CheckStatus, sweep
from tidy.cli.commands.sweep import _import_module_from_path
from tidy.cli.cli import cli
from tidy.config.tidy_config import TidyConfig
from tidy.manifest.v10.nodes.models.model import (
    ModelNode as ModelV10,
)
from tidy.manifest.v10.bases.depends_on import (
    DependsOn as DependsOnV10,
)
from tidy.manifest.v10.bases.file_hash import FileHash as FileHashV10
from tidy.manifest.v11.nodes.models.model import (
    Model as ModelV11,
)
from tidy.manifest.v11.bases.depends_on import (
    DependsOn as DependsOnV11,
)
from tidy.manifest.v11.bases.file_hash import FileHash as FileHashV11
from tidy.manifest.v12.nodes.models.model import (
    Model as ModelV12,
)
from tidy.manifest.v12.bases.depends_on import (
    DependsOn as DependsOnV12,
)
from tidy.manifest.v12.bases.file_hash import FileHash as FileHashV12


@pytest.fixture
def mock_tidy_config():
    mock_config = MagicMock(spec=TidyConfig)
    mock_config.mode = "all"
    mock_config.sweeps = []
    mock_config.custom_sweeps_path = Path(".tidy")
    
    with patch.object(TidyConfig, "load_from_yaml", return_value=None):
        yield mock_config


@pytest.fixture
def mock_manifestv10():
    return MagicMock(
        metadata={
            "project_name": "package"
        },
        nodes={
            "node_one": ModelV10(
                database="test_db",
                schema="test_schema",
                name="test",
                resource_type="model",
                package_name="test_package",
                path="/models/marts/test.sql",
                original_file_path="/models/marts/test.sql",
                unique_id="model.package.node_one",
                fqn=[
                    "package",
                    "node_one",
                ],
                alias="",
                checksum=FileHashV10(
                    name="test",
                    checksum="123abc",
                ),
                depends_on=DependsOnV10(
                    nodes=[
                        "source.package.source",
                        "model.package.model",
                    ]
                ),
            )
        }
    )


@pytest.fixture
def mock_check_result():
    return CheckResult(
        name="test_check",
        status=CheckStatus.FAIL,
        nodes=["model.package.node_1"],
        resolution="resolve this.",
    )


@patch("tidy.manifest.ManifestWrapper.load", autospec=True)
def test_sweep_manifestv10(mock_load_manifest, mock_manifestv10):
    runner = click.testing.CliRunner()
    
    mock_load_manifest.return_value = mock_manifestv10

    result = runner.invoke(
        cli, ["sweep"]
    )
    breakpoint()
    assert result.exit_code == 0


# @patch("tidy.cli.commands.sweep.importlib.util.spec_from_file_location")
# @patch("tidy.cli.commands.sweep.importlib.util.module_from_spec")
# def test_import_module_from_path(mock_module_from_spec, mock_spec_from_file_location):
#     mock_spec = mock_spec_from_file_location.return_value
#     mock_spec.loader.exec_module = MagicMock()
#     mock_module = mock_module_from_spec.return_value

#     module = _import_module_from_path("test_module", "/path/to/module.py")

#     assert mock_spec_from_file_location.called
#     assert mock_module_from_spec.called
#     assert module is mock_module


# @patch("tidy.manifest.ManifestWrapper.load", autospec=True)
# @patch("importlib.import_module")
# @patch("pkgutil.walk_packages")
# @patch("importlib.resources.files")
# def test_discover_and_run_checks(mock_files, mock_walk_packages, mock_import_module, mock_load_manifest):
#     runner = click.testing.CliRunner()
#     fake_path = Path("/mock/sweeps")
#     mock_files.return_value = fake_path

#     mock_walk_packages.return_value = [(None, "tidy.sweeps", False)]

#     @sweep("Builtin Check")
#     def builtin_check(manifest):
#         return ["node_1"]

#     @sweep("Builtin Check Two")
#     def builtin_check_two(manifest):
#         return ["node_1"]

#     mock_module = types.ModuleType("mock_builtin_module")
#     setattr(mock_module, "builtin_check", builtin_check)
#     setattr(mock_module, "builtin_check_two", builtin_check_two)

#     mock_import_module.return_value = mock_module

#     result = runner.invoke(
#         cli, ["sweep", "--sweeps", "builtin_check", "builtin_check_two"]
#     )

#     mock_import_module.assert_called_with("tidy.sweeps")

#     assert result.exit_code == 1
#     assert "Builtin Check" in result.output
#     assert "Builtin Check Two" in result.output


# @patch("tidy.cli.commands.sweep._discover_and_run_checks")
# @patch("tidy.cli.commands.sweep.ManifestWrapper.load")
# def test_cli_sweep_command(
#     mock_manifest_load,
#     mock_discover_and_run_checks,
#     monkeypatch,
#     mock_manifest,
#     mock_check_result,
#     mock_tidy_config
# ):
#     runner = click.testing.CliRunner()
#     monkeypatch.setattr("tidy.cli.commands.sweep.TidyConfig", mock_tidy_config)
#     mock_manifest_load.return_value = mock_manifest
#     mock_discover_and_run_checks.return_value = [mock_check_result]

#     result = runner.invoke(cli, ["sweep", "--manifest-path", "target/manifest.json"])

#     assert result.exit_code == 1
#     assert "Sweeping..." in result.output
#     assert "test_check" in result.output
#     assert "Status: fail" in result.output
#     assert "Nodes:" in result.output
#     assert "node_1" in result.output
#     assert "Resolution: " in result.output


# @patch("pathlib.Path.open", new_callable=mock_open)
# @patch("tidy.cli.commands.sweep._discover_and_run_checks")
# @patch("tidy.cli.commands.sweep.ManifestWrapper.load")
# def test_cli_sweep_command_output_file(
#     mock_manifest_load,
#     mock_discover_and_run_checks,
#     mock_json_write,
#     monkeypatch,
#     mock_manifest,
#     mock_check_result,
#     mock_tidy_config
# ):
#     runner = click.testing.CliRunner()
#     monkeypatch.setattr("tidy.cli.commands.sweep.TidyConfig", mock_tidy_config)

#     mock_manifest_load.return_value = mock_manifest
#     mock_discover_and_run_checks.return_value = [mock_check_result]

#     result = runner.invoke(cli, ["sweep", "--output-failures", "./test_fails.json"])

#     mock_json_write.assert_called_once()
#     assert result.exit_code == 1


# @patch("pathlib.Path.open", new_callable=mock_open)
# @patch("tidy.cli.commands.sweep._discover_and_run_checks")
# @patch("tidy.cli.commands.sweep.ManifestWrapper.load")
# def test_cli_sweep_command_output_file_default(
#     mock_manifest_load,
#     mock_discover_and_run_checks,
#     mock_json_write,
#     monkeypatch,
#     mock_manifest,
#     mock_check_result,
#     mock_tidy_config,
# ):
#     runner = click.testing.CliRunner()
#     monkeypatch.setattr("tidy.cli.commands.sweep.TidyConfig", mock_tidy_config)
#     mock_manifest_load.return_value = mock_manifest
#     mock_discover_and_run_checks.return_value = [mock_check_result]

#     result = runner.invoke(cli, ["sweep", "--output-failures", "."])

#     mock_json_write.assert_called_once()
#     assert result.exit_code == 1
