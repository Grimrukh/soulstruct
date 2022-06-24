__all__ = ["EVSParser"]

from soulstruct.base.events.emevd.evs import EVSParser as _BaseEVSParser
from soulstruct.bloodborne import game_types, events
from .compiler import COMPILER, compile_instruction, compile_game_object_test
from .emedf import EMEDF_ALIASES


class EVSParser(_BaseEVSParser):

    EMEDF_ALIASES = EMEDF_ALIASES
    EVENTS_MODULE = events
    GAME_TYPES = game_types
    OR_SLOTS = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]
    AND_SLOTS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    COMPILER = COMPILER
    COMPILE = staticmethod(compile_instruction)
    COMPILE_OBJECT_TEST = staticmethod(compile_game_object_test)
