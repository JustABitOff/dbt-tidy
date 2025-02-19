from factory import Factory

from tidy.manifest.exposures.exposure import Exposure, ExposureConfig


class ExposureConfigFactory(Factory):
    class Meta:
        model = ExposureConfig


class ExposureFactory(Factory):
    class Meta:
        model = Exposure
