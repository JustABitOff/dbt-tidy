import factory

from tidy.manifest.docs.documentation import Documentation


class DocumentationFactory(factory.Factory):
    class Meta:
        model = Documentation

    name = factory.Faker("word")
    package_name = factory.Faker("word")
    path = factory.Faker("word")
    original_file_path = factory.Faker("word")
    unique_id = factory.Faker("word")
    block_contents = factory.Faker("sentence")
