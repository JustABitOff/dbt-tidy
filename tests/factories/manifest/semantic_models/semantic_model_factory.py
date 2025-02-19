from factory import Factory

from tidy.manifest.semantic_models.semantic_model import (
    NodeRelation,
    Defaults,
    SemanticLayerElementConfig,
    Entity,
    MeasureAggregationParameters,
    NonAdditiveDimension,
    Measure,
    DimensionValidityParams,
    DimensionTypeParams,
    Dimension,
    SemanticModelConfig,
    SemanticModel,
)


class NodeRelationFactory(Factory):
    class Meta:
        model = NodeRelation


class DefaultsFactory(Factory):
    class Meta:
        model = Defaults


class SemanticLayerElementConfigFactory(Factory):
    class Meta:
        model = SemanticLayerElementConfig


class EntityFactory(Factory):
    class Meta:
        Entity = Entity


class MeasureAggregationParametersFactory(Factory):
    class Meta:
        model = MeasureAggregationParameters


class NonAdditiveDimensionFactory(Factory):
    class Meta:
        model = NonAdditiveDimension


class MeasureFactory(Factory):
    class Meta:
        model = Measure


class DimensionValidityParamsFactory(Factory):
    class Meta:
        model = DimensionValidityParams


class DimensionTypeParamsFactory(Factory):
    class Meta:
        model = DimensionTypeParams


class DimensionFactory(Factory):
    class Meta:
        model = Dimension


class SemanticModelConfigFactory(Factory):
    class Meta:
        model = SemanticModelConfig


class SemanticModelFactory(Factory):
    class Meta:
        model = SemanticModel                        