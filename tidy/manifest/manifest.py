import json
from typing import Dict, Union

from pydantic import BaseModel

from tidy.manifest.nodes import (
    Analysis,
    GenericTest,
    HookNode,
    Model,
    Seed,
    SingularTest,
    Snapshot,
    SqlOperation,
)
from tidy.manifest.sources import Source
from tidy.manifest.macros import Macro
from tidy.manifest.docs import Documentation
from tidy.manifest.exposures import Exposure
from tidy.manifest.metrics import Metric


class Manifest(BaseModel):
    nodes: Dict[
        str,
        Union[
            Analysis,
            GenericTest,
            HookNode,
            Model,
            Seed,
            SingularTest,
            Snapshot,
            SqlOperation,
        ],
    ] = {}
    sources: Dict[str, Source] = {}
    macros: Dict[str, Macro] = {}
    docs: Dict[str, Documentation] = {}
    exposures: Dict[str, Exposure] = {}
    metrics: Dict[str, Metric] = {}

    @classmethod
    def load_from_json(cls, file_path: str) -> "Manifest":
        with open(file_path, "r") as file:
            data = json.load(file)
            return cls.model_validate(data)
