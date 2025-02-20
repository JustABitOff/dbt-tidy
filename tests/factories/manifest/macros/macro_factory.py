import random

import factory

from tests.factories.manifest.bases.docs_config_factory import DocsConfigFactory
from tidy.manifest.macros.macro import Macro, MacroArgument, MacroDependsOn



class MacroDependsOnFactory(factory.Factory):
    class Meta:
        model = MacroDependsOn

    macros = factory.List([factory.Faker("word")])


class MacroArgumentFactory(factory.Factory):
    class Meta:
        model = MacroArgument

    name = factory.Faker("word")
    type = factory.Faker("word")
    description = factory.Faker("word")


class MacroFactory(factory.Factory):
    class Meta:
        model = Macro                

    name = factory.Faker("word")
    package_name = factory.Faker("word")
    path = factory.Faker("file_path")
    original_file_path = factory.Faker("file_path")
    unique_id = factory.LazyAttribute(lambda obj: f"{obj.package_name}.{obj.name}")
    macro_sql = factory.Faker("sentence")
    depends_on = factory.SubFactory(MacroDependsOnFactory)
    description = factory.Faker("sentence")
    meta = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(None, None, {'locale': 'en_US'}): 
            factory.Faker("word").evaluate(None, None, {'locale': 'en_US'})
            for _ in range(2)
        }
    )
    docs = factory.SubFactory(DocsConfigFactory)
    patch_path = factory.Faker("file_path")
    arguments = factory.List([factory.SubFactory(MacroArgumentFactory) for _ in range(3)])
    created_at = factory.Faker("unix_time")
    supported_languages = factory.LazyFunction(
        lambda: random.sample(["python", "sql"], k=random.randint(1, 2))
    )