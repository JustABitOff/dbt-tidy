import json
from typing import Dict, Union

from pydantic import BaseModel

from tidy.manifest.nodes import (
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
from tidy.manifest.macros import Macro
from tidy.manifest.docs import Documentation
from tidy.manifest.exposures import Exposure
from tidy.manifest.metrics import Metric
from tidy.manifest.groups import Group
from tidy.manifest.selectors import Selector
from tidy.manifest.parent_map import ParentMap
from tidy.manifest.child_map import ChildMap
from tidy.manifest.group_map import GroupMap
from tidy.manifest.saved_queries import SavedQuery
from tidy.manifest.semantic_models import SemanticModel


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
                    # UnitTest,
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

    @classmethod
    def load_from_json(cls, file_path: str) -> "Manifest":
        with open(file_path, "r") as file:
            data = json.load(file)
            return cls.model_validate(data)
