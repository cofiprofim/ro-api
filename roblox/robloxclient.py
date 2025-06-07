from httpx import URL, Response, Client

from .utils.subdomains import LoadUrl
from .api import GamesApi

from typing import Union


class _CustomRobloxClient(Client):
    def request(self, method: str,
                url: Union[URL, str, LoadUrl], **kwargs) -> Response:
        return super().request(method, str(url), **kwargs)


class RobloxClient(GamesApi):
    def __init__(self, auth=None):
        self._client = _CustomRobloxClient(auth=auth)

    def request(self, method, url):
        return self._client.request(method, url)

    def __getattribute__(self, item: str):
        attr = super().__getattribute__(item)
        from functools import partial
        if hasattr(attr, "_IS_API"):
            return partial(attr, client=self)

        return attr

