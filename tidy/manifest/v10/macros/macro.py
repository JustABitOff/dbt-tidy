from typing import Optional, Dict, Any, List

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v10.macros.macro_depends_on import MacroDependsOn
from tidy.manifest.v10.macros.macro_argument import MacroArgument
from tidy.manifest.v10.bases.docs import Docs
from tidy.manifest.v10.bases.enums import SupportedLanguage, ResourceType


class Macro(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    resource_type: ResourceType
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    macro_sql: str
    depends_on: Optional[MacroDependsOn] = Field(
        default_factory=lambda: MacroDependsOn.model_validate({"macros": []})
    )
    description: Optional[str] = ""
    meta: Optional[Dict[str, Any]] = {}
    docs: Optional[Docs] = Field(
        default_factory=lambda: Docs.model_validate({"show": True, "node_color": None})
    )
    patch_path: Optional[str] = None
    arguments: Optional[List[MacroArgument]] = []
    created_at: Optional[float] = 1696465994.421958
    supported_languages: Optional[List[SupportedLanguage]] = None
