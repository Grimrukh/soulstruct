import pydses as p


def enable_hitbox(entity_id):
    return set_hitbox_state(entity_id, 1)


def disable_hitbox(entity_id):
    return set_hitbox_state(entity_id, 0)


def set_hitbox_state(entity_id, activation_state):
    # 1 = Hitbox is enabled.
    event_format = ['2011', '01', 'iB']
    return p.format_instruction(event_format, entity_id, activation_state)
