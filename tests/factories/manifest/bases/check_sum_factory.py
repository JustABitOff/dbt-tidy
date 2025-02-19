from factory import Factory

from tidy.manifest.bases.check_sum import Checksum


class ChecksumFactory(Factory):
    class Meta:
        model = Checksum
