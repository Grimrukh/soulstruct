__all__ = ["EMEVD", "Event", "Instruction"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.events.emevd import EMEVD as _BaseEMEVD, Event as _BaseEvent, Instruction as _BaseInstruction
from .decompiler import DECOMPILER, OPT_ARGS_DECOMPILER, decompile_instruction
from .emedf import EMEDF, EMEDF_TESTS, EMEDF_COMPARISON_TESTS
from .entity_enums_manager import GameEnumsManager
from .evs import EVSParser


@dataclass(slots=True)
class Instruction(_BaseInstruction):
    EMEDF: tp.ClassVar = EMEDF
    DECOMPILER: tp.ClassVar = DECOMPILER
    OPT_ARGS_DECOMPILER: tp.ClassVar = OPT_ARGS_DECOMPILER
    DECOMPILE: tp.ClassVar = staticmethod(decompile_instruction)

    def get_called_event(self) -> tp.Optional[int]:
        """Returns called event ID if instruction is `RunEvent` or `RunCommonEvent`. Returns `None` otherwise."""
        if self.category == 2000:
            if self.index == 0:
                return self.args_list[1]
            elif self.index == 6:  # now has a first argument, like 2000[00]
                return self.args_list[1]
        return None


@dataclass(slots=True)
class Event(_BaseEvent):
    INSTRUCTION_CLASS: tp.ClassVar = Instruction
    EMEDF_TESTS: tp.ClassVar = EMEDF_TESTS
    EMEDF_COMPARISON_TESTS: tp.ClassVar = EMEDF_COMPARISON_TESTS
    USE_HIGH_LEVEL_LANGUAGE: tp.ClassVar = True


@dataclass(slots=True)
class EMEVD(_BaseEMEVD):

    events: dict[int, Event] = field(default_factory=dict)

    EVENT_CLASS: tp.ClassVar = Event
    EVS_PARSER: tp.ClassVar = EVSParser
    ENTITY_ENUMS_MANAGER: tp.ClassVar = GameEnumsManager
    STRING_ENCODING: tp.ClassVar = "utf-16le"
    HEADER_VERSION_INFO: tp.ClassVar = (True, -1, 205)  # TODO: Sekiro uses this too.
