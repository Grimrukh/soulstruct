__all__ = ["EVSParser"]

from soulstruct.base.events.evs import EVSParser as _BaseEVSParser
from soulstruct.eldenring import events, game_types
from .compiler import EVSInstructionCompiler
from .emedf import EMEDF_ALIASES, EMEDF_TESTS, EMEDF_COMPARISON_TESTS


class EVSParser(_BaseEVSParser):

    EMEDF_ALIASES = EMEDF_ALIASES
    EMEDF_TESTS = EMEDF_TESTS
    EMEDF_COMPARISON_TESTS = EMEDF_COMPARISON_TESTS
    EVENTS_MODULE = events
    GAME_TYPES = game_types
    OR_SLOTS = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]
    AND_SLOTS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    COMPILER_CLASS = EVSInstructionCompiler
    SUPPORTS_COMMON_FUNC = True
    USES_COMMON_FUNC_SLOT = True
    SPECIAL_EVENT_NAMES = {
        0: "Constructor",
        50: "Preconstructor",
        100: "Postconstructor1",
        200: "Postconstructor2",
    }
