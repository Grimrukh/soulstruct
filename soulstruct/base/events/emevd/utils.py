from __future__ import annotations

__all__ = [
    "COMPARISON_NODES",
    "NEG_COMPARISON_NODES",
    "no_skip_or_negate_or_return",
    "negate_only",
    "skip_and_negate_and_return",
    "get_coord_entity_type",
    "EventArgumentData",
    "boolify",
    "get_write_offset",
    "get_instruction_args",
    "get_byte_offset_from_struct",
    "format_event_layers",
]

import ast
import logging
import struct
import typing as tp
from enum import IntEnum
from functools import wraps

from .exceptions import NoSkipOrReturnError, NoNegateError

if tp.TYPE_CHECKING:
    from soulstruct.base.game_types import GAME_TYPE
    from soulstruct.utilities.binary import BinaryReader

_LOGGER = logging.getLogger(__name__)

COMPARISON_NODES = {ast.Eq: 0, ast.NotEq: 1, ast.Gt: 2, ast.Lt: 3, ast.GtE: 4, ast.LtE: 5}
NEG_COMPARISON_NODES = {ast.Eq: 1, ast.NotEq: 0, ast.Gt: 5, ast.Lt: 4, ast.GtE: 3, ast.LtE: 2}

_OPTIONAL_ARGS_ALLOWED = ((2000, 0), (2000, 6))


def no_skip_or_negate_or_return(func):
    @wraps(func)
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines != 0:
            raise NoSkipOrReturnError
        if negate:
            raise NoNegateError
        if end_event or restart_event:
            raise NoSkipOrReturnError
        if condition is None:
            raise ValueError("Condition index must be specified.")
        return func(*args, condition=condition, **kwargs)

    return decorated


def negate_only(func):
    @wraps(func)
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines != 0:
            raise NoSkipOrReturnError
        if end_event or restart_event:
            raise NoSkipOrReturnError
        if condition is None:
            raise ValueError("Condition index must be specified.")
        return func(*args, condition=condition, negate=negate, **kwargs)

    return decorated


def skip_and_negate_and_return(func):
    @wraps(func)
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines > 0:
            if condition is not None or end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, skip_lines=skip_lines, negate=negate, **kwargs)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, condition=condition, negate=negate, **kwargs)

        if end_event:
            if restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, end_event=True, negate=negate, **kwargs)

        if restart_event:
            return func(*args, restart_event=True, negate=negate, **kwargs)

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")

    return decorated


class EventArgumentData:
    """Holds event argument offset tuple, e.g. `(12, 4)`, and event argument type, e.g. `Region`.

    Passed to EMEVD instructions/tests so that arguments like `anchor_type` and `destination_type` do not need to be
    specified with properly type-annotated event arguments.
    """
    offset_tuple: tuple[int, int]
    arg_class: tp.Optional[GAME_TYPE]

    def __init__(self, offset_tuple: tuple[int, int], arg_class: tp.Optional[GAME_TYPE] = None):
        self.offset_tuple = offset_tuple
        self.arg_class = arg_class

    def get_coord_entity_type(self, coord_entity_type_enum: tp.Type[IntEnum]):
        try:
            return get_coord_entity_type(coord_entity_type_enum, self.arg_class)
        except KeyError:
            raise ValueError("Event argument does not have a `CoordEntityType`.")

    def __repr__(self):
        if self.arg_class:
            return f"EventArgumentData({self.offset_tuple[0]}, {self.offset_tuple[1]}, {self.arg_class})"
        return f"EventArgumentData({self.offset_tuple[0]}, {self.offset_tuple[1]})"


def get_coord_entity_type(coord_entity_type_enum: tp.Type[IntEnum], arg_type) -> IntEnum:
    try:
        return coord_entity_type_enum[arg_type.__name__]
    except KeyError:
        raise KeyError(f"Cannot auto-detect `CoordEntityType` from argument type: {arg_type.__name__}")


def get_byte_offset_from_struct(format_string: str) -> dict[int, tuple[int, str]]:
    """Returns a dictionary mapping `byte_offset` to `(struct_index, struct_format)` tuples.

    The byte offsets indicate where the associated element in the struct format string begins. Note that native byte
    alignment "@" is critical here, as EMEVD uses byte-aligned packed binary data.
    """
    format_string = format_string.replace("|", "")
    byte_offset_array = {}
    for i in range(len(format_string)):
        offset = struct.calcsize("@" + format_string[:i + 1]) - struct.calcsize("@" + format_string[i])
        byte_offset_array[offset] = (i, format_string[i])
    return byte_offset_array


def get_instruction_args(
    reader: BinaryReader, category: int, index: int, first_arg_offset: int, event_args_size: int, emedf: dict
) -> tuple[str, list[tp.Any]]:
    """Process instruction arguments (required and optional) from EMEVD reader.

    Uses the `EMEDF` class variable attached to the caller `Instruction`.
    """

    try:
        emedf_args_info = emedf[category, index]["args"]
    except KeyError:
        raise KeyError(f"Could not find instruction ({category}, {index}) in `Instruction.EMEDF`.")
    previous_offset = reader.position
    if event_args_size == 0:
        return "", []
    try:
        args_format = "@" + "".join(arg["internal_type"].get_fmt() for arg in emedf_args_info.values())
    except KeyError:
        raise KeyError(f"Cannot find argument types for instruction {category}[{index:02d}] ({event_args_size} bytes)")

    # 's' arguments are actually four-byte offsets into the packed string data, though we will keep the 's' symbol.
    struct_args_format = args_format.replace("s", "I")
    required_args_size = struct.calcsize(struct_args_format)
    if required_args_size > event_args_size:
        raise ValueError(
            f"Documented size of minimum required args for instruction {category}"
            f"[{index}] is {required_args_size}, but size of args specified in EMEVD file is "
            f"only {event_args_size}."
        )

    # NOTE: Reader will be reset to initial offset below.
    reader.seek(first_arg_offset)
    args = reader.unpack(struct_args_format)

    # Additional arguments may appear for the instruction 2000[00], 'RunEvent'. These instructions are tightly packed
    # and are always aligned to 4. We read them here as unsigned integers and must actually parse the called event ID to
    # interpret them properly (done at `EMEVD` class level).

    extra_size = event_args_size - required_args_size

    opt_arg_count = extra_size // 4
    if opt_arg_count == 0:
        reader.seek(previous_offset)
        return args_format[1:], list(args)
    elif (category, index) not in _OPTIONAL_ARGS_ALLOWED:
        raise ValueError(
            f"Extra arguments found for instruction {category}[{index}], which is not permitted. Arg types may be "
            f"wrong (too short) for this instruction.\n"
            f"    required size = {required_args_size}\n"
            f"    actual size = {event_args_size}"
        )
    elif extra_size % 4 != 0:
        raise ValueError(
            f"Error interpreting instruction {category}[{index}]: optional argument "
            f"size is not a multiple of four bytes ({extra_size})."
        )

    opt_args = [reader["I"] for _ in range(opt_arg_count)]
    reader.seek(previous_offset)
    return args_format[1:] + "|" + "I" * (extra_size // 4), list(args) + opt_args


def get_write_offset(event_format, arg_index) -> int:
    """Iterate over event format string to determine write offset of given argument index."""
    offset = 0
    for i, c in enumerate(event_format):
        if c in "Hh":
            if (offset % 2) != 0:
                # Fill in remainder of 2-byte chunk.
                offset += 1
        elif c in "Iif":
            while (offset % 4) != 0:
                # Fill in remainder of 4-byte chunk.
                offset += 1
        if i == arg_index:
            return offset
        if c in "Bb":
            offset += 1
        elif c in "Hh":
            offset += 2
        elif c in "Iif":
            offset += 4


def boolify(integer):
    """Converts argument to a boolean if it's 0 or 1; otherwise passes it through (e.g. for event args)."""
    if isinstance(integer, int):
        if integer == 0:
            return False
        elif integer == 1:
            return True
    return integer


def format_event_layers(event_layers):
    if event_layers is None:
        return ""
    if isinstance(event_layers, int):
        event_layers = [event_layers]
    if not isinstance(event_layers, (list, tuple)):
        raise TypeError
    return f"<" + ", ".join(str(i) for i in event_layers) + ">"
