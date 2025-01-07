from __future__ import annotations

__all__ = [
    "EventArgumentData",
    "get_coord_entity_type",
    "boolify",
    "get_write_offset",
    "get_instruction_args",
    "get_byte_offset_from_struct",
    "format_event_layers",
]

import logging
import struct
import typing as tp
from enum import IntEnum

from soulstruct.base.game_types import GameObjectInt, GAME_INT_TYPE

if tp.TYPE_CHECKING:
    from .emedf import EMEDF_TYPING
    from soulstruct.utilities.binary import BinaryReader

_LOGGER = logging.getLogger("soulstruct")

_OPTIONAL_ARGS_ALLOWED = ((2000, 0), (2000, 6))


class EventArgumentData(tp.NamedTuple):
    """Holds event argument offset/size, e.g. 12 and 4, and optional event argument type, e.g. `Region`.

    Passed to EMEVD instructions/tests so that arguments like `anchor_type` and `destination_type` do not need to be
    specified with properly type-annotated event arguments.
    """
    offset: int
    size: int
    arg_class: tp.Optional[GAME_INT_TYPE] = None

    def get_coord_entity_type(self, coord_entity_type_enum: type[IntEnum]):
        """Forwards to `get_coord_entity_type` with `self.arg_class` as `arg_or_type`."""
        try:
            return get_coord_entity_type(coord_entity_type_enum, self.arg_class)
        except KeyError:
            raise ValueError("Event argument does not have a `CoordEntityType`.")

    def __repr__(self):
        if self.arg_class:
            return f"EventArgumentData({self.offset}, {self.size}, {self.arg_class})"
        return f"EventArgumentData({self.offset}, {self.size})"


def get_coord_entity_type(
    coord_entity_type_enum: type[IntEnum],
    arg_or_type: EventArgumentData | GameObjectInt | GAME_INT_TYPE,
) -> IntEnum:
    """Automatically detect `CoordEntityType` from argument `arg_or_type`."""
    if isinstance(arg_or_type, EventArgumentData):
        arg_or_type = arg_or_type.arg_class
    if isinstance(arg_or_type, GameObjectInt):
        arg_or_type = arg_or_type.__class__

    # Check supported types using names of types in `__mro__`.
    mro_names = [parent_type.__name__ for parent_type in arg_or_type.__mro__]
    for coord_entity_name in coord_entity_type_enum.__members__:  # type: ignore
        if coord_entity_name in mro_names:
            return coord_entity_type_enum[coord_entity_name]

    raise KeyError(f"Cannot auto-detect `CoordEntityType` from argument type: {arg_or_type.__name__}")


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
    reader: BinaryReader, category: int, index: int, first_arg_offset: int, event_args_size: int, emedf: EMEDF_TYPING
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

    # Additional arguments may appear for the instruction 2000[00], 'RunEvent', and from DS3 onward, 2000[06],
    # 'RunCommonEvent'. These instructions are tightly packed and are always aligned to 4. We read them here as
    # unsigned integers and must actually parse the called event ID (or `common_func` event ID) to interpret them
    # properly (done at `EMEVD` class level).

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


def get_write_offset(event_format: str, arg_index: int) -> int:
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
