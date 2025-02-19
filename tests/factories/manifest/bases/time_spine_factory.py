from factory import Factory

from tidy.manifest.bases.time_spine import CustomGranularity, TimeSpine


class CustomGranularityFactory(Factory):
    class Meta:
        model = CustomGranularity


class TimeSpineFactory(Factory):
    class Meta:
        model = TimeSpine        