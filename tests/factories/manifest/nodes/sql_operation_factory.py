from factory import Factory

from tidy.manifest.nodes.sql_operation import SqlOperation


class SqlOperationFactory(Factory):
    class Meta:
        model = SqlOperation
