from soulstruct.emevd.pydses import format_instruction


def award_item_lot(item_lot_id):
    # Directly gives to player (pops up on screen).
    event_format = ['2003', '04', 'i']
    return format_instruction(event_format, item_lot_id)


def remove_items_from_player(item_type, item_id, quantity):
    # Quantity may be broken (always removes all).
    event_format = ['2003', '24', 'iii']
    return format_instruction(event_format, item_type, item_id, quantity)


def snuggly_item_drop(item_lot_id, area_entity_id, event_flag_id, hitbox_entity_id):
    event_format = ['2003', '34', 'iiii']
    return format_instruction(event_format, item_lot_id, area_entity_id, event_flag_id, hitbox_entity_id)


def award_item_to_host_only(item_lot_id):
    event_format = ['2003', '36', 'i']
    return format_instruction(event_format, item_lot_id)


def set_snuggly_next_trade(event_flag_id):
    event_format = ['2003', '33', 'i']
    return format_instruction(event_format, event_flag_id)