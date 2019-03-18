import pydses as p


def enable_ai(entity_id):
    return set_ai(entity_id, 1)


def disable_ai(entity_id):
    return set_ai(entity_id, 0)


def set_ai(entity_id, desired_state):
    event_format = ['2004', '01', 'iB']
    return p.format_instruction(event_format, entity_id, p.bint(desired_state))


def set_team_type(entity_id, new_team):
    event_format = ['2004', '02', 'ib']
    return p.format_instruction(event_format, entity_id, new_team)


def kill(entity_id, award_souls=0):
    # Technically a kill 'request.'
    event_format = ['2004', '04', 'iB']
    return p.format_instruction(event_format, entity_id, p.bint(award_souls))


def enable(entity_id):
    return set_character_state(entity_id, 1)


def disable(entity_id):
    return set_character_state(entity_id, 0)


def set_character_state(entity_id, desired_state):
    event_format = ['2004', '05', 'iB']
    return p.format_instruction(event_format, entity_id, p.bint(desired_state))


def ezstate_ai_request(entity_id, command_id, slot_number):
    # Slot number from 0-3.
    event_format = ['2004', '06', 'iiB']
    return p.format_instruction(event_format, entity_id, command_id, slot_number)


def set_special_effect(entity_id, special_effect_id):
    # 'Special effect' as in buff/debuff, not graphics.
    event_format = ['2004', '08', 'ii']
    return p.format_instruction(event_format, entity_id, special_effect_id)


def set_standby_animation_settings_to_default(entity_id):
    return set_standby_animation_settings(entity_id, -1, -1, -1, -1, -1)


def set_standby_animation_settings(entity_id, standby_animation=-1, damage_animation=-1, cancel_animation=-1,
                                   death_animation=-1, standby_return_animation=-1):
    # Sets entity's standby animations. -1 is default for each category.
    event_format = ['2004', '09', 'iiiiii']
    return p.format_instruction(event_format, entity_id, standby_animation, damage_animation, cancel_animation,
                                death_animation, standby_return_animation)


def enable_gravity(entity_id):
    return set_gravity(entity_id, 1)


def disable_gravity(entity_id):
    return set_gravity(entity_id, 0)


def set_gravity(entity_id, desired_state):
    # 1 = enabled
    # Does NOT allow any sort of RigidBody activity, but rather determines if
    # the entity changes height as it moves around.
    event_format = ['2004', '10', 'iB']
    return p.format_instruction(event_format, entity_id, p.bint(desired_state))


def enable_immortality(entity_id):
    return set_immortality(entity_id, 1)


def disable_immortality(entity_id):
    return set_immortality(entity_id, 0)


def set_immortality(entity_id, desired_state):
    # Character will take damage, but not die.
    event_format = ['2004', '12', 'iB']
    return p.format_instruction(event_format, entity_id, p.bint(desired_state))


def set_nest(entity_id, region):
    # Home point for entity AI.
    event_format = ['2004', '13', 'ii']
    return p.format_instruction(event_format, entity_id, region)


def rotate_to_face_entity(entity_id, target_entity_id):
    # Rotate first entity to face towards second.
    event_format = ['2004', '14', 'ii']
    return p.format_instruction(event_format, entity_id, target_entity_id)


def enable_invincibility(entity_id):
    return set_invincibility(entity_id, 1)


def disable_invincibility(entity_id):
    return set_invincibility(entity_id, 0)


def set_invincibility(entity_id, desired_state):
    # Character cannot take damage or die.
    event_format = ['2004', '15', 'iB']
    return p.format_instruction(event_format, entity_id, p.bint(desired_state))


def clear_ai_target_list(entity_id):
    event_format = ['2004', '16', 'i']
    return p.format_instruction(event_format, entity_id)


def ai_instruction(entity_id, command_id, slot_number):
    event_format = ['2004', '17', 'iiB']
    return p.format_instruction(event_format, entity_id, command_id, slot_number)


def set_event_point(entity_id, event_area_entity_id, reaction_range):
    event_format = ['2004', '18', 'iif']
    return p.format_instruction(event_format, entity_id, event_area_entity_id, reaction_range)


def set_ai_id(entity_id, ai_id):
    event_format = ['2004', '19', 'ii']
    return p.format_instruction(event_format, entity_id, ai_id)


def replan_ai(entity_id):
    # Force entity to re-plan AI.
    event_format = ['2004', '20', 'i']
    return p.format_instruction(event_format, entity_id)


def cancel_special_effect(entity_id, special_effect_id):
    event_format = ['2004', '21', 'ii']
    return p.format_instruction(event_format, entity_id, special_effect_id)


def create_multipart_npc_part(entity_id, part_npc_type, part_index, part_health,
                              damage_correction, body_damage_correction, is_invincible, start_in_stop_state):
    # Obviously complex and I'm not planning to do much other than copy existing use.
    event_format = ['2004', '22', 'ihhiffBB']
    return p.format_instruction(event_format, entity_id, part_npc_type, part_index, part_health,
                                damage_correction, body_damage_correction, p.bint(is_invincible),
                                p.bint(start_in_stop_state))


def set_multipart_npc_part_health(entity_id, part_npc_type, desired_hp, overwrite_max):
    event_format = ['2004', '23', 'iiiB']
    return p.format_instruction(event_format, entity_id, part_npc_type, desired_hp, p.bint(overwrite_max))


def set_multipart_npc_part_effects(entity_id, part_npc_type, material_special_effect_id, material_SFX_id):
    event_format = ['2004', '24', 'iiii']
    return p.format_instruction(event_format, entity_id, part_npc_type, material_special_effect_id, material_SFX_id)


def set_multipart_npc_part_bullet_damage_scaling(entity_id, part_npc_type, desired_scaling):
    event_format = ['2004', '25', 'iif']
    return p.format_instruction(event_format, entity_id, part_npc_type, desired_scaling)


def set_display_mask(entity_id, bit_number, switch_type):
    # 0 = off, 1 = on, 2 = change
    event_format = ['2004', '26', 'iBB']
    return p.format_instruction(event_format, entity_id, bit_number, switch_type)


def set_hitbox_mask(entity_id, bit_number, switch_type):
    # 0 = off, 1 = on, 2 = change
    event_format = ['2004', '27', 'iBB']
    return p.format_instruction(event_format, entity_id, bit_number, switch_type)


def set_network_update_authority(entity_id, authority_level):
    # 0 = normal, 4095 = forced (or -1 I assume)
    event_format = ['2004', '28', 'ii']
    return p.format_instruction(event_format, entity_id, authority_level)


def enable_backread(entity_id):
    return set_backread_state(entity_id, 0)


def disable_backread(entity_id):
    return set_backread_state(entity_id, 1)


def set_backread_state(entity_id, desired_state):
    # 'Setting to remove from back lead' - involved in permanent disabling
    # 1 = remove, 0 = don't remove
    # Not sure if it can be restored once removed
    event_format = ['2004', '29', 'iB']
    return p.format_instruction(event_format, entity_id, p.bint(desired_state))


def enable_health_bar(entity_id):
    return set_health_bar_display(entity_id, 1)


def disable_health_bar(entity_id):
    return set_health_bar_display(entity_id, 0)


def set_health_bar_display(entity_id, desired_state):
    # Normal bar, not boss bar.
    event_format = ['2004', '30', 'iB']
    return p.format_instruction(event_format, entity_id, p.bint(desired_state))


def enable_collision(entity_id):
    return set_collision(entity_id, 0)


def disable_collision(entity_id):
    return set_collision(entity_id, 1)


def set_collision(entity_id, is_disabled):
    # 1 = no collision
    event_format = ['2004', '31', 'iB']
    return p.format_instruction(event_format, entity_id, p.bint(is_disabled))


def ai_event(entity_id, command_id, slot_number, start_event_flag_id, end_event_flag_id):
    # Complex AI stuff.
    event_format = ['2004', '32', 'iiBii']
    return p.format_instruction(event_format, entity_id, command_id, slot_number, start_event_flag_id, end_event_flag_id)


def refer_damage_to_entity(entity_id, target_entity_id):
    # Damage to first entity affects second (a la Four Kings).
    event_format = ['2004', '33', 'ii']
    return p.format_instruction(event_format, entity_id, target_entity_id)


def set_network_update_rate(entity_id, is_fixed, frequency):
    """
    Frequency:
        -1: "Never",
        0: "Always",
        2: "Every 2 frames",
        5: "Every 5 frames
    """
    event_format = ['2004', '34', 'iBb']
    return p.format_instruction(event_format, entity_id, p.bint(is_fixed), frequency)


def set_backread_state_alternate(entity_id, desired_state):
    # Not sure how this relates to 2004[29] above.
    # TODO: Check and compare usage.
    event_format = ['2004', '35', 'iB']
    return p.format_instruction(event_format, entity_id, p.bint(desired_state))


def drop_mandatory_treasure(entity_id):
    # Forces drop of mandatory treasure, e.g. NPC drop on reload.
    event_format = ['2004', '37', 'i']
    return p.format_instruction(event_format, entity_id)


def set_team_type_and_exit_standby_animation(entity_id, new_team):
    event_format = ['2004', '44', 'iB']
    return p.format_instruction(event_format, entity_id, new_team)


def humanity_registration(entity_id, event_flag_id):
    # Not known exactly what the event flag does, but this instruction is
    # always called to initialize NPCs who drop humanity. It probably makes the
    # game's sin system aware of the NPC's death, etc.
    event_format = ['2004', '45', 'ii']
    return p.format_instruction(event_format, entity_id, event_flag_id)


def reset_animation(entity_id, disable_interpolation):
    # 0 = interpolated, 1 = not interpolated
    event_format = ['2004', '43', 'iB']
    return p.format_instruction(event_format, entity_id, p.bint(disable_interpolation))


def activate_npc_buffs(entity_id):
    event_format = ['2009', '04', 'i']
    return p.format_instruction(event_format, entity_id)
