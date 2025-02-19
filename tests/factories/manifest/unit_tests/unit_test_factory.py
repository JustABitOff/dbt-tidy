from factory import Factory

from tidy.manifest.unit_tests.unit_test import (
    UnitTestInputFixture,
    UnitTestOutputFixture,
    UnitTestOverrides,
    UnitTestConfig,
    UnitTestNodeVersions,
    UnitTest,
)

class UnitTestInputFixtureFactory(Factory):
    class Meta:
        model = UnitTestInputFixture


class UnitTestOutputFixtureFactory(Factory):
    class Meta:
        model = UnitTestOutputFixture


class UnitTestOverridesFactory(Factory):
    class Meta:
        model = UnitTestOverrides


class UnitTestConfigFactory(Factory):
    class Meta:
        model = UnitTestConfig


class UnitTestNodeVersionsFactory(Factory):
    class Meta:
        model = UnitTestNodeVersions


class UnitTestFactory(Factory):
    class Meta:
        model = UnitTest                