from soulstruct.emevd.pydses import format_instruction, bint


def enable_spawner(entity_id):
    return set_spawner_state(entity_id, 1)


def disable_spawner(entity_id):
    return set_spawner_state(entity_id, 0)


def set_spawner_state(entity_id, desired_state):
    event_format = ['2003', '03', 'iB']
    return format_instruction(event_format, entity_id, bint(desired_state))


def shoot_projectile(owner_entity_id, projectile_entity_id, damipoly_id, behavior_id,
                     launch_angle_x=0, launch_angle_y=0, launch_angle_z=0):
    event_format = ['2003', '05', 'iiiiiii']
    return format_instruction(event_format, owner_entity_id, projectile_entity_id, damipoly_id, behavior_id,
                              launch_angle_x, launch_angle_y, launch_angle_z)


def create_spawner(entity_id):
    # Technically create 'bullet owner.'
    event_format = ['2004', '07', 'i']
    return format_instruction(event_format, entity_id)
