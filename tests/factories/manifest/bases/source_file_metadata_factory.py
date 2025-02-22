import factory
from factory.fuzzy import FuzzyInteger

from tidy.manifest.bases.source_file_metadata import FileSlice, SourceFileMetadata


class FileSliceFactory(factory.Factory):
    class Meta:
        model = FileSlice

    filename = factory.Faker("word")
    content = factory.Faker("sentence")
    start_line_number = FuzzyInteger(1, 150)
    end_line_number = FuzzyInteger(151, 300)


class SourceFileMetadataFactory(factory.Factory):
    class Meta:
        model = SourceFileMetadata

    repo_file_path = factory.Faker("file_path")
    file_slice = factory.SubFactory(FileSliceFactory)
