from datetime import datetime
import random

import factory
from factory.fuzzy import FuzzyInteger

from tests.factories.manifest.bases.contract_config_factory import ContractConfigFactory
from tests.factories.manifest.bases.docs_config_factory import DocsConfigFactory
from tests.factories.manifest.bases.hook_factory import HookFactory
from tidy.manifest.bases.base_config import BaseConfig



class BaseConfigFactory(factory.Factory):
    class Meta:
        model = BaseConfig

    alias = factory.Faker("word")
    schema_name = factory.Faker("word")
    database = factory.Faker("word")
    tags = factory.List([factory.Faker("word") for _ in range(3)])
    meta = {
        "test_key": "test_value"
    }
    group = factory.Faker("word")
    materialized = factory.LazyFunction(lambda: random.choice(["view", "incremental", "table"]))
    incremental_strategy = factory.LazyAttribute(
        lambda obj: "merge" if obj.materialized == "incremental" else None
    )
    batch_size = factory.LazyFunction(lambda: str(FuzzyInteger(1, 10).fuzz()))
    begin = "1999-12-31"
    persist_docs = {
        "relation": True,
        "columns": True,
    }
    post_hook = factory.List([factory.SubFactory(HookFactory) for _ in range(2)])
    pre_hook = factory.List([factory.SubFactory(HookFactory) for _ in range(2)])
    quoting = {
        "database": True,
        "schema": True,
        "identifier": True,
    }
    column_types = {
        "test_column": "varchar(255)"
    }
    full_refresh = factory.Faker("boolean")
    unique_key = ["id", "timestamp"]
    grants = {
        "select": "test_object"
    }
    packages = factory.List([factory.Faker("word") for _ in range(2)])
    docs = factory.SubFactory(DocsConfigFactory)
    contract = factory.SubFactory(ContractConfigFactory)
    event_time = int(datetime.now().timestamp())
