from typing import Optional, Literal, List, Dict, Any, Union

from functools import cached_property

from jinja2 import Environment, nodes
from pydantic import BaseModel, ConfigDict, Field, computed_field
import networkx as nx

from tidy.manifest.v12.bases.file_hash import FileHash
from tidy.manifest.v12.bases.column_info import ColumnInfo
from tidy.manifest.v12.bases.docs import Docs
from tidy.manifest.v12.bases.ref_args import RefArgs
from tidy.manifest.v12.bases.depends_on import DependsOn
from tidy.manifest.v12.bases.injected_cte import InjectedCTE
from tidy.manifest.v12.bases.contract import Contract
from tidy.manifest.v12.bases.defer_relation import DeferRelation
from tidy.manifest.v12.bases.enums import Access
from tidy.manifest.v12.nodes.models.model_config import ModelConfig
from tidy.manifest.v12.nodes.models.model_level_constraint import ModelLevelConstraint
from tidy.manifest.v12.nodes.models.time_spine import TimeSpine
from tidy.manifest.v12.nodes.models.model_freshness import ModelFreshness


class Model(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    database: Optional[str] = None
    schema_: str = Field(..., alias="schema")
    name: str
    resource_type: Literal["model"]
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: List[str]
    alias: str
    checksum: FileHash = Field(..., title="FileHash")
    config: Optional[ModelConfig] = Field(None, title="ModelConfig")
    tags: Optional[List[str]] = None
    description: Optional[str] = ""
    columns: Optional[Dict[str, ColumnInfo]] = None
    meta: Optional[Dict[str, Any]] = None
    group: Optional[str] = None
    docs: Optional[Docs] = Field(None, title="Docs")
    patch_path: Optional[str] = None
    build_path: Optional[str] = None
    unrendered_config: Optional[Dict[str, Any]] = None
    created_at: Optional[float] = None
    config_call_dict: Optional[Dict[str, Any]] = None
    unrendered_config_call_dict: Optional[Dict[str, Any]] = None
    relation_name: Optional[str] = None
    raw_code: Optional[str] = ""
    doc_blocks: Optional[List[str]] = None
    language: Optional[str] = "sql"
    refs: Optional[List[RefArgs]] = None
    sources: Optional[List[List[str]]] = None
    metrics: Optional[List[List[str]]] = None
    depends_on: Optional[DependsOn] = Field(None, title="DependsOn")
    compiled_path: Optional[str] = None
    compiled: Optional[bool] = False
    compiled_code: Optional[str] = None
    extra_ctes_injected: Optional[bool] = False
    extra_ctes: Optional[List[InjectedCTE]] = None
    field_pre_injected_sql: Optional[str] = Field(None, alias="_pre_injected_sql")
    contract: Optional[Contract] = Field(None, title="Contract")
    access: Optional[Access] = Access.protected
    constraints: Optional[List[ModelLevelConstraint]] = None
    version: Optional[Union[str, float]] = None
    latest_version: Optional[Union[str, float]] = None
    deprecation_date: Optional[str] = None
    defer_relation: Optional[DeferRelation] = None
    primary_key: Optional[List[str]] = None
    time_spine: Optional[TimeSpine] = None
    freshness: Optional[ModelFreshness] = None

    @computed_field
    @property
    def config_block(self) -> Optional[Dict[str, Any]]:
        env = Environment(extensions=["jinja2.ext.do"])
        ast = env.parse(self.raw_code)

        def find_config_call(node):
            if (
                isinstance(node, nodes.Call)
                and isinstance(node.node, nodes.Name)
                and node.node.name == "config"
            ):
                return {kw.key: kw.value.as_const() for kw in node.kwargs}

            for child in node.iter_child_nodes():
                result = find_config_call(child)
                if result:
                    return result

            return None

        return find_config_call(ast)


    @computed_field(repr=False)
    @cached_property
    def ancestors(self) -> Optional[List]:
        return build_dbt_graph_from_manifest(self)



def build_dbt_graph_from_manifest(manifest) -> nx.DiGraph:
    """Constructs a DAG from dbt manifest.json using the depends_on field."""
    
    G = nx.DiGraph()

    # Add nodes
    for unique_id, node in manifest.nodes.items():
        G.add_node(unique_id, name=node.name)

    # Add edges based on `depends_on.nodes` (parent → child)
    for unique_id, node in manifest.nodes.items():
        # breakpoint()
        if hasattr(node.depends_on, "nodes"):
            for parent_id in node.depends_on.nodes:
                if parent_id in manifest.nodes:  # Ensure parent exists in manifest
                    G.add_edge(parent_id, unique_id)

    return G