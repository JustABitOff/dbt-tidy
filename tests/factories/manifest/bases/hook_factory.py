import factory

from tidy.manifest.bases.hook import Hook


class HookFactory(factory.Factory):
    class Meta:
        model = Hook

    sql = factory.Faker("sentence")
    index = 0
