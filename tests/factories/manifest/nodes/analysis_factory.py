from factory import Factory

from tidy.manifest.nodes.analysis import Analysis


class AnalysisFactory(Factory):
    class Meta:
        model = Analysis
