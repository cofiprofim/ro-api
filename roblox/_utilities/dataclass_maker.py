from dataclasses import dataclass, field
from enum import Enum
import re

from typing import Callable, Any


class FormatType(Enum):
    """

    """

    default = "Default"
    camel_case = "CamelCase"
    title_case = "TitleCase"


# noinspection PyPep8Naming
@dataclass(slots=True, kw_only=True)
class param:
    key_name: str = field(default=None)
    optional: bool = field(default=False)
    handler: Callable = field(default=None)

    def fetch_value(self, data: dict) -> Any:
        fetched = data.get(self.key_name) if self.optional else data[self.key_name]

        if self.handler is None:
            return fetched

        return self.handler(fetched)

    def format_key_name(self, format_type: FormatType = FormatType.default) -> str:
        case_regex = re.compile(r"[_ ]([a-zA-Z])([a-zA-Z]+)")

        def format_case() -> str:
            return case_regex.sub(lambda m: m.group(1).upper() + m.group(2).lower(),
                                  self.key_name)

        match format_type:
            case FormatType.camel_case:
                formated = format_case()
                return formated[0].lower() + formated[1:]
            case FormatType.title_case:
                formated = format_case()
                return formated[0].upper() + formated[1:]
            case _:
                return self.key_name


def _load_fields(cls) -> dict[str, param]:
    fields = dict()

    for n in cls.__annotations__.keys():
        val: param = getattr(cls, n, None)

        if val is not None:
            if not isinstance(val, param):
                raise ValueError(f"Class attribute's value can only be param class,"
                                 f"not {val.__name__}")
            else:
                if val.key_name is None: val.key_name = n
                fields.update({n: val})
        else:
            fields.update({n: param(key_name=n)})

    for n, v in cls.__dict__.items():
        if (
            not callable(v)
            and not n.startswith("_")
            and n not in fields
        ):
            if not isinstance(v, param):
                raise AttributeError(f"You can't set a class attribute with not param class value ({n})")

            fields.update({n: v})

    return fields


def _process_class(cls, format_type):
    fields = _load_fields(cls)

    def __init__(self, data: dict, client=None) -> None:
        self._client = client
        try:
            super(cls, self).__init__(data)
        except TypeError:
            pass

        fields_attr = getattr(self, "_FIELDS", None)
        if fields_attr is None:
            setattr(self, "_FIELDS", fields)
        else:
            fields_attr.update(fields)

        if cls is self.__class__:
            for field_name, field in self._FIELDS.copy().items():
                field.key_name = field.format_key_name(format_type)
                val = field.fetch_value(data)

                if field.optional and val is None:
                    self._FIELDS.pop(field_name)
                else:
                    setattr(self, field_name, val)

        # if exclude_params:
        #     if is_base:
        #         raise ValueError(f"You can't exclude params for base class ({cls.__qualname__})")
        #
        #     for param in exclude_params:
        #         try:
        #             fields.pop(param)
        #         except KeyError:
        #             raise KeyError(f"Non-existing param name provided: {param}")

    def __repr__(self) -> str:
        return self.__class__.__qualname__ + "(" + (
            ', '.join([f"{n}={getattr(self, n, None)!r}"
                       for n in self._FIELDS.keys()])) + ")"

    cls.__init__ = __init__
    cls.__repr__ = __repr__

    return cls


def item_dataclass(cls=None, /, *,
                   format_type: FormatType = FormatType.default):
    def wrapper(new_cls):
        return _process_class(new_cls, format_type)

    if cls is None:
        return wrapper

    return wrapper(cls)
