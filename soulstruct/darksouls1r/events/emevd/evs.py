__all__ = ["EVSParser"]

from soulstruct.base.events.evs import EVSParser as _BaseEVSParser
from soulstruct.darksouls1r import events, game_types
from .compiler import EVSInstructionCompiler
from .emedf import EMEDF_ALIASES, EMEDF_TESTS, EMEDF_COMPARISON_TESTS


class EVSParser(_BaseEVSParser):

    EMEDF_ALIASES = EMEDF_ALIASES
    EMEDF_TESTS = EMEDF_TESTS
    EMEDF_COMPARISON_TESTS = EMEDF_COMPARISON_TESTS
    EVENTS_MODULE = events
    GAME_TYPES = game_types
    # TODO: I think DSR may actually support more slots (16?), as m12_01 Battle of Stoicism events use slot 8.
    OR_SLOTS = [-1, -2, -3, -4, -5, -6, -7]
    AND_SLOTS = [1, 2, 3, 4, 5, 6, 7]
    COMPILER_CLASS = EVSInstructionCompiler
    SPECIAL_EVENT_NAMES = {
        0: "Constructor",
        50: "Preconstructor",
    }
