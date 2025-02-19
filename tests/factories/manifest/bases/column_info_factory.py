from factory import Factory

from tidy.manifest.bases.column_info import ColumnLevelConstraint, ColumnInfo


class ColumnLevelConstraintFactory(Factory):
    class Meta:
        model = ColumnLevelConstraint


class ColumnInfoFactory(Factory):
    class Meta:
        model = ColumnInfo
        