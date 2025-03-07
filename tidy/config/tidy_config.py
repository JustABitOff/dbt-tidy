from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict, model_validator
from typing import List, Literal, Optional
import yaml

from tidy.config.constants import TIDY_CONFIG_PATH


class TidyConfig(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    custom_sweeps_path: Path = Path(".tidy")
    mode: Literal["all", "include", "exclude"] = "all"
    sweeps: Optional[List[str]] = Field(default_factory=list)

    @model_validator(mode='before')
    @classmethod
    def load_from_yaml(cls, values) -> "TidyConfig":
        if not TIDY_CONFIG_PATH.exists():
            message = "Error: `tidy.yaml` not found."
            raise FileNotFoundError(message)
        
        if not values:
            try:
                return yaml.safe_load(TIDY_CONFIG_PATH.read_text())
            except yaml.YAMLError as e:
                raise ValueError(f"Invalid YAML format in {TIDY_CONFIG_PATH}: {e}")

        return values
