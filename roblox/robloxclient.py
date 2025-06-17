from httpx import URL, Response, Client
import functools

from .utils.subdomains import LoadUrl


from typing import Union

# def func(self):
#     import importlib
#
#     mod = importlib.import_module("roblox.api.games")
#
#
#     class t(type):
#
#
#     class games(metaclass=t):
#         pass
#
#     for n, f in mod.__dict__.items():
#         if hasattr(f, "_IS_API"):
#             setattr(games, n, f)
#     return games


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

    from .api.games import fetch_games, fetch_user_games

