"""

"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from ... import RobloxClient
from .. import param


class ClientAttr:
    """
    Literal client attr for IDLE
    """
    _client: RobloxClient


class BaseItem:
    id: int

    def __init_subclass__(cls, id_key: Optional[str] = "id", **kwargs):
        cls._FIELDS = {"id": param(key_name=id_key)}
        super().__init_subclass__(**kwargs)


# from .basegame import *
# from .baseuser import *
# from .baseplace import *
# from .basecreator import *
