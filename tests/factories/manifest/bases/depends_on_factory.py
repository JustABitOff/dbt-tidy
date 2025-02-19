from factory import Factory

from tidy.manifest.bases.depends_on import DependsOn


class DependsOnFactory(Factory):
    class Meta:
        model = DependsOn