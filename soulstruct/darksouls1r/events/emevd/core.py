"""Minor changes to DS1PTDE classes (expanded instruction set and use of DCX)."""

__all__ = ["EMEVD", "Event", "Instruction"]

from soulstruct.base.events.emevd import EMEVD as _BaseEMEVD
from soulstruct.containers.dcx import DCXType
from soulstruct.darksouls1ptde.events.emevd.core import Event as _BaseEvent, Instruction as _BaseInstruction
from .emedf import EMEDF, EMEDF_TESTS, EMEDF_COMPARISON_TESTS
from .entity_enums_manager import EntityEnumsManager
from .evs import EVSParser
from .decompiler import DECOMPILER, OPT_ARGS_DECOMPILER, decompile_instruction


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
    DCX_TYPE = DCXType.DCX_DFLT_10000_24_9
    HEADER_VERSION_INFO = (False, 0, 204)
