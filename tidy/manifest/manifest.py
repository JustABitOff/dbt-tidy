import pathlib
from typing import Dict, Union

from pydantic import BaseModel

from tidy.manifest import (
    Analysis,
    GenericTest,
    HookNode,
    Model,
    Seed,
    SingularTest,
    Snapshot,
    SqlOperation,
    Source,
    Macro,
    Documentation,
    Exposure,
    Metric,
    Group,
    Selector,
    ParentMap,
    ChildMap,
    GroupMap,
    SavedQuery,
    SemanticModel,
    UnitTest,
)


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
