from factory import Factory

from tidy.manifest.bases.injected_cte import InjectedCte


class InjectedCteFactory(Factory):
    class Meta:
        model = InjectedCte