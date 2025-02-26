from enum import Enum


class OnConfigurationChange(Enum):
    apply = "apply"
    continue_ = "continue"
    fail = "fail"


class ConstraintType(Enum):
    check = "check"
    not_null = "not_null"
    unique = "unique"
    primary_key = "primary_key"
    foreign_key = "foreign_key"
    custom = "custom"


class Granularity(Enum):
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


class ResourceType(Enum):
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


class Access(Enum):
    private = "private"
    protected = "protected"
    public = "public"


class DependsOn(Enum):
    all = "all"
    any = "any"


class Period(Enum):
    minute = "minute"
    hour = "hour"
    day = "day"


class SupportedLanguage(Enum):
    python = "python"
    sql = "sql"


class ExposureType(Enum):
    dashboard = "dashboard"
    notebook = "notebook"
    analysis = "analysis"
    ml = "ml"
    application = "application"


class Maturity(Enum):
    low = "low"
    medium = "medium"
    high = "high"


class MetricType(Enum):
    simple = "simple"
    ratio = "ratio"
    cumulative = "cumulative"
    derived = "derived"
    conversion = "conversion"


class MetricCalculation(Enum):
    conversions = "conversions"
    conversion_rate = "conversion_rate"


class PeriodAgg(Enum):
    first = "first"
    last = "last"
    average = "average"


class ExportAs(Enum):
    table = "table"
    view = "view"


class EntityType(Enum):
    foreign = "foreign"
    natural = "natural"
    primary = "primary"
    unique = "unique"


class Agg(Enum):
    sum = "sum"
    min = "min"
    max = "max"
    count_distinct = "count_distinct"
    sum_boolean = "sum_boolean"
    average = "average"
    percentile = "percentile"
    median = "median"
    count = "count"


class DimensionType(Enum):
    categorical = "categorical"
    time = "time"


class UnitTestFixtureFormat(Enum):
    csv = "csv"
    dict = "dict"
    sql = "sql"
