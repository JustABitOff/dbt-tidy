import pytest
from unittest.mock import MagicMock

from tidy.manifest.v12.sources.source_definition import SourceDefinition
from tidy.sweeps.base import CheckResult, CheckStatus
from tidy.sweeps.modeling.duplicate_sources import duplicate_sources


def test_duplicate_sources_fail():
    mock_manifest = MagicMock(
        sources={
            "source_one": SourceDefinition(
                database="mock_db",
                schema="mock_schema",
                name="mock_table",
                resource_type="source",
                package_name="mock_package",
                path="sources.mock",
                original_file_path="/sources/mock",
                unique_id="mock_package.source_one",
                fqn=[""],
                source_name="",
                source_description="",
                loader="",
                identifier="",
            ),
            "source_two": SourceDefinition(
                database="mock_db",
                schema="mock_schema",
                name="mock_table",
                resource_type="source",
                package_name="mock_package",
                path="sources.mock",
                original_file_path="/sources/mock",
                unique_id="mock_package.source_two",
                fqn=[""],
                source_name="",
                source_description="",
                loader="",
                identifier="",
            ),
        }
    )

    result = duplicate_sources(mock_manifest)

    expected = CheckResult(
        name=duplicate_sources.__sweep_name__,
        status=CheckStatus.FAIL,
        nodes=[
            mock_manifest.sources.get("source_one").unique_id,
            mock_manifest.sources.get("source_two").unique_id,
        ],
    )
    
    assert result == expected


def test_duplicate_sources_pass():
    mock_manifest = MagicMock(
        sources={
            "source_one": SourceDefinition(
                database="mock_db",
                schema="mock_schema",
                name="mock_table",
                resource_type="source",
                package_name="mock_package",
                path="sources.mock",
                original_file_path="/sources/mock",
                unique_id="mock_package.source_one",
                fqn=[""],
                source_name="",
                source_description="",
                loader="",
                identifier="",
            ),
            "source_two": SourceDefinition(
                database="mock_db",
                schema="mock_schema",
                name="mock_table_two",
                resource_type="source",
                package_name="mock_package",
                path="sources.mock",
                original_file_path="/sources/mock",
                unique_id="mock_package.source_two",
                fqn=[""],
                source_name="",
                source_description="",
                loader="",
                identifier="",
            ),
        }
    )

    result = duplicate_sources(mock_manifest)

    expected = CheckResult(
        name=duplicate_sources.__sweep_name__,
        status=CheckStatus.PASS,
        nodes=[],
    )
    
    assert result == expected