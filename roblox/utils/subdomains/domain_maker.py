import re

from typing import NoReturn, Optional

__all__ = ("LoadUrl", "LoadDomain")


class LoadUrl:
    base_protocol = "https"

    __slots__ = ("domain", "path", "kwargs")

    def __init__(self, domain):
        self.domain = domain
        self.path = list()
        self.kwargs = dict()

    def add_path(self, *args):
        self.path.extend(map(str, args))
        return self

    def add_kwargs(self, **kwargs):
        for name, value in kwargs.items():
            if isinstance(value, (list, tuple, set)):
                new_val = ",".join(map(str, value))
                kwargs.update({name: new_val})

        self.kwargs.update(kwargs)
        return self

    def __repr__(self):
        path = "/".join(self.path)
        url = f"{self.base_protocol}://{self.domain}/{path}"

        if self.kwargs:
            args = "&".join(f"{name}={val}" for name, val in self.kwargs.items())
            url = f"{url}?{args}"

        return url

    __str__ = __repr__


class LoadDomain:
    base_domain = "roblox.com"

    v1: LoadUrl; v2: LoadUrl

    __slots__ = ("domain", "vers_limit")

    def __init__(self, sub_domain: str, *,
                 versions_limit: Optional[int] = None):
        self.domain = f"{sub_domain}.{self.base_domain}"
        self.vers_limit = versions_limit

    def __getattr__(self, item) -> LoadUrl | NoReturn:
        vers_num = re.fullmatch(r"[1-9]\d*(?=v)", item) or 0
        if self.vers_limit is None or int(vers_num) <= self.vers_limit:
            return LoadUrl(f"{self.domain}/{item}")

        raise KeyError(f"Invalid key provided: {item}")

    def __repr__(self):
        return self.domain

    __str__ = __repr__
games = LoadDomain("games", versions_limit=2)
games.v1