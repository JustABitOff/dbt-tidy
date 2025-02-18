from typing import Dict, List, Any, Literal

from pydantic import BaseModel

from tidy.manifest.bases import DocsConfig


class MacroDependsOn(BaseModel):
    macros: List[str] = []


class MacroArgument(BaseModel):
    name: str
    type: str | None = None
    description: str = ""


class Macro(BaseModel):
    name: str
    resource_type: Literal["macro"] = "macro"
    package_name: str
    path: str
    origional_file_path: str | None = None
    unique_id: str
    macro_sql: str
    depends_on: MacroDependsOn
    description: str = ""
    meta: Dict[str, Any] = {}
    docs: DocsConfig
    patch_path: str | None = None
    arguments: List[MacroArgument] = []
    created_at: float
    supported_languages: List[Literal["python", "sql"]] | None = None
