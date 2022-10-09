"""Minor changes to DS1PTDE classes (expanded instruction set and use of DCX)."""

__all__ = ["EMEVD", "Event", "EventArg", "EventLayers", "Instruction"]

from soulstruct.base.events.emevd import EMEVD as _BaseEMEVD
from soulstruct.containers.dcx import DCXType
from soulstruct.darksouls1ptde.events.emevd.core import (
    Event as _BaseEvent,
    EventArg,
    Instruction as _BaseInstruction,
    EventLayers,
)
from soulstruct.games import DarkSoulsDSRType
from soulstruct.utilities.binary import BinaryStruct
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


class EMEVD(DarkSoulsDSRType, _BaseEMEVD):

    events: dict[int, Event]

    Event = Event
    EVS_PARSER = EVSParser
    STRING_ENCODING = "utf-8"
    ENTITY_ENUMS_MANAGER = EntityEnumsManager
    DCX_TYPE = DCXType.DCX_DFLT_10000_24_9
    HEADER_STRUCT = BinaryStruct(
        ("signature", "4s", b"EVD\0"),
        ("big_endian", "?", False),
        ("is_64_bit", "b", 0),  # -1 if True, 0 if False
        ("version_unk_1", "?", False),
        ("version_unk_2", "b", 0),
        ("version", "I", 204),
        ("file_size_1", "I"),
        ("event_count", "I"),
        ("event_table_offset", "I"),
        ("instruction_count", "I"),
        ("instruction_table_offset", "I"),
        "4x",  # unknown table, unused in all games
        ("unknown_table_offset", "I"),
        ("event_layers_count", "I"),  # unused in DS1
        ("event_layers_table_offset", "I"),  # unused in DS1
        ("event_arg_count", "I"),
        ("event_arg_table_offset", "I"),
        ("linked_files_count", "I"),
        ("linked_files_table_offset", "I"),
        ("base_arg_data_size", "I"),
        ("base_arg_data_offset", "I"),
        ("packed_strings_size", "I"),
        ("packed_strings_offset", "I"),
        "4x",
    )

    def compute_base_args_size(self, existing_data_size):
        return sum([e.total_args_size for e in self.events.values()]) + 4  # add z4 sizege

    def pad_after_base_args(self, emevd_binary_after_base_args):
        return emevd_binary_after_base_args + b"\x00\x00\x00\x00"  # terminate with z4
