import pydses as p


def enable_boss_health_bar(entity_id, name_id):
    return set_boss_health_bar_with_slot(1, entity_id, 0, name_id)


def disable_boss_health_bar(entity_id, name_id):
    return set_boss_health_bar_with_slot(0, entity_id, 0, name_id)


def enable_boss_health_bar_with_slot(entity_id, slot_number, name_id):
    return set_boss_health_bar_with_slot(1, entity_id, slot_number, name_id)


def disable_boss_health_bar_with_slot(entity_id, slot_number, name_id):
    return set_boss_health_bar_with_slot(0, entity_id, slot_number, name_id)


def set_boss_health_bar_with_slot(desired_state, entity_id, slot_number, name_id):
    # Note: slot number can only be 0 (bottom) or 1 (top).
    event_format = ['2003', '11', 'bihh']
    return p.format_instruction(event_format, desired_state, entity_id, slot_number, name_id)


def kill_boss(entity_id):
    event_format = ['2003', '12', 'i']
    return p.format_instruction(event_format, entity_id)
