from unittest.mock import MagicMock

from tidy.manifest.v10.nodes.models.model import (
    ModelNode as ModelV10,
)
from tidy.manifest.v10.bases.depends_on import (
    DependsOn as DependsOnV10,
)
from tidy.manifest.v10.bases.file_hash import FileHash as FileHashV10
from tidy.manifest.v11.nodes.models.model import (
    Model as ModelV11,
)
from tidy.manifest.v11.bases.depends_on import (
    DependsOn as DependsOnV11,
)
from tidy.manifest.v11.bases.file_hash import FileHash as FileHashV11
from tidy.manifest.v12.nodes.models.model import (
    Model as ModelV12,
)
from tidy.manifest.v12.bases.depends_on import (
    DependsOn as DependsOnV12,
)
from tidy.manifest.v12.bases.file_hash import FileHash as FileHashV12
from tidy.sweeps.base import CheckResult, CheckStatus
from tidy.sweeps.modeling.direct_join_to_source import direct_join_to_source


def test_manifest_v10_direct_join_to_source_fail():
    mock_manifest = MagicMock(
        nodes={
            "node_one": ModelV10(
                database="",
                schema="",
                name="",
                resource_type="model",
                package_name="",
                path="",
                original_file_path="",
                unique_id="package.node_one",
                fqn=[""],
                alias="",
                checksum=FileHashV10(
                    name="",
                    checksum="",
                ),
                depends_on=DependsOnV10(
                    nodes=[
                        "source.source",
                        "model.model",
                    ]
                ),
            )
        }
    )

    result = direct_join_to_source(mock_manifest)
    
    expected = CheckResult(
        name=direct_join_to_source.__sweep_name__,
        status=CheckStatus.FAIL,
        nodes=[mock_manifest.nodes.get("node_one").unique_id],
        resolution=direct_join_to_source.__resolution__,
    )

    assert result == expected


def test_manifest_v10_direct_join_to_source_pass():
    mock_manifest = MagicMock(
        nodes={
            "node_one": ModelV10(
                database="",
                schema="",
                name="",
                resource_type="model",
                package_name="",
                path="",
                original_file_path="",
                unique_id="package.node_one",
                fqn=[""],
                alias="",
                checksum=FileHashV10(
                    name="",
                    checksum="",
                ),
                depends_on=DependsOnV10(
                    nodes=[
                        "model.model_two",
                        "model.model",
                    ]
                ),
            )
        }
    )

    result = direct_join_to_source(mock_manifest)
    
    expected = CheckResult(
        name=direct_join_to_source.__sweep_name__,
        status=CheckStatus.PASS,
        nodes=[],
    )

    assert result == expected


def test_manifest_v11_direct_join_to_source_fail():
    mock_manifest = MagicMock(
        nodes={
            "node_one": ModelV11(
                database="",
                schema="",
                name="",
                resource_type="model",
                package_name="",
                path="",
                original_file_path="",
                unique_id="package.node_one",
                fqn=[""],
                alias="",
                checksum=FileHashV11(
                    name="",
                    checksum="",
                ),
                depends_on=DependsOnV11(
                    nodes=[
                        "source.source",
                        "model.model",
                    ]
                ),
            )
        }
    )

    result = direct_join_to_source(mock_manifest)

    expected = CheckResult(
        name=direct_join_to_source.__sweep_name__,
        status=CheckStatus.FAIL,
        nodes=[mock_manifest.nodes.get("node_one").unique_id],
        resolution=direct_join_to_source.__resolution__,
    )

    assert result == expected


def test_manifest_v11_direct_join_to_source_pass():
    mock_manifest = MagicMock(
        nodes={
            "node_one": ModelV11(
                database="",
                schema="",
                name="",
                resource_type="model",
                package_name="",
                path="",
                original_file_path="",
                unique_id="package.node_one",
                fqn=[""],
                alias="",
                checksum=FileHashV11(
                    name="",
                    checksum="",
                ),
                depends_on=DependsOnV11(
                    nodes=[
                        "model.model_two",
                        "model.model",
                    ]
                ),
            )
        }
    )

    result = direct_join_to_source(mock_manifest)

    expected = CheckResult(
        name=direct_join_to_source.__sweep_name__,
        status=CheckStatus.PASS,
        nodes=[],
    )

    assert result == expected


def test_manifest_v12_direct_join_to_source_fail():
    mock_manifest = MagicMock(
        nodes={
            "node_one": ModelV12(
                database="",
                schema="",
                name="",
                resource_type="model",
                package_name="",
                path="",
                original_file_path="",
                unique_id="package.node_one",
                fqn=[""],
                alias="",
                checksum=FileHashV12(
                    name="",
                    checksum="",
                ),
                depends_on=DependsOnV12(
                    nodes=[
                        "source.source",
                        "model.model",
                    ]
                ),
            )
        }
    )

    result = direct_join_to_source(mock_manifest)

    expected = CheckResult(
        name=direct_join_to_source.__sweep_name__,
        status=CheckStatus.FAIL,
        nodes=[mock_manifest.nodes.get("node_one").unique_id],
        resolution=direct_join_to_source.__resolution__,
    )

    assert result == expected


def test_manifest_v12_direct_join_to_source_pass():
    mock_manifest = MagicMock(
        nodes={
            "node_one": ModelV12(
                database="",
                schema="",
                name="",
                resource_type="model",
                package_name="",
                path="",
                original_file_path="",
                unique_id="package.node_one",
                fqn=[""],
                alias="",
                checksum=FileHashV12(
                    name="",
                    checksum="",
                ),
                depends_on=DependsOnV12(
                    nodes=[
                        "model.model_two",
                        "model.model",
                    ]
                ),
            )
        }
    )

    result = direct_join_to_source(mock_manifest)

    expected = CheckResult(
        name=direct_join_to_source.__sweep_name__,
        status=CheckStatus.PASS,
        nodes=[],
    )

    assert result == expected
