__all__ = ["EMEVD", "Event", "Instruction"]

from soulstruct.base.events.emevd import (
    Instruction as _BaseInstruction,
    Event as _BaseEvent,
    EMEVD as _BaseEMEVD,
)
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


class Event(_BaseEvent):
    Instruction = Instruction
    EMEDF_TESTS = EMEDF_TESTS
    EMEDF_COMPARISON_TESTS = EMEDF_COMPARISON_TESTS


class EMEVD(_BaseEMEVD):

    events: dict[int, Event]

    Event = Event
    ENTITY_ENUMS_MANAGER = EntityEnumsManager
    EVS_PARSER = EVSParser
    STRING_ENCODING = "utf-16le"
    DCX_TYPE = DCXType.DCX_DFLT_10000_44_9
    HEADER_VERSION_INFO = (False, 0, 204)
