from factory import Factory

from tidy.manifest.nodes.snapshot import (
    SnapshotMetaColumnNames,
    SnapshotConfig,
    Snapshot,
)

class SnapshotMetaColumnNamesFactory(Factory):
    class Meta:
        model = SnapshotMetaColumnNames


class SnapshotConfigFactory(Factory):
    class Meta:
        model = SnapshotConfig


class SnapshotFactory(Factory):
    class Meta:
        model = Snapshot        