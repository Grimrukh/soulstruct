import soulstruct.emevd.pydses as p


def destroy(entity_id, slot_number):
    # Technically requests the object's destruction. Not sure what the slot
    # number does.
    event_format = ['2005', '01', 'ib']
    return p.format_instruction(event_format, entity_id, slot_number)


def restore(entity_id):
    event_format = ['2005', '02', 'i']
    return p.format_instruction(event_format, entity_id)


def enable(entity_id):
    return set_object_state(entity_id, 1)


def disable(entity_id):
    return set_object_state(entity_id, 0)


def set_object_state(entity_id, desired_state):
    event_format = ['2005', '03', 'iB']
    return p.format_instruction(event_format, entity_id, desired_state)


def enable_treasure(entity_id):
    return set_treasure_state(entity_id, 1)


def disable_treasure(entity_id):
    return set_treasure_state(entity_id, 0)


def set_treasure_state(entity_id, activation_status):
    event_format = ['2005', '04', 'iB']
    return p.format_instruction(event_format, entity_id, activation_status)


def start_object_activation(entity_id, object_parameter_id, relative_idx):
    # Calls ObjAct function of object. Not sure what relative IDX does.
    event_format = ['2005', '05', 'iii']
    return p.format_instruction(event_format, entity_id, object_parameter_id, relative_idx)


def enable_activation(entity_id, object_parameter_id):
    return set_object_activation(entity_id, object_parameter_id, 1)


def disable_activation(entity_id, object_parameter_id):
    return set_object_activation(entity_id, object_parameter_id, 0)


def set_object_activation(entity_id, object_parameter_id, activation_status):
    # Sets whether the object can be activated (1) or not activated (0).
    event_format = ['2005', '06', 'iiB']
    return p.format_instruction(event_format, entity_id, object_parameter_id, activation_status)


def end_destruction(entity_id, slot_number):
    # Sets object to whatever state it would have after destruction.
    event_format = ['2005', '08', 'ib']
    return p.format_instruction(event_format, entity_id, slot_number)


def create_damaging_object(entity_flag_id, entity_id, damipoly_id, behavior_id, target_type, radius, life,
                           repetition_time):
    # Used to create things like the Sen's Fortress dart traps.
    # TODO: Check usage and confirm argument functions.
    """
    Damage target type list:
        1: Character
        2: Map
        3: Character and Map
    """
    event_format = ['2005', '09', 'iiiiifff']
    return p.format_instruction(event_format, entity_flag_id, entity_id, damipoly_id, behavior_id, target_type, radius, life,
                              repetition_time)


def register_statue_object(entity_id, area_number, block_number, statue_type):
    # I believe this creates a petrified or crystallized statue.
    # TODO: Check usage.
    event_format = ['2005', '10', 'iBBB']
    return p.format_instruction(event_format, entity_id, area_number, block_number, statue_type)


def remove_object_event_flag(event_flag_id):
    # TODO: Check when this is actually used.
    event_format = ['2005', '12', 'i']
    return p.format_instruction(event_format, event_flag_id)


def enable_invulnerability(entity_id):
    return set_object_invulnerability(entity_id, 1)


def disable_invulnerability(entity_id):
    return set_object_invulnerability(entity_id, 0)


def set_object_invulnerability(entity_id, invulnerability_state):
    # 1 = invulnerable
    event_format = ['2005', '13', 'iB']
    return p.format_instruction(event_format, entity_id, invulnerability_state)


def activate_object_with_idx(entity_id, object_parameter_id, relative_idx):
    return set_object_activation_with_idx(entity_id, object_parameter_id, relative_idx, 1)


def deactivate_object_with_idx(entity_id, object_parameter_id, relative_idx):
    return set_object_activation_with_idx(entity_id, object_parameter_id, relative_idx, 0)


def set_object_activation_with_idx(entity_id, object_parameter_id, relative_idx, activation_state):
    event_format = ['2005', '14', 'iiiB']
    return p.format_instruction(event_format, entity_id, object_parameter_id, relative_idx, activation_state)


def enable_treasure_collection(entity_id):
    # TODO: Speculated use only. Check usage.
    event_format = ['2005', '15', 'i']
    return p.format_instruction(event_format, entity_id)
