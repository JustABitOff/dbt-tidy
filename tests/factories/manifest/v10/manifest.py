from typing import Dict

import factory

from tidy.manifest.v10.manifest import ManifestV10
from tidy.manifest.v10.metadata.metadata import ManifestMetadata
from tidy.manifest.v10.nodes.models.model import ModelNode
from tidy.manifest.v10.sources.source_definition import SourceDefinition
from tidy.manifest.v10.macros.macro import Macro
from tidy.manifest.v10.documentation.documentation import Documentation
from tidy.manifest.v10.exposures.exposure import Exposure
from tidy.manifest.v10.metrics.metric import Metric
from tidy.manifest.v10.groups.group import Group
from tidy.manifest.v10.semantic_models.semantic_model import SemanticModel


class ManifestMetadataFactory(factory.Factory):
    class Meta:
        model = ManifestMetadata
    
    project_name = "unit_test_package"

class ModelNodeFactory(factory.Factory):
    class Meta:
        model = ModelNode

    database = "unit_test_db"
    schema = "unit_test_schema"
    name = factory.Sequence(lambda n: f"model_{n}")
    resource_type = "model"
    path = f"marts/{name}.sql"
    original_file_path = f"models/marts/{name}.sql"
    description = "Test model node"

class SourceDefinitionFactory(factory.Factory):
    class Meta:
        model = SourceDefinition
    
    name = factory.Sequence(lambda n: f"source_{n}")

class ManifestV10Factory(factory.Factory):
    class Meta:
        model = ManifestV10

    metadata = factory.SubFactory(ManifestMetadataFactory)
    nodes = {}
    sources = {}
    # nodes = factory.LazyAttribute(lambda _: {
    #     f"model_{i}": ModelNodeFactory()
    #     for i in range(3)
    # })
    # sources = factory.LazyAttribute(lambda _: {
    #     f"source_{i}": SourceDefinitionFactory()
    #     for i in range(2)
    # })
    macros = {}
    docs = {}
    exposures = {}
    metrics = {}
    groups = {}
    selectors = {}
    disabled = None
    parent_map = {}
    child_map = {}
    group_map = {}
    semantic_models = {}