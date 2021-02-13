__all__ = ["EVSParser"]

from soulstruct.base.events.emevd.evs import EVSParser as _BaseEVSParser
from soulstruct.darksouls1r import events
from .arg_types import INSTRUCTION_ARG_TYPES


class EVSParser(_BaseEVSParser):

    GAME_MODULE = events
    OR_SLOTS = [-1, -2, -3, -4, -5, -6, -7]
    AND_SLOTS = [1, 2, 3, 4, 5, 6, 7]
    CONDITION_COUNT = 15
    INSTRUCTION_ARG_TYPES = INSTRUCTION_ARG_TYPES
