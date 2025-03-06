from functools import cached_property
from typing import Any, Dict, List, Optional, Union

from networkx import DiGraph
from pydantic import BaseModel, ConfigDict, Field, computed_field

from tidy.manifest.utils.dag import (
    build_dbt_graph_from_manifest,
    get_ancestors,
    get_descendants,
)
from tidy.manifest.v10.metadata.metadata import ManifestMetadata
from tidy.manifest.v10.nodes.seeds.seed import SeedNode
from tidy.manifest.v10.nodes.analysis.analysis import AnalysisNode
from tidy.manifest.v10.nodes.tests.singular_test import SingularTestNode
from tidy.manifest.v10.nodes.hooks.hook import HookNode
from tidy.manifest.v10.nodes.models.model import ModelNode
from tidy.manifest.v10.nodes.rpc.rpc import RPCNode
from tidy.manifest.v10.nodes.sql.sql import SqlNode
from tidy.manifest.v10.nodes.tests.generic_test import GenericTestNode
from tidy.manifest.v10.nodes.snapshots.snapshot import SnapshotNode
from tidy.manifest.v10.sources.source_definition import SourceDefinition
from tidy.manifest.v10.macros.macro import Macro
from tidy.manifest.v10.documentation.documentation import Documentation
from tidy.manifest.v10.exposures.exposure import Exposure
from tidy.manifest.v10.metrics.metric import Metric
from tidy.manifest.v10.groups.group import Group
from tidy.manifest.v10.semantic_models.semantic_model import SemanticModel


class ManifestV10(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        arbitrary_types_allowed=True,
    )
    metadata: ManifestMetadata = Field(..., description="Metadata about the manifest")
    nodes: Dict[
        str,
        Union[
            AnalysisNode,
            SingularTestNode,
            HookNode,
            ModelNode,
            RPCNode,
            SqlNode,
            GenericTestNode,
            SnapshotNode,
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
                    AnalysisNode,
                    SingularTestNode,
                    HookNode,
                    ModelNode,
                    RPCNode,
                    SqlNode,
                    GenericTestNode,
                    SnapshotNode,
                    SeedNode,
                    SourceDefinition,
                    Exposure,
                    Metric,
                    SemanticModel,
                ]
            ],
        ]
    ] = Field(None, description="A mapping of the disabled nodes in the target")
    parent_map: Optional[Dict[str, List[str]]] = Field(
        None, description="A mapping from\xa0child nodes to their dependencies"
    )
    child_map: Optional[Dict[str, List[str]]] = Field(
        None, description="A mapping from parent nodes to their dependents"
    )
    group_map: Optional[Dict[str, List[str]]] = Field(
        None, description="A mapping from group names to their nodes"
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
