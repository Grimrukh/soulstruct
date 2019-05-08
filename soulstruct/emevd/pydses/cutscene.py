from soulstruct.emevd.pydses import format_instruction


def play_cutscene_and_warp_player(cutscene_id, playback_method, point_entity_id, area_id, block_id):
    event_format = ['2002', '02', 'iIiBB']
    return format_instruction(event_format, cutscene_id, playback_method, point_entity_id, area_id, block_id)


def play_cutscene_to_player(cutscene_id, playback_method, player_entity_id):
    event_format = ['2002', '03', 'iIi']
    return format_instruction(event_format, cutscene_id, playback_method, player_entity_id)


def play_cutscene_and_warp_specific_player(cutscene_id, playback_method, point_entity_id, area_id, block_id,
                                           player_entity_id):
    event_format = ['2002', '04', 'iIiBBi']
    return format_instruction(event_format, cutscene_id, playback_method, point_entity_id, area_id, block_id,
                              player_entity_id)


def play_cutscene_and_rotate_player(cutscene_id, playback_method, axis_x, axis_z, rotation, translation_y,
                                    player_entity_id):
    event_format = ['2002', '05', 'iIffifi']
    return format_instruction(event_format, cutscene_id, playback_method, axis_x, axis_z, rotation, translation_y,
                              player_entity_id)
