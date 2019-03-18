from pydses import format_instruction


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
    return '2004[47]'


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
