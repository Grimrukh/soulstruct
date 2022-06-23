__all__ = ["EVSParser"]

from soulstruct.base.events.emevd.evs import EVSParser as _BaseEVSParser
from soulstruct.games import DarkSoulsPTDEType
from soulstruct.darksouls1ptde import events, game_types
from .compiler import COMPILER, compile_instruction
from .emedf import EMEDF_ALIASES


class EVSParser(DarkSoulsPTDEType, _BaseEVSParser):

    EMEDF_ALIASES = EMEDF_ALIASES
    EVENTS_MODULE = events
    GAME_TYPES = game_types
    OR_SLOTS = [-1, -2, -3, -4, -5, -6, -7]
    AND_SLOTS = [1, 2, 3, 4, 5, 6, 7]
    CONDITION_COUNT = 15
    COMPILER = COMPILER
    COMPILE = staticmethod(compile_instruction)
