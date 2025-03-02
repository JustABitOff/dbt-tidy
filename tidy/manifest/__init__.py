from pathlib import Path
from pydantic import BaseModel
import json

from tidy.manifest.v10.manifest import ManifestV10
from tidy.manifest.v11.manifest import ManifestV11
from tidy.manifest.v12.manifest import ManifestV12

DBT_MANIFEST_VERSION_MAP = {
    "https://schemas.getdbt.com/dbt/manifest/v10.json": "ManifestV10",
    "https://schemas.getdbt.com/dbt/manifest/v11.json": "ManifestV11",
    "https://schemas.getdbt.com/dbt/manifest/v12.json": "ManifestV12",
}

MANIFEST_MODELS = {
    "ManifestV10": ManifestV10,
    "ManifestV11": ManifestV11,
    "ManifestV12": ManifestV12,
}


class MetadataModel(BaseModel):
    dbt_schema_version: str


class ManifestWrapper(BaseModel):
    """Wrapper to extract manifest version and load the correct model."""

    metadata: MetadataModel

    @classmethod
    def load(cls, manifest_path: Path):
        with open(manifest_path, "r") as f:
            metadata = json.loads(f.read())["metadata"]

        schema_url = metadata["dbt_schema_version"]
        model_name = DBT_MANIFEST_VERSION_MAP.get(schema_url)

        if model_name is None or model_name not in MANIFEST_MODELS:
            raise ValueError(f"Unsupported dbt manifest version: {schema_url}")

        ManifestModel = MANIFEST_MODELS[model_name]

        return ManifestModel.model_validate_json(Path(manifest_path).read_text())
