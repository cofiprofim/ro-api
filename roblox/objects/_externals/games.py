from typing import Literal, Optional

from .. import item_dataclass, FormatType
from roblox.objects.bases import BaseItem


@item_dataclass(format_type=FormatType.camel_case)
class GameMedia(BaseItem):
    asset_type_id: Literal[1]
    asset_type: Literal["Image"]
    image_id: str
    video_hash: Optional[str]
    video_title: Optional[str]
    approved: bool
    alt_text: str
