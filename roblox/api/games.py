from ..objects.bases.basegame import BaseGame
from ..objects.game import Game
from .._utilities.cursor_iterator import CursorIterator
from .._utilities.types import BaseId, ClientType
from .._utilities.subdomains import games_domain
from .._utilities import make_docs

from typing import Union, List


from .._api.games import fetch_game_media


@make_docs(description="Fetch user's created games")
def fetch_user_games(user_id: BaseId, client: ClientType = None) -> CursorIterator:
    return CursorIterator(
        games_domain.v2.add_path("users", user_id, "games"),
        client=client,
        handler=BaseGame,
        handler_kwargs={"client": client}
    )


@make_docs(description="hi")
def fetch_games(games_ids: Union[int, List[int]], client: ClientType = None) -> List[Game]:
    response = client.get(
        games_domain.v1.add_path("games").add_kwargs(universeIds=(games_ids,))
    ).json()
    return [Game(game_data) for game_data in response["data"]]
