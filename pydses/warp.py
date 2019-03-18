import pydses as p


def warp_player(area_id, block_id, player_entity_id):
    event_format = ['2003', '14', 'BBi']
    return p.format_instruction(event_format, area_id, block_id, player_entity_id)


def move_dropped_items_and_bloodstains(source_area_entity_id, destination_area_entity_id):
    event_format = ['2003', '35', 'ii']
    return p.format_instruction(event_format, source_area_entity_id, destination_area_entity_id)


def warp(entity_id, warp_destination_type, destination_target_id, damipoly_id):
    # Technically a warp 'request.'
    if isinstance(warp_destination_type, str):
        warp_destination_type = p.category_type(warp_destination_type)
    event_format = ['2004', '03', 'iBii']
    return p.format_instruction(event_format, entity_id, warp_destination_type, destination_target_id, damipoly_id)


def warp_and_set_floor(entity_id, warp_destination_type, destination_entity_id, damipoly_id, hitbox_entity_id):
    if isinstance(warp_destination_type, str):
        warp_destination_type = p.category_type(warp_destination_type)
    event_format = ['2004', '40', 'iBiii']
    return p.format_instruction(event_format, entity_id, warp_destination_type, destination_entity_id, damipoly_id,
                                hitbox_entity_id)


def short_warp(entity_id, warp_destination_type, destination_target_id, damipoly_id=-1):
    if isinstance(warp_destination_type, str):
        warp_destination_type = p.category_type(warp_destination_type)
    event_format = ['2004', '41', 'iBii']
    return p.format_instruction(event_format, entity_id, warp_destination_type, destination_target_id, damipoly_id)


def warp_and_copy_floor(entity_id, warp_destination_type, destination_target_id, damipoly_id, copy_floor_of_entity_id):
    if isinstance(warp_destination_type, str):
        warp_destination_type = p.category_type(warp_destination_type)
    event_format = ['2004', '42', 'iBiii']
    return p.format_instruction(event_format, entity_id, warp_destination_type, destination_target_id, damipoly_id,
                                copy_floor_of_entity_id)


def warp_object_to_character(entity_id, character_entity_id, damipoly_id):
    # TODO: Check when this is actually used, as I'm not sure what use it has.
    event_format = ['2005', '11', 'iih']
    return p.format_instruction(event_format, entity_id, character_entity_id, damipoly_id)


def set_player_respawn_point(respawn_point_id):
    event_format = ['2003', '23', 'i']
    return p.format_instruction(event_format, respawn_point_id)
