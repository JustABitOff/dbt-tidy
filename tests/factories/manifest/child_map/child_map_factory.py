from factory import Factory

from tidy.manifest.child_map.child_map import ChildMap


class ChildMapFactory(Factory):
    class Meta:
        model = ChildMap
