from soulstruct.emevd.pydses import format_instruction


def increment_new_game_plus_counter():
    event_format = ['2003', '21', 'B']
    return format_instruction(event_format, 0)


def award_achievement(achievement_id):
    event_format = ['2003', '28', 'i']
    return format_instruction(event_format, achievement_id)


def betray_current_covenant():
    event_format = ['2004', '38', 'B']
    return format_instruction(event_format, 0)


def equal_recovery():
    # No arguments; HPR speculates that it may trigger a garbage collection.
    event_format = ['2004', '47', '']
    return format_instruction(event_format)


def set_locked_camera_slot_number(area_id, block_id, locked_camera_slot_number):
    # This doesn't seem to be used as often as I'd expect, given the number
    # of different camera settings in the params. Camera settings triggered by
    # boss battles may be handled elsewhere.
    event_format = ['2008', '03', 'BBH']
    return format_instruction(event_format, area_id, block_id, locked_camera_slot_number)


def hellkite_breath_control(entity_id, object_entity_id, animation_id):
    # I don't expect to be reusing this, obviously.
    event_format = ['2004', '36', 'iii']
    return format_instruction(event_format, entity_id, object_entity_id, animation_id)


def arena_1v1_request():
    event_format = ['2003', '37', '']
    return format_instruction(event_format)


def arena_2v2_request():
    event_format = ['2003', '38', '']
    return format_instruction(event_format)


def arena_FFA_request():
    event_format = ['2003', '39', '']
    return format_instruction(event_format)


def arena_exit_request():
    event_format = ['2003', '40', '']
    return format_instruction(event_format)


def arena_set_nametag_1():
    event_format = ['2007', '05', '']
    return format_instruction(event_format)


def arena_set_nametag_2():
    event_format = ['2007', '06', '']
    return format_instruction(event_format)


def arena_set_nametag_3():
    event_format = ['2007', '07', '']
    return format_instruction(event_format)


def arena_set_nametag_4():
    event_format = ['2007', '08', '']
    return format_instruction(event_format)


def display_arena_dissolution_message(text_id):
    event_format = ['2007', '09', 'i']
    return format_instruction(event_format, text_id)


