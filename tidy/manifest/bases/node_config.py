from typing import Literal

from tidy.manifest.bases.base_config import BaseConfig


class NodeConfig(BaseConfig):
    access: Literal["private", "protected", "public"] = "public"
