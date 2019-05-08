# -*- coding: utf-8 -*-
""" Verbose output that matches EVS language for 'decompiling'. (Does not use IF blocks.) """
import struct


GAME_MAPS = {
    (10, 0): "DEPTHS",
    (10, 1): "UNDEAD_BURG",
    (10, 2): "FIRELINK_SHRINE",
    (11, 0): "PAINTED_WORLD",
    (12, 0): "DARKROOT_GARDEN",
    (12, 1): "OOLACILE",
    (13, 0): "CATACOMBS",
    (13, 1): "TOMB_OF_THE_GIANTS",
    (13, 2): "ASH_LAKE",
    (14, 0): "BLIGHTTOWN",
    (14, 1): "LOST_IZALITH",
    (15, 0): "SENS_FORTRESS",
    (15, 1): "ANOR_LONDO",
    (16, 0): "NEW_LONDO_RUINS",
    (17, 0): "DUKES_ARCHIVES",
    (18, 0): "KILN_OF_THE_FIRST_FLAME",
    (18, 1): "UNDEAD_ASYLUM",
}

ENUM_RESTART_TYPE = {
    0: "NeverRestart",
    1: "RestartOnRest",
    2: "UnknownRestart",
}

ENUM_SOUND_TYPE = {
    0: "SoundType.a_ambient",
    1: "SoundType.c_character_motion",
    2: "SoundType.f_menu_se",
    3: "SoundType.o_object",
    4: "SoundType.p_cutscene",
    5: "SoundType.s_sfx",
    6: "SoundType.m_music",
    7: "SoundType.v_voice",
    8: "SoundType.x_floor_material_dependent",
    9: "SoundType.b_armor_material_dependent",
    10: "SoundType.g_ghost",
}

ENUM_BUTTON_TYPE = {
    0: "ButtonType.yes_no",
    1: "ButtonType.ok_cancel"
}

ENUM_CLASS_TYPE = {
    0: "ClassType.warrior",
    1: "ClassType.knight",
    2: "ClassType.wanderer",
    3: "ClassType.thief",
    4: "ClassType.bandit",
    5: "ClassType.hunter",
    6: "ClassType.sorcerer",
    7: "ClassType.pyromancer",
    8: "ClassType.cleric",
    9: "ClassType.deprived",
    # UNUSED:
    20: "Temp: Warrior", 21: "Temp: Knight", 22: "Temp: Sorcerer", 23: "Temp: Pyromancer", 24: "Chi: Warrior",
    25: "Chi: Knight", 26: "Chi: Sorcerer", 27: "Chi: Pyromancer",
}

ENUM_CHARACTER_TYPE = {
    0: "CharacterType.human",
    1: "CharacterType.white_phantom",
    2: "CharacterType.black_phantom",
    8: "CharacterType.hollow",
    12: "CharacterType.intruder",
}

ENUM_NAVIMESH_TYPE = {
    # Used as display bit masks.
    1: "NavimeshType.solid", 2: "NavimeshType.exit", 4: "NavimeshType.obstacle", 8: "NavimeshType.wall",
    32: "NavimeshType.wall_touching_floor", 64: "NavimeshType.landing_point",
    128: "NavimeshType.event", 256: "NavimeshType.cliff", 512: "NavimeshType.wide", 1024: "NavimeshType.ladder",
    2048: "NavimeshType.hole", 4096: "NavimeshType.door", 8192: "NavimeshType.closed_door",
}

ENUM_TEAM_TYPE = {
    255: "TeamType.default",
    0: "TeamType.invalid",
    1: "TeamType.human",
    2: "TeamType.white_phantom",  # Can't be hurt by allied teams.
    3: "TeamType.black_phantom",
    4: "TeamType.hollow",
    5: "TeamType.wandering_ghost",  # Vagrant, I believe.
    6: "TeamType.enemy",
    7: "TeamType.boss",  # Can damage any other team (including Boss).
    8: "TeamType.ally",
    9: "TeamType.hostile_ally",
    10: "TeamType.decoy_enemy",  # Unused.
    11: "TeamType.red_child",  # Unused.
    12: "TeamType.fighting_ally",
    13: "TeamType.intruder",
}

ENUM_AI_STATUS_TYPE = {
    0: "AIStatusType.normal",
    1: "AIStatusType.recognition",
    2: "AIStatusType.alert",
    3: "AIStatusType.battle"
}

ENUM_SIGN_TYPE = {
    0: "SummonSignType.blue_eye_sign",
    1: "SummonSignType.black_eye_sign",
    2: "SummonSignType.red_eye_sign",
    3: "SummonSignType.detection_sign",
    4: "SummonSignType.white_help_sign",
    5: "SummonSignType.black_help_sign",
}

ENUM_CATEGORY = {
    0: "Category.object",
    1: "Category.region",
    2: "Category.character",
}

ENUM_DAMAGE_TARGET_TYPE = {
    1: "DamageTargetType.character",
    2: "DamageTargetType.map",
    3: "DamageTargetType.character_and_map",
}

ENUM_BUTTON_NUMBER = {
    1: "NumberButtons.one_button",
    2: "NumberButtons.two_button",
    6: "NumberButtons.no_button",
}

ENUM_CHARACTER_UPDATE_RATE = {
    -1: "CharacterUpdateRate.never",
    0: "CharacterUpdateRate.always",
    2: "CharacterUpdateRate.every_two_frames",
    5: "CharacterUpdateRate.every_five_frames",
}

ENUM_UPDATE_AUTH = {
    0: "UpdateAuthority.normal",
    4095: "UpdateAuthority.forced",
}

ENUM_COMPARISON_TYPE = {
    0: "Equal",
    1: "NotEqual",
    2: "GreaterThan",
    3: "LessThan",
    4: "GreaterThanOrEqual",
    5: "LessThanOrEqual",
}

ENUM_TEXT_BANNER_TYPE = {
    1: "TextBannerType.boss_defeated",
    2: "TextBannerType.you_died",
    3: "TextBannerType.resurrection",
    4: "TextBannerType.souls_retrieved",
    5: "TextBannerType.target_defeated",
    6: "TextBannerType.ghost_death",
    7: "TextBannerType.black_ghost_death,",
    8: "TextBannerType.map_name",
    12: "TextBannerType.congratulations",
    15: "TextBannerType.arena_victory",
    16: "TextBannerType.arena_loss",
    17: "TextBannerType.arena_draw",
}

ENUM_MULTIPLAYER_STATE = {
    0: "Host",
    1: "Client",
    2: "Multiplayer",
    3: "SinglePlayer",
}

ENUM_STATUE_TYPE = {
    0: "StatueType.stone",
    1: "StatueType.crystal",
}

ENUM_ITEM_TYPE = {
    0: "Weapon",
    1: "Armor",
    2: "Ring",
    3: "Good",
}

ENUM_LOGICAL_OPERATION_TYPE = {
    0: "AllOn",
    1: "AllOff",
    2: "AnyOn",
    3: "AnyOff",
}

ENUM_COVENANT_TYPE = {
    0: "Covenant.none",
    1: "Covenant.way_of_white",
    2: "Covenant.princess_guard",
    3: "Covenant.warrior_of_sunlight",
    4: "Covenant.darkwraith",
    5: "Covenant.path_of_the_dragon",
    6: "Covenant.gravelord_servant",
    7: "Covenant.forest_hunter",
    8: "Covenant.darkmoon_blade",
    9: "Covenant.chaos_servant",
}


def default_readable(instr_class, instr_index, req_args, opt_args):
    """Creates a default readable representation of the command with
    command instr_class and instr_index with arguments fixed_args and var_args.
    Provides no information about the command's purpose.
    """
    if opt_args:
        arg_array_string = f"({repr(req_args)} | {repr(opt_args)}"
    else:
        arg_array_string = f"({repr(req_args)})"

    return f"{instr_class:04d}[{instr_index:02d}] {arg_array_string}"


def process_args(integer_args, arg_type_string):
    """ Re-interpret integers as a given struct. """
    packed = struct.pack(len(integer_args) * 'i', *integer_args)
    return struct.unpack('@' + arg_type_string, packed[:struct.calcsize(arg_type_string)])


def decompile_instruction(instruction_class, instruction_index, req_args, opt_args, arg_types=None):
    """ Restores low-level EVS language instructions and tests. Not intelligent enough to create IF blocks, though. """

    # Instructions that accept optional arguments (currently just 2000[00]):

    if instruction_class == 2000 and instruction_index == 0:
        slot, event_id, first_arg = req_args
        if arg_types:
            args = (first_arg, *opt_args)
            if not arg_types.replace('i', ''):
                # All signed integers (default).
                return f"RunEvent({event_id}, slot={slot}, args={args})"
            elif all(isinstance(i, int) for i in args):
                try:
                    args = process_args(args, arg_types)
                except struct.error:
                    print(event_id, args, arg_types)
                    raise
            return f"RunEvent({event_id}, slot={slot}, args={args}, arg_types='{arg_types}')"
        elif not opt_args and first_arg == 0:
            if slot > 0:
                raise ValueError(f"Event {event_id} was run with slot > 0, but has no optional arguments.")
            return f"RunEvent({event_id})"
        else:
            # Assume all integers.
            return f"RunEvent({event_id}, slot={slot}, args={(first_arg, *opt_args)})"

    if opt_args:
        raise ValueError(f"Command {instruction_class}[{instruction_index}] cannot use optional arguments")

    # Remaining instructions do not accept optional arguments.

    if instruction_class == 2000:  # SYSTEM
        if instruction_index == 2:
            enable, = req_args
            if enable:
                return "EnableNetworkSync()"
            else:
                return "DisableNetworkSync()"
        if instruction_index == 4:
            request_id, = req_args
            return f"IssuePrefetchRequest({request_id})"
        if instruction_index == 5:
            return "SaveRequest()"

    if instruction_class == 2002:  # CUTSCENE
        if instruction_index == 2:
            cutscene_id, playback_method, warp_region_id, block_id, sub_id = req_args
            skippable = True if playback_method in (0, 8) else False
            fade_out = True if playback_method in (8, 10) else False
            return (f"PlayCutscene(cutscene_id={cutscene_id}, skippable={skippable}, fade_out={fade_out}, "
                    f"warp_to_region={warp_region_id}, warp_to_map={GAME_MAPS[(int(block_id), int(sub_id))]})")
        if instruction_index == 3:
            cutscene_id, playback_method, player_id = req_args
            skippable = True if playback_method in (0, 8) else False
            fade_out = True if playback_method in (8, 10) else False
            return (f"PlayCutscene(cutscene_id={cutscene_id}, skippable={skippable}, fade_out={fade_out}, "
                    f"player_id={player_id})")
        if instruction_index == 4:
            cutscene_id, playback_method, warp_region_id, block_id, sub_id, player_id = req_args
            skippable = True if playback_method in (0, 8) else False
            fade_out = True if playback_method in (8, 10) else False
            return (f"PlayCutscene(cutscene_id={cutscene_id}, skippable={skippable}, fade_out={fade_out}, "
                    f"player_id={player_id}, warp_to_region={warp_region_id}, "
                    f"warp_to_map={GAME_MAPS[(int(block_id), int(sub_id))]})")
        if instruction_index == 5:
            cutscene_id, playback_method, x_axis, z_axis, rotation, y_trans, player_id = req_args
            skippable = True if playback_method in (0, 8) else False
            fade_out = True if playback_method in (8, 10) else False
            return (f"PlayCutscene(cutscene_id={cutscene_id}, skippable={skippable}, fade_out={fade_out}, "
                    f"player_id={player_id}, rotation={rotation}, relative_rotation_axis_x={x_axis}, "
                    f"relative_rotation_axis_z={z_axis}, vertical_translation={y_trans})")

    if instruction_class == 2003:  # EVENT
        if instruction_index == 1:
            entity_id, animation_id, loop, wait = req_args
            return f"RequestAnimation({entity_id}, {animation_id}, loop={bool(loop)}, wait_for_completion={bool(wait)})"
        if instruction_index == 2:
            flag_id, state = req_args
            if state == 1:
                return f"EnableFlag({flag_id})"
            elif state == 0:
                return f"DisableFlag({flag_id})"
            else:
                return f"SetFlagState({flag_id}, {state})"
        if instruction_index == 3:
            spawner_id, state = req_args
            if state == 1:
                return f"EnableSpawner({spawner_id})"
            elif state == 0:
                return f"DisableSpawner({spawner_id})"
        if instruction_index == 4:
            item_lot, = req_args
            return f"AwardItemLot({item_lot}, host_only=False)"
        if instruction_index == 5:
            owner_id, projectile_id, model_point, behavior_id, x, y, z = req_args
            return (f"ShootProjectile(owner_entity={owner_id}, projectile_id={projectile_id}, "
                    f"model_point={model_point}, behavior_id={behavior_id}, "
                    f"launch_angle_x={x}, launch_angle_y={y}, launch_angle_z={z})")
        if instruction_index == 8:
            event_id, slot, end_type = req_args
            if end_type:
                return f"RestartEvent({event_id}, slot={slot})"
            else:
                return f"StopEvent({event_id}, slot={slot})"
        if instruction_index == 11:
            state, boss_id, health_bar_slot, name_id = req_args
            if state == 1:
                return f"EnableBossHealthBar({boss_id}, name_id={name_id}, slot={health_bar_slot})"
            elif state == 0:
                # Name and slot are not used here (all health bars are disabled at once).
                return f"DisableBossHealthBar({boss_id}, name_id={name_id}, slot={health_bar_slot})"
        if instruction_index == 12:
            game_area_param_id, = req_args
            return f"KillBoss({game_area_param_id})"
        if instruction_index == 13:
            navimesh_id, navimesh_type, bitop = req_args
            navimesh_type = ENUM_NAVIMESH_TYPE[navimesh_type]
            if bitop == 2:
                return f"ToggleNavimeshType({navimesh_id}, {navimesh_type})"
            elif bitop == 1:
                return f"DisableNavimeshType({navimesh_id}, {navimesh_type})"
            elif bitop == 0:
                return f"EnableNavimeshType({navimesh_id}, {navimesh_type})"
        if instruction_index == 14:
            block_id, sub_id, player_entity_id = req_args
            return f"WarpToMap({GAME_MAPS[(int(block_id), int(sub_id))]}, player_entity_id={player_entity_id})"
        if instruction_index == 16:
            multiplayer_event_id, = req_args
            return f"TriggerMultiplayerEvent({multiplayer_event_id})"
        if instruction_index == 17:
            first_flag, last_flag, state = req_args
            if state == 1:
                return f"EnableRandomFlagInRange({first_flag}, {last_flag})"
            elif state == 0:
                return f"DisableRandomFlagInRange({first_flag}, {last_flag})"
        if instruction_index == 18:
            entity_id, animation_id, loop, wait, skip_transition = req_args
            return (f"ForceAnimation({entity_id}, {animation_id}, loop={bool(loop)}, wait_for_completion={bool(wait)}, "
                    f"skip_transition={bool(skip_transition)})")
        if instruction_index == 19:
            block_id, drawparam_slot = req_args
            return f"SetMapDrawParamSlot({block_id}, slot={drawparam_slot})"
        if instruction_index == 21:
            return "IncrementNewGameCycle()"
        if instruction_index == 22:
            first_flag, last_flag, state = req_args
            if state == 1:
                return f"EnableFlagRange({first_flag}, {last_flag})"
            elif state == 0:
                return f"DisableFlagRange({first_flag}, {last_flag})"
        if instruction_index == 23:
            respawn_point_id, = req_args
            return f"SetRespawnPoint({respawn_point_id})"
        if instruction_index == 24:
            item_type, item_id, quantity = req_args
            try:
                item_type = ENUM_ITEM_TYPE[item_type]
            except KeyError:
                if quantity > 0:
                    return f"RemoveItemFromPlayer({item_id}, item_type={item_type}, quantity={quantity})"
                return f"RemoveItemFromPlayer({item_id}, item_type={item_type})"
            if quantity > 0:
                return f"Remove{item_type}FromPlayer({item_id}, quantity={quantity})"
            return f"Remove{item_type}FromPlayer({item_id})"
        if instruction_index == 25:
            sign_type, character, region_id, summon_flag, dismissal_flag = req_args
            sign_type = ENUM_SIGN_TYPE[sign_type]
            return (f"PlaceSummonSign({sign_type}, {character}, region={region_id}, summon_flag={summon_flag}, "
                    f"dismissal_flag={dismissal_flag})")
        if instruction_index == 26:
            tip_message_id, state = req_args
            if state == 1:
                return f"EnableDeveloperMessage({tip_message_id})"
            elif state == 0:
                return f"DisableDeveloperMessage({tip_message_id})"
            else:
                return f"SetDeveloperMessageState({tip_message_id}, visible={state})"
        if instruction_index == 28:
            achievement_id, = req_args
            return f"AwardAchievement({achievement_id})"
        if instruction_index == 30:
            is_disabled, = req_args
            if is_disabled:
                return "DisableVagrantSpawning()"
            else:
                return "EnableVagrantSpawning()"
        if instruction_index == 31:
            flag_id, bit_count, max_value = req_args
            return f"IncrementEventValue({flag_id}, bit_count={bit_count}, max_value={max_value})"
        if instruction_index == 32:
            flag_id, bit_count = req_args
            return f"ClearEventValue({flag_id}, bit_count={bit_count})"
        if instruction_index == 33:
            next_snuggly_flag, = req_args
            return f"SetNextSnugglyTrade({next_snuggly_flag})"
        if instruction_index == 34:
            item_lot_id, region_id, flag_id, hitbox_id = req_args
            return f"SnugglyItemDrop({item_lot_id}, region={region_id}, flag={flag_id}, hitbox={hitbox_id})"
        if instruction_index == 35:
            source_region, dest_region = req_args
            return f"MoveRemains(source_region={source_region}, destination_region={dest_region})"
        if instruction_index == 36:
            item_lot_id, = req_args
            return f"AwardItemLot({item_lot_id}, host_only=True)"
        if instruction_index == 37:
            return "ArenaRankingRequest1v1()"
        if instruction_index == 38:
            return "ArenaRankingRequest2v2()"
        if instruction_index == 39:
            return "ArenaRankingRequestFFA()"
        if instruction_index == 40:
            return "ArenaExitRequest()"
        if instruction_index == 41:
            block_id, sub_id, y, target_model_id = req_args
            game_map = GAME_MAPS[(int(block_id), int(sub_id))]
            return f"ActivateKillplane(game_map={game_map}, y_threshold={y}, target_model_id={target_model_id})"
    
    if instruction_class == 2004:  # CHARACTER
        if instruction_index == 1:
            character, state = req_args
            if state == 1:
                return f"EnableAI({character})"
            elif state == 0:
                return f"DisableAI({character})"
            else:
                return f"SetAIState({character}, {state})"
        if instruction_index == 2:
            character, team_type = req_args
            team_type = ENUM_TEAM_TYPE[team_type]
            return f"SetTeamType({character}, {team_type})"
        if instruction_index == 3:
            character, destination_type, destination_id, model_point = req_args
            destination_type = ENUM_CATEGORY[destination_type]
            return (f"WarpToEntity({character}, destination={destination_id}, model_point={model_point}, "
                    f"destination_type={destination_type})")
        if instruction_index == 4:
            character, award_souls = req_args
            return f"Kill({character}, award_souls={bool(award_souls)})"
        if instruction_index == 5:
            character, state = req_args
            if state == 1:
                return f"EnableCharacter({character})"
            elif state == 0:
                return f"DisableCharacter({character})"
            else:
                return f"SetCharacterState({character}, {state})"
        if instruction_index == 6:
            character, command_id, slot = req_args
            return f"EzstateAIRequest({character}, command_id={command_id}, slot={slot})"
        if instruction_index == 7:
            entity_id, = req_args
            return f"CreateSpawner({entity_id})"
        if instruction_index == 8:
            character, special_effect_id = req_args
            return f"AddSpecialEffect({character}, {special_effect_id})"
        if instruction_index == 9:
            character, standby, damage, cancel, death, standby_return = req_args
            if standby == damage == cancel == death == standby_return == -1:
                return f"ResetStandbyAnimationSettings({character})"
            args = f"{character}"
            for name, a in (('standby', standby), ('damage', damage), ('cancel', cancel), ('death', death),
                            ('standby_return', standby_return)):
                if a != -1:
                    args += f", {name}_animation={a}"
            return f"SetStandbyAnimationSettings({args})"
        if instruction_index == 10:
            character, state = req_args
            if state == 1:
                return f"EnableGravity({character})"
            elif state == 0:
                return f"DisableGravity({character})"
            else:
                return f"SetGravityState({character}, {state})"
        if instruction_index == 12:
            character, state = req_args
            if state == 1:
                return f"EnableImmortality({character})"
            elif state == 0:
                return f"DisableImmortality({character})"
            else:
                return f"SetImmortalityState({character}, {state})"
        if instruction_index == 13:
            character, nest_region = req_args
            return f"SetNest({character}, {nest_region})"
        if instruction_index == 14:
            character, target_entity_id = req_args
            return f"RotateToFaceEntity({character}, {target_entity_id})"
        if instruction_index == 15:
            character, state = req_args
            if state == 1:
                return f"EnableInvincibility({character})"
            elif state == 0:
                return f"DisableInvincibility({character})"
            else:
                return f"SetInvincibilityState({character}, {state})"
        if instruction_index == 16:
            character, = req_args
            return f"ClearTargetList({character})"
        if instruction_index == 17:
            character, command_id, slot = req_args
            return f"AICommand({character}, command_id={command_id}, slot={slot})"
        if instruction_index == 18:
            character, region_id, reaction_range = req_args
            return f"SetEventPoint({character}, region_id={region_id}, reaction_range={reaction_range})"
        if instruction_index == 19:
            character, ai_id = req_args
            return f"SetAIParamID({character}, {ai_id})"
        if instruction_index == 20:
            character, = req_args
            return f"ReplanAI({character})"
        if instruction_index == 21:
            character, special_effect_id = req_args
            return f"CancelSpecialEffect({character}, {special_effect_id})"
        if instruction_index == 22:
            character, part_npc_type, part_index, part_hp, \
                damage_correction, body_damage_correction, invincible, start_in_stop_state = req_args
            return (f"CreateNPCPart({character}, part_npc_type={part_npc_type}, part_index={part_index}, "
                    f"part_health={part_hp}, damage_correction={damage_correction}, "
                    f"body_damage_correction={body_damage_correction}, is_invincible={invincible}, "
                    f"start_in_stop_state={start_in_stop_state})")
        if instruction_index == 23:
            character, part_npc_type, desired_hp, overwrite_max = req_args
            return (f"SetNPCPartHealth({character}, part_npc_type={part_npc_type}, "
                    f"desired_hp={desired_hp}, overwrite_max={overwrite_max})")
        if instruction_index == 24:
            character, part_npc_type, material_special_effect_id, material_fx_id = req_args
            return (f"SetNPCPartEffects({character}, part_npc_type={part_npc_type}, "
                    f"material_special_effect_id={material_special_effect_id}, material_fx_id={material_fx_id})")
        if instruction_index == 25:
            character, part_npc_type, bullet_scaling = req_args
            return (f"SetNPCPartBulletDamageScaling({character}, part_npc_type={part_npc_type}, "
                    f"desired_scaling={bullet_scaling})")
        if instruction_index == 26:
            character, bit_index, switch_type = req_args
            return f"SetDisplayMask({character}, bit_index={bit_index}, switch_type={switch_type})"
        if instruction_index == 27:
            character, bit_index, switch_type = req_args
            return f"SetHitboxMask({character}, bit_index={bit_index}, switch_type={switch_type})"
        if instruction_index == 28:
            character, update_auth_type = req_args
            update_auth_type = ENUM_UPDATE_AUTH[update_auth_type]
            return f"SetNetworkUpdateAuthority({character}, {update_auth_type})"
        if instruction_index == 29:
            character, remove = req_args
            if remove:
                return f"DisableBackread({character})"
            else:
                return f"EnableBackread({character})"
        if instruction_index == 30:
            character, state = req_args
            if state == 1:
                return f"EnableHealthBar({character})"
            elif state == 0:
                return f"DisableHealthBar({character})"
            else:
                return f"SetHealthBarState({character}, {state})"
        if instruction_index == 31:
            character, disabled = req_args
            if disabled == 1:
                return f"DisableCollision({character})"
            elif disabled == 0:
                return f"EnableCollision({character})"
            else:
                return f"SetCollisionState({character}, is_disabled={disabled})"
        if instruction_index == 32:
            character, command_id, slot, start_flag, end_flag = req_args
            return (f"AIEvent({character}, command_id={command_id}, slot={slot}, "
                    f"first_event_flag={start_flag}, last_event_flag={end_flag})")
        if instruction_index == 33:
            character, target_entity_id = req_args
            return f"ReferDamageToEntity({character}, {target_entity_id})"
        if instruction_index == 34:
            character, is_fixed, frequency = req_args
            frequency = ENUM_CHARACTER_UPDATE_RATE[frequency]
            return f"SetNetworkUpdateRate({character}, is_fixed={is_fixed}, frequency={frequency})"
        if instruction_index == 35:
            character, state = req_args
            return f"SetBackreadStateAlternate({character}, desired_state={state})"
        if instruction_index == 36:
            character, object_id, animation_id = req_args
            return f"HellkiteBreathControl({character}, obj={object_id}, animation_id={animation_id})"
        if instruction_index == 37:
            character, = req_args
            return f"DropMandatoryTreasure({character})"
        if instruction_index == 38:
            return "BetrayCurrentCovenant()"
        if instruction_index == 39:
            character, state = req_args
            if state == 1:
                return f"EnableAnimations({character})"
            elif state == 0:
                return f"DisableAnimations({character})"
            else:
                return f"SetAnimationsState({character}, {state})"
        if instruction_index == 40:
            character, destination_type, destination_id, model_point, hitbox_id = req_args
            destination_type = ENUM_CATEGORY[destination_type]
            return (f"WarpToEntity({character}, destination={destination_id}, "
                    f"destination_type={destination_type}, model_point={model_point}, "
                    f"set_draw_hitbox={hitbox_id})")
        if instruction_index == 41:
            character, destination_type, destination_id, model_point = req_args
            destination_type = ENUM_CATEGORY[destination_type]
            return (f"WarpToEntity({character}, destination={destination_id}, "
                    f"destination_type={destination_type}, model_point={model_point}, short_warp=True)")
        if instruction_index == 42:
            character, destination_type, destination_id, model_point, copy_hitbox = req_args
            destination_type = ENUM_CATEGORY[destination_type]
            return (f"WarpToEntity({character}, destination={destination_id}, "
                    f"destination_type={destination_type}, model_point={model_point}, "
                    f"copy_draw_hitbox={copy_hitbox})")
        if instruction_index == 43:
            character, disable_interpolation = req_args
            return f"ResetAnimation({character}, disable_interpolation={bool(disable_interpolation)})"
        if instruction_index == 44:
            character, team_type = req_args
            team_type = ENUM_TEAM_TYPE[team_type]
            return f"SetTeamTypeAndExitStandbyAnimation({character}, {team_type})"
        if instruction_index == 45:
            character, initial_humanity_flag_id = req_args
            return f"HumanityRegistration({character}, {initial_humanity_flag_id})"
        if instruction_index == 46:
            return "IncrementPvPSin()"
        if instruction_index == 47:
            return "EqualRecovery()"

    if instruction_class == 2005:  # OBJECT
        if instruction_index == 1:
            obj, slot = req_args
            if slot == 0:
                return f"DestroyObject({obj})"
            else:
                return f"DestroyObject({obj}, slot={slot})"
        if instruction_index == 2:
            obj, = req_args
            return f"RestoreObject({obj})"
        if instruction_index == 3:
            obj, state = req_args
            if state == 1:
                return f"EnableObject({obj})"
            elif state == 0:
                return f"DisableObject({obj})"
            else:
                return f"SetObjectState({obj}, {state})"
        if instruction_index == 4:
            obj, state = req_args
            if state == 1:
                return f"EnableTreasure({obj})"
            elif state == 0:
                return f"DisableTreasure({obj})"
            else:
                return f"SetTreasureState({obj}, {state})"
        if instruction_index == 5:
            obj, objact_id, relative_idx = req_args
            return f"ActivateObject({obj}, objact_param_id={objact_id}, relative_idx={relative_idx})"
        if instruction_index == 6:
            obj, objact_id, state = req_args
            if state == 1:
                return f"EnableObjectActivation({obj}, objact_param_id={objact_id})"
            elif state == 0:
                return f"DisableObjectActivation({obj}, objact_param_id={objact_id})"
        if instruction_index == 7:
            # I have not wrapped this instruction. Just using standard EndOfAnimation (as the game does).
            obj, animation_id = req_args
            return f"EndOfAnimation({obj}, {animation_id})"
        if instruction_index == 8:
            obj, slot = req_args
            return f"PostDestruction({obj}, slot={slot})"
        if instruction_index == 9:
            obj_flag, obj, model_point, behavior_id, anchor_type, radius, life, repetition_time = req_args
            anchor_type = ENUM_DAMAGE_TARGET_TYPE[anchor_type]
            return (f"CreateHazard({obj_flag}, {obj}, model_point={model_point}, behavior_param_id={behavior_id}, "
                    f"target_type={anchor_type}, radius={radius}, life={life}, repetition_time={repetition_time})")
        if instruction_index == 10:
            obj, block_id, sub_id, statue_type = req_args
            statue_type = ENUM_STATUE_TYPE[statue_type]
            return f"RegisterStatue({obj}, {GAME_MAPS[(int(block_id), int(sub_id))]}, {statue_type})"
        if instruction_index == 11:
            obj, character, model_point = req_args
            return f"WarpObjectToCharacter({obj}, character={character}, model_point={model_point})"
        if instruction_index == 12:
            obj_flag, = req_args
            return f"RemoveObjectFlag({obj_flag})"
        if instruction_index == 13:
            obj, state = req_args
            if state == 1:
                return f"EnableObjectInvulnerability({obj})"
            elif state == 0:
                return f"DisableObjectInvulnerability({obj})"
        if instruction_index == 14:
            obj, objact_id, relative_idx, state = req_args
            if state == 1:
                return f"EnableObjectActivation({obj}, objact_param_id={objact_id}, relative_idx={relative_idx})"
            elif state == 0:
                return f"DisableObjectActivation({obj}, objact_param_id={objact_id}, relative_idx={relative_idx})"
        if instruction_index == 15:
            obj, = req_args
            return f"EnableTreasureCollection({obj})"

    if instruction_class == 2006:  # SFX
        if instruction_index == 1:
            fx_id, erase_root_only = req_args
            return f"DeleteFX({fx_id}, erase_root_only={bool(erase_root_only)})"
        if instruction_index == 2:
            fx_id, = req_args
            return f"CreateFX({fx_id})"
        if instruction_index == 3:
            anchor_type, anchor_entity_id, model_point, fx_id = req_args
            anchor_type = ENUM_CATEGORY[anchor_type]
            return (f"CreateTemporaryFX({fx_id}, anchor_entity={anchor_entity_id}, "
                    f"anchor_type={anchor_type}, model_point={model_point})")
        if instruction_index == 4:
            obj, model_point, fx_id = req_args
            return f"CreateObjectFX({fx_id}, obj={obj}, model_point={model_point})"
        if instruction_index == 5:
            obj, erase_root = req_args
            return f"DeleteObjectFX({obj}, erase_root={bool(erase_root)})"

    if instruction_class == 2007:  # MESSAGE
        if instruction_index == 1:
            text_id, button_type, number_buttons, entity_id, display_distance = req_args
            button_type = ENUM_BUTTON_TYPE[button_type]
            number_buttons = ENUM_BUTTON_NUMBER[number_buttons]
            return (f"DisplayDialog({text_id}, anchor_entity={entity_id}, display_distance={display_distance}, "
                    f"button_type={button_type}, number_buttons={number_buttons})")
        if instruction_index == 2:
            banner_type, = req_args
            banner_type = ENUM_TEXT_BANNER_TYPE[banner_type]
            return f"DisplayBanner({banner_type})"
        if instruction_index == 3:
            text_id, pad_enabled = req_args
            return f"DisplayStatus({text_id}, pad_enabled={bool(pad_enabled)})"
        if instruction_index == 4:
            text_id, location = req_args
            return f"DisplayBattlefieldMessage({text_id}, display_location_index={location})"
        if instruction_index == 5:
            return "ArenaSetNametag1()"
        if instruction_index == 6:
            return "ArenaSetNametag2()"
        if instruction_index == 7:
            return "ArenaSetNametag3()"
        if instruction_index == 8:
            return "ArenaSetNametag4()"
        if instruction_index == 9:
            text_id, = req_args
            return f"DisplayArenaDissolutionMessage({text_id})"

    if instruction_class == 2008:  # CAMERA
        if instruction_index == 3:
            block_id, sub_id, camera_slot = req_args
            return f"SetLockedCameraSlot({GAME_MAPS[(int(block_id), int(sub_id))]}, {camera_slot})"

    if instruction_class == 2009:  # SCRIPT
        if instruction_index == 0:
            on_flag, off_flag, ladder = req_args
            return f"RegisterLadder(start_climbing_flag={on_flag}, stop_climbing_flag={off_flag}, obj={ladder})"
        if instruction_index == 3:
            bonfire_flag, obj, reaction_distance, reaction_angle, kindle = req_args
            return (f"RegisterBonfire({bonfire_flag}, obj={obj}, reaction_distance={reaction_distance}, "
                    f"reaction_angle={reaction_angle}, initial_kindle_level={kindle})")
        if instruction_index == 4:
            npc_id, = req_args
            return f"ActivateMultiplayerBuffs({npc_id})"
        if instruction_index == 6:
            return "NotifyBossBattleStart()"

    if instruction_class == 2010:  # SOUND
        if instruction_index == 2:
            anchor_entity_id, sound_type, sound_id = req_args
            sound_type = ENUM_SOUND_TYPE[sound_type]
            return f"PlaySoundEffect(anchor_entity={anchor_entity_id}, sound_type={sound_type}, sound_id={sound_id})"
        if instruction_index == 3:
            sound_id, state = req_args
            if state == 1:
                return f"EnableMapSound({sound_id})"
            elif state == 0:
                return f"DisableMapSound({sound_id})"
            else:
                return f"SetMapSoundState({sound_id}, {state})"

    if instruction_class == 2011:  # ヒット
        if instruction_index == 1:
            hitbox_id, state = req_args
            if state == 1:
                return f"EnableHitbox({hitbox_id})"
            elif state == 0:
                return f"DisableHitbox({hitbox_id})"
            else:
                return f"SetHitboxState({hitbox_id}, {state})"

    if instruction_class == 2012:  # マップ
        if instruction_index == 1:
            map_part_id, state = req_args
            if state == 1:
                return f"EnableMapPart({map_part_id})"
            elif state == 0:
                return f"DisableMapPart({map_part_id})"
            else:
                return f"SetMapPartState({map_part_id}, {state})"

    if instruction_class == 1000:  # 【実行制御】システム
        if instruction_index == 1:
            skip_count, state, condition = req_args
            if state == 1:
                return f"SkipLinesIfConditionTrue({skip_count}, {condition})"
            elif state == 0:
                return f"SkipLinesIfConditionFalse({skip_count}, {condition})"
        if instruction_index == 2:
            end_type, state, condition = req_args
            if end_type:
                if state == 1:
                    return f"RestartIfConditionTrue({condition})"
                elif state == 0:
                    return f"RestartIfConditionFalse({condition})"
            else:
                if state == 1:
                    return f"EndIfConditionTrue({condition})"
                elif state == 0:
                    return f"EndIfConditionFalse({condition})"
        if instruction_index == 3:
            skip_count, = req_args
            return f"SkipLines({skip_count})"
        if instruction_index == 4:
            end_type, = req_args
            if end_type:
                return "Restart()"
            else:
                return "End()"
        if instruction_index == 5:
            skip_count, comparison_type, left, right = req_args
            comparison_type = ENUM_COMPARISON_TYPE[comparison_type]
            return f"SkipLinesIf{comparison_type}({skip_count}, left_value={left}, right_value={right})"
        if instruction_index == 6:
            end_type, comparison_type, left, right = req_args
            comparison_type = ENUM_COMPARISON_TYPE[comparison_type]
            if end_type:
                return f"RestartIf{comparison_type}(left_value={left}, right_value={right})"
            else:
                return f"EndIf{comparison_type}(left_value={left}, right_value={right})"
        if instruction_index == 7:
            skip_count, state, condition = req_args
            if state == 1:
                return f"SkipLinesIfFinishedConditionTrue({skip_count}, {condition})"
            elif state == 0:
                return f"SkipLinesIfFinishedConditionFalse({skip_count}, {condition})"
        if instruction_index == 8:
            end_type, state, condition = req_args
            if end_type:
                if state == 1:
                    return f"RestartIfFinishedConditionTrue({condition})"
                elif state == 0:
                    return f"RestartIfFinishedConditionFalse({condition})"
            else:
                if state == 1:
                    return f"EndIfFinishedConditionTrue({condition})"
                elif state == 0:
                    return f"EndIfFinishedConditionFalse({condition})"
        if instruction_index == 9:
            seconds, = req_args
            return f"WaitForNetworkApproval(max_seconds={seconds})"
    if instruction_class == 1001:  # 実行制御】タイマー
        if instruction_index == 0:
            seconds, = req_args
            return f"Wait({seconds})"
        if instruction_index == 1:
            frames, = req_args
            return f"WaitFrames({frames})"
        if instruction_index == 2:
            min_seconds, max_seconds = req_args
            return f"WaitRandomSeconds(min_seconds={min_seconds}, max_seconds={max_seconds})"
    if instruction_class == 1003:  # 【実行制御】イベント
        if instruction_index == 1:
            skip_count, state, flag_type, flag_id = req_args
            state = 'On' if state else 'Off'
            if flag_type == 0:
                return f"SkipLinesIfFlag{state}({skip_count}, {flag_id})"
            elif flag_type == 1:
                return f"SkipLinesIfThisEvent{state}({skip_count})"
            elif flag_type == 2:
                return f"SkipLinesIfThisEventSlot{state}({skip_count})"
        if instruction_index == 2:
            end_type, state, flag_type, flag_id = req_args
            state = 'On' if state else 'Off'
            end_type = 'Restart' if end_type else 'End'
            if flag_type == 0:
                return f"{end_type}IfFlag{state}({flag_id})"
            elif flag_type == 1:
                return f"{end_type}IfThisEvent{state}()"
            elif flag_type == 2:
                return f"{end_type}IfThisEventSlot{state}()"
        if instruction_index == 3:
            skip_count, state, flag_type, first_flag, last_flag = req_args
            state = ENUM_LOGICAL_OPERATION_TYPE[state]
            if flag_type == 0:
                return f"SkipLinesIfFlagRange{state}({skip_count}, {first_flag}, {last_flag})"
            else:
                raise ValueError(f"Did not expect to encounter flag type {flag_type} for FlagRange instruction.")
        if instruction_index == 4:
            end_type, state, flag_type, first_flag, last_flag = req_args
            state = ENUM_LOGICAL_OPERATION_TYPE[state]
            end_type = 'Restart' if end_type else 'End'
            if flag_type == 0:
                return f"{end_type}IfFlagRange{state}({first_flag}, {last_flag})"
            else:
                raise ValueError(f"Did not expect to encounter flag type {flag_type} for FlagRange instruction.")
        if instruction_index == 5:
            skip_count, multiplayer_state = req_args
            multiplayer_state = ENUM_MULTIPLAYER_STATE[multiplayer_state]
            return f"SkipLinesIf{multiplayer_state}({skip_count})"
        if instruction_index == 6:
            end_type, multiplayer_state = req_args
            multiplayer_state = ENUM_MULTIPLAYER_STATE[multiplayer_state]
            end_type = 'Restart' if end_type else 'End'
            return f"{end_type}If{multiplayer_state}()"
        if instruction_index == 7:
            skip_count, state, block_id, sub_id = req_args
            game_map = GAME_MAPS[(int(block_id), int(sub_id))]
            state = 'Inside' if state else 'Outside'
            return f"SkipLinesIf{state}Map({skip_count}, {game_map})"
        if instruction_index == 8:  # マップIDでイベント終了
            end_type, state, block_id, sub_id = req_args
            game_map = GAME_MAPS[(int(block_id), int(sub_id))]
            state = 'Inside' if state else 'Outside'
            end_type = 'Restart' if end_type else 'End'
            return f"{end_type}If{state}Map({game_map})"

    if instruction_class == 1005:  # 【実行制御】オブジェクト
        if instruction_index == 1:
            skip_count, destroyed_state, obj = req_args
            destroyed_state = 'Destroyed' if destroyed_state else 'NotDestroyed'
            return f"SkipLinesIfObject{destroyed_state}({skip_count}, {obj})"
        if instruction_index == 2:
            end_type, destroyed_state, obj = req_args
            destroyed_state = 'Destroyed' if destroyed_state else 'NotDestroyed'
            end_type = 'Restart' if end_type else 'End'
            return f"{end_type}IfObject{destroyed_state}({obj})"

    if instruction_class == 0:  # 《条件登録》システム
        if instruction_index == 0:
            target_condition, state, source_condition = req_args
            state = 'True' if state else 'False'
            return f"IfCondition{state}({target_condition}, input_condition={source_condition})"

    if instruction_class == 1:  # 《条件登録》タイマー
        if instruction_index == 0:
            target_condition, seconds = req_args
            return f"IfTimeElapsed({target_condition}, {seconds})"
        if instruction_index == 1:
            target_condition, frames = req_args
            return f"IfFramesElapsed({target_condition}, {frames})"

    if instruction_class == 3:  # CONTROL (EVENT)
        if instruction_index == 0:
            target_condition, state, flag_type, flag_id = req_args
            if state == 1:
                state = 'On'
            elif state == 0:
                state = 'Off'
            else:
                if flag_type == 0:
                    return f"IfFlagState({target_condition}, {flag_id}, state={state})"
                elif flag_type == 1:
                    return f"IfThisEventState({target_condition}, state={state})"
                elif flag_type == 2:
                    return f"IfThisEventSlotState({target_condition}, state={state})"
            if flag_type == 0:
                return f"IfFlag{state}({target_condition}, {flag_id})"
            elif flag_type == 1:
                return f"IfThisEvent{state}({target_condition})"
            elif flag_type == 2:
                return f"IfThisEventSlot{state}({target_condition})"
        if instruction_index == 1:
            target_condition, state, flag_type, first_flag, last_flag = req_args
            state = ENUM_LOGICAL_OPERATION_TYPE[state]
            if flag_type == 0:
                return f"IfFlagRange{state}({target_condition}, {first_flag}, {last_flag})"
            else:
                raise ValueError(f"Did not expect to encounter flag type {flag_type} for FlagRange instruction.")
        if instruction_index == 2:
            target_condition, inside, entity, region = req_args
            state = 'Inside' if inside else 'Outside'
            if entity == 10000:
                return f"IfPlayer{state}Region({target_condition}, {region})"
            return f"IfEntity{state}Region({target_condition}, {entity}, {region})"
        if instruction_index == 3:
            target_condition, inside, entity, other_entity, radius = req_args
            state = 'Within' if inside else 'Beyond'
            if entity == 10000:
                return f"IfPlayer{state}Distance({target_condition}, {other_entity}, {radius})"
            return f"IfEntity{state}Distance({target_condition}, {entity}, {other_entity}, {radius})"
        if instruction_index == 4:
            target_condition, item_type, item_id, owns = req_args
            state = 'Owns' if owns else 'DoesNotOwn'
            try:
                item_type = ENUM_ITEM_TYPE[item_type]
            except KeyError:
                return f"IfPlayer{state}Item({target_condition}, {item_id}, item_type={item_type}, including_box=False)"
            return f"IfPlayer{state}{item_type}({target_condition}, {item_id}, including_box=False)"
        if instruction_index == 5:
            target_condition, anchor_type, anchor_entity, reaction_angle, model_point, \
                reaction_distance, text_id, reaction_attribute, pad_id = req_args
            anchor_type = ENUM_CATEGORY[anchor_type]
            model_point_arg = f'model_point={model_point}, ' if model_point != -1 else ''
            button_arg = f'button={pad_id}, ' if pad_id != 0 else ''
            human_or_hollow_only = True if reaction_attribute == 48 else False
            return (f"IfDialogPromptActivated({target_condition}, prompt_text={text_id}, "
                    f"anchor_entity={anchor_entity}, anchor_type={anchor_type}, facing_angle={reaction_angle}, "
                    f"max_distance={reaction_distance}, {model_point_arg}{button_arg}"
                    f"human_or_hollow_only={human_or_hollow_only})")
        if instruction_index == 6:
            target_condition, multiplayer_state = req_args
            multiplayer_state = ENUM_MULTIPLAYER_STATE[multiplayer_state]
            return f"If{multiplayer_state}({target_condition})"
        if instruction_index == 7:
            target_condition, inside, region = req_args
            state = 'Inside' if inside else 'Outside'
            return f"IfAllPlayers{state}Region({target_condition}, {region})"
        if instruction_index == 8:
            target_condition, inside, block_id, sub_id = req_args
            game_map = GAME_MAPS[(int(block_id), int(sub_id))]
            state = 'Inside' if inside else 'Outside'
            return f"If{state}Map({target_condition}, {game_map})"
        if instruction_index == 9:
            target_condition, multiplayer_event_id = req_args
            return f"IfMultiplayerEvent({target_condition}, {multiplayer_event_id})"
        if instruction_index == 10:
            target_condition, flag_type, first_flag, last_flag, comparison_type, comparison_value = req_args
            comparison_type = ENUM_COMPARISON_TYPE[comparison_type]
            return (f"IfTrueFlagCount{comparison_type}({target_condition}, {comparison_value}, "
                    f"{first_flag}, {last_flag})")
        if instruction_index == 11:
            target_condition, tendency_type, comparison_type, comparison_value = req_args
            tendency_type = 'Black' if tendency_type else 'White'
            if comparison_type == 4:
                return f"If{tendency_type}WorldTendencyGreaterThanOrEqual({target_condition}, {comparison_value})"
            return (f"If{tendency_type}WorldTendencyComparison({target_condition}, "
                    f"comparison_type_enum={comparison_type}, value={comparison_value})")
        if instruction_index == 12:
            target_condition, flag_id, bit_count, comparison_type, comparison_value = req_args
            if comparison_value == 0:
                return (f"IfEventValueEqual({target_condition}, {flag_id}, bit_count={bit_count}, "
                        f"value={comparison_value})")
            if comparison_type == 2:
                return (f"IfEventValueGreaterThan({target_condition}, {flag_id}, bit_count={bit_count}, "
                        f"value={comparison_value})")
            return (f"IfEventValueComparison({target_condition}, {flag_id}, bit_count={bit_count}, "
                    f"comparison_type_enum={comparison_type}, value={comparison_value})")
        if instruction_index == 13:
            target_condition, anchor_type, anchor_entity, reaction_angle, model_point, \
                reaction_distance, text_id, reaction_attribute, pad_id = req_args
            anchor_type = ENUM_CATEGORY[anchor_type]
            model_point_arg = f'model_point={model_point}, ' if model_point != -1 else ''
            button_arg = f'button={pad_id}, ' if pad_id != 0 else ''
            human_or_hollow_only = True if reaction_attribute == 48 else False
            return (f"IfDialogPromptActivated({target_condition}, prompt_text={text_id}, "
                    f"anchor_entity={anchor_entity}, anchor_type={anchor_type}, facing_angle={reaction_angle}, "
                    f"max_distance={reaction_distance}, {model_point_arg}{button_arg}"
                    f"human_or_hollow_only={human_or_hollow_only}, boss_version=True)")
        if instruction_index == 14:
            target_condition, region = req_args
            return f"IfAnyItemDroppedInRegion({target_condition}, {region})"
        if instruction_index == 15:
            target_condition, item_type, item_id = req_args
            return f"IfItemDropped({target_condition}, {item_id}, item_type={item_type})"
        if instruction_index == 16:
            target_condition, item_type, item_id, owns = req_args
            state = 'Owns' if owns else 'DoesNotOwn'
            try:
                item_type = ENUM_ITEM_TYPE[item_type]
            except KeyError:
                return f"IfPlayer{state}Item({target_condition}, {item_id}, item_type={item_type}, including_box=True)"
            return f"IfPlayer{state}{item_type}({target_condition}, {item_id}, including_box=True)"
        if instruction_index == 17:
            target_condition, comparison_type, completion_count = req_args
            if comparison_type == 0:
                return f"IfNewGameCycleThanOrEqual({target_condition}, {completion_count})"
            if comparison_type == 4:
                return f"IfNewGameCycleGreaterThanOrEqual({target_condition}, {completion_count})"
            return (f"IfNewGameCycleComparison({target_condition}, comparison_type_enum={comparison_type}, "
                    f"completion_count={completion_count})")
        if instruction_index == 18:
            target_condition, anchor_type, anchor_entity, reaction_angle, model_point, \
                reaction_distance, text_id, reaction_attribute, pad_id, line_intersects = req_args
            anchor_type = ENUM_CATEGORY[anchor_type]
            model_point_arg = f'model_point={model_point}, ' if model_point != -1 else ''
            button_arg = f'button={pad_id}, ' if pad_id != 0 else ''
            human_or_hollow_only = True if reaction_attribute == 48 else False
            return (f"IfDialogPromptActivated({target_condition}, prompt_text={text_id}, "
                    f"anchor_entity={anchor_entity}, anchor_type={anchor_type}, facing_angle={reaction_angle}, "
                    f"max_distance={reaction_distance}, {model_point_arg}{button_arg}"
                    f"human_or_hollow_only={human_or_hollow_only}, line_intersects={line_intersects})")
        if instruction_index == 19:
            target_condition, anchor_type, anchor_entity, reaction_angle, model_point, \
                reaction_distance, text_id, reaction_attribute, pad_id, line_intersects = req_args
            anchor_type = ENUM_CATEGORY[anchor_type]
            model_point_arg = f'model_point={model_point}, ' if model_point != -1 else ''
            button_arg = f'button={pad_id}, ' if pad_id != 0 else ''
            human_or_hollow_only = True if reaction_attribute == 48 else False
            return (f"IfDialogPromptActivated({target_condition}, prompt_text={text_id}, "
                    f"anchor_entity={anchor_entity}, anchor_type={anchor_type}, facing_angle={reaction_angle}, "
                    f"max_distance={reaction_distance}, {model_point_arg}{button_arg}"
                    f"human_or_hollow_only={human_or_hollow_only}, line_intersects={line_intersects}, "
                    f"boss_version=True)")
        if instruction_index == 20:
            target_condition, left_flag, left_bit_count, comparison_type, right_flag, right_bit_count = req_args
            return (f"IfEventComparison({target_condition}, {left_flag}, {left_bit_count}, {comparison_type}, "
                    f"{right_flag}, {right_bit_count})")
        if instruction_index == 21:
            target_condition, state = req_args
            if state == 1:
                return f"IfDLCOwned({target_condition})"
            elif state == 0:
                return f"IfDLCNotOwned({target_condition})"
        if instruction_index == 22:
            target_condition, state = req_args
            if state == 1:
                return f"IfOnline({target_condition})"
            elif state == 0:
                return f"IfOffline({target_condition})"

    if instruction_class == 4:  # CONTROL (CHARACTER)
        if instruction_index == 0:
            target_condition, character, is_dead = req_args
            if is_dead:
                return f"IfDead({target_condition}, {character})"
            else:
                return f"IfAlive({target_condition}, {character})"
        if instruction_index == 1:
            target_condition, attacked, attacker = req_args
            return f"IfAttacked({target_condition}, {attacked}, attacking_character={attacker})"
        if instruction_index == 2:
            target_condition, character, comparison_type, comparison_value = req_args
            comparison_type = ENUM_COMPARISON_TYPE[comparison_type]
            return f"IfHealth{comparison_type}({target_condition}, {character}, {comparison_value})"
        if instruction_index == 3:
            target_condition, character, character_type = req_args
            if character == 10000:
                character = 'PLAYER'
            character_type = ENUM_CHARACTER_TYPE[character_type]
            if character_type.endswith('hollow'):
                return f"IfCharacterHollow({target_condition}, {character})"
            if character_type.endswith('human'):
                return f"IfCharacterHuman({target_condition}, {character})"
            return f"IfCharacterType({target_condition}, {character}, {character_type})"
        if instruction_index == 4:
            target_condition, targeting_character, targeted_character, state = req_args
            state = '' if state else 'Not'
            return f"IfCharacter{state}Targeting({target_condition}, {targeting_character}, {targeted_character})"
        if instruction_index == 5:
            target_condition, character, special_effect, state = req_args
            state = 'Has' if state else 'DoesNotHave'
            if character == 10000:
                return f"IfPlayer{state}SpecialEffect({target_condition}, {special_effect})"
            return f"IfCharacter{state}SpecialEffect({target_condition}, {character}, {special_effect})"
        if instruction_index == 6:
            target_condition, character, npc_part_type, comparison_value, comparison_type = req_args
            if comparison_type == 5:
                return (f"IfCharacterPartHealthLessThanOrEqual({target_condition}, {character}, "
                        f"npc_part_type={npc_part_type}, value={comparison_value})")
            return (f"IfCharacterPartHealthComparison({target_condition}, {character}, "
                    f"npc_part_type={npc_part_type}, comparison_type_enum={comparison_type}, value={comparison_value})")
        if instruction_index == 7:
            target_condition, character, state = req_args
            state = 'Enabled' if state else 'Disabled'
            return f"IfBackread{state}({target_condition}, {character})"
        if instruction_index == 8:
            target_condition, character, tae_event_id, state = req_args
            state = 'Has' if state else 'DoesNotHave'
            return f"If{state}TAEEvent({target_condition}, {character}, tae_event_id={tae_event_id})"
        if instruction_index == 9:
            target_condition, character, ai_status = req_args
            ai_status = ENUM_AI_STATUS_TYPE[ai_status]
            return f"IfHasAIStatus({target_condition}, {character}, ai_status={ai_status})"
        if instruction_index == 10:
            target_condition, active = req_args
            state = 'Active' if active else 'NotActive'
            return f"IfSkullLantern{state}({target_condition})"
        if instruction_index == 11:
            target_condition, class_type = req_args
            class_type = ENUM_CLASS_TYPE.get(class_type, class_type)
            return f"IfPlayerClass({target_condition}, {class_type})"
        if instruction_index == 12:
            target_condition, covenant = req_args
            covenant = ENUM_COVENANT_TYPE.get(covenant, covenant)
            return f"IfPlayerCovenant({target_condition}, {covenant})"
        if instruction_index == 13:
            target_condition, comparison_type, comparison_value = req_args
            if comparison_type == 4:
                return f"IfPlayerSoulLevelGreaterThanOrEqual({target_condition}, {comparison_value})"
            if comparison_type == 5:
                return f"IfPlayerSoulLevelLessThanOrEqual({target_condition}, {comparison_value})"
            return f"IfPlayerSoulLevelComparison({target_condition}, {comparison_type}, {comparison_value})"
        if instruction_index == 14:
            target_condition, character, comparison_type, comparison_value = req_args
            comparison_type = ENUM_COMPARISON_TYPE[comparison_type]
            return f"IfHealthValue{comparison_type}({target_condition}, {character}, {comparison_value})"

    if instruction_class == 5:  # CONTROL (OBJECT)
        if instruction_index == 0:
            target_condition, destroyed_state, obj = req_args
            state = '' if destroyed_state else 'Not'
            return f"IfObject{state}Destroyed({target_condition}, {obj})"
        if instruction_index == 1:
            target_condition, obj, attacker = req_args
            return f"IfObjectDamagedBy({target_condition}, {obj}, attacker={attacker})"
        if instruction_index == 2:
            target_condition, objact_id = req_args
            return f"IfObjectActivated({target_condition}, objact_id={objact_id})"

    if instruction_class == 11:  # CONTROL (HITBOX)
        if instruction_index == 0:
            target_condition, hitbox_id = req_args
            return f"IfMovingOnHitbox({target_condition}, {hitbox_id})"
        if instruction_index == 1:
            target_condition, hitbox_id = req_args
            return f"IfRunningOnHitbox({target_condition}, {hitbox_id})"
        if instruction_index == 2:
            target_condition, hitbox_id = req_args
            return f"IfStandingOnHitbox({target_condition}, {hitbox_id})"

    # If no matching return statement exists, print the default (un-translated) representation.
    return default_readable(instruction_class, instruction_index, req_args, opt_args)
