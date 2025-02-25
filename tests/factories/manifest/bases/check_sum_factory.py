import factory

from tidy.manifest.bases.check_sum import Checksum


class ChecksumFactory(factory.Factory):
    class Meta:
        model = Checksum

    name = factory.Faker("word")
    checksum = factory.Faker("sha256")
