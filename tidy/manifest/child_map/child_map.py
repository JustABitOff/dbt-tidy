from pydantic import RootModel


class ChildMap(RootModel[dict[str, list[str]]]):
    pass
