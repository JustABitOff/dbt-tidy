from pydantic import RootModel


class GroupMap(RootModel[dict[str, list[str]]]):
    pass
