from factory import Factory

from tidy.manifest.bases.hook import Hook


class HookFactory(Factory):
    class Meta:
        model = Hook