from factory import Factory

from tidy.manifest.bases.base_config import BaseConfig


class BaseConfigFactory(Factory):
    class Meta:
        model = BaseConfig
