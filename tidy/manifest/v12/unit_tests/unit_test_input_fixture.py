from typing import Optional, Union, List, Dict, Any

from pydantic import BaseModel, ConfigDict

from tidy.manifest.v12.bases.enums import UnitTestFixtureFormat


class UnitTestInputFixture(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    input: str
    rows: Optional[Union[str, List[Dict[str, Any]]]] = None
    format: Optional[UnitTestFixtureFormat] = "dict"
    fixture: Optional[str] = None
