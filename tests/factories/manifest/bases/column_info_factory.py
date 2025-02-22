import factory

from tidy.manifest.bases.column_info import ColumnLevelConstraint, ColumnInfo


class ColumnLevelConstraintFactory(factory.Factory):
    class Meta:
        model = ColumnLevelConstraint

    type = factory.Iterator(
        ["check", "not_null", "unique", "primary_key", "foreign_key", "custom"]
    )
    name = factory.Faker("word")
    expression = factory.Faker("sentence")
    to = factory.Faker("word")
    to_columns = factory.List([factory.Faker("word") for _ in range(2)])


class ColumnInfoFactory(factory.Factory):
    class Meta:
        model = ColumnInfo

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    meta = {"test_key": "test_value"}
    data_type = factory.Faker("word")
    constraints = factory.List(
        [factory.SubFactory(ColumnLevelConstraintFactory) for _ in range(2)]
    )
    quote = factory.Faker("boolean", chance_of_getting_true=50)
    tags = factory.List([factory.Faker("word") for _ in range(3)])
    granularity = factory.Iterator(
        [
            "nanosecond",
            "microsecond",
            "millisecond",
            "second",
            "minute",
            "hour",
            "day",
            "week",
            "month",
            "quarter",
            "year",
        ]
    )
