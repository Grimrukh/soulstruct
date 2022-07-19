__all__ = ["EMEVD", "Event", "EventArg", "EventLayers", "Instruction"]

import typing as tp

from soulstruct.base.events.emevd import (
    EMEVD as _BaseEMEVD,
    Event as _BaseEvent,
    EventArg as _BaseEventArg,
    Instruction as _BaseInstruction,
    EventLayers as _BaseEventLayers,
)
from soulstruct.containers.dcx import DCXType
from soulstruct.games import EldenRingType
from soulstruct.utilities.binary import BinaryStruct
from .decompiler import DECOMPILER, OPT_ARGS_DECOMPILER, decompile_instruction
from .emedf import EMEDF, EMEDF_TESTS, EMEDF_COMPARISON_TESTS
from .entity_enums_manager import EntityEnumsManager
from .evs import EVSParser


class EventLayers(_BaseEventLayers):
    HEADER_STRUCT = BinaryStruct(
        ("two", "I", 2),
        ("event_layers", "I"),  # 32-bit bit field
        ("zero", "Q", 0),
        ("minus_one", "q", -1),
        ("one", "Q", 1),
    )


class EventArg(_BaseEventArg):
    HEADER_STRUCT = BinaryStruct(
        ("instruction_line", "Q"),
        ("write_from_byte", "Q"),
        ("read_from_byte", "Q"),
        ("bytes_to_write", "i"),
        ("unknown", "i"),
    )


class Instruction(_BaseInstruction):
    EMEDF = EMEDF
    DECOMPILER = DECOMPILER
    OPT_ARGS_DECOMPILER = OPT_ARGS_DECOMPILER
    DECOMPILE = staticmethod(decompile_instruction)
    EventLayers = EventLayers
    HEADER_STRUCT = BinaryStruct(
        ("category", "I"),
        ("index", "I"),
        ("base_args_size", "Q"),
        ("first_base_arg_offset", "q"),
        ("first_event_layers_offset", "q"),
    )

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
    EventArg = EventArg
    EMEDF_TESTS = EMEDF_TESTS
    EMEDF_COMPARISON_TESTS = EMEDF_COMPARISON_TESTS
    HEADER_STRUCT = BinaryStruct(
        ("event_id", "Q"),
        ("instruction_count", "Q"),
        ("first_instruction_offset", "Q"),
        ("event_arg_count", "Q"),
        ("first_event_arg_offset", "q"),
        ("restart_type", "I"),
        "4x",
    )
    USE_HIGH_LEVEL_LANGUAGE = True


class EMEVD(EldenRingType, _BaseEMEVD):
    """Same file format (header) as Sekiro."""

    events: dict[int, Event]

    Event = Event
    EVS_PARSER = EVSParser
    ENTITY_ENUMS_MANAGER = EntityEnumsManager
    STRING_ENCODING = "utf-16le"
    DCX_TYPE = DCXType.DCX_KRAK
    HEADER_STRUCT = BinaryStruct(
        ("signature", "4s", b"EVD\0"),
        ("big_endian", "?", False),
        ("is_64_bit", "b", -1),  # -1 if True, 0 if False
        ("version_unk_1", "?", True),
        ("version_unk_2", "b", -1),
        ("version", "I", 205),  # same as DS3
        ("file_size_1", "I"),
        ("event_count", "Q"),
        ("event_table_offset", "Q"),
        ("instruction_count", "Q"),
        ("instruction_table_offset", "Q"),
        "8x",  # unknown table, unused in all games
        ("unknown_table_offset", "Q"),
        ("event_layers_count", "Q"),
        ("event_layers_table_offset", "Q"),
        ("event_arg_count", "Q"),
        ("event_arg_table_offset", "Q"),
        ("linked_files_count", "Q"),
        ("linked_files_table_offset", "Q"),
        ("base_arg_data_size", "Q"),
        ("base_arg_data_offset", "Q"),
        ("packed_strings_size", "Q"),
        ("packed_strings_offset", "Q"),
        # No more 4x at the end.
    )

    def compute_base_args_size(self, existing_data_size):
        total_arg_size = sum([e.total_args_size for e in self.events.values()])
        while (existing_data_size + total_arg_size) % 16 != 0:
            total_arg_size += 1  # pad to multiple of 16
        return total_arg_size

    def pad_after_base_args(self, emevd_binary_after_base_args):
        while len(emevd_binary_after_base_args) % 16 != 0:
            emevd_binary_after_base_args += b"\0"  # pad to multiple of 16
        return emevd_binary_after_base_args
