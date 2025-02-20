import factory

from tests.factories.manifest.bases.base_config_factory import BaseConfigFactory
from tidy.manifest.bases.node_config import NodeConfig


class NodeConfigFactory(BaseConfigFactory):
    class Meta:
        model = NodeConfig

    access = factory.Iterator(["private", "protected", "public"])