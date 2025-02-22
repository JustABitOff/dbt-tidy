import factory

from tidy.manifest.metadata.metadata import Metadata


class MetadataFactory(factory.Factory):
    class Meta:
        model = Metadata

    dbt_schema_version = "https://schemas.getdbt.com/dbt/manifest/v12.json"
    dbt_version = "1.9.0"
    generated_at = factory.LazyFunction(
        lambda: str(
            factory.Faker("date_this_year").evaluate(None, None, {"locale": "en_US"})
        )
    )
    invocation_id = factory.Faker("uuid4")
    env = factory.LazyFunction(
        lambda: {
            factory.Faker("word").evaluate(
                None, None, {"locale": "en_US"}
            ): factory.Faker("word").evaluate(None, None, {"locale": "en_US"})
            for _ in range(2)
        }
    )
    project_name = factory.Faker("word")
    project_id = factory.Faker("uuid4")
    user_id = factory.Faker("uuid4")
    send_anonymous_usage_stats = factory.Faker("boolean")
    adapter_type = "postgres"
