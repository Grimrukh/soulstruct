import ast
import logging
import struct
from functools import wraps

__all__ = [
    "COMPARISON_NODES", "NEG_COMPARISON_NODES",
    "no_skip_or_negate_or_terminate", "negate_only", "skip_and_negate_and_terminate",
    "NoSkipOrTerminateError", "NoNegateError", "InstructionNotFoundError", "EnumStringError",
    "ConstantCondition", "get_value_test", "get_enum_name", "get_game_map_name", "boolify",
    "get_write_offset", "get_instruction_args", "get_byte_offset_from_struct",
]
_LOGGER = logging.getLogger(__name__)

COMPARISON_NODES = {ast.Eq: 0, ast.NotEq: 1, ast.Gt: 2, ast.Lt: 3, ast.GtE: 4, ast.LtE: 5}
NEG_COMPARISON_NODES = {ast.Eq: 1, ast.NotEq: 0, ast.Gt: 5, ast.Lt: 4, ast.GtE: 3, ast.LtE: 2}


def no_skip_or_negate_or_terminate(func):
    @wraps(func)
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines != 0:
            raise NoSkipOrTerminateError
        if negate:
            raise NoNegateError
        if end_event or restart_event:
            raise NoSkipOrTerminateError
        if condition is None:
            raise ValueError("Condition index must be specified (-7 to 7).")
        return func(*args, condition=condition, **kwargs)

    return decorated


def negate_only(func):
    @wraps(func)
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines != 0:
            raise NoSkipOrTerminateError
        if end_event or restart_event:
            raise NoSkipOrTerminateError
        if condition is None:
            raise ValueError("Condition index must be specified (-7 to 7).")
        return func(*args, condition=condition, negate=negate, **kwargs)

    return decorated


def skip_and_negate_and_terminate(func):
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
            if condition not in range(-7, 8):
                raise ValueError("Condition register index must be in range [-7, 7], inclusive.")
            return func(*args, condition=condition, negate=negate, **kwargs)

        if end_event:
            if restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, end_event=True, negate=negate, **kwargs)

        if restart_event:
            return func(*args, restart_event=True, negate=negate, **kwargs)

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")

    return decorated


class NoSkipOrTerminateError(Exception):
    """Indicates that a test call has no skip/terminate variant in the EMEVD language.

    This is generally handled internally by constructing a condition (which all test types can do) and skipping or
    terminating based on that condition's truth value.
    """
    pass


class InstructionNotFoundError(Exception):
    """Indicates that an instruction was not found in some code segment."""


class NoNegateError(Exception):
    """Indicates that a test call has no negated variant in the EMEVD language.

    This is generally handled internally by constructing a condition (which all test types can do) and negating a test
    of that condition's truth value.
    """
    pass


class ConstantCondition(object):
    """ Condition with no arguments. These conditions have 'hard-coded' methods in the EMEVD API. """

    def __init__(self, if_true_func=None, if_false_func=None,
                 skip_if_true_func=None, skip_if_false_func=None,
                 end_if_true_func=None, end_if_false_func=None,
                 restart_if_true_func=None, restart_if_false_func=None):
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
                    raise NoSkipOrTerminateError
                return self.skip_if_true_func(skip_lines)
            if self.skip_if_false_func is None:
                raise NoSkipOrTerminateError
            return self.skip_if_false_func(skip_lines)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if condition not in range(-7, 8):
                raise ValueError("Condition register index must be between -7 and 7.")
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
                    raise NoSkipOrTerminateError
                return self.end_if_false_func()
            if self.end_if_true_func is None:
                raise NoSkipOrTerminateError
            return self.end_if_true_func()

        if restart_event:
            if negate:
                if self.restart_if_false_func is None:
                    raise NoSkipOrTerminateError
                return self.restart_if_false_func()
            if self.restart_if_true_func is None:
                raise NoSkipOrTerminateError
            return self.restart_if_true_func()

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")


def get_value_test(
        value, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False,
        skip_if_true_func=None, skip_if_false_func=None,
        if_true_func=None, if_false_func=None,
        end_if_true_func=None, end_if_false_func=None,
        restart_if_true_func=None, restart_if_false_func=None):
    if skip_lines > 0:
        if condition is not None or end_event or restart_event:
            raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
        if skip_if_true_func is None or skip_if_false_func is None:
            raise NoSkipOrTerminateError  # Both of these functions must be defined.
        if negate:
            return skip_if_true_func(skip_lines, value)
        return skip_if_false_func(skip_lines, value)
    elif skip_lines < 0:
        raise ValueError("You cannot skip a negative number of lines.")

    if condition is not None:
        if condition not in range(-7, 8):
            raise ValueError("Condition register index must be between -7 and 7.")
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
                raise NoSkipOrTerminateError
            return end_if_false_func(value)
        if end_if_true_func is None:
            raise NoSkipOrTerminateError
        return end_if_true_func(value)

    if restart_event:
        if negate:
            if restart_if_false_func is None:
                raise NoSkipOrTerminateError
            return restart_if_false_func(value)
        if restart_if_true_func is None:
            raise NoSkipOrTerminateError
        return restart_if_true_func(value)

    raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")


def get_enum_name(enum, value, ignore_string_error=False):
    """ Decompiles a full enum attribute string, a la 'BannerType.VictoryAchieved', from the enum value. Raises
    a ValueError if the enum name is invalid (e.g. if it's a placeholder arg string). """
    try:
        return f'{enum.__name__}.{enum(value).name}'
    except ValueError:
        if isinstance(value, str):
            if ignore_string_error:
                return value
            raise EnumStringError(f"Unrecognized {str(enum)} value: {value}")
        raise ValueError(f"Invalid enum value: {value}")


class EnumStringError(Exception):
    """Indicates that a value expected to be found in an enum was a string, suggesting it is a placeholder arg."""
    pass


def get_byte_offset_from_struct(format_string):
    """Returns a dictionary of {byte_offset: (struct_index, struct_format)}.

    The byte offsets indicate where the associated element in the struct format string begins. Note that endian-type '@'
    (native byte alignment) is critical here, as EMEVD uses byte-aligned packed binary data.
    """
    endian = format_string[0]
    format_string = format_string[1:]
    byte_offset_array = {}
    for i in range(0, len(format_string)):
        offset = struct.calcsize(endian + format_string[:i + 1]) - struct.calcsize(endian + format_string[i])
        byte_offset_array[offset] = (i, format_string[i])
    return byte_offset_array


def get_instruction_args(file, instruction_class, instruction_index, first_arg_offset, event_args_size, format_dict):
    """Process instruction arguments (required and optional) from EMEVD binary."""

    previous_offset = file.tell()
    if event_args_size == 0:
        return "", []
    try:
        args_format = '@' + format_dict[instruction_class][instruction_index]
    except KeyError:
        raise KeyError(f"Cannot find argument types for instruction {instruction_class}[{instruction_index}].")

    # 's' arguments are actually four-byte offsets into the packed string data, though we will keep the 's' symbol.
    true_args_format = args_format.replace('s', 'I')
    required_args_size = struct.calcsize(true_args_format)
    if required_args_size > event_args_size:
        raise ValueError(f"Documented size of minimum required args for instruction {instruction_class}"
                         f"[{instruction_index}] is {required_args_size}, but size of args specified in EMEVD file is "
                         f"only {event_args_size}.")

    file.seek(first_arg_offset)
    req_args = struct.unpack(true_args_format, file.read(required_args_size))

    # Additional arguments may appear for the instruction 2000[00], 'RunEvent'. These instructions are tightly packed,
    # and are simply read here as unsigned integers; we need to actually parse the event to interpret them properly.

    extra_size = event_args_size - required_args_size

    opt_arg_count = extra_size // 4
    if opt_arg_count == 0:
        file.seek(previous_offset)
        return args_format[1:], list(req_args)
    elif extra_size % 4 != 0:
        _LOGGER.error(
            f"Error in optional arguments for instruction {instruction_class}[{instruction_index}]: "
            f"event_args_size = {event_args_size}, required_args_size = {required_args_size}")
        raise ValueError(f"Optional argument size must be a multiple of four bytes. Your EMEVD file seems malformed.")

    opt_args = [struct.unpack('<I', file.read(4))[0] for _ in range(opt_arg_count)]
    file.seek(previous_offset)
    return args_format[1:] + "|" + "I" * (extra_size // 4), list(req_args) + opt_args


def get_write_offset(event_format, arg_index):
    """Iterate over event format string to determine write offset of given argument index."""
    offset = 0
    for i, c in enumerate(event_format):
        if c in 'Hh':
            if (offset % 2) != 0:
                # Fill in remainder of 2-byte chunk.
                offset += 1
        elif c in 'Iif':
            while (offset % 4) != 0:
                # Fill in remainder of 4-byte chunk.
                offset += 1
        if i == arg_index:
            return offset
        if c in 'Bb':
            offset += 1
        elif c in 'Hh':
            offset += 2
        elif c in 'Iif':
            offset += 4


def boolify(integer):
    """Converts argument to a boolean if it's 0 or 1; otherwise passes it through (e.g. for event args)."""
    if isinstance(integer, int):
        if integer == 0:
            return False
        elif integer == 1:
            return True
    return integer


def get_game_map_name(area_id, block_id, game_module):
    """ Attempts to get the name of the game map. """
    try:
        area_id = int(area_id)
        block_id = int(block_id)
        return game_module.constants.MAP_NAMES[(int(area_id), int(block_id))]
    except (ValueError, KeyError):
        # Event arg replacement(s) or unknown map. Return tuple instead, stripping quotes from any string elements.
        return f"({area_id}, {block_id})"
