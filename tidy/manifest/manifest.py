import pathlib
from typing import Dict, Union

from pydantic import BaseModel

from tidy.manifest.nodes import(
    Analysis,
    GenericTest,
    HookNode,
    Model,
    Seed,
    SingularTest,
    Snapshot,
    SqlOperation,
)
from tidy.manifest.sources import Source
from tidy.manifest.macros.macro import Macro
from tidy.manifest.docs.documentation import Documentation
from tidy.manifest.exposures.exposure import Exposure
from tidy.manifest.metrics.metric import Metric
from tidy.manifest.groups.group import Group
from tidy.manifest.selectors.selector import Selector
from tidy.manifest.parent_map.parent_map import ParentMap
from tidy.manifest.child_map.child_map import ChildMap
from tidy.manifest.group_map.group_map import GroupMap
from tidy.manifest.saved_queries.saved_query import SavedQuery
from tidy.manifest.semantic_models.semantic_model import SemanticModel
from tidy.manifest.unit_tests.unit_test import UnitTest


class Manifest(BaseModel):
    nodes: Dict[
        str,
        Union[
            Analysis,
            GenericTest,
            HookNode,
            Model,
            Seed,
            SingularTest,
            Snapshot,
            SqlOperation,
        ],
    ] = {}
    sources: Dict[str, Source] = {}
    macros: Dict[str, Macro] = {}
    docs: Dict[str, Documentation] = {}
    exposures: Dict[str, Exposure] = {}
    metrics: Dict[str, Metric] = {}
    groups: Dict[str, Group] = {}
    selectors: Dict[str, Selector] = {}
    disabled: (
        Dict[
            str,
            list[
                Union[
                    Analysis,
                    GenericTest,
                    HookNode,
                    Model,
                    Seed,
                    SingularTest,
                    Snapshot,
                    SqlOperation,
                    Source,
                    Exposure,
                    Metric,
                    SavedQuery,
                    SemanticModel,
                    UnitTest,
                ]
            ],
        ]
        | None
    ) = None
    parent_map: ParentMap | None = None
    child_map: ChildMap | None = None
    group_map: GroupMap | None = None
    saved_queries: dict[str, SavedQuery] = {}
    semantic_models: dict[str, SemanticModel] = {}
    unit_tests: dict[str, UnitTest] = {}

    @classmethod
    def validate(cls, manifest_path: str = "target/manifest.json") -> "Manifest":
        return cls.model_validate_json(
            pathlib.Path(manifest_path).read_text()
        )
