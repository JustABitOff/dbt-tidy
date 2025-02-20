import factory

from tests.factories.manifest.bases.owner_factory import OwnerFactory
from tests.factories.manifest.bases.depends_on_factory import DependsOnFactory
from tests.factories.manifest.bases.ref_args_factory import RefArgsFactory
from tidy.manifest.exposures.exposure import Exposure, ExposureConfig


class ExposureConfigFactory(factory.Factory):
    class Meta:
        model = ExposureConfig

    enabled = factory.Faker("boolean")


class ExposureFactory(factory.Factory):
    class Meta:
        model = Exposure

    name = factory.Faker("word")
    package_name = factory.Faker("word")
    path = factory.Faker("file_path")
    original_file_path = factory.Faker("file_path")
    unique_id = factory.LazyAttribute(lambda obj: f"{obj.package_name}.{obj.name}")
    fqn = factory.LazyAttribute(lambda obj: [obj.package_name, obj.name])
    type = factory.Faker("random_element", elements=["dashboard", "notebook", "analysis", "ml", "application"])
    owner = factory.SubFactory(OwnerFactory)
    description = factory.Faker("sentence")
    label = factory.Faker("word")
    maturity = factory.Faker("random_element", elements=["low", "medium", "high", None])
    meta = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(None, None, {'locale': 'en_US'}): 
            factory.Faker("word").evaluate(None, None, {'locale': 'en_US'})
            for _ in range(2)
        }
    )
    tags = factory.List([factory.Faker("word") for _ in range(3)])
    config = factory.SubFactory(ExposureConfigFactory)
    unrendered_config = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(None, None, {'locale': 'en_US'}): 
            factory.Faker("word").evaluate(None, None, {'locale': 'en_US'})
            for _ in range(2)
        }
    )
    url = factory.Faker("url")
    depends_on = factory.SubFactory(DependsOnFactory)
    refs = factory.List([factory.SubFactory(RefArgsFactory) for _ in range(2)])
    sources = factory.List([factory.List([factory.Faker("word")])  for _ in range(3)])
    metrics = factory.List([factory.List([factory.Faker("word")])  for _ in range(3)])
    created_at = factory.Faker("unix_time")