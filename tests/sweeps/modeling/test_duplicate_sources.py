from unittest.mock import MagicMock

from tidy.manifest.v10.sources.source_definition import (
    SourceDefinition as SourceDefinitionV10,
)
from tidy.manifest.v11.sources.source_definition import (
    SourceDefinition as SourceDefinitionV11,
)
from tidy.manifest.v12.sources.source_definition import (
    SourceDefinition as SourceDefinitionV12,
)
from tidy.sweeps.base import CheckResult, CheckStatus
from tidy.sweeps.modeling.duplicate_sources import duplicate_sources


def test_v10_manifest_duplicate_sources_fail():
    mock_manifest = MagicMock(
        sources={
            "source_one": SourceDefinitionV10(
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
            "source_two": SourceDefinitionV12(
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
        resolution=duplicate_sources.__resolution__,
    )

    assert result == expected


def test_v10_manifest_duplicate_sources_pass():
    mock_manifest = MagicMock(
        sources={
            "source_one": SourceDefinitionV10(
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
            "source_two": SourceDefinitionV12(
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


def test_v11_manifest_duplicate_sources_fail():
    mock_manifest = MagicMock(
        sources={
            "source_one": SourceDefinitionV11(
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
            "source_two": SourceDefinitionV12(
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
        resolution=duplicate_sources.__resolution__,
    )

    assert result == expected


def test_v11_manifest_duplicate_sources_pass():
    mock_manifest = MagicMock(
        sources={
            "source_one": SourceDefinitionV11(
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
            "source_two": SourceDefinitionV12(
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


def test_v12_manifest_duplicate_sources_fail():
    mock_manifest = MagicMock(
        sources={
            "source_one": SourceDefinitionV12(
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
            "source_two": SourceDefinitionV12(
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
        resolution=duplicate_sources.__resolution__,
    )

    assert result == expected


def test_v12_manifest_duplicate_sources_pass():
    mock_manifest = MagicMock(
        sources={
            "source_one": SourceDefinitionV12(
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
            "source_two": SourceDefinitionV12(
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
