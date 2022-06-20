import abc

from soulstruct.base.ezstate.esd import (
    ESD as _BaseESD,
    Command as _BaseCommand,
    Condition as _BaseCondition,
    State as _BaseState,
)
from soulstruct.containers.dcx import DCXType
from soulstruct.games import DarkSoulsDSRType
from soulstruct.game_types.internal_types import ESDType
from soulstruct.utilities.binary import BinaryStruct

__all__ = ["TalkESD", "ChrESD"]


GAME_VERSION = 1
LONG_FORMAT = True


class Command(_BaseCommand, abc.ABC):
    STRUCT = BinaryStruct(
        ("bank", "i"),  # Values of 1, 5, 6, 7 have been encountered.
        ("index", "i"),
        ("args_offset", "q"),
        ("args_count", "q"),
    )
    ARG_STRUCT = BinaryStruct(("arg_ezl_offset", "q"), ("arg_ezl_size", "q"), )


class Condition(_BaseCondition, abc.ABC):
    STRUCT = BinaryStruct(
        ("next_state_offset", "q"),
        ("pass_commands_offset", "q"),
        ("pass_commands_count", "q"),
        ("subcondition_pointers_offset", "q"),
        ("subcondition_pointers_count", "q"),
        ("test_ezl_offset", "q"),
        ("test_ezl_size", "q"),
    )
    POINTER_STRUCT = BinaryStruct(
        ("condition_offset", "q"),
    )
    STATE_ID_STRUCT = BinaryStruct(
        ("state_id", "q"),
    )


class State(_BaseState, abc.ABC):
    STRUCT = BinaryStruct(
        ("index", "q"),
        ("condition_pointers_offset", "q"),
        ("condition_pointers_count", "q"),
        ("enter_commands_offset", "q"),
        ("enter_commands_count", "q"),
        ("exit_commands_offset", "q"),
        ("exit_commands_count", "q"),
        ("ongoing_commands_offset", "q"),
        ("ongoing_commands_count", "q"),
    )


class ESD(_BaseESD, DarkSoulsDSRType, abc.ABC):

    DCX_TYPE = DCXType.DCX_DFLT_10000_24_9

    EXTERNAL_HEADER_STRUCT = BinaryStruct(
        ("version", "4s", b"fsSL"),  # Note specific case.
        ("one", "i", 1),
        ("game_version", "2i", [GAME_VERSION, GAME_VERSION]),
        ("table_size_offset", "i", 84),
        ("internal_data_size", "i"),  # excludes this external header
        ("unk", "i", 6),
        ("internal_header_size", "i", 72),
        ("internal_header_count", "i", 1),
        ("state_machine_header_size", "i", 32),
        ("state_machine_count", "i"),
        ("state_size", "i", 72),
        ("state_count", "i"),
        ("condition_size", "i", 56),
        ("condition_count", "i"),
        ("command_size", "i", 24),
        ("command_count", "i"),
        ("command_arg_size", "i", 16),
        ("command_arg_count", "i"),
        ("condition_pointers_offset", "i"),
        ("condition_pointers_count", "i"),
        ("esd_name_offset_minus_1", "i"),
        # Not sure why this is minus 1. Use the internal header for the real offset.
        ("esd_name_length", "i"),  # equal to internal header
        ("unk_offset_1", "i"),
        ("unk_size_1", "i", 0),
        ("unk_offset_2", "i"),
        ("unk_size_2", "i", 0),
    )
    INTERNAL_HEADER_STRUCT = BinaryStruct(
        ("one", "i", 1),
        ("magic", "4i"),
        "4x",
        ("state_machine_headers_offset", "q", 72),
        ("state_machine_count", "q"),
        ("esd_name_offset", "q"),  # accurate, unlike external header
        ("esd_name_length", "q"),
        # identical to external header entry; note this is only *half* the name byte size due to UTF-16
        "16x",
    )
    STATE_MACHINE_HEADER_STRUCT = BinaryStruct(
        ("state_machine_index", "q"),
        ("state_machine_offset", "q"),
        ("state_count", "q"),  # number of states
        ("state_machine_offset_2", "q"),  # duplicate
    )


class TalkCommand(Command):
    ESD_TYPE = ESDType.TALK


class ChrCommand(Command):
    ESD_TYPE = ESDType.CHR


class TalkCondition(Condition):
    ESD_TYPE = ESDType.TALK
    Command = TalkCommand


class ChrCondition(Condition):
    ESD_TYPE = ESDType.CHR
    Command = ChrCommand


class TalkState(State):
    ESD_TYPE = ESDType.TALK
    Condition = TalkCondition
    Command = TalkCommand


class ChrState(State):
    ESD_TYPE = ESDType.CHR
    Condition = ChrCondition
    Command = ChrCommand


class TalkESD(ESD):
    ESD_TYPE = ESDType.TALK
    State = TalkState


class ChrESD(ESD):
    ESD_TYPE = ESDType.CHR
    State = ChrState
