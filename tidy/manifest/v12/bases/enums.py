from enum import StrEnum


class OnConfigurationChange(StrEnum):
    apply = "apply"
    continue_ = "continue"
    fail = "fail"


class ConstraintType(StrEnum):
    check = "check"
    not_null = "not_null"
    unique = "unique"
    primary_key = "primary_key"
    foreign_key = "foreign_key"
    custom = "custom"


class Granularity(StrEnum):
    nanosecond = "nanosecond"
    microsecond = "microsecond"
    millisecond = "millisecond"
    second = "second"
    minute = "minute"
    hour = "hour"
    day = "day"
    week = "week"
    month = "month"
    quarter = "quarter"
    year = "year"


class ResourceType(StrEnum):
    model = "model"
    analysis = "analysis"
    test = "test"
    snapshot = "snapshot"
    operation = "operation"
    seed = "seed"
    rpc = "rpc"
    sql_operation = "sql_operation"
    doc = "doc"
    source = "source"
    macro = "macro"
    exposure = "exposure"
    metric = "metric"
    group = "group"
    saved_query = "saved_query"
    semantic_model = "semantic_model"
    unit_test = "unit_test"
    fixture = "fixture"


class Access(StrEnum):
    private = "private"
    protected = "protected"
    public = "public"


class DependsOn(StrEnum):
    all = "all"
    any = "any"


class Period(StrEnum):
    minute = "minute"
    hour = "hour"
    day = "day"


class SupportedLanguage(StrEnum):
    python = "python"
    sql = "sql"


class ExposureType(StrEnum):
    dashboard = "dashboard"
    notebook = "notebook"
    analysis = "analysis"
    ml = "ml"
    application = "application"


class Maturity(StrEnum):
    low = "low"
    medium = "medium"
    high = "high"


class MetricType(StrEnum):
    simple = "simple"
    ratio = "ratio"
    cumulative = "cumulative"
    derived = "derived"
    conversion = "conversion"


class MetricCalculation(StrEnum):
    conversions = "conversions"
    conversion_rate = "conversion_rate"


class PeriodAgg(StrEnum):
    first = "first"
    last = "last"
    average = "average"


class ExportAs(StrEnum):
    table = "table"
    view = "view"


class EntityType(StrEnum):
    foreign = "foreign"
    natural = "natural"
    primary = "primary"
    unique = "unique"


class Agg(StrEnum):
    sum = "sum"
    min = "min"
    max = "max"
    count_distinct = "count_distinct"
    sum_boolean = "sum_boolean"
    average = "average"
    percentile = "percentile"
    median = "median"
    count = "count"


class DimensionType(StrEnum):
    categorical = "categorical"
    time = "time"


class UnitTestFixtureFormat(StrEnum):
    csv = "csv"
    dict = "dict"
    sql = "sql"
