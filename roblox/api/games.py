from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..robloxclient import RobloxClient

from roblox.objects.bases.basegame import BaseGame
from ..utils.subdomains import games
from ..utils.cursor_iterator import CursorIterator


def get_user_games(user_id: int, client: RobloxClient) -> CursorIterator:
    return CursorIterator(
        games.v2.add_path("users", user_id, "games"),
        client=client,
        handler=lambda x: map(BaseGame, x)
    )
