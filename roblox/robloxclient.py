from httpx import URL, Response, Client
import functools

from .utils.subdomains import LoadUrl
from .api.games import fetch_user_games

from typing import Union


class RobloxClient(Client):
    """

    """

    def __init__(self, auth=None):
        super().__init__(auth=auth)

    def __getattribute__(self, item: str):
        attr = super().__getattribute__(item)

        if hasattr(attr, "_IS_API"):
            return functools.partial(attr, client=self)

        return attr

    def request(self, method: str,
                url: Union[URL, str, LoadUrl], **kwargs) -> Response:
        return super().request(method, str(url), **kwargs)

    fetch_user_games = fetch_user_games