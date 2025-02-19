from factory import Factory

from tidy.manifest.bases.docs_config import DocsConfig


class DocsConfigFactory(Factory):
    class Meta:
        model = DocsConfig