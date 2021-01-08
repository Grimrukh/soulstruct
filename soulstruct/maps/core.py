__all__ = ["MapError", "MapFieldInfo"]

import typing as tp

from soulstruct.core import SoulstructError


class MapError(SoulstructError):
    """Error caused by a map-related file or class."""


class MapFieldInfo(tp.NamedTuple):
    nickname: str
    display_type: type
    default: tp.Any
    description: str
