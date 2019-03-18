import pydses as p


def delete_map_sfx(entity_id, erase_root_only=True):
    # Erasing the root only probably allows easy recreation later (default).
    event_format = ['2006', '01', 'iB']

    return p.format_instruction(event_format, entity_id, p.bint(erase_root_only))


def create_map_sfx(entity_id):
    event_format = ['2006', '02', 'i']
    return p.format_instruction(event_format, entity_id)


def create_oneoff_sfx(sfx_type, entity_id, damipoly_id, sfx_id):
    """
    SFX categories:
        0: "Object",
        1: "Area",
        2: "Character"
    """
    event_format = ['2006', '03', 'iiii']
    if isinstance(sfx_type, str):
        sfx_type = p.category_type(sfx_type)
    return p.format_instruction(event_format, sfx_type, entity_id, damipoly_id, sfx_id)


def create_object_sfx(entity_id, damipoly_id, sfx_id):
    event_format = ['2006', '04', 'iii']
    return p.format_instruction(event_format, entity_id, damipoly_id, sfx_id)


def delete_object_sfx(entity_id, erase_root=True):
    # Note `erase_root` vs. `erase_root_only` for map SFX.
    event_format = ['2006', '05', 'ii']
    return p.format_instruction(event_format, entity_id, p.bint(erase_root))
