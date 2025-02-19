from factory import Factory

from tidy.manifest.parent_map.parent_map import ParentMap


class ParentMapFactory(Factory):
    class Meta:
        model = ParentMap
