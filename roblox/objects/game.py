from enum import Enum

from . import item_dataclass, param, FormatType
from .bases.baseplace import BaseRootPlace
from .bases.basegame import BaseGame
from .creator import Creator

from typing import Optional, List


class UniverseAvatarType(Enum):
    """

    """

    R6 = "MorphToR6"
    R15 = "MorphToR15"
    player_choice = "PlayerChoice"


class Genre(Enum):
    """
    The universe's genre.
    """

    all = "All"
    building = "Building"
    horror = "Horror"
    town_and_city = "Town and City"
    military = "Military"
    comedy = "Comedy"
    medieval = "Medieval"
    adventure = "Adventure"
    sci_fi = "Sci-Fi"
    naval = "Naval"
    fps = "FPS"
    rpg = "RPG"
    sports = "Sports"
    fighting = "Fighting"
    western = "Western"


@item_dataclass(format_type=FormatType.camel_case)
class Game(BaseGame):
    creator: Creator = param(handler=Creator)
    root_place: BaseRootPlace = param(key_name="rootPlaceId",
                                      handler=lambda x: BaseRootPlace({"id": x}))
    price: Optional[int]
    allowed_gear_genres: List[str]
    allowed_gear_categories: List[str]
    is_genre_enforced: bool
    copying_allowed: bool
    playing: int
    visits: int = param(key_name="visits")
    max_players: int
    studio_access_to_apis_allowed: bool
    create_vip_servers_allowed: bool
    universe_avatar_type: UniverseAvatarType = param(handler=UniverseAvatarType)
    genre: Genre = param(handler=Genre)
    is_all_genre: bool
    is_favorited_by_user: bool
    favorited_count: int
