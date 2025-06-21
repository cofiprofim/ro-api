from enum import Enum

from .. import item_dataclass, param
from . import BaseItem, ClientAttr


class CreatorType(Enum):
    """

    """

    group = "Group"
    user = "User"


@item_dataclass
class BaseCreator(BaseItem, ClientAttr):
    type: CreatorType = param(handler=CreatorType)
