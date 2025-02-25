from typing import Any, Union, Literal

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.bases.depends_on import DependsOn


class UnitTestInputFixture(BaseModel):
    input: str
    rows: Union[str, list[dict[str, Any]], None] = None
    format: Literal["csv", "dict", "sql"] = "dict"
    fixture: str | None = None


class UnitTestOutputFixture(BaseModel):
    rows: Union[str, list[dict[str, Any]], None] = None
    format: Literal["csv", "dict", "sql"] = "dict"
    fixture: str | None = None


class UnitTestOverrides(BaseModel):
    macros: dict[str, Any] = {}
    vars: dict[str, Any] = {}
    env_vars: dict[str, Any] = {}


class UnitTestConfig(BaseModel):
    tags: str | list[str] = []
    meta: dict[str, Any] = {}
    enabled: bool = True

    model_config = ConfigDict(
        extra="allow",
    )


class UnitTestNodeVersions(BaseModel):
    include: list[str | float] | None = None
    exclude: list[str | float] | None = None


class UnitTest(BaseModel):
    model: str
    given: list[UnitTestInputFixture] = []
    expect: list[UnitTestOutputFixture] = []
    name: str
    resource_type: Literal["unit_test"] = "unit_test"
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: list[str]
    description: str = ""
    overrides: UnitTestOverrides | None = None
    depends_on: DependsOn = DependsOn()
    config: UnitTestConfig = UnitTestConfig()
    checksum: str | None = None
    schema_name: str = Field(None, alias="schema")
    created_at: float
    versions: UnitTestNodeVersions | None = None
    version: Union[str, float, None] = None
