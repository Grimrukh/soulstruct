__all__ = ["EVSParser"]

from soulstruct.base.events.emevd.evs import EVSParser as _BaseEVSParser
from soulstruct.darksouls3 import events, game_types
from soulstruct.games import DarkSouls3Type
from .compiler import COMPILER, compile_instruction, compile_game_object_test
from .emedf import EMEDF_ALIASES, EMEDF_TESTS


class EVSParser(DarkSouls3Type, _BaseEVSParser):

    EMEDF_ALIASES = EMEDF_ALIASES
    EMEDF_TESTS = EMEDF_TESTS
    EVENTS_MODULE = events
    GAME_TYPES = game_types
    OR_SLOTS = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]
    AND_SLOTS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    COMPILER = COMPILER
    COMPILE = staticmethod(compile_instruction)
    COMPILE_OBJECT_TEST = staticmethod(compile_game_object_test)
