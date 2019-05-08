from soulstruct.emevd.pydses import format_instruction


def activate_player_killplane(map_id, block_id, threshold_Y, target_model_id):
    event_format = ['2003', '41', 'iifi']
    return format_instruction(event_format, map_id, block_id, threshold_Y, target_model_id)


def register_ladder(event_flag_id_1, event_flag_id_2, entity_id):
    # Not sure what the different event flags do. Called on area initialization
    # to make ladders interactable.
    event_format = ['2009', '00', 'iii']
    return format_instruction(event_format, event_flag_id_1, event_flag_id_2, entity_id)


def register_bonfire(event_flag_id, entity_id, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0):
    # Initial kindle level should be 0, 10, 20, or 30 (it gives you half that many Estus flask uses plus 5).
    event_format = ['2009', '03', 'iiffi']
    return format_instruction(event_format, event_flag_id, entity_id, reaction_distance, reaction_angle,
                              initial_kindle_level)


def enable_map_part(map_part_id):
    return set_map_part_state(map_part_id, 1)


def disable_map_part(map_part_id):
    return set_map_part_state(map_part_id, 0)


def set_map_part_state(map_part_id, activation_state):
    # TODO: Check usage of this.
    event_format = ['2012', '01', 'iB']
    return format_instruction(event_format, map_part_id, activation_state)