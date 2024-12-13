__all__ = ["EMEVD", "Event", "Instruction"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.events.emevd import (
    EMEVD as _BaseEMEVD,
    Event as _BaseEvent,
    Instruction as _BaseInstruction,
)
from soulstruct.darksouls1ptde.game_types.game_enums_manager import GameEnumsManager

from .decompiler import DECOMPILER, OPT_ARGS_DECOMPILER, decompile_instruction
from .emedf import EMEDF, EMEDF_TESTS, EMEDF_COMPARISON_TESTS
from .evs import EVSParser


@dataclass(slots=True)
class Instruction(_BaseInstruction):
    EMEDF: tp.ClassVar = EMEDF
    DECOMPILER: tp.ClassVar = DECOMPILER
    OPT_ARGS_DECOMPILER: tp.ClassVar = OPT_ARGS_DECOMPILER
    DECOMPILE: tp.ClassVar = staticmethod(decompile_instruction)


@dataclass(slots=True)
class Event(_BaseEvent):
    INSTRUCTION_CLASS: tp.ClassVar = Instruction
    EMEDF_TESTS: tp.ClassVar = EMEDF_TESTS
    EMEDF_COMPARISON_TESTS: tp.ClassVar = EMEDF_COMPARISON_TESTS


class EMEVD(_BaseEMEVD):

    events: dict[int, Event] = field(default_factory=dict)

    EVENT_CLASS: tp.ClassVar = Event
    EVS_PARSER: tp.ClassVar = EVSParser
    STRING_ENCODING: tp.ClassVar = "utf-8"
    ENTITY_ENUMS_MANAGER: tp.ClassVar = GameEnumsManager
    HEADER_VERSION_INFO: tp.ClassVar = (False, 0, 204)
    LONG_VARINTS = False
