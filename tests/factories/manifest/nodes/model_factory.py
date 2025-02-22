from factory import Factory

from tidy.manifest.nodes.model import (
    ModelLevelConstraint,
    ModelBuildAfter,
    ModelFreshness,
    Model,
)


class ModelLevelConstraintFactory(Factory):
    class Meta:
        model = ModelLevelConstraint


class ModelBuildAfterFactory(Factory):
    class Meta:
        model = ModelBuildAfter


class ModelFreshnessFactory(Factory):
    class Meta:
        model = ModelFreshness


class ModelFactory(Factory):
    class Meta:
        model = Model
