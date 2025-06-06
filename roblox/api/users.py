from __future__ import annotations

import httpx

from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..robloxclient import RobloxClient

from roblox.utils.subdomains.domain_maker import games
from ..objects.bases import BaseGame


def get_user_games(self, user_id: int, client: Optional[RobloxClient] = None) -> List[BaseGame]:
    return BaseGame(httpx.get(f"{games}/v2/users/{user_id}/games").json())

