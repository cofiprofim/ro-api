from httpx import URL, Response, Client

from .utils.subdomains import LoadUrl
from .api.games import get_user_games

from typing import Union


class _CustomRobloxClient(Client):
    def request(self, method: str,
                url: Union[URL, str, LoadUrl], **kwargs) -> Response:
        return super().request(method, str(url), **kwargs)


class RobloxClient:
    def __init__(self, auth=None):
        self._client = _CustomRobloxClient(auth=auth)

    def request(self, method, url):
        return self._client.request(method, url)
