import pytest
from pathlib import Path
from unittest.mock import MagicMock

from tidy.config.tidy_config import TidyConfig


@pytest.fixture
def tidy_config_fixture():
    config = MagicMock(spec=TidyConfig)
    config.custom_sweeps_path = Path(".mock_tidy")
    config.manifest_path = "mock_target/manifest.json"
    config.mode = "all"
    config.sweeps = []
    config.load_from_yaml.return_value = "Mocked load behavior"

    return config
