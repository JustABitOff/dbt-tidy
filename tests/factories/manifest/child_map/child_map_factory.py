import factory

from tidy.manifest.child_map.child_map import ChildMap


class ChildMapFactory(factory.Factory):
    class Meta:
        model = ChildMap

    root = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(None, None, {'locale': 'en_US'}): [
                factory.Faker("word").evaluate(None, None, {'locale': 'en_US'}) for _ in range(3)
            ]
            for _ in range(2)
        }
    )