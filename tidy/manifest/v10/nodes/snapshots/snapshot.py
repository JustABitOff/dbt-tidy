from typing import Optional, List, Dict, Any

from pydantic import BaseModel, ConfigDict, Field, computed_field

from tidy.manifest.v10.bases.file_hash import FileHash
from tidy.manifest.v10.bases.column_info import ColumnInfo
from tidy.manifest.v10.bases.docs import Docs
from tidy.manifest.v10.bases.ref_args import RefArgs
from tidy.manifest.v10.bases.depends_on import DependsOn
from tidy.manifest.v10.bases.injected_cte import InjectedCTE
from tidy.manifest.v10.bases.contract import Contract
from tidy.manifest.v10.bases.defer_relation import DeferRelation
from tidy.manifest.v10.bases.enums import ResourceType
from tidy.manifest.v10.nodes.snapshots.snapshot_config import SnapshotConfig
from tidy.manifest.utils.config_block import get_config_block


class SnapshotNode(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    database: Optional[str] = None
    schema_: str = Field(..., alias="schema")
    name: str
    resource_type: ResourceType
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: List[str]
    alias: str
    checksum: FileHash
    config: SnapshotConfig
    tags: Optional[List[str]] = []
    description: Optional[str] = ""
    columns: Optional[Dict[str, ColumnInfo]] = {}
    meta: Optional[Dict[str, Any]] = {}
    group: Optional[str] = None
    docs: Optional[Docs] = Field(
        default_factory=lambda: Docs.model_validate({"show": True, "node_color": None})
    )
    patch_path: Optional[str] = None
    build_path: Optional[str] = None
    deferred: Optional[bool] = False
    unrendered_config: Optional[Dict[str, Any]] = {}
    created_at: Optional[float] = 1696465994.418854
    config_call_dict: Optional[Dict[str, Any]] = {}
    relation_name: Optional[str] = None
    raw_code: Optional[str] = ""
    language: Optional[str] = "sql"
    refs: Optional[List[RefArgs]] = []
    sources: Optional[List[List[str]]] = []
    metrics: Optional[List[List[str]]] = []
    depends_on: Optional[DependsOn] = Field(
        default_factory=lambda: DependsOn.model_validate({"macros": [], "nodes": []})
    )
    compiled_path: Optional[str] = None
    compiled: Optional[bool] = False
    compiled_code: Optional[str] = None
    extra_ctes_injected: Optional[bool] = False
    extra_ctes: Optional[List[InjectedCTE]] = []
    contract: Optional[Contract] = Field(
        default_factory=lambda: Contract.model_validate(
            {"enforced": False, "checksum": None}
        )
    )
    defer_relation: Optional[DeferRelation] = None

    @computed_field
    @property
    def config_block(self) -> Optional[Dict[str, Any]]:
        return get_config_block(self.raw_code)
