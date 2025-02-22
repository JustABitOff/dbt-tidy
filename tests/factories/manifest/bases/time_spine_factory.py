import factory

from tidy.manifest.bases.time_spine import CustomGranularity, TimeSpine


class CustomGranularityFactory(factory.Factory):
    class Meta:
        model = CustomGranularity

    name = factory.Faker("word")
    column_name = factory.Faker("word")


class TimeSpineFactory(factory.Factory):
    class Meta:
        model = TimeSpine

    standard_granularity_column = factory.Faker("word")
    custom_granularities = factory.List(
        [factory.SubFactory(CustomGranularityFactory) for _ in range(2)]
    )
