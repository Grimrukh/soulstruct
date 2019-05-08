from soulstruct.emevd.pydses import format_instruction, bint


def place_summon_sign(sign_type, entity_id, summon_point, summon_event_flag_id, dismissal_event_flag_id):
    event_format = ['2003', '25', 'iiiii']
    return format_instruction(event_format, sign_type, entity_id, summon_point, summon_event_flag_id,
                              dismissal_event_flag_id)


def set_tip_message_visibility(entity_id, desired_state):
    event_format = ['2003', '26', 'iB']
    return format_instruction(event_format, entity_id, desired_state)


def dialog(message_id, button_type, number_buttons, entity_id, display_distance):
    """ Small message box at the bottom of the screen (with YES/NO or OK/CANCEL). """
    event_format = ['2007', '01', 'ihhif']
    return format_instruction(event_format, message_id, button_type, number_buttons, entity_id, display_distance)


def banner(banner_type):
    # Displays large preset banners.
    """
    Banner list:
        1: "Demon Killed",
        2: "Death",
        3: "Revival",
        4: "Soul Acquisition",
        5: "Target Killed",
        6: "Ghost Death",
        7: "Black Ghost Death",
        8: "Map Name",
        12: "Congratulations",
        15: "Stadium Victory",
        16: "Stadium Defeat",
        17: "Stadium Draw"
    """
    event_format = ['2007', '02', 'B']
    return format_instruction(event_format, banner_type)


def status_explanation(message_id, pad_enabled=1):
    # Displays messages explaining curse, no bonfire warp, etc.
    # TODO: Check usage for pad_enabled; when would it be used?
    event_format = ['2007', '03', 'iB']
    return format_instruction(event_format, message_id, bint(pad_enabled))


def battlefield_message(message_id, display_location_index):
    # TODO: Check usage.
    event_format = ['2007', '04', 'iB']
    return format_instruction(event_format, message_id, display_location_index)
