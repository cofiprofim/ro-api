"""

"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from ... import RobloxClient

from ..._utilities.dataclass_maker import item_dataclass, param, FormatType


class ClientAttr:
    """
    Literal client attr for IDLE
    """
    _client: RobloxClient


class BaseItem:
    id: int

    def __init__(self):
        if not isinstance(self, BaseItem):
            raise TypeError("BaseItem can't be initialized")

    def __init_subclass__(cls, id_key: Optional[str] = "id", **kwargs):
        cls._FIELDS = {"id": param(key_name=id_key)}
        super().__init_subclass__(**kwargs)
