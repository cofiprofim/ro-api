from datetime import datetime

from ..bases.basecreator import BaseCreator
from ..bases.baseplace import BaseRootPlace
from .. import item_dataclass, param, FormatType
from ...utils.decorators import make_docs
from ...utils.timestamps import from_timestamp
from ...utils.subdomains import games



@item_dataclass(format_type=FormatType.camel_case)
class GameMedia(BaseItem):
    asset_type_id: Literal[1]
    asset_type: Literal["Image"]
    image_id: str
    video_hash: Optional[str]
    video_title: Optional[str]
    approved: bool
    alt_text: str


@item_dataclass(format_type=FormatType.camel_case)
class BaseGame(BaseItem, ClientAttr):
    name: str
    description: Optional[str]
    creator: BaseCreator = param(handler=BaseCreator)
    root_place: BaseRootPlace = param(handler=BaseRootPlace)
    created: datetime = param(handler=from_timestamp)
    updated: datetime = param(handler=from_timestamp)
    visits: int = param(key_name="placeVisits")

    @make_docs("dsd", "dsds", False)
    def fetch_game_media(self, client: RobloxClient = None) -> GameMedia:
        response = client.get(
            games.v1.add_path("games", self.id, "media")
        ).json()
        return GameMedia(response["data"][0])
