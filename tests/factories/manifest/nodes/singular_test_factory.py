from factory import Factory

from tidy.manifest.nodes.singular_test import SingularTest


class SingularTestFactory(Factory):
    class Meta:
        model = SingularTest
