from . import item_dataclass, param, FormatType
from .bases.basecreator import BaseCreator


@item_dataclass(format_type=FormatType.camel_case)
class Creator(BaseCreator):
    name: str
    is_rnva_account: bool = param(key_name="isRNVAccount")
    has_verified_badge: bool
