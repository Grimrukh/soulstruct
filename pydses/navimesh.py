from pydses import format_instruction


def add_navimesh_collision_bitflags(entity_id, navimesh_collision_bit):
    return modify_navimesh_collision_bitflags(entity_id, navimesh_collision_bit, 0)


def delete_navimesh_collision_bitflags(entity_id, navimesh_collision_bit):
    return modify_navimesh_collision_bitflags(entity_id, navimesh_collision_bit, 1)


def modify_navimesh_collision_bitflags(entity_id, navimesh_collision_bit, modification_type):
    # Modification type: 0 = add, 1 = delete, 2 = invert
    event_format = ['2003', '13', 'iIB']
    return format_instruction(event_format, entity_id, navimesh_collision_bit, modification_type)
