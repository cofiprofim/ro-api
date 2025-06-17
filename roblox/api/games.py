from __future__ import annotations
import itertools

from typing import TYPE_CHECKING, Union, List

if TYPE_CHECKING:
    from ..robloxclient import RobloxClient

from ..objects.bases import BaseGame
from ..objects import Game
from ..utils.subdomains import games
from ..utils.cursor_iterator import CursorIterator
from ..utils.decorators import make_docs


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
