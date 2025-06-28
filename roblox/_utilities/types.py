from httpx import Client

from typing import TypeVar, Optional
from roblox.objects.bases import BaseItem


ClientType = TypeVar("ClientType", bound=Client)
OptionalClient = Optional[ClientType]

BaseId = TypeVar("BaseId", bound=BaseItem)
