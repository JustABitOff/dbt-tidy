import factory
from factory.fuzzy import FuzzyInteger

from tidy.manifest.bases.ref_args import RefArgs


class RefArgsFactory(factory.Factory):
    class Meta:
        model = RefArgs

    name = factory.Faker("word")
    package = factory.Faker("word")
    version = FuzzyInteger(1, 5)
