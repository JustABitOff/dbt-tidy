from functools import cached_property
from typing import Any, Dict, List, Optional, Union

from networkx import DiGraph
from pydantic import BaseModel, ConfigDict, Field, computed_field

from tidy.manifest.utils.dag import (
    build_dbt_graph_from_manifest,
    get_ancestors,
    get_descendants,
)
from tidy.manifest.v11.metadata.metadata import ManifestMetadata
from tidy.manifest.v11.nodes.seeds.seed import SeedNode
from tidy.manifest.v11.nodes.analysis.analysis import Analysis
from tidy.manifest.v11.nodes.tests.singular_test import SingularTest
from tidy.manifest.v11.nodes.hooks.hook import HookNode
from tidy.manifest.v11.nodes.models.model import Model
from tidy.manifest.v11.nodes.rpc.rpc import RPCNode
from tidy.manifest.v11.nodes.sql.sql import SqlNode
from tidy.manifest.v11.nodes.tests.generic_test import GenericTest
from tidy.manifest.v11.nodes.snapshots.snapshot import Snapshot
from tidy.manifest.v11.sources.source_definition import SourceDefinition
from tidy.manifest.v11.macros.macro import Macro
from tidy.manifest.v11.documentation.documentation import Documentation
from tidy.manifest.v11.exposures.exposure import Exposure
from tidy.manifest.v11.metrics.metric import Metric
from tidy.manifest.v11.groups.group import Group
from tidy.manifest.v11.saved_queries.saved_query import SavedQuery
from tidy.manifest.v11.semantic_models.semantic_model import SemanticModel


class ManifestV11(BaseModel):
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
            Analysis,
            SingularTest,
            HookNode,
            Model,
            RPCNode,
            SqlNode,
            GenericTest,
            Snapshot,
            SeedNode,
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
    disabled: Optional[
        Dict[
            str,
            List[
                Union[
                    Analysis,
                    SingularTest,
                    HookNode,
                    Model,
                    RPCNode,
                    SqlNode,
                    GenericTest,
                    Snapshot,
                    SeedNode,
                    SourceDefinition,
                    Exposure,
                    Metric,
                    SavedQuery,
                    SemanticModel,
                ]
            ],
        ]
    ] = Field(..., description="A mapping of the disabled nodes in the target")
    parent_map: Optional[Dict[str, List[str]]] = Field(
        ..., description="A mapping from\xa0child nodes to their dependencies"
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

    @computed_field(repr=False)
    @cached_property
    def dag(self) -> DiGraph:
        return build_dbt_graph_from_manifest(self)

    def ancestors(self, dbt_unique_id: str) -> list[tuple[str, int]]:
        return get_ancestors(self.dag, node=dbt_unique_id)

    def descendants(self, dbt_unique_id: str) -> dict[str, int]:
        return get_descendants(self.dag, node=dbt_unique_id)
