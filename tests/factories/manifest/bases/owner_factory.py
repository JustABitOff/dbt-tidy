import factory

from tidy.manifest.bases.owner import Owner


class OwnerFactory(factory.Factory):
    class Meta:
        model = Owner

    email = factory.Faker("email")
    name = factory.Faker("name")
