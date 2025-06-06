from datetime import datetime

from ...utils.dataclass_make import item_dataclass, param, FormatType
from ...utils.timestamps import from_timestamp
from .basecreator import BaseCreator
from .baseplace import BaseRootPlace

from typing import Optional


@item_dataclass(format_type=FormatType.camel_case)
class BaseGame:
    name: str
    description: Optional[str]
    creator: BaseCreator = param(handler=BaseCreator)
    root_place: BaseRootPlace = param(handler=BaseRootPlace)
    created: datetime = param(handler=from_timestamp)
    updated: datetime = param(handler=from_timestamp)
    visits: int = param(key_name="placeVisits")
