from ..objects.bases.basegame import BaseGame
from ..objects.game import Game
from .._utilities.cursor_iterator import CursorIterator
from .._utilities.types import BaseId, ClientType
from .._utilities.subdomains import games_domain
from .._utilities import make_docs

from typing import Union, List

from roblox.utils.subdomains import games
from roblox.utils.decorators import make_docs

from .._api.games import fetch_game_media

from roblox.objects.game import Game
from roblox.objects.bases.basegame import BaseGame
from roblox.utils.cursor_iterator import CursorIterator


@make_docs("Fetch user's created games", "Yea")
def fetch_user_games(user_id: int, client: RobloxClient = None) -> CursorIterator:
    return CursorIterator(
        games.v2.add_path("users", user_id, "games"),
        client=client,
        handler=lambda x: map(BaseGame, x)
    )


@make_docs("d", "ds")
def fetch_games(games_ids: Union[int, List[int]], client: RobloxClient = None) -> List[Game]:
    response = client.get(
        games.v1.add_path("games").add_kwargs(universeIds=(games_ids,))
    ).json()
    return [Game(game_data) for game_data in response["data"]]
