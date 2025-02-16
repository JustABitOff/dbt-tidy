from pydantic import RootModel


class ParentMap(RootModel[dict[str, list[str]]]):
    pass
