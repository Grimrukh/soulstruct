__all__ = ["EMEVD", "Event", "EventArg", "EventLayers", "Instruction"]

from soulstruct.base.events.emevd import (
    EMEVD as _BaseEMEVD,
    Event as _BaseEvent,
    EventArg as _BaseEventArg,
    Instruction as _BaseInstruction,
    EventLayers as _BaseEventLayers,
)
from soulstruct.utilities.binary import BinaryStruct
from .arg_types import INSTRUCTION_ARG_TYPES
from .decompiler import InstructionDecompiler
from .evs import EVSParser


class EventLayers(_BaseEventLayers):
    """Never used in DS1 and very probably not actually supported by the engine."""

    HEADER_STRUCT = BinaryStruct(
        ("two", "I", 2),
        ("event_layers", "I"),  # 32-bit bit field
        ("zero", "I", 0),  # format is a guess
        ("minus_one", "i", -1),  # format is a guess
        ("one", "I", 1),  # format is a guess
    )


class EventArg(_BaseEventArg):
    HEADER_STRUCT = BinaryStruct(
        ("instruction_line", "I"),
        ("write_from_byte", "I"),
        ("read_from_byte", "I"),
        ("bytes_to_write", "I"),
        ("unknown", "i"),
    )


class Instruction(_BaseInstruction):
    DECOMPILER = InstructionDecompiler()
    INSTRUCTION_ARG_TYPES = INSTRUCTION_ARG_TYPES
    EventLayers = EventLayers
    HEADER_STRUCT = BinaryStruct(
        ("category", "I"),
        ("index", "I"),
        ("base_args_size", "I"),
        ("first_base_arg_offset", "i"),
        ("first_event_layers_offset", "i"),
        "4x",
    )


class Event(_BaseEvent):
    Instruction = Instruction
    EventArg = EventArg
    EVENT_ARG_TYPES = {}
    HEADER_STRUCT = BinaryStruct(
        ("event_id", "I"),
        ("instruction_count", "I"),
        ("first_instruction_offset", "I"),
        ("event_arg_count", "I"),
        ("first_event_arg_offset", "i"),
        ("restart_type", "I"),
        "4x",
    )


class EMEVD(_BaseEMEVD):

    events: dict[int, Event]

    Event = Event
    EVS_PARSER = EVSParser
    IMPORT_STRING = "soulstruct.darksouls1ptde.events"
    STRING_ENCODING = "utf-8"
    DCX_MAGIC = ()
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
