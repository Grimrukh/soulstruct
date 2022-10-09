__all__ = ["EVSParser"]

from soulstruct.base.events.emevd.evs import EVSParser as _BaseEVSParser
from soulstruct.games import DarkSoulsDSRType
from soulstruct.darksouls1r import events, game_types
from .compiler import COMPILER, compile_instruction, compile_game_object_test
from .emedf import EMEDF_ALIASES, EMEDF_TESTS, EMEDF_COMPARISON_TESTS


class EVSParser(DarkSoulsDSRType, _BaseEVSParser):

    EMEDF_ALIASES = EMEDF_ALIASES
    EMEDF_TESTS = EMEDF_TESTS
    EMEDF_COMPARISON_TESTS = EMEDF_COMPARISON_TESTS
    EVENTS_MODULE = events
    GAME_TYPES = game_types
    OR_SLOTS = [-1, -2, -3, -4, -5, -6, -7]
    AND_SLOTS = [1, 2, 3, 4, 5, 6, 7]
    COMPILER = COMPILER
    COMPILE = staticmethod(compile_instruction)
    COMPILE_OBJECT_TEST = staticmethod(compile_game_object_test)
