import factory

from tidy.manifest.parent_map.parent_map import ParentMap


class ParentMapFactory(factory.Factory):
    class Meta:
        model = ParentMap

    root = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(None, None, {"locale": "en_US"}): [
                factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
                for _ in range(3)
            ]
            for _ in range(2)
        }
    )
