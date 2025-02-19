from factory import Factory

from tidy.manifest.bases.source_file_metadata import FileSlice, SourceFileMetadata


class FileSliceFactory(Factory):
    class Meta:
        model = FileSlice


class SourceFileMetadataFactory(Factory):
    class Meta:
        model = SourceFileMetadata