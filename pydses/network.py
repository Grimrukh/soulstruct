from pydses import format_instruction, bint


def set_sync(network_sync_state):
    event_format = ['2000', '02', 'B']
    return format_instruction(event_format, bint(network_sync_state))


def disable_sync():
    return set_sync(0)


def enable_sync():
    return set_sync(0)


def issue_prefetch_request(request_id):
    event_format = ['2000', '04', 'I']
    return format_instruction(event_format, request_id)


def save_request():
    event_format = ['2000', '05', 'B']
    return format_instruction(event_format, 0)


def trigger_multiplayer_event(multiplayer_event_id):
    event_format = ['2003', '16', 'i']
    return format_instruction(event_format, multiplayer_event_id)


def set_vagrant_spawning(desired_state):
    # 1 = disable
    event_format = ['2003', '30', 'B']
    return format_instruction(event_format, desired_state)


def increment_player_pvp_sin():
    event_format = ['2004', '46', 'B']
    return format_instruction(event_format, 0)


def notify_boss_room_entry():
    # Triggers message for summons that player has challenged the boss.
    # Might do other things for online play as well, no doubt.
    event_format = ['2009', '06', 'B']
    return format_instruction(event_format, 0)