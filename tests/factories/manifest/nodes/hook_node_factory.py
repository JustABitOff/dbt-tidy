from factory import Factory

from tidy.manifest.nodes.hook_node import HookNode


class HookNodeFactory(Factory):
    class Meta:
        model = HookNode
