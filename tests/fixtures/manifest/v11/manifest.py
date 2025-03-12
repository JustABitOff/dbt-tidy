import pytest

from tidy.manifest.v11.manifest import ManifestV11
from tidy.manifest.v11.bases.file_hash import FileHash
from tidy.manifest.v11.bases.depends_on import DependsOn
from tidy.manifest.v11.metadata.metadata import ManifestMetadata
from tidy.manifest.v11.nodes.models.model import Model
from tidy.manifest.v11.sources.source_definition import SourceDefinition


PACKAGE_NAME = "unit_test_package"


@pytest.fixture
def manifestv11_fixture():
    return ManifestV11(
        metadata=ManifestMetadata(
            project_name=PACKAGE_NAME,
        ),
        nodes={
            f"model.{PACKAGE_NAME}.stg_source_one__table_one": Model(
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
            f"model.{PACKAGE_NAME}.stg_source_two__table_two": Model(
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
            f"model.{PACKAGE_NAME}.int_source_one__table_one": Model(
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
            f"model.{PACKAGE_NAME}.int_source_two__table_two": Model(
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
            f"model.{PACKAGE_NAME}.dim_one": Model(
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
            f"model.{PACKAGE_NAME}.fct_one": Model(
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
            f"model.{PACKAGE_NAME}.dim_two": Model(
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
            f"model.{PACKAGE_NAME}.fct_two": Model(
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
        parent_map={},
        child_map={},
        group_map={},
        semantic_models={},
        saved_queries={},
    )
