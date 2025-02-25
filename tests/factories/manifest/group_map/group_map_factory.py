import factory

from tidy.manifest.group_map.group_map import GroupMap


class GroupMapFactory(factory.Factory):
    class Meta:
        model = GroupMap

    root = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(None, None, {"locale": "en_US"}): [
                factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
                for _ in range(3)
            ]
            for _ in range(2)
        }
    )
