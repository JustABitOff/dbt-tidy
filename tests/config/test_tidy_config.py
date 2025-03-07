import pytest
from unittest.mock import patch, mock_open
from pathlib import Path
import yaml
from pydantic import ValidationError

from tidy.config.tidy_config import TidyConfig


@pytest.fixture
def mock_tidy_yaml():
    with patch("tidy.config.tidy_config.TIDY_CONFIG_PATH", new=Path("tidy.yaml")):
        yield

def yaml_content():
    return {
        "custom_sweeps_path": ".mock_custom_path",
        "manifest_path" : "mock/manifest.json",
        "mode": "include",
        "sweeps": ["a", "b"],
    }

@patch("pathlib.Path.exists", return_value=False)
def test_loads_default_values(mock_path_exists, mock_tidy_yaml):
    result = TidyConfig()

    result.custom_sweeps_path = Path("./.tidy")
    result.manifest_path = Path("./target/manifest.json")
    result.mode = "all"
    result.sweeps = []


@patch("tidy.config.tidy_config.Path.read_text")
@patch("yaml.safe_load")
@patch("tidy.config.tidy_config.Path.exists", return_value=True)
def test_loads_valid_yaml(mock_exists, mock_yaml_safe_load, mock_read_text, mock_tidy_yaml):
    mock_yaml_safe_load.return_value = yaml_content()

    config = TidyConfig()

    assert config.mode == "include"
    assert config.sweeps == ["a", "b"]
    assert config.custom_sweeps_path == Path(".mock_custom_path")
    assert config.manifest_path == Path("mock/manifest.json")


@patch("tidy.config.tidy_config.Path.read_text")
@patch("pathlib.Path.exists", return_value=True)
@patch("yaml.safe_load", side_effect=yaml.YAMLError("Invalid YAML"))
def test_invalid_yaml_format(mock_safe_load, mock_exists, mock_read_text):
    with pytest.raises(ValueError):
        TidyConfig()


def test_user_can_override_defaults():
    config = TidyConfig(mode="include", sweeps=["x"])

    assert config.mode == "include"
    assert config.sweeps == ["x"]
