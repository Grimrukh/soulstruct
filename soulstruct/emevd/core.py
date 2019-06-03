from enum import Enum


class EnumStringError(Exception):
    """ Indicates that a value expected to be found in an enum was a string, suggesting it is a placeholder arg. """
    pass


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


def resolve_flag_range(flag_range):
    try:
        first_flag = flag_range.first
        last_flag = flag_range.last
        return first_flag, last_flag
    except AttributeError:
        pass
    try:
        return flag_range[0], flag_range[1]
    except (IndexError, TypeError):
        raise ValueError("Flag range must be a FlagRange instance or pair of values (first, last).")


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
