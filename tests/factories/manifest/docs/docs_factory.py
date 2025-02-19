from factory import Factory

from tidy.manifest.docs.documentation import Documentation


class DocumentationFactory(Factory):
    class Meta:
        model = Documentation
