from factory import Factory

from tidy.manifest.bases.owner import Owner


class OwnerFactory(Factory):
    class Meta:
        model = Owner