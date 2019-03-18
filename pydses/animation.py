import pydses as p


def animation_playback_request(entity_id, animation_id, loop=0, wait_for_completion=0):
    event_format = ['2003', '01', 'iiBB']
    return p.format_instruction(event_format, entity_id, animation_id, p.bint(loop), p.bint(wait_for_completion))


def force_animation(entity_id, animation_id, loop=False, wait_for_completion=False, do_not_wait_for_transition=False):
    event_format = ['2003', '18', 'iiBBB']
    return p.format_instruction(event_format, entity_id, animation_id, p.bint(loop), p.bint(wait_for_completion),
                                p.bint(do_not_wait_for_transition))


def enable_animations(entity_id):
    return set_animation_state(entity_id, 1)


def disable_animations(entity_id):
    return set_animation_state(entity_id, 0)


def set_animation_state(entity_id, desired_state):
    event_format = ['2004', '39', 'iB']
    return p.format_instruction(event_format, entity_id, p.bint(desired_state))


def end_animation(entity_id, animation_id):
    # Sets object to whatever state it would have given the activation.
    event_format = ['2005', '07', 'ii']
    return p.format_instruction(event_format, entity_id, animation_id)