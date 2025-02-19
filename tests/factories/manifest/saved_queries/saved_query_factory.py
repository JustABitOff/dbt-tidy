from factory import Factory

from tidy.manifest.saved_queries.saved_query import (
    QueryParams,
    ExportConfig,
    Export,
    SavedQueryCache,
    SavedQueryConfig,
    SavedQuery,
)


class QueryParamsFactory(Factory):
    class Meta:
        model = QueryParams


class ExportConfigFactory(Factory):
    class Meta:
        model = ExportConfig


class ExportFactory(Factory):
    class Meta:
        model = Export    


class SavedQueryCacheFactory(Factory):
    class Meta:
        model = SavedQueryCache    


class SavedQueryConfigFactory(Factory):
    class Meta:
        model = SavedQueryConfig            


class SavedQueryFactory(Factory):
    class Meta:
        model = SavedQuery
