from factory import Factory

from tidy.manifest.selectors.selector import Selector


class SelectorFactory(Factory):
    class Meta:
        model = Selector
