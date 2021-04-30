"""Minor changes to DS1PTDE classes (expanded instruction set and use of DCX)."""

__all__ = ["EMEVD", "Event", "EventArg", "EventLayers", "Instruction"]

from soulstruct.darksouls1ptde.events.emevd.core import (
    EMEVD as _BaseEMEVD,
    Event as _BaseEvent,
    EventArg,
    Instruction as _BaseInstruction,
    EventLayers,
)
from .arg_types import INSTRUCTION_ARG_TYPES
from .decompiler import InstructionDecompiler
from .evs import EVSParser


class Instruction(_BaseInstruction):
    DECOMPILER = InstructionDecompiler()
    INSTRUCTION_ARG_TYPES = INSTRUCTION_ARG_TYPES


class Event(_BaseEvent):
    Instruction = Instruction


class EMEVD(_BaseEMEVD):

    events: dict[int, Event]

    Event = Event
    EVS_PARSER = EVSParser
    IMPORT_STRING = "soulstruct.darksouls1r.events"
    DCX_MAGIC = (36, 44)
