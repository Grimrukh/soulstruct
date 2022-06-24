import abc

from soulstruct.base.ezstate.esd import (
    ESD as _BaseESD,
    Command as _BaseCommand,
    Condition as _BaseCondition,
    State as _BaseState,
)
from soulstruct.games import DarkSoulsPTDEType
from soulstruct.base.ezstate.esd.esd_type import ESDType
from soulstruct.utilities.binary import BinaryStruct

__all__ = ["TalkESD", "ChrESD"]


GAME_VERSION = 1
LONG_FORMAT = False


class Command(_BaseCommand, abc.ABC):
    STRUCT = BinaryStruct(
        ("bank", "i"),  # Values of 1, 5, 6, 7 have been encountered.
        ("index", "i"),
        ("args_offset", "i"),
        ("args_count", "i"),
    )
    ARG_STRUCT = BinaryStruct(
        ("arg_ezl_offset", "i"),
        ("arg_ezl_size", "i"),
    )


class Condition(_BaseCondition, abc.ABC):
    STRUCT = BinaryStruct(
        ("next_state_offset", "i"),
        ("pass_commands_offset", "i"),
        ("pass_commands_count", "i"),
        ("subcondition_pointers_offset", "i"),
        ("subcondition_pointers_count", "i"),
        ("test_ezl_offset", "i"),
        ("test_ezl_size", "i"),
    )
    POINTER_STRUCT = BinaryStruct(
        ("condition_offset", "i"),
    )
    STATE_ID_STRUCT = BinaryStruct(
        ("state_id", "i"),
    )


class State(_BaseState, abc.ABC):
    STRUCT = BinaryStruct(
        ("index", "i"),
        ("condition_pointers_offset", "i"),
        ("condition_pointers_count", "i"),
        ("enter_commands_offset", "i"),
        ("enter_commands_count", "i"),
        ("exit_commands_offset", "i"),
        ("exit_commands_count", "i"),
        ("ongoing_commands_offset", "i"),
        ("ongoing_commands_count", "i"),
    )


class ESD(_BaseESD, DarkSoulsPTDEType, abc.ABC):

    EXTERNAL_HEADER_STRUCT = BinaryStruct(
        ("version", "4s", b"fSSL"),  # Note specific case.
        ("one", "i", 1),
        ("game_version", "2i", [GAME_VERSION, GAME_VERSION]),
        ("table_size_offset", "i", 84),
        ("internal_data_size", "i"),  # excludes header size
        ("unk", "i", 6),
        ("internal_header_size", "i", 44),
        ("internal_header_count", "i", 1),
        ("state_machine_header_size", "i", 16),
        ("state_machine_count", "i"),
        ("state_size", "i", 36),
        ("state_count", "i"),
        ("condition_size", "i", 28),
        ("condition_count", "i"),
        ("command_size", "i", 16),
        ("command_count", "i"),
        ("command_arg_size", "i", 8),
        ("command_arg_count", "i"),
        ("condition_pointers_offset", "i"),
        ("condition_pointers_count", "i"),
        ("esd_name_offset_minus_1", "i"),
        ("esd_name_length", "i"),
        ("unk_offset_1", "i"),
        ("unk_size_1", "i", 0),
        ("unk_offset_2", "i"),
        ("unk_size_2", "i", 0),
    )
    INTERNAL_HEADER_STRUCT = BinaryStruct(
        ("one", "i", 1),
        ("magic", "4i"),  # TODO: constant within games, at least?
        ("state_machine_headers_offset", "i", 44),
        ("state_machine_count", "i"),
        ("esd_name_offset", "i"),  # accurate, unlike external header
        ("esd_name_length", "i"),
        "8x",
    )
    STATE_MACHINE_HEADER_STRUCT = BinaryStruct(
        ("state_machine_index", "i"),
        ("state_machine_offset", "i"),
        ("state_count", "i"),  # number of states
        ("state_machine_offset_2", "i"),  # duplicate
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
