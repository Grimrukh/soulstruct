__all__ = ["EVSParser"]

from soulstruct.base.events.emevd.evs import EVSParser as _BaseEVSParser
from soulstruct.eldenring import events
from .arg_types import INSTRUCTION_ARG_TYPES


class EVSParser(_BaseEVSParser):

    EVENTS_MODULE = events
    OR_SLOTS = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]
    AND_SLOTS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    INSTRUCTION_ARG_TYPES = INSTRUCTION_ARG_TYPES
