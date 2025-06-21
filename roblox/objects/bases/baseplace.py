from .. import item_dataclass, param
from . import BaseItem, ClientAttr


@item_dataclass
class BaseRootPlace(BaseItem, ClientAttr):
    type: str = param(optional=True)
