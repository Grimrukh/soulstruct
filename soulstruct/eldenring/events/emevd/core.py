__all__ = ["EMEVD", "Event", "Instruction"]

import typing as tp

from soulstruct.base.events.emevd import EMEVD as _BaseEMEVD, Event as _BaseEvent, Instruction as _BaseInstruction
from soulstruct.containers.dcx import DCXType
from .decompiler import DECOMPILER, OPT_ARGS_DECOMPILER, decompile_instruction
from .emedf import EMEDF, EMEDF_TESTS, EMEDF_COMPARISON_TESTS
from .entity_enums_manager import EntityEnumsManager
from .evs import EVSParser


class Instruction(_BaseInstruction):
    EMEDF = EMEDF
    DECOMPILER = DECOMPILER
    OPT_ARGS_DECOMPILER = OPT_ARGS_DECOMPILER
    DECOMPILE = staticmethod(decompile_instruction)

    def get_called_event(self) -> tp.Optional[int]:
        """Returns called event ID if instruction is `RunEvent` or `RunCommonEvent`. Returns `None` otherwise."""
        if self.category == 2000:
            if self.index == 0:
                return self.args_list[1]
            elif self.index == 6:  # now has a first argument, like 2000[00]
                return self.args_list[1]
        return None


class Event(_BaseEvent):
    Instruction = Instruction
    EMEDF_TESTS = EMEDF_TESTS
    EMEDF_COMPARISON_TESTS = EMEDF_COMPARISON_TESTS
    USE_HIGH_LEVEL_LANGUAGE = True


class EMEVD(_BaseEMEVD):

    events: dict[int, Event]

    Event = Event
    EVS_PARSER = EVSParser
    ENTITY_ENUMS_MANAGER = EntityEnumsManager
    STRING_ENCODING = "utf-16le"
    DCX_TYPE = DCXType.DCX_KRAK
    HEADER_VERSION_INFO = (True, -1, 205)  # TODO: Sekiro uses this too.
