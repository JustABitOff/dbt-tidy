import json
from pathlib import Path
from unittest.mock import mock_open, patch, MagicMock

import pytest

from tidy.manifest import ManifestWrapper
from tidy.manifest.v10.manifest import ManifestV10
from tidy.manifest.v11.manifest import ManifestV11
from tidy.manifest.v12.manifest import ManifestV12


VALID_MANIFEST_V10 = json.dumps(
    {
        "metadata": {
            "dbt_schema_version": "https://schemas.getdbt.com/dbt/manifest/v10.json"
        }
    }
)
VALID_MANIFEST_V11 = json.dumps(
    {
        "metadata": {
            "dbt_schema_version": "https://schemas.getdbt.com/dbt/manifest/v11.json"
        }
    }
)
VALID_MANIFEST_V12 = json.dumps(
    {
        "metadata": {
            "dbt_schema_version": "https://schemas.getdbt.com/dbt/manifest/v12.json"
        }
    }
)

INVALID_MANIFEST = json.dumps(
    {
        "metadata": {
            "dbt_schema_version": "https://schemas.getdbt.com/dbt/manifest/v99.json"
        },
        "nodes": {},
    }
)

MALFORMED_MANIFEST = "{ metadata: { dbt_schema_version: 'bad_format' } }"


@pytest.mark.parametrize(
    "mock_data, expected_model",
    [
        (VALID_MANIFEST_V10, ManifestV10),
        (VALID_MANIFEST_V11, ManifestV11),
        (VALID_MANIFEST_V12, ManifestV12),
    ],
)
@patch("builtins.open", new_callable=mock_open)
@patch.object(Path, "read_text")
@patch.object(
    ManifestV10, "model_validate_json", return_value=MagicMock(spec=ManifestV10)
)
@patch.object(
    ManifestV11, "model_validate_json", return_value=MagicMock(spec=ManifestV11)
)
@patch.object(
    ManifestV12, "model_validate_json", return_value=MagicMock(spec=ManifestV12)
)
def test_load_valid_manifest(
    mock_validate_v12,
    mock_validate_v11,
    mock_validate_v10,
    mock_read_text,
    mock_open,
    mock_data,
    expected_model,
):
    """Test that valid manifest versions load the correct model."""
    mock_open.return_value.read.return_value = mock_data
    mock_read_text.return_value = mock_data

    mock_validate = {
        ManifestV10: mock_validate_v10,
        ManifestV11: mock_validate_v11,
        ManifestV12: mock_validate_v12,
    }[expected_model]

    manifest = ManifestWrapper.load(Path("dummy/path"))

    assert isinstance(manifest, expected_model)
    mock_validate.assert_called_once()


@patch("builtins.open", new_callable=mock_open, read_data=INVALID_MANIFEST)
@patch.object(Path, "read_text", return_value=INVALID_MANIFEST)
def test_load_unsupported_manifest(mock_read_text, mock_open_file):
    with pytest.raises(ValueError, match="Unsupported dbt manifest version"):
        ManifestWrapper.load(Path("dummy/path"))


@patch("builtins.open", new_callable=mock_open, read_data=MALFORMED_MANIFEST)
@patch.object(Path, "read_text", return_value=MALFORMED_MANIFEST)
def test_load_malformed_manifest(mock_read_text, mock_open_file):
    with pytest.raises(json.JSONDecodeError):
        ManifestWrapper.load(Path("dummy/path"))
