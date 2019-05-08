import soulstruct.emevd.pydses as p


def restart_event_id(event_id):
    return set_event_id_state_with_slot(event_id, 0, 1)


def cancel_event_id(event_id):
    return set_event_id_state_with_slot(event_id, 0, 0)


def restart_event_id_with_slot(event_id, event_slot_id):
    return set_event_id_state_with_slot(event_id, event_slot_id, 1)


def cancel_event_id_with_slot(event_id, event_slot_id):
    return set_event_id_state_with_slot(event_id, event_slot_id, 0)


def set_event_id_state_with_slot(event_id, event_slot_id, desired_state):
    event_format = ['2003', '08', 'iiB']
    return p.format_instruction(event_format, event_id, event_slot_id, p.bint(desired_state))