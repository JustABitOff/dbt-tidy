from factory import Factory

from tidy.manifest.bases.ref_args import RefArgs


class RefArgsFactory(Factory):
    class Meta:
        model = RefArgs