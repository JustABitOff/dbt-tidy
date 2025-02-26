from typing import List, Optional, Union, Literal

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v12.bases.depends_on import DependsOn
from tidy.manifest.v12.unit_tests.unit_test_input_fixture import UnitTestInputFixture
from tidy.manifest.v12.unit_tests.unit_test_output_fixture import UnitTestOutputFixture
from tidy.manifest.v12.unit_tests.unit_test_overrides import UnitTestOverrides
from tidy.manifest.v12.unit_tests.unit_test_config import UnitTestConfig
from tidy.manifest.v12.unit_tests.unit_test_node_versions import UnitTestNodeVersions


class UnitTestDefinition(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    model: str
    given: List[UnitTestInputFixture]
    expect: UnitTestOutputFixture = Field(..., title="UnitTestOutputFixture")
    name: str
    resource_type: Literal["unit_test"]
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: List[str]
    description: Optional[str] = ""
    overrides: Optional[UnitTestOverrides] = None
    depends_on: Optional[DependsOn] = Field(None, title="DependsOn")
    config: Optional[UnitTestConfig] = Field(None, title="UnitTestConfig")
    checksum: Optional[str] = None
    schema_: Optional[str] = Field(None, alias="schema")
    created_at: Optional[float] = None
    versions: Optional[UnitTestNodeVersions] = None
    version: Optional[Union[str, float]] = None
