from enum import IntEnum
from typing import Union

from soulstruct.events.shared import instructions as instr
from soulstruct.game_types.basic_types import GameObject

__all__ = ['SpecialEffect']


class BaseParam(GameObject, IntEnum):
    """Base class for IDs of param entries."""
    pass


class SpecialEffect(BaseParam):
    """Base class for special effect param IDs."""
    pass


SpecialEffectInt = Union[SpecialEffect, int]
