from factory import Factory

from tidy.manifest.nodes.seed import SeedConfig, Seed


class SeedConfigFactory(Factory):
    class Meta:
        model = SeedConfig


class SeedFactory(Factory):
    class Meta:
        model = Seed
