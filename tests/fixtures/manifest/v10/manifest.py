import pytest

from tidy.manifest.v10.manifest import ManifestV10
from tidy.manifest.v10.bases.file_hash import FileHash
from tidy.manifest.v10.bases.depends_on import DependsOn
from tidy.manifest.v10.metadata.metadata import ManifestMetadata
from tidy.manifest.v10.nodes.models.model import ModelNode
from tidy.manifest.v10.sources.source_definition import SourceDefinition


PACKAGE_NAME = "unit_test_package"


@pytest.fixture
def manifestv10_fixture():
    return ManifestV10(
        metadata=ManifestMetadata(
            project_name=PACKAGE_NAME,
        ),
        nodes={
            f"model.{PACKAGE_NAME}.stg_source_one__table_one": ModelNode(
                database="unit_test_db",
                schema="staging",
                name="stg_source_one__table_one",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.stg_source_one__table_one",
                fqn=[
                    PACKAGE_NAME,
                    "stg_source_one__table_one",
                ],
                alias="stg_source_one__table_one",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"source.{PACKAGE_NAME}.source_one.table_one",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.stg_source_two__table_two": ModelNode(
                database="unit_test_db",
                schema="staging",
                name="stg_source_two__table_two",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.stg_source_two__table_two",
                fqn=[
                    PACKAGE_NAME,
                    "stg_source_two__table_two",
                ],
                alias="stg_source_two__table_two",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"source.{PACKAGE_NAME}.source_two.table_two",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.int_source_one__table_one": ModelNode(
                database="unit_test_db",
                schema="intermediate",
                name="int_source_one__table_one",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.int_source_one__table_one",
                fqn=[
                    PACKAGE_NAME,
                    "int_source_one__table_one",
                ],
                alias="int_source_one__table_one",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.stg_source_one__table_one",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.int_source_two__table_two": ModelNode(
                database="unit_test_db",
                schema="intermediate",
                name="int_source_two__table_two",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.int_source_two__table_two",
                fqn=[
                    PACKAGE_NAME,
                    "int_source_two__table_two",
                ],
                alias="int_source_two__table_two",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.stg_source_two__table_two",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.dim_one": ModelNode(
                database="unit_test_db",
                schema="marts",
                name="dim_one",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.dim_one",
                fqn=[
                    PACKAGE_NAME,
                    "dim_one",
                ],
                alias="dim_one",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.int_source_one__table_one",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.fct_one": ModelNode(
                database="unit_test_db",
                schema="marts",
                name="fct_one",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.fct_one",
                fqn=[
                    PACKAGE_NAME,
                    "fct_one",
                ],
                alias="fct_one",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.int_source_one__table_one",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.dim_two": ModelNode(
                database="unit_test_db",
                schema="marts",
                name="dim_two",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.dim_two",
                fqn=[
                    PACKAGE_NAME,
                    "dim_two",
                ],
                alias="dim_two",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.int_source_two__table_two",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.fct_two": ModelNode(
                database="unit_test_db",
                schema="marts",
                name="fct_two",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.fct_two",
                fqn=[
                    PACKAGE_NAME,
                    "fct_two",
                ],
                alias="fct_two",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.int_source_two__table_two",
                    ]
                ),
            ),
        },
        sources={
            f"source.{PACKAGE_NAME}.source_one.table_one": SourceDefinition(
                database="unit_test_db",
                schema="source_one",
                name="table_one",
                resource_type="source",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"source.{PACKAGE_NAME}.source_one.table_one",
                fqn=[
                    PACKAGE_NAME,
                    "source_one",
                    "table_one",
                ],
                source_name="source_one",
                source_description="",
                loader="",
                identifier="",
            ),
            f"source.{PACKAGE_NAME}.source_two.table_two": SourceDefinition(
                database="unit_test_db",
                schema="source_two",
                name="table_two",
                resource_type="source",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"source.{PACKAGE_NAME}.source_two.table_two",
                fqn=[
                    PACKAGE_NAME,
                    "source_two",
                    "table_two",
                ],
                source_name="source_two",
                source_description="",
                loader="",
                identifier="",
            ),
        },
        macros={},
        docs={},
        exposures={},
        metrics={},
        groups={},
        selectors={},
        disabled=None,
        parent_map={
            f"model.{PACKAGE_NAME}.stg_source_one__table_one": [
                f"source.{PACKAGE_NAME}.source_one.table_one",
            ],
            f"model.{PACKAGE_NAME}.stg_source_two__table_two": [
                f"source.{PACKAGE_NAME}.source_two.table_two",
            ],
            f"model.{PACKAGE_NAME}.int_source_one__table_one": [
                f"model.{PACKAGE_NAME}.stg_source_one__table_one",
            ],
            f"model.{PACKAGE_NAME}.int_source_two__table_two": [
                f"model.{PACKAGE_NAME}.stg_source_two__table_two",
            ],
            f"model.{PACKAGE_NAME}.dim_one": [
                f"model.{PACKAGE_NAME}.int_source_one__table_one",
            ],
            f"model.{PACKAGE_NAME}.fct_one": [
                f"model.{PACKAGE_NAME}.int_source_one__table_one",
            ],
            f"model.{PACKAGE_NAME}.dim_two": [
                f"model.{PACKAGE_NAME}.int_source_two__table_two",
            ],
            f"model.{PACKAGE_NAME}.fct_two": [
                f"model.{PACKAGE_NAME}.int_source_two__table_two",
            ],
            f"source.{PACKAGE_NAME}.source_one.table_one": [],
            f"source.{PACKAGE_NAME}.source_two.table_two": [],
        },
        child_map={
            f"source.{PACKAGE_NAME}.source_one.table_one": [
                f"model.{PACKAGE_NAME}.stg_source_one__table_one",
            ],
            f"source.{PACKAGE_NAME}.source_two.table_two": [
                f"model.{PACKAGE_NAME}.stg_source_two__table_two",
            ],
            f"model.{PACKAGE_NAME}.stg_source_one__table_one": [
                f"model.{PACKAGE_NAME}.int_source_one__table_one",
            ],
            f"model.{PACKAGE_NAME}.stg_source_two__table_two": [
                f"model.{PACKAGE_NAME}.int_source_two__table_two",
            ],
            f"model.{PACKAGE_NAME}.int_source_one__table_one": [
                f"model.{PACKAGE_NAME}.dim_one",
                f"model.{PACKAGE_NAME}.fct_one",
            ],
            f"model.{PACKAGE_NAME}.int_source_two__table_two": [
                f"model.{PACKAGE_NAME}.dim_two",
                f"model.{PACKAGE_NAME}.fct_two",
            ],
            f"model.{PACKAGE_NAME}.dim_one": [],
            f"model.{PACKAGE_NAME}.fct_one": [],
            f"model.{PACKAGE_NAME}.dim_two": [],
            f"model.{PACKAGE_NAME}.fct_two": [],
        },
        group_map={},
        semantic_models={},
    )


@pytest.fixture
def manifestv10_direct_join_to_source_fixture():
    return ManifestV10(
        metadata=ManifestMetadata(
            project_name=PACKAGE_NAME,
        ),
        nodes={
            f"model.{PACKAGE_NAME}.stg_source_one__table_one": ModelNode(
                database="unit_test_db",
                schema="staging",
                name="stg_source_one__table_one",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.stg_source_one__table_one",
                fqn=[
                    PACKAGE_NAME,
                    "stg_source_one__table_one",
                ],
                alias="stg_source_one__table_one",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"source.{PACKAGE_NAME}.source_one.table_one",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.int_source_one__table_one": ModelNode(
                database="unit_test_db",
                schema="intermediate",
                name="int_source_one__table_one",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.int_source_one__table_one",
                fqn=[
                    PACKAGE_NAME,
                    "int_source_one__table_one",
                ],
                alias="int_source_one__table_one",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.stg_source_one__table_one",
                        f"source.{PACKAGE_NAME}.source_two.table_two",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.dim_one": ModelNode(
                database="unit_test_db",
                schema="marts",
                name="dim_one",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.dim_one",
                fqn=[
                    PACKAGE_NAME,
                    "dim_one",
                ],
                alias="dim_one",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.int_source_one__table_one",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.fct_one": ModelNode(
                database="unit_test_db",
                schema="marts",
                name="fct_one",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.fct_one",
                fqn=[
                    PACKAGE_NAME,
                    "fct_one",
                ],
                alias="fct_one",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.int_source_one__table_one",
                    ]
                ),
            ),
        },
        sources={
            f"source.{PACKAGE_NAME}.source_one.table_one": SourceDefinition(
                database="unit_test_db",
                schema="source_one",
                name="table_one",
                resource_type="source",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"source.{PACKAGE_NAME}.source_one.table_one",
                fqn=[
                    PACKAGE_NAME,
                    "source_one",
                    "table_one",
                ],
                source_name="source_one",
                source_description="",
                loader="",
                identifier="",
            ),
            f"source.{PACKAGE_NAME}.source_two.table_two": SourceDefinition(
                database="unit_test_db",
                schema="source_two",
                name="table_two",
                resource_type="source",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"source.{PACKAGE_NAME}.source_two.table_two",
                fqn=[
                    PACKAGE_NAME,
                    "source_two",
                    "table_two",
                ],
                source_name="source_two",
                source_description="",
                loader="",
                identifier="",
            ),
        },
        macros={},
        docs={},
        exposures={},
        metrics={},
        groups={},
        selectors={},
        disabled=None,
        parent_map={
            f"model.{PACKAGE_NAME}.stg_source_one__table_one": [
                f"source.{PACKAGE_NAME}.source_one.table_one",
            ],
            f"model.{PACKAGE_NAME}.int_source_one__table_one": [
                f"model.{PACKAGE_NAME}.stg_source_one__table_one",
                f"source.{PACKAGE_NAME}.source_two.table_two",
            ],
            f"model.{PACKAGE_NAME}.dim_one": [
                f"model.{PACKAGE_NAME}.int_source_one__table_one",
            ],
            f"model.{PACKAGE_NAME}.fct_one": [
                f"model.{PACKAGE_NAME}.int_source_one__table_one",
            ],
            f"source.{PACKAGE_NAME}.source_one.table_one": [],
            f"source.{PACKAGE_NAME}.source_two.table_two": [],
        },
        child_map={
            f"source.{PACKAGE_NAME}.source_one.table_one": [
                f"model.{PACKAGE_NAME}.stg_source_one__table_one",
            ],
            f"source.{PACKAGE_NAME}.source_two.table_two": [
                f"model.{PACKAGE_NAME}.int_source_one__table_one",
            ],
            f"model.{PACKAGE_NAME}.stg_source_one__table_one": [
                f"model.{PACKAGE_NAME}.int_source_one__table_one",
            ],
            f"model.{PACKAGE_NAME}.int_source_one__table_one": [
                f"model.{PACKAGE_NAME}.dim_one",
                f"model.{PACKAGE_NAME}.fct_one",
            ],
            f"model.{PACKAGE_NAME}.dim_one": [],
            f"model.{PACKAGE_NAME}.fct_one": [],
        },
        group_map={},
        semantic_models={},
    )


@pytest.fixture
def manifestv10_duplicate_sources_fixture():
    return ManifestV10(
        metadata=ManifestMetadata(
            project_name=PACKAGE_NAME,
        ),
        nodes={},
        sources={
            f"source.{PACKAGE_NAME}.source_one.table_one": SourceDefinition(
                database="unit_test_db",
                schema="source_one",
                name="table_one",
                resource_type="source",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"source.{PACKAGE_NAME}.source_one.table_one",
                fqn=[
                    PACKAGE_NAME,
                    "source_one",
                    "table_one",
                ],
                source_name="source_one",
                source_description="",
                loader="",
                identifier="",
            ),
            f"source.{PACKAGE_NAME}.source_two.table_two": SourceDefinition(
                database="unit_test_db",
                schema="source_one",
                name="table_one",
                resource_type="source",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"source.{PACKAGE_NAME}.source_two.table_two",
                fqn=[
                    PACKAGE_NAME,
                    "source_two",
                    "table_two",
                ],
                source_name="source_two",
                source_description="",
                loader="",
                identifier="",
            ),
        },
        macros={},
        docs={},
        exposures={},
        metrics={},
        groups={},
        selectors={},
        disabled=None,
        parent_map={
            f"source.{PACKAGE_NAME}.source_one.table_one": [],
            f"source.{PACKAGE_NAME}.source_two.table_two": [],
        },
        child_map={
            f"source.{PACKAGE_NAME}.source_one.table_one": [],
            f"source.{PACKAGE_NAME}.source_two.table_two": [],
        },
        group_map={},
        semantic_models={},
    )


@pytest.fixture
def manifestv10_model_fanout_fixture():
    return ManifestV10(
        metadata=ManifestMetadata(
            project_name=PACKAGE_NAME,
        ),
        nodes={
            f"model.{PACKAGE_NAME}.stg_source_one__table_one": ModelNode(
                database="unit_test_db",
                schema="staging",
                name="stg_source_one__table_one",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.stg_source_one__table_one",
                fqn=[
                    PACKAGE_NAME,
                    "stg_source_one__table_one",
                ],
                alias="stg_source_one__table_one",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        "source.{PACKAGE_NAME}.source_one.table_one",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.stg_source_two__table_two": ModelNode(
                database="unit_test_db",
                schema="staging",
                name="stg_source_two__table_two",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.stg_source_two__table_two",
                fqn=[
                    PACKAGE_NAME,
                    "stg_source_two__table_two",
                ],
                alias="stg_source_two__table_two",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"source.{PACKAGE_NAME}.source_two.table_two",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.int_source_one__table_one": ModelNode(
                database="unit_test_db",
                schema="intermediate",
                name="int_source_one__table_one",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.int_source_one__table_one",
                fqn=[
                    PACKAGE_NAME,
                    "int_source_one__table_one",
                ],
                alias="int_source_one__table_one",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.stg_source_one__table_one",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.int_source_two__table_two": ModelNode(
                database="unit_test_db",
                schema="intermediate",
                name="int_source_two__table_two",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.int_source_two__table_two",
                fqn=[
                    PACKAGE_NAME,
                    "int_source_two__table_two",
                ],
                alias="int_source_two__table_two",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.stg_source_two__table_two",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.dim_one": ModelNode(
                database="unit_test_db",
                schema="marts",
                name="dim_one",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.dim_one",
                fqn=[
                    PACKAGE_NAME,
                    "dim_one",
                ],
                alias="dim_one",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.int_source_one__table_one",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.fct_one": ModelNode(
                database="unit_test_db",
                schema="marts",
                name="fct_one",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.fct_one",
                fqn=[
                    PACKAGE_NAME,
                    "fct_one",
                ],
                alias="fct_one",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.int_source_one__table_one",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.dim_two": ModelNode(
                database="unit_test_db",
                schema="marts",
                name="dim_two",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.dim_two",
                fqn=[
                    PACKAGE_NAME,
                    "dim_two",
                ],
                alias="dim_two",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.int_source_two__table_two",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.fct_two": ModelNode(
                database="unit_test_db",
                schema="marts",
                name="fct_two",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.fct_two",
                fqn=[
                    PACKAGE_NAME,
                    "fct_two",
                ],
                alias="fct_two",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.int_source_two__table_two",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.fct_three": ModelNode(
                database="unit_test_db",
                schema="marts",
                name="fct_three",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.fct_three",
                fqn=[
                    PACKAGE_NAME,
                    "fct_three",
                ],
                alias="fct_three",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.int_source_two__table_two",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.fct_four": ModelNode(
                database="unit_test_db",
                schema="marts",
                name="fct_four",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.fct_four",
                fqn=[
                    PACKAGE_NAME,
                    "fct_four",
                ],
                alias="fct_four",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.int_source_two__table_two",
                    ]
                ),
            ),
            f"model.{PACKAGE_NAME}.fct_five": ModelNode(
                database="unit_test_db",
                schema="marts",
                name="fct_five",
                resource_type="model",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"model.{PACKAGE_NAME}.fct_five",
                fqn=[
                    PACKAGE_NAME,
                    "fct_five",
                ],
                alias="fct_five",
                checksum=FileHash(name="", checksum=""),
                depends_on=DependsOn(
                    nodes=[
                        f"model.{PACKAGE_NAME}.int_source_two__table_two",
                    ]
                ),
            ),
        },
        sources={
            f"source.{PACKAGE_NAME}.source_one.table_one": SourceDefinition(
                database="unit_test_db",
                schema="source_one",
                name="table_one",
                resource_type="source",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"source.{PACKAGE_NAME}.source_one.table_one",
                fqn=[
                    PACKAGE_NAME,
                    "source_one",
                    "table_one",
                ],
                source_name="source_one",
                source_description="",
                loader="",
                identifier="",
            ),
            f"source.{PACKAGE_NAME}.source_two.table_two": SourceDefinition(
                database="unit_test_db",
                schema="source_two",
                name="table_two",
                resource_type="source",
                package_name=PACKAGE_NAME,
                path="",
                original_file_path="",
                unique_id=f"source.{PACKAGE_NAME}.source_two.table_two",
                fqn=[
                    PACKAGE_NAME,
                    "source_two",
                    "table_two",
                ],
                source_name="source_two",
                source_description="",
                loader="",
                identifier="",
            ),
        },
        macros={},
        docs={},
        exposures={},
        metrics={},
        groups={},
        selectors={},
        disabled=None,
        parent_map={
            f"model.{PACKAGE_NAME}.stg_source_one__table_one": [
                f"source.{PACKAGE_NAME}.source_one.table_one",
            ],
            f"model.{PACKAGE_NAME}.stg_source_two__table_two": [
                f"source.{PACKAGE_NAME}.source_two.table_two",
            ],
            f"model.{PACKAGE_NAME}.int_source_one__table_one": [
                f"model.{PACKAGE_NAME}.stg_source_one__table_one",
            ],
            f"model.{PACKAGE_NAME}.int_source_two__table_two": [
                f"model.{PACKAGE_NAME}.stg_source_two__table_two",
            ],
            f"model.{PACKAGE_NAME}.dim_one": [
                f"model.{PACKAGE_NAME}.int_source_one__table_one",
            ],
            f"model.{PACKAGE_NAME}.fct_one": [
                f"model.{PACKAGE_NAME}.int_source_one__table_one",
            ],
            f"model.{PACKAGE_NAME}.dim_two": [
                f"model.{PACKAGE_NAME}.int_source_two__table_two",
            ],
            f"model.{PACKAGE_NAME}.fct_two": [
                f"model.{PACKAGE_NAME}.int_source_two__table_two",
            ],
            f"model.{PACKAGE_NAME}.fct_three": [
                f"model.{PACKAGE_NAME}.int_source_two__table_two",
            ],
            f"model.{PACKAGE_NAME}.fct_four": [
                f"model.{PACKAGE_NAME}.int_source_two__table_two",
            ],
            f"model.{PACKAGE_NAME}.fct_five": [
                f"model.{PACKAGE_NAME}.int_source_two__table_two",
            ],                      
            f"source.{PACKAGE_NAME}.source_one.table_one": [],
            f"source.{PACKAGE_NAME}.source_two.table_two": [],
        },
        child_map={
            f"source.{PACKAGE_NAME}.source_one.table_one": [
                f"model.{PACKAGE_NAME}.stg_source_one__table_one",
            ],
            f"source.{PACKAGE_NAME}.source_two.table_two": [
                f"model.{PACKAGE_NAME}.stg_source_two__table_two",
            ],
            f"model.{PACKAGE_NAME}.stg_source_one__table_one": [
                f"model.{PACKAGE_NAME}.int_source_one__table_one",
            ],
            f"model.{PACKAGE_NAME}.stg_source_two__table_two": [
                f"model.{PACKAGE_NAME}.int_source_two__table_two",
            ],
            f"model.{PACKAGE_NAME}.int_source_one__table_one": [
                f"model.{PACKAGE_NAME}.dim_one",
                f"model.{PACKAGE_NAME}.fct_one",
            ],
            f"model.{PACKAGE_NAME}.int_source_two__table_two": [
                f"model.{PACKAGE_NAME}.dim_two",
                f"model.{PACKAGE_NAME}.fct_two",
                f"model.{PACKAGE_NAME}.fct_three",
                f"model.{PACKAGE_NAME}.fct_four",
                f"model.{PACKAGE_NAME}.fct_five",
            ],
            f"model.{PACKAGE_NAME}.dim_one": [],
            f"model.{PACKAGE_NAME}.fct_one": [],
            f"model.{PACKAGE_NAME}.dim_two": [],
            f"model.{PACKAGE_NAME}.fct_two": [],
            f"model.{PACKAGE_NAME}.fct_three": [],
            f"model.{PACKAGE_NAME}.fct_four": [],
            f"model.{PACKAGE_NAME}.fct_five": [],
        },
        group_map={},
        semantic_models={},
    )