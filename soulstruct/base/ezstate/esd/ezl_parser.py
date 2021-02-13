from __future__ import annotations

__all__ = ["decompile", "FUNCTION_ARG_BYTES_BY_COUNT", "OPERATORS_BY_NODE", "CLEAR_REGISTERS", "SET_INTERNAL_SYMBOLS"]

import ast
import logging
import struct
from binascii import hexlify

from soulstruct.game_types.internal_types import ESDType
from soulstruct.utilities.core import read_chars_from_buffer

from .functions import TEST_FUNCTIONS

_LOGGER = logging.getLogger(__name__)

_REGISTERS = [""] * 8
_SHOW_INTERNAL_SYMBOLS = False

FUNCTION_ARG_COUNTS_BY_BYTE = {
    b"\x84": 0,
    b"\x85": 1,
    b"\x86": 2,
    b"\x87": 3,
    b"\x88": 4,
    b"\x89": 5,
    b"\x8a": 6,
}
FUNCTION_ARG_BYTES_BY_COUNT = {v: k for k, v in FUNCTION_ARG_COUNTS_BY_BYTE.items()}

UNARY_OPERATORS_BY_BYTE = {
    b"\x8d": "<N",  # TODO: Unpack to 'not' I guess.
}

BINARY_OPERATORS_BY_BYTE = {
    # byte: (symbol, priority)
    b"\x8c": ("+", 4),
    # b'\x8d' is the unary negate operator. # TODO: Implement negation.
    b"\x8e": ("-", 4),
    b"\x8f": ("*", 5),
    b"\x90": ("/", 5),
    b"\x91": ("<=", 3),
    b"\x92": (">=", 3),
    b"\x93": ("<", 3),
    b"\x94": (">", 3),
    b"\x95": ("==", 3),
    b"\x96": ("!=", 3),
    # b'\x97' is unknown (never seems to appear).
    b"\x98": ("and", 2),
    b"\x99": ("or", 1),
}
OPERATORS_BY_NODE = {
    ast.Add: b"\x8c",
    # TODO: What would negate look like in Python? "not FunctionCall()"?
    ast.Sub: b"\x8e",
    ast.Mult: b"\x8f",
    ast.Div: b"\x90",
    ast.LtE: b"\x91",
    ast.GtE: b"\x92",
    ast.Lt: b"\x93",
    ast.Gt: b"\x94",
    ast.Eq: b"\x95",
    ast.NotEq: b"\x96",
    # b'\x97' is unknown (never seems to appear).
}


def CLEAR_REGISTERS():
    """ Called when evaluating conditions in a new state.
    TODO: Confirm that subconditions do not clear the registers.
    """
    global _REGISTERS
    _REGISTERS = [""] * 8


def SET_INTERNAL_SYMBOLS(value: bool):
    """ Show symbols for register loads, 'continue if false', and 'continue if true'. """
    global _SHOW_INTERNAL_SYMBOLS
    _SHOW_INTERNAL_SYMBOLS = value


def nice_hex_bytes(byte_sequence):
    return b" ".join(hexlify(byte_sequence[i : i + 1]) for i in range(len(byte_sequence)))


def pop_multiple(sequence: list, count: int):
    return [sequence.pop() for _ in range(count)]


def format_function(sequence: list, arg_count_key: bytes, esd_type: ESDType, func_prefix=""):
    arg_count = FUNCTION_ARG_COUNTS_BY_BYTE[arg_count_key]
    if arg_count == 0:
        f_id = sequence.pop()
        args = []
    else:
        *args, f_id = pop_multiple(sequence, arg_count + 1)
    try:
        # TODO: not using arg names or types yet, but make them available as kwargs?
        function_name, arg_names, arg_types = TEST_FUNCTIONS[esd_type][int(f_id)]
    except KeyError:
        function_name = f"Test_{esd_type}_{f_id}"
    return f"{func_prefix}{function_name}({', '.join(str(arg) for arg in reversed(args))})"


def format_binary_operator(sequence: list, operator_key: bytes):
    operator, priority = BINARY_OPERATORS_BY_BYTE[operator_key]
    right, left = pop_multiple(sequence, 2)
    # Put parentheses around operands if they contain any other lower-priority binary operators.
    if isinstance(left, str) and any(o in left for o, p in BINARY_OPERATORS_BY_BYTE.values() if p < priority):
        left = f"({left})"
    if isinstance(right, str) and any(o in right for o, p in BINARY_OPERATORS_BY_BYTE.values() if p < priority):
        right = f"({right})"
    return f"{left} {operator} {right}"


def decompile(byte_sequence, esd_type: ESDType, func_prefix=""):
    """Decompile `byte_sequence`."""
    esd_type = ESDType(esd_type)

    # _LOGGER.debug(f"Unparsed: {nice_hex_bytes(byte_sequence)}")

    output = []  # Used as a stack.

    i = 0
    while i < len(byte_sequence):

        b = byte_sequence[i : i + 1]

        if b"\x00" <= b <= b"\x7f":
            output.append(struct.unpack("<b", b)[0] - 64)
            i += 1

        elif b == b"\x80":
            # Start of a 32-bit float (single).
            output.append(struct.unpack("<f", byte_sequence[i + 1 : i + 5])[0])
            i += 5

        elif b == b"\x81":
            # Start of a 64-bit float (double).
            output.append(struct.unpack("<d", byte_sequence[i + 1 : i + 9])[0])
            i += 9

        elif b == b"\x82":
            # Start of a 32-bit signed integer.
            output.append(struct.unpack("<i", byte_sequence[i + 1 : i + 5])[0])
            i += 5

        # b'\x83' is unknown. Possibly a 64-bit signed integer.

        elif b"\x84" <= b <= b"\x8a":
            # Function call with 0-6 arguments.
            output.append(format_function(output, b, esd_type, func_prefix))
            i += 1

        # b'\x8b' is unknown. Could simply be a function with seven arguments.

        elif b"\x8c" <= b <= b"\x99":
            # Binary operation on last two elements. Includes logical operations (and/or).
            output.append(format_binary_operator(output, b))
            i += 1

        # b'\xa0' is unknown.

        elif b == b"\xa1":
            # End of line. Not printed (and technically not that useful).
            i += 1
            if i != len(byte_sequence):
                raise ValueError("Encounter end-of-line marker \xa1 before end of line.")

        # Bytes b'\xa2' to b'\xa4' are unknown. Could be different types of strings.

        elif b == b"\xa5":
            # Start of a null-terminated string. I believe it is always UTF-16LE.
            try:
                string = read_chars_from_buffer(byte_sequence, offset=i + 1, encoding="utf-16le")
            except ValueError:
                _LOGGER.error(f"Could not interpret ESD string from bytes: {byte_sequence}")
                raise
            output.append(repr(string))
            i += 2 * len(string) + 3  # includes \xa5 and null termination

        elif b == b"\xa6":
            # "Continue If False". Seems useless, as this is the default behavior.
            if _SHOW_INTERNAL_SYMBOLS:
                output[-1] += "..."
            i += 1

        elif b"\xa7" <= b <= b"\xae":
            # Save (output of) last element to register.
            _REGISTERS[struct.unpack("<B", b)[0] - 167] = output[-1]
            i += 1

        elif b"\xaf" <= b <= b"\xb6":
            # Load (output of) last element from register.
            loaded_expr = _REGISTERS[struct.unpack("<B", b)[0] - 175]
            if _SHOW_INTERNAL_SYMBOLS:
                loaded_expr = "&" + loaded_expr
            output.append(loaded_expr)
            i += 1

        elif b == b"\xb7":
            # "Return If False". Optimizes code by ensuring that conditions that have already
            # failed an 'AND' logical operation only continue if needed for a register write.
            if _SHOW_INTERNAL_SYMBOLS:
                output[-1] += "!"
            i += 1

        elif b == b"\xb8":
            # Get state machine argument at index.
            output.append(f"MACHINE_ARGS[{output.pop()}]")
            i += 1

        elif b == b"\xb9":
            # Check status of state machine called (presumably just the last one called).
            output.append("MACHINE_CALL_STATUS")
            i += 1

        elif b == b"\xba":
            # State machine status. (No other values known, or used.)
            output.append("ONGOING")
            i += 1

        else:
            msg = f"Unknown EZL byte encountered: {b}, after output {output}"
            _LOGGER.error(msg)
            raise ValueError(msg)

    # _LOGGER.debug(f"Parsed: {output}")
    return "".join(str(o) for o in output)
