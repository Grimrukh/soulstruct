__all__ = ["EMEVD", "Event", "Instruction"]

from soulstruct.base.events.emevd import (
    EMEVD as _BaseEMEVD,
    Event as _BaseEvent,
    Instruction as _BaseInstruction,
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
    EVS_PARSER = EVSParser
    STRING_ENCODING = "utf-8"
    ENTITY_ENUMS_MANAGER = EntityEnumsManager
    DCX_TYPE = DCXType.Null
