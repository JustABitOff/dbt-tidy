from factory import Factory

from tidy.manifest.bases.defer_relation import DeferRelation


class DeferRelationFactory(Factory):
    class Meta:
        model = DeferRelation