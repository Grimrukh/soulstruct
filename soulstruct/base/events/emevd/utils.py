from __future__ import annotations

__all__ = [
    "COMPARISON_NODES",
    "NEG_COMPARISON_NODES",
    "no_skip_or_negate_or_return",
    "negate_only",
    "skip_and_negate_and_return",
    "ConstantCondition",
    "get_value_test",
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
from functools import wraps

from .exceptions import NoSkipOrReturnError, NoNegateError

if tp.TYPE_CHECKING:
    from soulstruct.utilities.binary import BinaryReader

_LOGGER = logging.getLogger(__name__)

COMPARISON_NODES = {ast.Eq: 0, ast.NotEq: 1, ast.Gt: 2, ast.Lt: 3, ast.GtE: 4, ast.LtE: 5}
NEG_COMPARISON_NODES = {ast.Eq: 1, ast.NotEq: 0, ast.Gt: 5, ast.Lt: 4, ast.GtE: 3, ast.LtE: 2}


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


class ConstantCondition:
    """Condition with no arguments. These conditions have 'hard-coded' methods in the EMEVD API."""

    def __init__(
        self,
        if_true_func=None,
        if_false_func=None,
        skip_if_true_func=None,
        skip_if_false_func=None,
        end_if_true_func=None,
        end_if_false_func=None,
        restart_if_true_func=None,
        restart_if_false_func=None,
    ):
        self.if_true_func = if_true_func
        self.if_false_func = if_false_func
        self.skip_if_true_func = skip_if_true_func
        self.skip_if_false_func = skip_if_false_func
        self.end_if_true_func = end_if_true_func
        self.end_if_false_func = end_if_false_func
        self.restart_if_true_func = restart_if_true_func
        self.restart_if_false_func = restart_if_false_func

    def __call__(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        """ Constants are called with no user-level args. """

        if skip_lines > 0:
            if condition is not None or end_event or restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if self.skip_if_true_func is None:
                    raise NoSkipOrReturnError
                return self.skip_if_true_func(skip_lines)
            if self.skip_if_false_func is None:
                raise NoSkipOrReturnError
            return self.skip_if_false_func(skip_lines)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if end_event or restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                return self.if_false_func(condition)
            return self.if_true_func(condition)

        if end_event:
            if restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if self.end_if_false_func is None:
                    raise NoSkipOrReturnError
                return self.end_if_false_func()
            if self.end_if_true_func is None:
                raise NoSkipOrReturnError
            return self.end_if_true_func()

        if restart_event:
            if negate:
                if self.restart_if_false_func is None:
                    raise NoSkipOrReturnError
                return self.restart_if_false_func()
            if self.restart_if_true_func is None:
                raise NoSkipOrReturnError
            return self.restart_if_true_func()

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")


def get_value_test(
    value,
    negate=False,
    condition=None,
    skip_lines=0,
    end_event=False,
    restart_event=False,
    skip_if_true_func=None,
    skip_if_false_func=None,
    if_true_func=None,
    if_false_func=None,
    end_if_true_func=None,
    end_if_false_func=None,
    restart_if_true_func=None,
    restart_if_false_func=None,
):
    if skip_lines > 0:
        if condition is not None or end_event or restart_event:
            raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
        if skip_if_true_func is None or skip_if_false_func is None:
            raise NoSkipOrReturnError  # Both of these functions must be defined.
        if negate:
            return skip_if_true_func(skip_lines, value)
        return skip_if_false_func(skip_lines, value)
    elif skip_lines < 0:
        raise ValueError("You cannot skip a negative number of lines.")

    if condition is not None:
        if end_event or restart_event:
            raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
        if negate:
            if if_false_func is None:
                raise NoNegateError  # Some game types only have a positive condition test (e.g. IfObjectActivated).
            return if_false_func(condition, value)
        return if_true_func(condition, value)

    if end_event:
        if restart_event:
            raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
        if negate:
            if end_if_false_func is None:
                raise NoSkipOrReturnError
            return end_if_false_func(value)
        if end_if_true_func is None:
            raise NoSkipOrReturnError
        return end_if_true_func(value)

    if restart_event:
        if negate:
            if restart_if_false_func is None:
                raise NoSkipOrReturnError
            return restart_if_false_func(value)
        if restart_if_true_func is None:
            raise NoSkipOrReturnError
        return restart_if_true_func(value)

    raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")


def get_byte_offset_from_struct(format_string):
    """Returns a dictionary of {byte_offset: (struct_index, struct_format)}.

    The byte offsets indicate where the associated element in the struct format string begins. Note that endian-type '@'
    (native byte alignment) is critical here, as EMEVD uses byte-aligned packed binary data.
    """
    endian = format_string[0]
    format_string = format_string[1:]
    byte_offset_array = {}
    for i in range(0, len(format_string)):
        offset = struct.calcsize(endian + format_string[: i + 1]) - struct.calcsize(endian + format_string[i])
        byte_offset_array[offset] = (i, format_string[i])
    return byte_offset_array


def get_instruction_args(
    reader: BinaryReader, instruction_class, instruction_index, first_arg_offset, event_args_size, format_dict
):
    """Process instruction arguments (required and optional) from EMEVD binary."""

    previous_offset = reader.position
    if event_args_size == 0:
        return "", []
    try:
        args_format = "@" + format_dict[instruction_class][instruction_index]
    except KeyError:
        raise KeyError(f"Cannot find argument types for instruction {instruction_class}[{instruction_index:02d}].")

    # 's' arguments are actually four-byte offsets into the packed string data, though we will keep the 's' symbol.
    true_args_format = args_format.replace("s", "I")
    required_args_size = struct.calcsize(true_args_format)
    if required_args_size > event_args_size:
        raise ValueError(
            f"Documented size of minimum required args for instruction {instruction_class}"
            f"[{instruction_index}] is {required_args_size}, but size of args specified in EMEVD file is "
            f"only {event_args_size}."
        )

    reader.seek(first_arg_offset)
    args = reader.unpack(true_args_format)

    # Additional arguments may appear for the instruction 2000[00], 'RunEvent'. These instructions are tightly packed,
    # and are simply read here as unsigned integers; we need to actually parse the event to interpret them properly.

    extra_size = event_args_size - required_args_size

    opt_arg_count = extra_size // 4
    if opt_arg_count == 0:
        reader.seek(previous_offset)
        return args_format[1:], list(args)
    elif extra_size % 4 != 0:
        raise ValueError(
            f"Error interpreting instruction {instruction_class}[{instruction_index}]: optional argument "
            f"size is not a multiple of four bytes ({extra_size})."
        )

    opt_args = [reader.unpack_value("<I") for _ in range(opt_arg_count)]
    reader.seek(previous_offset)
    return args_format[1:] + "|" + "I" * (extra_size // 4), list(args) + opt_args


def get_write_offset(event_format, arg_index):
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
