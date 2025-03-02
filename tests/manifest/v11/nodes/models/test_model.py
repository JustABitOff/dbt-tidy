from tidy.manifest.v11.nodes.models.model import Model


def test_config_block_extraction():
    raw_code = """
    {{ config(materialized='view', schema='analytics') }}
    SELECT * FROM some_table
    """

    model = Model(
        schema="public",
        name="test_model",
        resource_type="model",
        package_name="my_package",
        path="models/test_model.sql",
        original_file_path="models/test_model.sql",
        unique_id="model.my_package.test_model",
        fqn=["my_package", "test_model"],
        alias="test_model",
        checksum={"name": "sha256", "checksum": "dummy_hash"},
        raw_code=raw_code,
    )

    expected_config = {"materialized": "view", "schema": "analytics"}
    assert model.config_block == expected_config


def test_config_block_no_config_call():
    raw_code = "SELECT * FROM some_table"

    model = Model(
        schema="public",
        name="test_model",
        resource_type="model",
        package_name="my_package",
        path="models/test_model.sql",
        original_file_path="models/test_model.sql",
        unique_id="model.my_package.test_model",
        fqn=["my_package", "test_model"],
        alias="test_model",
        checksum={"name": "sha256", "checksum": "dummy_hash"},
        raw_code=raw_code,
    )

    assert model.config_block is None
