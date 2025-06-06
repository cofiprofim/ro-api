from ...utils.dataclass_make import item_dataclass, param


@item_dataclass
class BaseRootPlace:
    type: str = param(optional=True)
