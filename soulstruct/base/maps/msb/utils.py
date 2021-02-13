__all__ = ["MapFieldInfo"]

import typing as tp


class MapFieldInfo(tp.NamedTuple):
    nickname: str
    display_type: type
    default: tp.Any
    description: str
