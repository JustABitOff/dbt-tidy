from typing import Dict, List, Any, Literal, Union
from pydantic import BaseModel, Field, ConfigDict


class MacroDependsOn(BaseModel):
    macros: List[str] = []


class DocsConfig(BaseModel):
    show: bool = True
    node_color: str | None = None


class MacroArgument(BaseModel):
    name: str
    type: str | None = None
    description: str = ""


class Macro(BaseModel):
    name: str
    resource_type: Literal["macro"] = "macro"
    package_name: str
    path: str
    origional_file_path: str
    unique_id: str
    macro_sql: str
    depends_on: MacroDependsOn
    description: str = ""
    meta: Dict[str, Any] = {}
    docs: DocsConfig
    patch_path: str | None = None
    arguments: List[MacroArgument] = []
    created_at: int
    supported_languages: List[Literal["python", "sql"]] | None = None
