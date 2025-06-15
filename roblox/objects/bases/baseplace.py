from roblox.utils.decorators.dataclass_maker import item_dataclass, param


@item_dataclass
class BaseRootPlace:
    type: str = param(optional=True)
