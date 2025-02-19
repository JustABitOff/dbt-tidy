from factory import Factory

from tidy.manifest.nodes.generic_test import (
    TestMetadata,
    TestConfig,
    GenericTest,
)    

class TestMetadataFactory(Factory):
    class Meta:
        model = TestMetadata


class TestConfigFactory(Factory):
    class Meta:
        model = TestConfig


class GenericTestFactory(Factory):
    class Meta:
        model = GenericTest                