from factory import Factory

from tidy.manifest.metadata.metadata import Metadata



class MetadataFactory(Factory):
    class Meta:
        model = Metadata
