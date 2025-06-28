from ..objects.bases.basegame import GameMedia
from .._utilities import make_docs
from .._utilities.types import ClientType, BaseId
from .._utilities.subdomains import games_domain

from typing import Optional


@make_docs(description="Fetch game media")
def fetch_game_media(game_id: BaseId,
                     client: Optional[ClientType] = None) -> GameMedia:
    response = client.get(
        games_domain.v1.add_path("games", game_id, "media")
    ).json()
    return GameMedia(response["data"][0])
