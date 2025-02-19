from factory import Factory

from tidy.manifest.macros.macro import Macro, MacroArgument, MacroDependsOn



class MacroDependsOnFactory(Factory):
    class Meta:
        model = MacroDependsOn


class MacroArgumentFactory(Factory):
    class Meta:
        model = MacroArgument


class MacroFactory(Factory):
    class Meta:
        model = Macro                