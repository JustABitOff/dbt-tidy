from factory import Factory

from tidy.manifest.bases.node_config import NodeConfig


class NodeConfigFactory(Factory):
    class Meta:
        model = NodeConfig