import factory

from tidy.manifest.bases.docs_config import DocsConfig


class DocsConfigFactory(factory.Factory):
    class Meta:
        model = DocsConfig

    node_color = factory.Faker("hex_color")
