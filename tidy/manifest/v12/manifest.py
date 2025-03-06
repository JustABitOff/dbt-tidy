from functools import cached_property
from typing import Any, Dict, List, Optional, Union

from networkx import DiGraph
from pydantic import BaseModel, ConfigDict, Field, computed_field

from tidy.manifest.utils.dag import (
    build_dbt_graph_from_manifest,
    get_ancestors,
    get_descendants,
)
from tidy.manifest.v12.metadata.metadata import ManifestMetadata
from tidy.manifest.v12.nodes.seeds.seed import Seed
from tidy.manifest.v12.nodes.analysis.analysis import Analysis
from tidy.manifest.v12.nodes.tests.singular_test import SingularTest
from tidy.manifest.v12.nodes.hooks.hook import HookNode
from tidy.manifest.v12.nodes.models.model import Model
from tidy.manifest.v12.nodes.sql_operations.sql_operation import SqlOperation
from tidy.manifest.v12.nodes.tests.generic_test import GenericTest
from tidy.manifest.v12.nodes.snapshots.snapshot import Snapshot
from tidy.manifest.v12.sources.source_definition import SourceDefinition
from tidy.manifest.v12.macros.macro import Macro
from tidy.manifest.v12.documentation.documentation import Documentation
from tidy.manifest.v12.exposures.exposure import Exposure
from tidy.manifest.v12.metrics.metric import Metric
from tidy.manifest.v12.groups.group import Group
from tidy.manifest.v12.saved_queries.saved_query import SavedQuery
from tidy.manifest.v12.semantic_models.semantic_model import SemanticModel
from tidy.manifest.v12.unit_tests.unit_test_definition import UnitTestDefinition


class ManifestV12(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        arbitrary_types_allowed=True,
    )
    metadata: ManifestMetadata = Field(
        ..., description="Metadata about the manifest", title="ManifestMetadata"
    )
    nodes: Dict[
        str,
        Union[
            Seed,
            Analysis,
            SingularTest,
            HookNode,
            Model,
            SqlOperation,
            GenericTest,
            Snapshot,
        ],
    ] = Field(
        ..., description="The nodes defined in the dbt project and its dependencies"
    )
    sources: Dict[str, SourceDefinition] = Field(
        ..., description="The sources defined in the dbt project and its dependencies"
    )
    macros: Dict[str, Macro] = Field(
        ..., description="The macros defined in the dbt project and its dependencies"
    )
    docs: Dict[str, Documentation] = Field(
        ..., description="The docs defined in the dbt project and its dependencies"
    )
    exposures: Dict[str, Exposure] = Field(
        ..., description="The exposures defined in the dbt project and its dependencies"
    )
    metrics: Dict[str, Metric] = Field(
        ..., description="The metrics defined in the dbt project and its dependencies"
    )
    groups: Dict[str, Group] = Field(
        ..., description="The groups defined in the dbt project"
    )
    selectors: Dict[str, Any] = Field(
        ..., description="The selectors defined in selectors.yml"
    )
    parent_map: Optional[Dict[str, List[str]]] = Field(
        ..., description="A mapping from child nodes to their dependencies"
    )
    child_map: Optional[Dict[str, List[str]]] = Field(
        ..., description="A mapping from parent nodes to their dependents"
    )
    group_map: Optional[Dict[str, List[str]]] = Field(
        ..., description="A mapping from group names to their nodes"
    )
    saved_queries: Dict[str, SavedQuery] = Field(
        ..., description="The saved queries defined in the dbt project"
    )
    semantic_models: Dict[str, SemanticModel] = Field(
        ..., description="The semantic models defined in the dbt project"
    )
    unit_tests: Dict[str, UnitTestDefinition] = Field(
        ..., description="The unit tests defined in the project"
    )
    disabled: Optional[
        Dict[
            str,
            List[
                Union[
                    Seed,
                    Analysis,
                    SingularTest,
                    HookNode,
                    Model,
                    SqlOperation,
                    GenericTest,
                    Snapshot,
                    SourceDefinition,
                    Exposure,
                    Metric,
                    SavedQuery,
                    SemanticModel,
                    UnitTestDefinition,
                ]
            ],
        ]
    ] = Field(..., description="A mapping of the disabled nodes in the target")

    @computed_field(repr=False)
    @cached_property
    def dag(self) -> DiGraph:
        return build_dbt_graph_from_manifest(self)

    def ancestors(self, dbt_unique_id: str) -> list[tuple[str, int]]:
        return get_ancestors(self.dag, node=dbt_unique_id)

    def descendants(self, dbt_unique_id: str) -> dict[str, int]:
        return get_descendants(self.dag, node=dbt_unique_id)
