from enum import Enum

from .. import item_dataclass, param


class CreatorType(Enum):
    """

    """

    group = "Group"
    user = "User"


@item_dataclass
class BaseCreator:
    type: CreatorType = param(handler=CreatorType)
