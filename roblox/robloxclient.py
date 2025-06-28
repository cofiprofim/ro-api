from httpx import URL, Response, Client

from ._utilities.subdomains import LoadUrl

from typing import Union


class RobloxClient(Client):
    def __init__(self, auth=None):
        super().__init__(auth=auth)

    def request(self, method: str,
                url: Union[URL, str, LoadUrl], **kwargs) -> Response:
        return super().request(method, str(url), **kwargs)

    from roblox.api.games import fetch_game_media, fetch_user_games, fetch_games