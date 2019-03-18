from pydses import format_instruction


def play_sound_effect(entity_id, sound_type, sound_id):
    # Entity specifies the sound's origin (direction), I assume.
    """
    Sound type list:
        0: "a: Environmental Sound",
        1: "c: Character Motion",
        2: "f: Menu SE",
        3: "o: Object",
        4: "p: Poly Drama",
        5: "s: SFX",
        6: "m: BGM",
        7: "v: Voice",
        8: "x: Floor Material Dependence",
        9: "b: Armor Material Dependence",
        10: "g: Ghost"
    """
    event_format = ['2010', '02', 'iii']
    return format_instruction(event_format, entity_id, sound_type, sound_id)


def enable_map_sound(entity_id):
    return set_map_sound(entity_id, 1)


def disable_map_sound(entity_id):
    return set_map_sound(entity_id, 0)


def set_map_sound(entity_id, sound_state):
    # Includes boss music, which is obviously the most common use.
    event_format = ['2010', '03', 'iB']
    return format_instruction(event_format, entity_id, sound_state)
