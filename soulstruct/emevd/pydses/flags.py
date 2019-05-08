from soulstruct.emevd.pydses import format_instruction, bint


def enable(event_flag_id):
    return set_flag_state(event_flag_id, 1)


def disable(event_flag_id):
    return set_flag_state(event_flag_id, 0)


def set_flag_state(event_flag_id, desired_state):
    event_format = ['2003', '02', 'iB']
    return format_instruction(event_format, event_flag_id, bint(desired_state))


def enable_random_in_chunk(start_event_flag_id, end_event_flag_id):
    return set_random_in_chunk(start_event_flag_id, end_event_flag_id, 1)


def disable_random_in_chunk(start_event_flag_id, end_event_flag_id):
    return set_random_in_chunk(start_event_flag_id, end_event_flag_id, 0)


def set_random_in_chunk(start_event_flag_id, end_event_flag_id, desired_state):
    event_format = ['2003', '17', 'IIB']
    return format_instruction(event_format, start_event_flag_id, end_event_flag_id, bint(desired_state))


def enable_chunk(start_event_flag_id, end_event_flag_id):
    return set_flag_chunk_state(start_event_flag_id, end_event_flag_id, 1)


def disable_chunk(start_event_flag_id, end_event_flag_id):
    return set_flag_chunk_state(start_event_flag_id, end_event_flag_id, 0)


def set_flag_chunk_state(start_event_flag_id, end_event_flag_id, desired_state):
    event_format = ['2003', '22', 'iiB']
    return format_instruction(event_format, start_event_flag_id, end_event_flag_id, desired_state)


def increment_event_value(event_flag_id, number_bits, max_value):
    event_format = ['2003', '31', 'iII']
    return format_instruction(event_format, event_flag_id, number_bits, max_value)


def clear_event_value(event_flag_id, number_bits):
    event_format = ['2003', '32', 'iI']
    return format_instruction(event_format, event_flag_id, number_bits)