"""
author: grimrhapsody
"""

from enum import Enum
import math
from struct import unpack, pack
from .event_enums import *


""" HELPER FUNCTIONS """


def floatify(i):
    """ Convert an integer to a float. Useful for ambiguous data in the unpacked files. """
    h = hex(i)[2:]
    return unpack('!f', bytes.fromhex(h))[0]


def int_to_two_shorts(integer, unsigned=True):
    """ Converted an integer (unsigned by default) to two shorts. """
    if unsigned:
        return unpack('<HH', pack('<I', integer))
    else:
        return unpack('<hh', pack('<i', integer))


def two_shorts_to_int(short1, short2, unsigned=True):
    """ Converted two shorts (unsigned by default) to one integer. """
    if unsigned:
        return unpack('<I', pack('<HH', short1, short2))
    else:
        return unpack('<i', pack('<hh', short1, short2))


def shift_msb_coordinates(ry, distance, xyz=(0.0, 0.0, 0.0)):
    """ Shift an MSB entity with given x, z, ry coordinates forward or back. """
    ry_rad = math.radians(ry)
    delta_x = -distance * math.sin(ry_rad)
    delta_z = -distance * math.cos(ry_rad)
    return xyz[0] + delta_x, xyz[1], xyz[2] + delta_z


""" PRIVATE HELPER FUNCTIONS """


def format_instruction(event_format, *args):
    args = list(args)
    arg_loads = []
    for x in range(len(args)):
        if isinstance(args[x], Enum):
            args[x] = args[x].value
        elif isinstance(args[x], tuple):
            # Start offset and size of an event argument.
            write_offset = get_byte_offset(event_format[2], x)
            arg_loads.append('    ^({} <- {}, {})'.format(write_offset, args[x][0], args[x][1]))
            args[x] = 0

    return [' {}[{}] ({}){}'.format(*event_format, args)] + arg_loads


def bint(bool_value):
    if isinstance(bool_value, int):
        return 1 if bool_value else 0
    return bool_value


def get_byte_offset(event_format, x):
    """ Iterate over event format string to determine write offset of x. """
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

        if i == x:
            return offset

        if c in 'Bb':
            offset += 1
        elif c in 'Hh':
            offset += 2
        elif c in 'Iif':
            offset += 4


def category_type(type_string):
    if type_string.lower() == 'object':
        return 0
    if type_string.lower() == 'region':
        return 1
    if type_string.lower() == 'character':
        return 2


""" EVENT MANAGEMENT """


def header(event_id, restart_type=0):
    """ restart_type:
        0: Event will run once on map load.
        1: Event will run again if you rest at a bonfire.
        2: Unknown - only used for reassembling skeletons.
    """
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
        args.append((get_byte_offset(arg_types, i), c_size))
    return args


def load_arg(write_from_offset, read_from_offset, bytes_length):
    """ Aiming to make this unnecessary. """
    # Loads bytes from event initialization arguments (see 0[00]) into the
    # instruction immediately above. Reading starts at read_from_offset and
    # writing starts at write_from_offset, and bytes_length bytes are written.
    return['    ^({} <- {}, {})'.format(write_from_offset, read_from_offset, bytes_length)]


""" 2000: SYSTEM """


# 0
def run_event(event_id, args=(0,), arg_types='I'):
    # Initializes event_id in slot 0 with event_args.
    return run_event_with_slot(event_id, 0, args=args, arg_types=arg_types)


def run_event_with_slot(event_id, event_slot_number=0, args=(0,), arg_types=None):
    # Initializes event_id in event_slot_number (used to distinguish
    # copies of the same event) and passes a variable number of args
    # depending on the event.
    if arg_types is None:
        arg_types = 'i' * len(args)  # Default is all-integer arguments.
    if len(args) != len(arg_types):
        raise ValueError("Number of event arguments does not match length of argument type string.")
    event_format = ['2000', '00', 'iI']
    event_format[2] += '{}'.format(arg_types[0])
    if len(arg_types) > 1:
        event_format[2] += '|{}'.format(arg_types[1:])
    return format_instruction(event_format, event_slot_number, event_id, *args)


""" 1000: EXECUTION CONTROL (SYSTEM) """


# 1
def skip_if_condition_true(number_lines, condition):
    # Skips some number of lines if the condition is true.
    # Default condition is MAIN.
    return skip_if_condition_state(number_lines, 1, condition)


def skip_if_condition_false(number_lines, condition):
    # Skips some number of lines if the condition is false.
    # Default condition is MAIN.
    return skip_if_condition_state(number_lines, 0, condition)


def skip_if_condition_state(number_lines, required_state, condition):
    # Skips some number of lines if the specified condition has the specified
    # state.
    """
    Condition values can be found within the event_enums.execution_condition enum
    (execution_condition.main, execution_condition.and1, execution_condition.or1, etc)
    OR, alternatively, as constants found directly within event_enums (MAIN, AND1, OR1, etc)
    """
    event_format = ['1000', '01', 'BBb']
    return format_instruction(event_format, number_lines, required_state, condition)


# 2
def restart_if_condition_true(condition=0):
    # Restart the event if the condition is true.
    # Default condition is MAIN.
    return terminate_if_condition_state(1, 1, condition)


def restart_if_condition_false(condition=0):
    # Restart the event if the condition is false.
    # Default condition is MAIN.
    return terminate_if_condition_state(1, 0, condition)


def end_if_condition_true(condition=0):
    # End (not restart) the event if the condition is true.
    # Default condition is MAIN.
    return terminate_if_condition_state(0, 1, condition)


def end_if_condition_false(condition=0):
    # End (not restart) the event if the condition is false.
    # Default condition is MAIN.
    return terminate_if_condition_state(0, 0, condition)


def terminate_if_condition_state(event_end_type, required_state, condition):
    event_format = ['1000', '02', 'BBb']
    return format_instruction(event_format, event_end_type, required_state, condition)


# 3
def skip(number_lines):
    # Unconditional line skip.
    event_format = ['1000', '03', 'B']
    return format_instruction(event_format, number_lines)


# 4
def restart():
    # Unconditional event restart.
    return terminate(1)


def end():
    # Unconditional event end (no restart).
    return terminate(0)


def terminate(event_end_type):
    # Unconditional event termination (1 = restart).
    event_format = ['1000', '04', 'B']
    return format_instruction(event_format, event_end_type)


# 5
def skip_if_equal(number_lines, left, right):
    return skip_if_value_comparison(number_lines, 0, left, right)


def skip_if_not_equal(number_lines, left, right):
    return skip_if_value_comparison(number_lines, 1, left, right)


def skip_if_greater_than(number_lines, left, right):
    return skip_if_value_comparison(number_lines, 2, left, right)


def skip_if_less_than(number_lines, left, right):
    return skip_if_value_comparison(number_lines, 3, left, right)


def skip_if_greater_than_or_equal(number_lines, left, right):
    return skip_if_value_comparison(number_lines, 4, left, right)


def skip_if_less_than_or_equal(number_lines, left, right):
    return skip_if_value_comparison(number_lines, 5, left, right)


def skip_if_value_comparison(number_lines, comparison_type, left, right):
    # Skips some number of lines if the specified (ordered) comparison is true.
    """
    Comparison types:
        0: "==",
        1: "!=",
        2: ">",
        3: "<",
        4: ">=",
        5: "<="
    """
    event_format = ['1000', '05', 'Bbii']
    return format_instruction(event_format, number_lines, comparison_type, left, right)


# 6
def end_if_equal(left, right):
    return terminate_if_value_comparison(0, 0, left, right)


def end_if_not_equal(left, right):
    return terminate_if_value_comparison(0, 1, left, right)


def end_if_greater_than(left, right):
    return terminate_if_value_comparison(0, 2, left, right)


def end_if_less_than(left, right):
    return terminate_if_value_comparison(0, 3, left, right)


def end_if_greater_than_or_equal(left, right):
    return terminate_if_value_comparison(0, 4, left, right)


def end_if_less_than_or_equal(left, right):
    return terminate_if_value_comparison(0, 5, left, right)


def restart_if_equal(left, right):
    return terminate_if_value_comparison(1, 0, left, right)


def restart_if_not_equal(left, right):
    return terminate_if_value_comparison(1, 1, left, right)


def restart_if_greater_than(left, right):
    return terminate_if_value_comparison(1, 2, left, right)


def restart_if_less_than(left, right):
    return terminate_if_value_comparison(1, 3, left, right)


def restart_if_greater_than_or_equal(left, right):
    return terminate_if_value_comparison(1, 4, left, right)


def restart_if_less_than_or_equal(left, right):
    return terminate_if_value_comparison(1, 5, left, right)


def terminate_if_value_comparison(event_end_type, comparison_type, left, right):
    # Terminates if some number of lines if the specified (ordered) comparison
    # is true (0 = end, 1 = restart).
    """
    Comparison types:
        0: "==",
        1: "!=",
        2: ">",
        3: "<",
        4: ">=",
        5: "<="
    """
    event_format = ['1000', '06', 'Bbii']
    return format_instruction(event_format, event_end_type, comparison_type, left, right)


# 7
def skip_if_condition_true_finished(number_lines, condition):
    # Default condition is MAIN.
    return skip_if_condition_state_finished(number_lines, 1, condition)


def skip_if_condition_false_finished(number_lines, condition):
    # Default condition is MAIN.
    return skip_if_condition_state_finished(number_lines, 0, condition)


def skip_if_condition_state_finished(number_lines, required_state, condition):
    # This command is used instead of 1000[01] when conditions are being
    # checked *after* they have already been uploaded into the MAIN
    # condition. For example, you might want to continue MAIN if either AND(01)
    # or AND(02) are true, but then afterwards, act conditionally on exactly
    # which one of those two registers caused you to continue.
    event_format = ['1000', '07', 'BBb']
    return format_instruction(event_format, number_lines, required_state, condition)


# 8
def restart_if_condition_true_finished(condition=0):
    # Restart the event if the condition is true.
    # Default condition is MAIN.
    return terminate_if_condition_state_finished(1, 1, condition)


def restart_if_condition_false_finished(condition=0):
    # Restart the event if the condition is false.
    # Default condition is MAIN.
    return terminate_if_condition_state_finished(1, 0, condition)


def end_if_condition_true_finished(condition=0):
    # End (not restart) the event if the condition is true.
    # Default condition is MAIN.
    return terminate_if_condition_state_finished(0, 1, condition)


def end_if_condition_false_finished(condition=0):
    # End (not restart) the event if the condition is true.
    # Default condition is MAIN.
    return terminate_if_condition_state_finished(0, 0, condition)


def terminate_if_condition_state_finished(event_end_type, required_state, condition):
    """ A 'finished' condition is one that has already been registered with MAIN
    (directly or indirectly). """
    event_format = ['1000', '08', 'BBb']
    return format_instruction(event_format, event_end_type, required_state, condition)


# 9
def wait_for_network_approval(timeout):
    # Wait for network to approve event (up to `timeout` seconds).
    event_format = ['1000', '09', 'f']
    return format_instruction(event_format, timeout)


""" 1001: EXECUTION CONTROL (TIMER) """


# 0
def wait(number_seconds):
    # Wait for some number of seconds.
    event_format = ['1001', '00', 'f']
    return format_instruction(event_format, number_seconds)


# 1
def wait_frames(number_frames):
    # Wait for some number of frames.
    event_format = ['1001', '01', 'i']
    return format_instruction(event_format, number_frames)


# 2
def wait_random_seconds(min_number_seconds, max_number_seconds):
    # Wait for a random number of seconds between min and max. I assume the
    # distribution is inclusive and uniform.
    event_format = ['1001', '02', 'ff']
    return format_instruction(event_format, min_number_seconds, max_number_seconds)


""" 1003: EXECUTION CONTROL (EVENT) """


# 1
def skip_if_this_event_on(number_lines):
    return skip_if_event_flag_state(number_lines, 1, FlagType.event, 0)


def skip_if_this_event_slot_on(number_lines):
    return skip_if_event_flag_state(number_lines, 1, FlagType.event_with_slot, 0)


def skip_if_this_event_off(number_lines):
    return skip_if_event_flag_state(number_lines, 0, FlagType.event, 0)


def skip_if_this_event_slot_off(number_lines):
    return skip_if_event_flag_state(number_lines, 0, FlagType.event_with_slot, 0)


def skip_if_event_flag_on(number_lines, event_flag_id, event_flag_type: FlagType = FlagType.event_flag):
    return skip_if_event_flag_state(number_lines, 1, event_flag_type, event_flag_id)


def skip_if_event_flag_off(number_lines, event_flag_id, event_flag_type: FlagType = FlagType.event_flag):
    return skip_if_event_flag_state(number_lines, 0, event_flag_type, event_flag_id)


def skip_if_event_flag_state(number_lines, required_flag_state, event_flag_type: FlagType, event_flag_id):
    # Skip some number of instructions if the specified flag has the specified
    # state (0 = off, 1 = on).
    event_format = ['1003', '01', 'BBBi']
    return format_instruction(event_format, number_lines, required_flag_state, event_flag_type, event_flag_id)


# 2
def end_if_this_event_slot_on():
    return terminate_if_event_flag_state(0, 1, FlagType.event_with_slot, 0)


def end_if_this_event_slot_off():
    return terminate_if_event_flag_state(0, 0, FlagType.event_with_slot, 0)


def end_if_this_event_on():
    return terminate_if_event_flag_state(0, 1, FlagType.event, 0)


def end_if_this_event_off():
    return terminate_if_event_flag_state(0, 0, FlagType.event, 0)


def end_if_event_flag_on(event_flag_id, event_flag_type: FlagType = FlagType.event_flag):
    return terminate_if_event_flag_state(0, 1, event_flag_type, event_flag_id)


def end_if_event_flag_off(event_flag_id, event_flag_type: FlagType = FlagType.event_flag):
    return terminate_if_event_flag_state(0, 0, event_flag_type, event_flag_id)


def restart_if_this_event_slot_on():
    return terminate_if_event_flag_state(1, 1, FlagType.event_with_slot, 0)


def restart_if_this_event_slot_off():
    return terminate_if_event_flag_state(1, 0, FlagType.event_with_slot, 0)


def restart_if_this_event_on():
    return terminate_if_event_flag_state(1, 1, FlagType.event, 0)


def restart_if_this_event_off():
    return terminate_if_event_flag_state(1, 0, FlagType.event, 0)


def restart_if_event_flag_on(event_flag_id, event_flag_type: FlagType = FlagType.event_flag):
    return terminate_if_event_flag_state(1, 1, event_flag_type, event_flag_id)


def restart_if_event_flag_off(event_flag_id, event_flag_type: FlagType = FlagType.event_flag):
    return terminate_if_event_flag_state(1, 0, event_flag_type, event_flag_id)


def terminate_if_event_flag_state(event_end_type, required_flag_state, event_flag_type: FlagType, event_flag_id):
    # Terminate (end or restart) event if the specified flag has the specified
    # state (0 = off, 1 = on).
    event_format = ['1003', '02', 'BBBi']
    return format_instruction(event_format, event_end_type, required_flag_state, event_flag_type, event_flag_id)


# 3
def skip_if_event_flag_range_all_on(number_lines, start_event_flag_id, end_event_flag_id,
                                    event_flag_type: FlagType = FlagType.event_flag):
    return skip_if_event_flag_range_state(number_lines, 0, event_flag_type, start_event_flag_id, end_event_flag_id)


def skip_if_event_flag_range_all_off(number_lines, start_event_flag_id, end_event_flag_id,
                                     event_flag_type: FlagType = FlagType.event_flag):
    return skip_if_event_flag_range_state(number_lines, 1, event_flag_type, start_event_flag_id, end_event_flag_id)


def skip_if_event_flag_range_not_all_off(number_lines, start_event_flag_id, end_event_flag_id,
                                         event_flag_type: FlagType = FlagType.event_flag):
    return skip_if_event_flag_range_state(number_lines, 2, event_flag_type, start_event_flag_id, end_event_flag_id)


def skip_if_event_flag_range_not_all_on(number_lines, start_event_flag_id, end_event_flag_id,
                                        event_flag_type: FlagType = FlagType.event_flag):
    return skip_if_event_flag_range_state(number_lines, 3, event_flag_type, start_event_flag_id, end_event_flag_id)


def skip_if_event_flag_range_state(number_lines, required_flag_state, event_flag_type: FlagType, start_event_flag_id,
                                   end_event_flag_id):
    # Skip some number of instructions if the specified range of flags all have
    # the specified state (0 = off, 1 = on).
    """
    Event flag type list:
        0: "Event Flag ID",
        1: "Event ID",
        2: "Event ID with Slot Number"
    """
    event_format = ['1003', '03', 'BBBii']
    return format_instruction(event_format, number_lines, required_flag_state, event_flag_type, start_event_flag_id,
                              end_event_flag_id)


# 4
def end_if_event_flag_range_all_on(start_event_flag_id, end_event_flag_id,
                                   event_flag_type: FlagType = FlagType.event_flag):
    return terminate_if_event_flag_range_state(0, 0, event_flag_type, start_event_flag_id, end_event_flag_id)


def end_if_event_flag_range_all_off(start_event_flag_id, end_event_flag_id,
                                    event_flag_type: FlagType = FlagType.event_flag):
    return terminate_if_event_flag_range_state(0, 1, event_flag_type, start_event_flag_id, end_event_flag_id)


def end_if_event_flag_range_not_all_off(start_event_flag_id, end_event_flag_id,
                                        event_flag_type: FlagType = FlagType.event_flag):
    return terminate_if_event_flag_range_state(0, 2, event_flag_type, start_event_flag_id, end_event_flag_id)


def end_if_event_flag_range_not_all_on(start_event_flag_id, end_event_flag_id,
                                       event_flag_type: FlagType = FlagType.event_flag):
    return terminate_if_event_flag_range_state(0, 3, event_flag_type, start_event_flag_id, end_event_flag_id)


def restart_if_event_flag_range_all_off(start_event_flag_id, end_event_flag_id,
                                        event_flag_type: FlagType = FlagType.event_flag):
    return terminate_if_event_flag_range_state(1, 0, event_flag_type, start_event_flag_id, end_event_flag_id)


def restart_if_event_flag_range_all_on(start_event_flag_id, end_event_flag_id,
                                       event_flag_type: FlagType = FlagType.event_flag):
    return terminate_if_event_flag_range_state(1, 1, event_flag_type, start_event_flag_id, end_event_flag_id)


def restart_if_event_flag_range_not_all_off(start_event_flag_id, end_event_flag_id,
                                            event_flag_type: FlagType = FlagType.event_flag):
    return terminate_if_event_flag_range_state(1, 3, event_flag_type, start_event_flag_id, end_event_flag_id)


def restart_if_event_flag_range_not_all_on(start_event_flag_id, end_event_flag_id,
                                           event_flag_type: FlagType = FlagType.event_flag):
    return terminate_if_event_flag_range_state(1, 2, event_flag_type, start_event_flag_id, end_event_flag_id)


def terminate_if_event_flag_range_state(event_end_type, required_flag_state, event_flag_type: FlagType,
                                        start_event_flag_id, end_event_flag_id):
    # Terminate (end or restart) event if the specified range of flags have
    # the specified state (0 = all off, 1 = all on, 2 = not all on, 3 = not all off).
    event_format = ['1003', '04', 'BBBii']
    return format_instruction(event_format, event_end_type, required_flag_state, event_flag_type, start_event_flag_id,
                              end_event_flag_id)


# 5
def skip_if_host(number_lines):
    return skip_if_multiplayer_state(number_lines, 0)


def skip_if_client(number_lines):
    return skip_if_multiplayer_state(number_lines, 1)


def skip_if_multiplayer(number_lines):
    return skip_if_multiplayer_state(number_lines, 2)


def skip_if_singleplayer(number_lines):
    return skip_if_multiplayer_state(number_lines, 3)


def skip_if_multiplayer_state(number_lines, required_multiplayer_state):
    # Skip some number of lines if the player has the specified multiplayer
    # state.
    """
    Multiplayer state list:
        0: "Host" (owner of world)
        1: "Client" (summon, not invader)
        2: "Multiplayer" (either has a client or is a client I believe)
        3: "Singleplayer" (host with no client)
    """
    event_format = ['1003', '05', 'Bb']
    return format_instruction(event_format, number_lines, required_multiplayer_state)


# 6
def end_if_host():
    return terminate_if_multiplayer_state(0, 0)


def end_if_client():
    return terminate_if_multiplayer_state(0, 1)


def end_if_multiplayer():
    return terminate_if_multiplayer_state(0, 2)


def end_if_singleplayer():
    return terminate_if_multiplayer_state(0, 3)


def restart_if_host():
    return terminate_if_multiplayer_state(1, 0)


def restart_if_client():
    return terminate_if_multiplayer_state(1, 1)


def restart_if_multiplayer():
    return terminate_if_multiplayer_state(1, 2)


def restart_if_singleplayer():
    return terminate_if_multiplayer_state(1, 3)


def terminate_if_multiplayer_state(event_end_type, required_multiplayer_state):
    # Terminate event (end or restart) if the player has the specified
    # multiplayer state.
    """
    Multiplayer state list:
        0: "Host" (owner of world)
        1: "Client" (summon, not invader)
        2: "Multiplayer" (either has a client or is a client I believe)
        3: "Singleplayer" (host with no client)
    """
    event_format = ['1003', '06', 'Bb']
    return format_instruction(event_format, event_end_type, required_multiplayer_state)


# 7
def skip_if_inside_area(number_lines, area_id, block_id):
    return skip_if_area_state(number_lines, 1, area_id, block_id)


def skip_if_outside_area(number_lines, area_id, block_id):
    return skip_if_area_state(number_lines, 0, area_id, block_id)


def skip_if_area_state(number_lines, required_area_state, area_id, block_id):
    # Skip some number of lines if the player is outside (0) or inside (1) the
    # specified area and block.
    event_format = ['1003', '07', 'BBBB']
    return format_instruction(event_format, number_lines, bint(required_area_state), area_id, block_id)


# 8
def end_if_inside_map(area_id, block_id):
    # TODO: This is a guess.
    return terminate_if_area_state(0, 1, area_id, block_id)


def end_if_outside_map(area_id, block_id):
    # TODO: This is a guess.
    return terminate_if_area_state(0, 0, area_id, block_id)


def restart_if_inside_map(area_id, block_id):
    # TODO: This is a guess.
    return terminate_if_area_state(1, 1, area_id, block_id)


def restart_if_outside_map(area_id, block_id):
    # TODO: This is a guess.
    return terminate_if_area_state(1, 0, area_id, block_id)


def terminate_if_area_state(event_end_type, required_area_state, area_id, block_id):
    # Terminates (ends or restarts) the event if the specified object has the
    # specified destruction state. Guessing that 1 = destroyed.
    # TODO: Confirm bool.
    event_format = ['1003', '08', 'BBBB']
    return format_instruction(event_format, event_end_type, bint(required_area_state), area_id, block_id)


""" 1005: EXECUTION CONTROL (OBJECT) """


# 1
def skip_if_object_destroyed(number_lines, entity_id):
    # TODO: The bool is a guess right now.
    return skip_if_object_destruction_state(number_lines, 1, entity_id)


def skip_if_object_not_destroyed(number_lines, entity_id):
    # TODO: The bool is a guess right now.
    return skip_if_object_destruction_state(number_lines, 0, entity_id)


def skip_if_object_destruction_state(number_lines, required_destruction_state, entity_id):
    # Skips some number of lines if the specified object has the specified
    # destruction state. I can't actually find this enum, so it's actually hard
    # to guess if 0 = destroyed or 1 = destroyed. I assume the latter, but only
    # tentatively (because it's the default).
    # TODO: Check usage to figure out state bool.
    event_format = ['1005', '01', 'BBi']
    return format_instruction(event_format, number_lines, required_destruction_state, entity_id)


# 2
def end_if_object_destroyed(entity_id):
    # TODO: This is a guess.
    return terminate_if_object_destruction_state(0, 1, entity_id)


def end_if_object_not_destroyed(entity_id):
    # TODO: This is a guess.
    return terminate_if_object_destruction_state(0, 0, entity_id)


def restart_if_object_destroyed(entity_id):
    # TODO: This is a guess.
    return terminate_if_object_destruction_state(1, 1, entity_id)


def restart_if_object_not_destroyed(entity_id):
    # TODO: This is a guess.
    return terminate_if_object_destruction_state(1, 0, entity_id)


def terminate_if_object_destruction_state(event_end_type, required_destruction_state, entity_id):
    # Terminates (ends or restarts) the event if the specified object has the
    # specified destruction state. Guessing that 1 = destroyed.
    # TODO: Confirm bool.
    event_format = ['1005', '02', 'BBi']
    return format_instruction(event_format, event_end_type, required_destruction_state, entity_id)


""" 0: EXECUTION CONDITIONS (SYSTEM) """


# 0
def if_condition_true(output_condition, input_condition):
    return if_condition_state(output_condition, 1, input_condition)


def if_condition_false(output_condition, input_condition):
    return if_condition_state(output_condition, 0, input_condition)


def if_condition_state(output_condition, required_result, input_condition):
    # Evaluates the input condition (as OR or AND), compares it to the
    # required result, and stores the result of the comparison in the output
    # condition (where many values can be stored).
    # The required result is 1 by default, which means that the output condition
    # will simply store the evaluation of the input.
    event_format = ['   0', '00', 'bBb']
    return format_instruction(event_format, output_condition, required_result, input_condition)


""" 1: EXECUTION CONDITIONS (TIME) """


# 0
def if_time_elapsed(output_condition, number_seconds):
    # Counts seconds since event started (I think).
    # TODO: Confirm time since event started.
    event_format = ['   1', '00', 'bf']
    return format_instruction(event_format, output_condition, number_seconds)


# 1
def if_frames_elapsed(output_condition, number_frames):
    # TODO: Confirm number of frames since event started.
    event_format = ['   1', '01', 'bi']
    return format_instruction(event_format, output_condition, number_frames)


# 2 and 3 choose a random number of seconds/frames, I think, but unused.

""" 3: EXECUTION CONDITIONS (EVENT) """


# 0
def if_this_event_on(output_condition):
    return if_event_flag_state(output_condition, 1, FlagType.event, 0)


def if_this_event_off(output_condition):
    return if_event_flag_state(output_condition, 0, FlagType.event, 0)


def if_this_event_slot_on(output_condition):
    return if_event_flag_state(output_condition, 1, FlagType.event_with_slot, 0)


def if_this_event_slot_off(output_condition):
    return if_event_flag_state(output_condition, 0, FlagType.event_with_slot, 0)


def if_event_flag_on(output_condition, event_flag_id, event_flag_type: FlagType = FlagType.event_flag):
    return if_event_flag_state(output_condition, 1, event_flag_type, event_flag_id)


def if_event_flag_off(output_condition, event_flag_id, event_flag_type: FlagType = FlagType.event_flag):
    return if_event_flag_state(output_condition, 0, event_flag_type, event_flag_id)


def if_event_flag_state(output_condition, required_flag_state, event_flag_type, event_flag_id):
    event_format = ['   3', '00', 'bBBi']
    return format_instruction(event_format, output_condition, required_flag_state, event_flag_type, event_flag_id)


# 1
def if_event_flag_range_all_on(output_condition, start_event_flag_id, end_event_flag_id,
                               event_flag_type: FlagType = FlagType.event_flag):
    return if_event_flag_range_state(output_condition, 0, event_flag_type, start_event_flag_id, end_event_flag_id)


def if_event_flag_range_all_off(output_condition, start_event_flag_id, end_event_flag_id,
                                event_flag_type: FlagType = FlagType.event_flag):
    return if_event_flag_range_state(output_condition, 1, event_flag_type, start_event_flag_id, end_event_flag_id)


def if_event_flag_range_not_all_off(output_condition, start_event_flag_id, end_event_flag_id,
                                    event_flag_type: FlagType = FlagType.event_flag):
    return if_event_flag_range_state(output_condition, 2, event_flag_type, start_event_flag_id, end_event_flag_id)


def if_event_flag_range_not_all_on(output_condition, start_event_flag_id, end_event_flag_id,
                                   event_flag_type: FlagType = FlagType.event_flag):
    return if_event_flag_range_state(output_condition, 3, event_flag_type, start_event_flag_id, end_event_flag_id)


def if_event_flag_range_state(output_condition, required_flag_state, event_flag_type: FlagType, start_event_flag_id,
                              end_event_flag_id):
    event_format = ['   3', '01', 'bBBii']
    return format_instruction(event_format, output_condition, required_flag_state, event_flag_type, start_event_flag_id,
                              end_event_flag_id)


# 2
def if_entity_inside_region(output_condition, entity_id, region_id):
    return if_entity_inside_or_outside_region(output_condition, entity_id, region_id, 1)


def if_entity_outside_region(output_condition, entity_id, region_id):
    return if_entity_inside_or_outside_region(output_condition, entity_id, region_id, 0)


def if_player_inside_region(output_condition, region_id):
    return if_entity_inside_or_outside_region(output_condition, 10000, region_id, 1)


def if_player_outside_region(output_condition, region_id):
    return if_entity_inside_or_outside_region(output_condition, 10000, region_id, 0)


def if_entity_inside_or_outside_region(output_condition, entity_id, region_id, is_inside):
    # Checks if specified entity is inside or outside specified area.
    # 0 = outside, 1 = inside.
    # Note that argument order has changed.
    event_format = ['   3', '02', 'bBii']
    return format_instruction(event_format, output_condition, bint(is_inside), entity_id, region_id)


# 3
def if_player_within_distance(output_condition, target_entity_id, required_distance):
    return if_entity_within_or_beyond_distance(output_condition, 10000, target_entity_id, required_distance, 1)


def if_player_beyond_distance(output_condition, target_entity_id, required_distance):
    return if_entity_within_or_beyond_distance(output_condition, 10000, target_entity_id, required_distance, 0)


def if_entity_within_distance(output_condition, first_entity_id, second_entity_id, required_distance):
    return if_entity_within_or_beyond_distance(output_condition, first_entity_id, second_entity_id, required_distance,
                                               1)


def if_entity_beyond_distance(output_condition, first_entity_id, second_entity_id, required_distance):
    return if_entity_within_or_beyond_distance(output_condition, first_entity_id, second_entity_id, required_distance,
                                               0)


def if_entity_within_or_beyond_distance(output_condition, first_entity_id, second_entity_id, required_distance,
                                        is_within):
    # Check is entity A is within (is_within == True) or beyond the specified
    # distance of entity B. Works for characters and objects, at the least. Not sure about regions.
    event_format = ['   3', '03', 'bBiif']
    return format_instruction(event_format, output_condition, bint(is_within), first_entity_id, second_entity_id,
                              required_distance)


# 4
def if_player_has_good(output_condition, item_id):
    return if_player_has_item(output_condition, ItemType.good, item_id)


def if_player_has_ring(output_condition, item_id):
    return if_player_has_item(output_condition, ItemType.ring, item_id)


def if_player_has_weapon(output_condition, item_id):
    return if_player_has_item(output_condition, ItemType.weapon, item_id)


def if_player_has_armor(output_condition, item_id):
    return if_player_has_item(output_condition, ItemType.armor, item_id)


def if_player_does_not_have_good(output_condition, item_id):
    return if_player_does_not_have_item(output_condition, ItemType.good, item_id)


def if_player_does_not_have_ring(output_condition, item_id):
    return if_player_does_not_have_item(output_condition, ItemType.ring, item_id)


def if_player_does_not_have_weapon(output_condition, item_id):
    return if_player_does_not_have_item(output_condition, ItemType.weapon, item_id)


def if_player_does_not_have_armor(output_condition, item_id):
    return if_player_does_not_have_item(output_condition, ItemType.armor, item_id)


def if_player_has_item(output_condition, item_type, item_id):
    return if_player_has_or_does_not_have_item(output_condition, item_type, item_id, 1)


def if_player_does_not_have_item(output_condition, item_type, item_id):
    return if_player_has_or_does_not_have_item(output_condition, item_type, item_id, 0)


def if_player_has_or_does_not_have_item(output_condition, item_type, item_id, required_state):
    # Check if player has specified item in inventory, not including Bottomless
    # Box (required_state == True) or does not have the item (required_state == False).
    event_format = ['   3', '04', 'bBiB']
    return format_instruction(event_format, output_condition, item_type, item_id, bint(required_state))


# 5

def if_action_button_in_region(output_condition, region, prompt_text, reaction_attribute=48,
                               pad_id=0, line_intersects=None, boss_version=False):
    if boss_version:
        if line_intersects is None:
            if_action_button_state_in_boss(output_condition, Category.region, region, 0.0, -1, 0.0,
                                           prompt_text, reaction_attribute, pad_id)
        else:
            if_action_button_state_and_line_segment_in_boss(output_condition, Category.region, region, 0.0, -1, 0.0,
                                                            prompt_text, reaction_attribute, pad_id, line_intersects)
    else:
        if line_intersects is None:
            if_action_button_state(output_condition, Category.region, region, 0.0, -1, 0.0,
                                   prompt_text, reaction_attribute, pad_id)
        else:
            if_action_button_state_and_line_segment(output_condition, Category.region, region, 0.0, -1, 0.0,
                                                    prompt_text, reaction_attribute, pad_id, line_intersects)


def if_action_button_state(output_condition, category, target_entity_id, reaction_angle,
                           damipoly_id, reaction_distance, help_id, reaction_attribute=48, pad_id=0):
    if isinstance(category, str):
        category = category_type(category)
    event_format = ['   3', '05', 'biifhfiBi']
    return format_instruction(event_format, output_condition, category, target_entity_id, reaction_angle, damipoly_id,
                              reaction_distance, help_id, reaction_attribute, pad_id)


# 6
def if_host(output_condition):
    return if_multiplayer_state(output_condition, 0)


def if_client(output_condition):
    return if_multiplayer_state(output_condition, 1)


def if_multiplayer(output_condition):
    return if_multiplayer_state(output_condition, 2)


def if_singleplayer(output_condition):
    return if_multiplayer_state(output_condition, 3)


def if_multiplayer_state(output_condition, required_state):
    # Check if player is host (0), summon (1), multiplayer (2), or
    # single player (3).
    event_format = ['   3', '06', 'bb']
    return format_instruction(event_format, output_condition, required_state)


# 7
def if_all_players_inside_region(output_condition, region):
    return if_all_players_inside_or_outside_region(output_condition, region, 1)


def if_all_players_outside_region(output_condition, region):
    return if_all_players_inside_or_outside_region(output_condition, region, 0)


def if_all_players_inside_or_outside_region(output_condition, region, is_inside):
    # Check if all players are inside (1) or outside (0) the specified area.
    event_format = ['   3', '07', 'bBi']
    return format_instruction(event_format, output_condition, is_inside, region)


# 8
def if_in_world_area(output_condition, area_id, block_id):
    return if_world_area_state(output_condition, area_id, block_id, 1)


def if_not_in_world_area(output_condition, area_id, block_id):
    return if_world_area_state(output_condition, area_id, block_id, 0)


def if_world_area_state(output_condition, area_id, block_id, is_inside):
    # Check if player is inside or outside the specified world area and block.
    event_format = ['   3', '08', 'bBBB']
    return format_instruction(event_format, output_condition, bint(is_inside), area_id, block_id)


# 9
def if_multiplayer_event(output_condition, multiplayer_event_id):
    # Check if a multiplayer event has occurred.
    event_format = ['   3', '09', 'bI']
    return format_instruction(event_format, output_condition, multiplayer_event_id)


# 10
def if_at_least_one_true_flag_in_range(output_condition, start_event_flag_id, end_event_flag_id,
                                       event_flag_type=FlagType.event_flag):
    # Check if at least one flag in the specified range is true.
    return if_count_true_event_flags_in_range(output_condition, event_flag_type, start_event_flag_id, end_event_flag_id,
                                              4, 1)


def if_number_true_flags_in_range_equal(output_condition, start_event_flag_id, end_event_flag_id,
                                        count, event_flag_type=FlagType.event_flag):
    # Check if the number of true flags in the specified range is greater than
    # or equal to the specified minimum.
    return if_count_true_event_flags_in_range(output_condition, event_flag_type, start_event_flag_id, end_event_flag_id,
                                              0, count)


def if_number_true_flags_in_range_not_equal(output_condition, start_event_flag_id, end_event_flag_id,
                                            count, event_flag_type=FlagType.event_flag):
    # Check if the number of true flags in the specified range is greater than
    # or equal to the specified minimum.
    return if_count_true_event_flags_in_range(output_condition, event_flag_type, start_event_flag_id, end_event_flag_id,
                                              1, count)


def if_number_true_flags_in_range_greater_than(output_condition, start_event_flag_id, end_event_flag_id,
                                               count, event_flag_type=FlagType.event_flag):
    # Check if the number of true flags in the specified range is greater than
    # or equal to the specified minimum.
    return if_count_true_event_flags_in_range(output_condition, event_flag_type, start_event_flag_id, end_event_flag_id,
                                              2, count)


def if_number_true_flags_in_range_less_than(output_condition, start_event_flag_id, end_event_flag_id,
                                            count, event_flag_type=FlagType.event_flag):
    # Check if the number of true flags in the specified range is greater than
    # or equal to the specified minimum.
    return if_count_true_event_flags_in_range(output_condition, event_flag_type, start_event_flag_id, end_event_flag_id,
                                              3, count)


def if_number_true_flags_in_range_greater_than_or_equal(output_condition, start_event_flag_id, end_event_flag_id,
                                                        min_count, event_flag_type=FlagType.event_flag):
    # Check if the number of true flags in the specified range is greater than
    # or equal to the specified minimum.
    return if_count_true_event_flags_in_range(output_condition, event_flag_type, start_event_flag_id, end_event_flag_id,
                                              4, min_count)


def if_number_true_flags_in_range_less_than_or_equal(output_condition, start_event_flag_id, end_event_flag_id,
                                                     max_count, event_flag_type=FlagType.event_flag):
    # Check if the number of true flags in the specified range is greater than
    # or equal to the specified minimum.
    return if_count_true_event_flags_in_range(output_condition, event_flag_type, start_event_flag_id, end_event_flag_id,
                                              5, max_count)


def if_count_true_event_flags_in_range(output_condition, event_flag_type: FlagType, start_event_flag_id,
                                       end_event_flag_id, comparison_type, count_comparison):
    # Checks if the count of true flags in the specified range satisfies the
    # specified comparison (usually 4: >=) with the specified count.
    event_format = ['   3', '10', 'bBiibi']
    return format_instruction(event_format, output_condition, event_flag_type, start_event_flag_id, end_event_flag_id,
                              comparison_type, count_comparison)


# 11
def if_world_tendency_greater_than_or_equal(output_condition, tendency_type, min_tendency):
    return if_world_tendency_comparison(output_condition, tendency_type, 4, min_tendency)


def if_world_tendency_comparison(output_condition, tendency_type, comparison_type, tendency_comparison):
    # Check if comparison of world tendency with specified value is true.
    # tendency_type: 0 = white tendency, 1 = black tendency.
    event_format = ['   3', '11', 'bBBB']
    return format_instruction(event_format, output_condition, tendency_type, comparison_type, tendency_comparison)


# 12
def if_event_value_equal(output_condition, event_flag_id, number_bits, comparison_value):
    return if_event_value_comparison(output_condition, event_flag_id, number_bits, 0, comparison_value)


def if_event_value_greater_than(output_condition, event_flag_id, number_bits, comparison_value):
    return if_event_value_comparison(output_condition, event_flag_id, number_bits, 2, comparison_value)


def if_event_value_comparison(output_condition, event_flag_id, number_bits, comparison_type, comparison_value):
    # Check if specified bit in event value (usually 0 I think) compares true
    # with specified value.
    event_format = ['   3', '12', 'biBBI']
    return format_instruction(event_format, output_condition, event_flag_id, number_bits,
                              comparison_type, comparison_value)


# 13
def if_action_button_state_in_boss(output_condition, category, target_entity_id, reaction_angle, damipoly_id,
                                   reaction_distance, help_id, reaction_attribute, pad_id):
    # Checks state of action button (A on the Xbox controller). I assume this
    # one only applies in boss rooms. See if_action_button_state docs.
    event_format = ['   3', '13', 'biifhfiBi']
    return format_instruction(event_format, output_condition, category, target_entity_id, reaction_angle, damipoly_id,
                              reaction_distance, help_id, reaction_attribute, pad_id)


# 14
def if_any_item_dropped_in_region(output_condition, region_entity_id):
    # Check if any item has been dropped in the specified area.
    event_format = ['   3', '14', 'bi']
    return format_instruction(event_format, output_condition, region_entity_id)


# 15
def if_item_dropped(output_condition, item_type, item_id):
    # Check if a specified item has been dropped (anywhere).
    # Item type:
    #     0: Weapon
    #     1: Armor
    #     2: Ring
    #     3: Item
    event_format = ['   3', '15', 'bii']
    return format_instruction(event_format, output_condition, item_type, item_id)


# 16
def if_player_owns_good(output_condition, good):
    return if_player_owns_item(output_condition, ItemType.good, good)


def if_player_owns_ring(output_condition, ring):
    return if_player_owns_item(output_condition, ItemType.ring, ring)


def if_player_owns_weapon(output_condition, weapon):
    return if_player_owns_item(output_condition, ItemType.weapon, weapon)


def if_player_owns_armor(output_condition, armor):
    return if_player_owns_item(output_condition, ItemType.armor, armor)


def if_player_does_not_own_good(output_condition, good):
    return if_player_does_not_own_item(output_condition, ItemType.good, good)


def if_player_does_not_own_ring(output_condition, ring):
    return if_player_does_not_own_item(output_condition, ItemType.ring, ring)


def if_player_does_not_own_weapon(output_condition, weapon):
    return if_player_does_not_own_item(output_condition, ItemType.weapon, weapon)


def if_player_does_not_own_armor(output_condition, armor):
    return if_player_does_not_own_item(output_condition, ItemType.armor, armor)


def if_player_owns_item(output_condition, item_type, item_id):
    # Includes Bottomless Box.
    return if_player_does_or_does_not_own_item(output_condition, item_type, item_id, 1)


def if_player_does_not_own_item(output_condition, item_type, item_id):
    # Includes Bottomless Box.
    return if_player_does_or_does_not_own_item(output_condition, item_type, item_id, 0)


def if_player_does_or_does_not_own_item(output_condition, item_type, item_id, owns_item):
    event_format = ['   3', '16', 'bBiB']
    return format_instruction(event_format, output_condition, item_type, item_id, owns_item)


# 17
def if_new_game_count_equal(output_condition, completion_count_comparison):
    # Checks if count of completed playthroughs is equal to some value.
    return if_new_game_count_comparison(output_condition, 0, completion_count_comparison)


def if_new_game_count_greater_than_or_equal(output_condition, min_completion_count):
    # Checks if count of completed playthroughs is greater than or equal to some value.
    return if_new_game_count_comparison(output_condition, 4, min_completion_count)


def if_new_game_count_comparison(output_condition, comparison_type, completion_count_comparison):
    # Checks count of completed playthroughs and compares to value.
    event_format = ['   3', '17', 'bBB']
    return format_instruction(event_format, output_condition, comparison_type, completion_count_comparison)


# 18
def if_action_button_state_and_line_segment(output_condition, category, target_entity_id, reaction_angle, damipoly_id,
                                            reaction_distance, help_id, reaction_attribute, pad_id,
                                            line_segment_endpoint_id):
    # Checks state of action button (A on the Xbox controller) and, I assume,
    # check if player forward line segment intersects entity?
    # TODO: Check usage of this.
    if isinstance(category, str):
        category = category_type(category)
    event_format = ['   3', '18', 'biifhfiBii']
    return format_instruction(event_format, output_condition, category, target_entity_id, reaction_angle, damipoly_id,
                              reaction_distance, help_id, reaction_attribute, pad_id, line_segment_endpoint_id)


# 19
def if_action_button_state_and_line_segment_in_boss(output_condition, category, target_entity_id, reaction_angle,
                                                    damipoly_id, reaction_distance, help_id, reaction_attribute, pad_id,
                                                    line_segment_endpoint_id):
    # Checks state of action button (A on the Xbox controller) and, I assume,
    # check if player forward line segment intersects entity? This is the boss
    # room version.
    if isinstance(category, str):
        category = category_type(category)
    event_format = ['   3', '19', 'biifhfiBii']
    return format_instruction(event_format, output_condition, category, target_entity_id, reaction_angle, damipoly_id,
                              reaction_distance, help_id, reaction_attribute, pad_id, line_segment_endpoint_id)


# 20
def if_event_flag_value_comparison(output_condition, left_event_flag_id, left_number_bits, comparison_type,
                                   right_event_flag_id, right_number_bits):
    # Check comparison of two event flag values.
    event_format = ['   3', '20', 'biBBiB']
    return format_instruction(event_format, output_condition, left_event_flag_id, left_number_bits, comparison_type,
                              right_event_flag_id, right_number_bits)


# 21
def if_owns_dlc(output_condition):
    # Check if player owns Artorias of the Abyss DLC expansion.
    # NOTE: Again, no generic function here.
    event_format = ['   3', '21', 'bB']
    return format_instruction(event_format, output_condition, 1)


def if_does_not_own_dlc(output_condition):
    # Check if player does not own Artorias of the Abyss DLC expansion.
    event_format = ['   3', '21', 'bB']
    return format_instruction(event_format, output_condition, 0)


# 22
def if_online(output_condition):
    return if_online_state(output_condition, 1)


def if_offline(output_condition):
    return if_online_state(output_condition, 0)


def if_online_state(output_condition, online_state):
    # Check if player is online (1) or offline (0).
    event_format = ['   3', '22', 'bB']
    return format_instruction(event_format, output_condition, online_state)


""" 4: EXECUTION CONDITIONS (CHARACTER) """


# 0
def if_entity_dead(output_condition, entity_id):
    return if_entity_death_state(output_condition, entity_id, 1)


def if_entity_alive(output_condition, entity_id):
    return if_entity_death_state(output_condition, entity_id, 0)


def if_entity_death_state(output_condition, entity_id, required_state):
    # Check if entity is alive (0) or dead (1).
    event_format = ['   4', '00', 'biB']
    return format_instruction(event_format, output_condition, entity_id, required_state)


# 1
def if_entity_attacked_by(output_condition, entity_id, attacking_entity_id):
    # Check if first entity has been attacked by the second entity.
    event_format = ['   4', '01', 'bii']
    return format_instruction(event_format, output_condition, entity_id, attacking_entity_id)


# 2
def if_entity_health_equal(output_condition, entity_id, health_comparison):
    # Check if entity health == value.
    return if_entity_health_comparison(output_condition, entity_id, 0, health_comparison)


def if_entity_health_not_equal(output_condition, entity_id, health_comparison):
    # Check if entity health != value.
    return if_entity_health_comparison(output_condition, entity_id, 1, health_comparison)


def if_entity_health_greater_than(output_condition, entity_id, health_comparison):
    # Check if entity health > value.
    return if_entity_health_comparison(output_condition, entity_id, 2, health_comparison)


def if_entity_health_less_than(output_condition, entity_id, health_comparison):
    # Check if entity health < value.
    return if_entity_health_comparison(output_condition, entity_id, 3, health_comparison)


def if_entity_health_greater_than_or_equal(output_condition, entity_id, health_comparison):
    # Check if entity health >= value.
    return if_entity_health_comparison(output_condition, entity_id, 4, health_comparison)


def if_entity_health_less_than_or_equal(output_condition, entity_id, health_comparison):
    # Check if entity health <= value.
    return if_entity_health_comparison(output_condition, entity_id, 5, health_comparison)


def if_entity_health_comparison(output_condition, entity_id, comparison_type, health_comparison):
    # Check comparison of entity health with specified value between 0 and 1.
    """
    Comparison type list:
        0: "==",
        1: "!=",
        2: ">",
        3: "<",
        4: ">=",
        5: "<="
    """
    event_format = ['   4', '02', 'bibf']
    return format_instruction(event_format, output_condition, entity_id, comparison_type, health_comparison)


# 3
def if_character_human(output_condition, entity_id):
    # Check if specified character entity is human ("Survival").
    return if_character_type(output_condition, entity_id, 0)


def if_character_hollow(output_condition, entity_id):
    # Check if specified character entity is hollow ("Gray Ghost").
    return if_character_type(output_condition, entity_id, 8)


def if_character_type(output_condition, entity_id, character_type):
    # Check if specified character entity is of given type.
    """
    Character type list:
        0: "Survival",
        1: "White Ghost",
        2: "Black Ghost",
        8: "Gray Ghost",
        12: "Intruder"
    """
    event_format = ['   4', '03', 'bib']
    return format_instruction(event_format, output_condition, entity_id, character_type)


# 4
def if_entity_targeting(output_condition, entity_id, targeted_entity_id):
    # Check if first entity is targeting second.
    return if_entity_target_state(output_condition, entity_id, targeted_entity_id, 1)


def if_entity_not_targeting(output_condition, entity_id, targeted_entity_id):
    # Check if first entity is not targeting second.
    return if_entity_target_state(output_condition, entity_id, targeted_entity_id, 0)


def if_entity_target_state(output_condition, entity_id, targeted_entity_id, required_target_state):
    # Check if first entity is (1) or is not (0) targeting the second entity.
    # Note this is HPR's speculation. Not sure if player target lock counts as
    # 'targeting' for this, or if it's just for NPC AI targets.
    event_format = ['   4', '04', 'biiB']
    return format_instruction(event_format, output_condition, entity_id, targeted_entity_id, required_target_state)


# 5
def if_player_has_special_effect(output_condition, special_effect_id):
    # Check if entity has specified special effect.
    return if_entity_special_effect_state(output_condition, 10000, special_effect_id, 1)


def if_player_does_not_have_special_effect(output_condition, special_effect_id):
    # Check if entity does not have specified special effect.
    return if_entity_special_effect_state(output_condition, 10000, special_effect_id, 0)


def if_entity_has_special_effect(output_condition, entity_id, special_effect_id):
    # Check if entity has specified special effect.
    return if_entity_special_effect_state(output_condition, entity_id, special_effect_id, 1)


def if_entity_does_not_have_special_effect(output_condition, entity_id, special_effect_id):
    # Check if entity does not have specified special effect.
    return if_entity_special_effect_state(output_condition, entity_id, special_effect_id, 0)


def if_entity_special_effect_state(output_condition, entity_id, special_effect_id, required_state):
    # Check if entity has (1) or doesn't have (0) specified special effect.
    event_format = ['   4', '05', 'biiB']
    return format_instruction(event_format, output_condition, entity_id, special_effect_id, required_state)


# 6
def if_body_part_health_less_than_or_equal(output_condition, entity_id, part_NPC_type, health_threshold):
    return if_body_part_health_comparison(output_condition, entity_id, part_NPC_type, health_threshold, 5)


def if_body_part_health_comparison(output_condition, entity_id, part_NPC_type, health_threshold, comparison_type):
    # Check comparison of NPC health part. I only really plan on copying this.
    event_format = ['   4', '06', 'biiib']
    return format_instruction(event_format, output_condition, entity_id, part_NPC_type,
                              health_threshold, comparison_type)


# 7
def if_entity_backread_enabled(output_condition, entity_id):
    return if_entity_backread_state(output_condition, entity_id, 1)


def if_entity_backread_disabled(output_condition, entity_id):
    return if_entity_backread_state(output_condition, entity_id, 0)


def if_entity_backread_state(output_condition, entity_id, loaded):
    # Check if entity is loaded in background (presumably) or not.
    event_format = ['   4', '07', 'biB']
    return format_instruction(event_format, output_condition, entity_id, loaded)


# 8
def if_has_tae_event(output_condition, entity_id, event_message_id):
    return if_tae_event_state(output_condition, entity_id, event_message_id, 1)


def if_does_not_have_tae_event(output_condition, entity_id, event_message_id):
    return if_tae_event_state(output_condition, entity_id, event_message_id, 0)


def if_tae_event_state(output_condition, entity_id, event_message_id, match_state):
    # Check if entity event message ID does or does not match another event
    # message ID. Not really sure when I'd use this.
    event_format = ['   4', '08', 'biiB']
    return format_instruction(event_format, output_condition, entity_id, event_message_id, bint(match_state))


# 9
def if_ai_state(output_condition, entity_id, required_ai_state):
    # Check if entity's AI state has a certain value.
    """
    AI state list:
        0: "Normal",
        1: "Recognition",
        2: "Alert",
        3: "Battle"
    """
    event_format = ['   4', '09', 'biB']
    return format_instruction(event_format, output_condition, entity_id, required_ai_state)


# 10
def if_skull_lantern_activated(output_condition):
    # Check if player is using (holding out) the Skull Lantern. Currently used
    # to alter enemy aggression in Tomb of the Giants, I think. No need for a
    # generic version.
    return if_skull_lantern_state(output_condition, 1)


def if_skull_lantern_not_activated(output_condition):
    # Check if player is using (holding out) the Skull Lantern. Currently used
    # to alter enemy aggression in Tomb of the Giants, I think. No need for a
    # generic version.
    return if_skull_lantern_state(output_condition, 0)


def if_skull_lantern_state(output_condition, lantern_active):
    event_format = ['   4', '10', 'bB']
    return format_instruction(event_format, output_condition, bint(lantern_active))


# 11
def if_player_class(output_condition, class_name):
    # Check if player class is the specific name. You can pass the class as a
    # string rather than an enum.
    """
    Class list:
        0: "Warrior",
        1: "Knight",
        2: "Wanderer",
        3: "Thief",
        4: "Bandit",
        5: "Hunter",
        6: "Sorcerer",
        7: "Pyromancer",
        8: "Cleric",
        9: "Deprived",
    10-27 include temporary classes not used.
    """
    class_list = ['warrior', 'knight', 'wanderer', 'thief', 'bandit', 'hunter',
                  'sorcerer', 'pyromancer', 'cleric', 'deprived']
    if isinstance(class_name, str):
        if class_name.lower() in class_list:
            class_name = class_list.index(class_name.lower())
        else:
            raise ValueError('Unrecognized class name.')
    event_format = ['   4', '11', 'bB']
    return format_instruction(event_format, output_condition, class_name)


# 12
def if_player_covenant(output_condition, covenant_name):
    # Check if player covenant is the specified name. You can pass the covenant
    # as a string rather than an enum. Pass 'none' or 0 for no covenant.
    """
    Covenant list:
        0: "None",
        1: "Way of White",
        2: "Princess's Guard",
        3: "Warrior of Sunlight",
        4: "Darkwraith",
        5: "Path of the Dragon",
        6: "Gravelord Servant",
        7: "Forest Hunter",
        8: "Darkmoon Blade",
        9: "Chaos Servant"
    """
    covenant_list = ['none', 'way of white', 'princess\'s guard',
                     'warrior of sunlight', 'darkwraith', 'path of the dragon',
                     'gravelord servant', 'forest hunter', 'darkmoon blade',
                     'chaos servant']
    if isinstance(covenant_name, str):
        if covenant_name.lower() in covenant_list:
            covenant_name = covenant_list.index(covenant_name.lower())
        else:
            raise ValueError('Unrecognized class name.')
    event_format = ['   4', '12', 'bB']
    return format_instruction(event_format, output_condition, covenant_name)


# 13
def if_player_soul_level_greater_than_or_equal(output_condition, comparison_value):
    return if_player_soul_level_comparison(output_condition, 4, comparison_value)


def if_player_soul_level_less_than_or_equal(output_condition, comparison_value):
    return if_player_soul_level_comparison(output_condition, 5, comparison_value)


def if_player_soul_level_comparison(output_condition, comparison_type, comparison_value):
    # Check if player soul level comparison returns true.
    event_format = ['   4', '13', 'bBI']
    return format_instruction(event_format, output_condition, comparison_type, comparison_value)


# 14
def if_entity_health_value_equal(output_condition, entity_id, comparison_value):
    return if_entity_health_value_comparison(output_condition, entity_id, 0, comparison_value)


def if_entity_health_value_not_equal(output_condition, entity_id, comparison_value):
    return if_entity_health_value_comparison(output_condition, entity_id, 1, comparison_value)


def if_entity_health_value_greater_than(output_condition, entity_id, comparison_value):
    return if_entity_health_value_comparison(output_condition, entity_id, 2, comparison_value)


def if_entity_health_value_less_than(output_condition, entity_id, comparison_value):
    return if_entity_health_value_comparison(output_condition, entity_id, 3, comparison_value)


def if_entity_health_value_greater_than_or_equal(output_condition, entity_id, comparison_value):
    return if_entity_health_value_comparison(output_condition, entity_id, 4, comparison_value)


def if_entity_health_value_less_than_or_equal(output_condition, entity_id, comparison_value):
    return if_entity_health_value_comparison(output_condition, entity_id, 5, comparison_value)


def if_entity_health_value_comparison(output_condition, entity_id, comparison_type, comparison_value):
    # Check if absolute entity health (NOT ratio) comparison returns true.
    event_format = ['   4', '14', 'biBi']
    return format_instruction(event_format, output_condition, entity_id, comparison_type, comparison_value)


""" 5: EXECUTION CONDITIONS (OBJECT) """


# 0
def if_object_destroyed(output_condition, entity_id):
    return if_object_destruction_state(output_condition, 1, entity_id)


def if_object_not_destroyed(output_condition, entity_id):
    return if_object_destruction_state(output_condition, 0, entity_id)


def if_object_destruction_state(output_condition, required_state, entity_id):
    # Check if object is destroyed or not.
    event_format = ['   5', '00', 'bBi']
    return format_instruction(event_format, output_condition, required_state, entity_id)


# 1
def if_object_damaged_by(output_condition, entity_id, attacking_entity_id):
    # Check if object was damaged by a specific attacker. If attacking_entity_id == -1, it will trigger on any attacker.
    event_format = ['   5', '01', 'bii']
    return format_instruction(event_format, output_condition, entity_id, attacking_entity_id)


# 2
def if_object_activated(output_condition, execution_event_id):
    # Check if object was activated.
    event_format = ['   5', '02', 'bi']
    return format_instruction(event_format, output_condition, execution_event_id)


""" 11: EXECUTION CONDITIONS (HIT) """


# 0
def if_player_moving_on_hitbox(output_condition, hitbox_entity_id):
    # Check if a local player is moving on the specified hitbox.
    event_format = ['  11', '00', 'bi']
    return format_instruction(event_format, output_condition, hitbox_entity_id)


# 1
def if_player_running_on_hitbox(output_condition, hitbox_entity_id):
    # Check if a local player is running on the specified hitbox.
    event_format = ['  11', '01', 'bi']
    return format_instruction(event_format, output_condition, hitbox_entity_id)


# 2
def if_player_standing_on_hitbox(output_condition, hitbox_entity_id):
    # Check if a local player is standing on the specified hitbox.
    event_format = ['  11', '02', 'bi']
    return format_instruction(event_format, output_condition, hitbox_entity_id)


"""
Parameter substitution instruction format:
    ^(X <- Y, Z)

    X : output_offset (offset in instruction arguments to start writing into)
    Y : input_offset (offset in event arguments to start writing from)
    Z : write_length (number of bytes to write)

HPR's code automatically supplies the substitution instruction's first
argument, which specifies which event instruction line to write into (it takes
the last instruction).

"""
