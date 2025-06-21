import typing
from functools import wraps
import itertools
from httpx import Client, URL, USE_CLIENT_DEFAULT, Response
from httpx._client import UseClientDefault
from httpx._types import RequestContent, RequestData, RequestFiles, QueryParamTypes, HeaderTypes, CookieTypes, \
    AuthTypes, TimeoutTypes, RequestExtensions


class C(Client):
    def request(
        self,
        method: str,
        url: URL | str,
        *,
        content: RequestContent | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        json: typing.Any | None = None,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        auth: AuthTypes | UseClientDefault | None = USE_CLIENT_DEFAULT,
        follow_redirects: bool | UseClientDefault = USE_CLIENT_DEFAULT,
        timeout: TimeoutTypes | UseClientDefault = USE_CLIENT_DEFAULT,
        extensions: RequestExtensions | None = None,
    ) -> Response:
        return super().request(method, str(url), content=content, data=data, files=files, json=json, params=params,
                              headers=headers, cookies=cookies, auth=auth, follow_redirects=follow_redirects,
                              timeout=timeout, extensions=extensions)

def make_docs(name: str, description: str, remove_self: bool = True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if any(isinstance(arg, Client) for arg in itertools.chain(args, kwargs.values())):
                return func(*args, **kwargs)
            return func(*args, client=C(), **kwargs)
        setattr(wrapper, "_IS_API", True)
        wrapper.__doc__ = f"{name}:\n{description}"
        return staticmethod(wrapper) if remove_self else wrapper

    return decorator


def make_api_function():
    pass
