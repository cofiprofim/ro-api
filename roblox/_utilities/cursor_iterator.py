import httpx

from .types import OptionalClient
from .subdomains import LoadUrl

from typing import Optional, Callable


class CursorIterator:
    def __init__(
            self,
            url: LoadUrl,
            *,
            client: OptionalClient = None,
            data_key: str = "data",
            handler: Optional[Callable] = None,
            handler_kwargs: Optional[dict] = None
    ):
        self.url = url

        self.client = httpx.Client() if client is None else client
        self.data_key = data_key
        self.handler = handler
        self.handler_kwargs = handler_kwargs or dict()

        self.previous_page_cursor: str = ""
        self.next_page_cursor: str = ""

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_page_cursor is None:
            raise StopIteration

        response = self.client.get(
            self.url.add_kwargs(cursor=self.next_page_cursor)
        ).json()

        self.previous_page_cursor = response["previousPageCursor"]
        self.next_page_cursor = response["nextPageCursor"]

        data = response[self.data_key]
        return (self.handler(batch, **self.handler_kwargs) for batch in data) \
            if self.handler else data
