from typing import Literal, Optional, Dict, Any, List

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v12.macros.macro_depends_on import MacroDependsOn
from tidy.manifest.v12.macros.macro_argument import MacroArgument
from tidy.manifest.v12.bases.docs import Docs
from tidy.manifest.v12.bases.enums import SupportedLanguage


class Macro(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str
    resource_type: Literal["macro"]
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    macro_sql: str
    depends_on: Optional[MacroDependsOn] = Field(None, title="MacroDependsOn")
    description: Optional[str] = ""
    meta: Optional[Dict[str, Any]] = None
    docs: Optional[Docs] = Field(None, title="Docs")
    patch_path: Optional[str] = None
    arguments: Optional[List[MacroArgument]] = None
    created_at: Optional[float] = None
    supported_languages: Optional[List[SupportedLanguage]] = None
