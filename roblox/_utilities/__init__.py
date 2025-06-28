from datetime import datetime
from functools import wraps
from inspect import get_annotations
from typing import Optional
from httpx import Client

from ..objects.bases import BaseItem, ClientAttr
from .._utilities.types import ClientType, BaseId


def from_timestamp(timestamp: str) -> datetime:
    return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")


def make_docs(*, description: str,
              response_reasons: dict[int, str] = None,
              is_deprecated: bool = False):
    def decorator(func):
        func_signature = get_annotations(func)
        func_signature.pop("return", None)

        @wraps(func)
        def wrapper(self=None, *args, **kwargs):
            def is_single_annotation(annotation) -> Optional[str]:
                type_names = [n for n, t in func_signature.items() if isinstance(annotation, type(t))]
                return type_names[0] if len(type_names) == 1 else None

            if isinstance(self, Client):
                kwargs.update({"client": self})
            elif (
                isinstance(self, ClientAttr)
                and is_single_annotation(ClientType)
            ):
                kwargs.update({"client": self._client})

            if (
                isinstance(self, BaseItem)
                and (name := is_single_annotation(BaseId))
            ):
                kwargs.update({name: self.id})

            return func(*args, **kwargs)

        wrapper.__description__ = description
        wrapper.__response_reasons__ = response_reasons
        wrapper.__is_deprecated__ = "Yes" if is_deprecated else "No"

        repr_reasons = "\n".join(f"  - {k}: {v}" for k, v in response_reasons.items()) \
                       if response_reasons else None
        doc_info = (f"{func.__name__}: {description}",
                    f"Reasons:\n{repr_reasons}",
                    f"Deprecated: {wrapper.__is_deprecated__}")

        if doc_info:
            wrapper.__doc__ = "\n\n".join(doc_info)

        return wrapper
    return decorator
