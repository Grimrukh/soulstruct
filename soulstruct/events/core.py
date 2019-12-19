import ast
from enum import Enum
from functools import wraps


class EnumStringError(Exception):
    """Indicates that a value expected to be found in an enum was a string, suggesting it is a placeholder arg."""
    pass


class InstructionNotFoundError(Exception):
    """Indicates that an instruction was not found in some code segment."""


class NoSkipOrTerminateError(Exception):
    """Indicates that a test call has no skip/terminate variant in the EMEVD language.

    This is generally handled internally by constructing a condition (which all test types can do) and skipping or
    terminating based on that condition's truth value.
    """
    pass


class NoNegateError(Exception):
    """Indicates that a test call has no negated variant in the EMEVD language.

    This is generally handled internally by constructing a condition (which all test types can do) and negating a test
    of that condition's truth value.
    """
    pass


INSTRUCTION_ARG_TYPES = {}


def set_instruction_arg_types(arg_type_dict):
    global INSTRUCTION_ARG_TYPES
    INSTRUCTION_ARG_TYPES = arg_type_dict


def numeric_instruction(instruction_info, *args, arg_types=None):
    """Instruction info should be (class, index, [defaults]), with defaults assumed all zeroes if absent."""
    global INSTRUCTION_ARG_TYPES
    event_args = []
    arg_loads = []
    if arg_types is None:
        try:
            arg_types = INSTRUCTION_ARG_TYPES[instruction_info[0]][instruction_info[1]]
        except KeyError:
            raise KeyError(f"Could not find instruction {instruction_info[0]}[{instruction_info[1]:02d} in type dict.")
    for i, arg in enumerate(args):
        if isinstance(arg, Enum):
            event_args.append(args[i].value)
        elif isinstance(arg, bool):
            event_args.append(int(arg))
        elif isinstance(arg, tuple):
            # Start offset and size of an event argument.
            write_offset = get_write_offset(arg_types, i)
            arg_loads.append(f'    ^({write_offset} <- {arg[0]}, {arg[1]})')
            if len(instruction_info) == 3:
                # Use optional dummy dictionary.
                event_args.append(instruction_info[2][i])
            else:
                event_args.append(0)
        else:
            event_args.append(arg)
    return [f'{instruction_info[0]: 5d}[{instruction_info[1]:02d}] ({arg_types}){event_args}'] + arg_loads


def header(event_id, restart_type=0):
    return [f"{event_id}, {restart_type}"]


def define_args(arg_types):
    args = []
    for i, c in enumerate(arg_types):
        if c in 'Bb':
            c_size = 1
        elif c in 'Hh':
            c_size = 2
        elif c in 'Iif':
            c_size = 4
        else:
            raise ValueError(f"Invalid character {c} in arg_types.")
        args.append((get_write_offset(arg_types, i), c_size))
    return args


def load_arg(write_from_offset, read_from_offset, bytes_length):
    """ Loads bytes from event initialization arguments (see 0[00]) into the instruction immediately above.
    Reading starts at read_from_offset and writing starts at write_from_offset, and bytes_length bytes are written. """
    return [f"    ^({write_from_offset} <- {read_from_offset}, {bytes_length})"]


def get_write_offset(event_format, arg_index):
    """ Iterate over event format string to determine write offset of given argument index. """
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
    """ Converts argument to a boolean if it's 0 or 1; otherwise passes it through (e.g. for event args). """
    if isinstance(integer, int):
        if integer == 0:
            return False
        elif integer == 1:
            return True
    return integer


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


def get_game_map_name(area_id, block_id, game_module):
    """ Attempts to get the name of the game map. """
    try:
        area_id = int(area_id)
        block_id = int(block_id)
        return game_module.MAP_NAMES[(int(area_id), int(block_id))]
    except (ValueError, KeyError):
        # Event arg replacement(s) or unknown map. Return tuple instead, stripping quotes from any string elements.
        return f"({area_id}, {block_id})"


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


COMPARISON_NODES = {ast.Eq: 0, ast.NotEq: 1, ast.Gt: 2, ast.Lt: 3, ast.GtE: 4, ast.LtE: 5}
NEG_COMPARISON_NODES = {ast.Eq: 1, ast.NotEq: 0, ast.Gt: 5, ast.Lt: 4, ast.GtE: 3, ast.LtE: 2}
