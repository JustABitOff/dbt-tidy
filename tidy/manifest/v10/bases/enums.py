from enum import Enum


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
    semantic_model = "semantic_model"


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


class Access(Enum):
    private = "private"
    protected = "protected"
    public = "public"


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


class GrainToDate(Enum):
    day = "day"
    week = "week"
    month = "month"
    quarter = "quarter"
    year = "year"


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
