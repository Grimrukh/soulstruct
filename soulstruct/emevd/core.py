from enum import Enum


class EnumStringError(Exception):
    """ Indicates that a value expected to be found in an enum was a string, suggesting it is a placeholder arg. """
    pass


class InstructionNotFoundError(Exception):
    """ Indicates that an instruction was not found in some code segment. """


INSTRUCTION_ARG_TYPES = {}


def set_instruction_arg_types(arg_type_dict):
    global INSTRUCTION_ARG_TYPES
    INSTRUCTION_ARG_TYPES = arg_type_dict


def numeric_instruction(instruction_info, *args, arg_types=None):
    """ Instruction info should be (class, index, [defaults]), with defaults assumed all zeroes if absent. """
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
    return ['{}, {}'.format(event_id, restart_type)]


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
            raise ValueError('Invalid character {} in arg_types.'.format(c))
        args.append((get_write_offset(arg_types, i), c_size))
    return args


def load_arg(write_from_offset, read_from_offset, bytes_length):
    """ Loads bytes from event initialization arguments (see 0[00]) into the instruction immediately above.
    Reading starts at read_from_offset and writing starts at write_from_offset, and bytes_length bytes are written. """
    return ['    ^({} <- {}, {})'.format(write_from_offset, read_from_offset, bytes_length)]


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
