import pytest
from tidy.manifest.v11.nodes.snapshots.snapshot import Snapshot
from tidy.manifest.v11.nodes.snapshots.snapshot_config import SnapshotConfig

def test_config_block_extraction():
    raw_code = """
    {{ config(materialized='view', schema='analytics') }}
    SELECT * FROM some_table
    """

    snapshot = Snapshot(
        schema="public",
        name="test_snapshot",
        resource_type="snapshot",
        package_name="my_package",
        path="snapshots/test_snapshot.sql",
        original_file_path="snapshots/test_snapshot.sql",
        unique_id="snapshot.my_package.test_snapshot",
        fqn=["my_package", "test_snapshot"],
        alias="test_snapshot",
        checksum={"name": "sha256", "checksum": "dummy_hash"},
        raw_code=raw_code,
        config=SnapshotConfig(),
    )

    expected_config = {"materialized": "view", "schema": "analytics"}
    assert snapshot.config_block == expected_config


def test_config_block_no_config_call():
    raw_code = "SELECT * FROM some_table"

    snapshot = Snapshot(
        schema="public",
        name="test_snapshot",
        resource_type="snapshot",
        package_name="my_package",
        path="snapshots/test_snapshot.sql",
        original_file_path="snapshots/test_snapshot.sql",
        unique_id="snapshot.my_package.test_snapshot",
        fqn=["my_package", "test_snapshot"],
        alias="test_snapshot",
        checksum={"name": "sha256", "checksum": "dummy_hash"},
        raw_code=raw_code,
        config=SnapshotConfig(),
    )

    assert snapshot.config_block is None
