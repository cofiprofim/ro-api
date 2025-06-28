from datetime import datetime

from .. import item_dataclass, param, FormatType
from ..._utilities import from_timestamp
from ..bases.basecreator import BaseCreator
from ..bases.baseplace import BaseRootPlace
from . import BaseItem, ClientAttr

from typing import Optional


from .._externals.games import GameMedia


@item_dataclass(format_type=FormatType.camel_case)
class BaseGame(BaseItem, ClientAttr):
    name: str
    description: Optional[str]
    creator: BaseCreator = param(handler=BaseCreator)
    root_place: BaseRootPlace = param(handler=BaseRootPlace)
    created: datetime = param(handler=from_timestamp)
    updated: datetime = param(handler=from_timestamp)
    visits: int = param(key_name="placeVisits")

    from ..._api.games import fetch_game_media
