import factory

from tidy.manifest.bases.defer_relation import DeferRelation
from tests.factories.manifest.bases.node_config_factory import NodeConfigFactory


class DeferRelationFactory(factory.Factory):
    class Meta:
        model = DeferRelation

    database = factory.Faker("word")
    schema_name = factory.Faker("word")
    alias = factory.Faker("word")
    relation_name = factory.Faker("word")
    resource_type = factory.Faker("word")
    name = factory.Faker("word")
    description = factory.Faker("sentence")
    compiled_code = factory.Faker("sentence")
    meta = {"test_key": "test_value"}
    tags = factory.List([factory.Faker("word") for _ in range(3)])
    config = factory.SubFactory(NodeConfigFactory)
