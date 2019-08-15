""" Verbose output that matches EVS language for 'decompiling'. (Does not use IF blocks.) """
import struct
from soulstruct.events.core import boolify, get_enum_name, get_game_map_name, EnumStringError, InstructionNotFoundError


def all_numbers(*args):
    """ Returns True if all of the given args are ints or floats, and False otherwise. """
    return all([isinstance(a, (int, float)) for a in args])


def process_args(integer_args, arg_type_string):
    """ Re-interpret integer data as a given struct. """
    true_arg_type_string = arg_type_string.replace('s', 'I')
    packed = struct.pack(len(integer_args) * 'I', *integer_args)
    return struct.unpack('@' + true_arg_type_string, packed[:struct.calcsize(true_arg_type_string)])


def decompile_run_event_instruction(req_args, opt_args, arg_types):
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
                print(f"Event ID: {event_id}, args: {args}, arg_types: {arg_types}")
                raise
        return f"RunEvent({event_id}, slot={slot}, args={args}, arg_types='{arg_types}')"
    elif not opt_args and first_arg == 0:
        # NOTE: Some Bloodborne events use slots for events without optional arguments.
        if slot != 0:
            return f"RunEvent({event_id}, slot={slot})"
        return f"RunEvent({event_id})"
    else:
        # Assume all integers.
        return f"RunEvent({event_id}, slot={slot}, args={(first_arg, *opt_args)})"


def decompile_run_common_event_instruction(req_args, opt_args, arg_types):
    event_id, first_arg = req_args
    if arg_types:
        args = (first_arg, *opt_args)
        if not arg_types.replace('i', ''):
            # All signed integers (default).
            return f"RunCommonEvent({event_id}, args={args})"
        elif all(isinstance(i, int) for i in args):
            try:
                args = process_args(args, arg_types)
            except struct.error:
                print(f"Event ID: {event_id}, args: {args}, arg_types: {arg_types}")
                raise
        return f"RunCommonEvent({event_id}, args={args}, arg_types='{arg_types}')"
    elif not opt_args and first_arg == 0:
        return f"RunCommonEvent({event_id})"
    else:
        # Assume all integers.
        return f"RunCommonEvent({event_id}, args={(first_arg, *opt_args)})"


def decompile_instruction(game_module, instruction_class, instruction_index, req_args, opt_args, arg_types=None):
    """ Restores low-level EVS language instructions and tests. Not intelligent enough to create IF blocks, though.

    This function only parses instructions from the 'shared' module, which are common to all games. However, it will
    call additional an game-specific decompiler from the 'game_module' argument.
    """

    # Instructions that accept optional arguments (currently just 2000[00] and, for DS3, 2000[06]).

    if instruction_class == 2000:

        if instruction_index == 0:
            return decompile_run_event_instruction(req_args, opt_args, arg_types)

        if instruction_index == 6:
            if game_module.NAME != 'darksouls3':
                raise ValueError('Instruction 2000[06] can only be used in Dark Souls 3 (darksouls3 subpackage).')
            # DS3 only. Same as above, but takes no slot argument. Functional difference unknown.
            return decompile_run_common_event_instruction(req_args, opt_args, arg_types)

    # Remaining instructions do not accept optional arguments.

    if opt_args or arg_types:
        print(req_args, opt_args)
        raise ValueError(f"Command {instruction_class}[{instruction_index}] cannot use optional arguments.")

    # Check game module first.
    try:
        return game_module.decompiler.decompile_instruction(instruction_class, instruction_index, req_args, game_module)
    except InstructionNotFoundError:
        # Instruction not found in game-specific decompiler module. Try shared module below.
        pass

    if instruction_class == 2000:  # SYSTEM

        if instruction_index == 2:
            state, = req_args
            if state == 1:
                return "EnableNetworkSync()"
            elif state == 0:
                return "DisableNetworkSync()"
            return f"SetNetworkSync(state={state})"

        if instruction_index == 3:
            dummy_arg, = req_args
            return f"ClearMainCondition({dummy_arg})"

        if instruction_index == 4:
            request_id, = req_args
            return f"IssuePrefetchRequest({request_id})"

        if instruction_index == 5:
            return "SaveRequest()"

    if instruction_class == 2002:  # CUTSCENE

        if instruction_index == 2:
            cutscene_id, playback_method, move_region, area_id, block_id = req_args
            game_map = get_game_map_name(area_id, block_id, game_module)
            if not isinstance(playback_method, int):
                # My wrapper instruction cannot wrap a variable cutscene playback type.
                return (f"PlayCutsceneAndMovePlayer({cutscene_id}, playback_method={playback_method}, "
                        f"region={move_region}, game_map={game_map})")
            skippable = True if playback_method in (0, 8) else False
            fade_out = True if playback_method in (8, 10) else False
            return (f"PlayCutscene({cutscene_id}, skippable={skippable}, fade_out={fade_out}, "
                    f"move_to_region={move_region}, move_to_map={game_map})")

        if instruction_index == 3:
            cutscene_id, playback_method, player_id = req_args
            player_id = 'PLAYER' if player_id == 10000 else player_id
            if not isinstance(playback_method, int):
                # My wrapper instruction cannot wrap a variable cutscene playback type.
                return (f"PlayCutsceneToPlayer({cutscene_id}, playback_method={playback_method}, "
                        f"player_id={player_id})")
            skippable = True if playback_method in (0, 8) else False
            fade_out = True if playback_method in (8, 10) else False
            return f"PlayCutscene({cutscene_id}, skippable={skippable}, fade_out={fade_out}, player_id={player_id})"

        if instruction_index == 4:
            cutscene_id, playback_method, move_region, area_id, block_id, player_id = req_args
            game_map = get_game_map_name(area_id, block_id, game_module)
            player_id = 'PLAYER' if player_id == 10000 else player_id
            if not isinstance(playback_method, int):
                # My wrapper instruction cannot wrap a variable cutscene playback type.
                return (f"PlayCutsceneAndMoveSpecificPlayer({cutscene_id}, playback_method={playback_method}, "
                        f"player_id={player_id})")
            skippable = True if playback_method in (0, 8) else False
            fade_out = True if playback_method in (8, 10) else False
            return (f"PlayCutscene({cutscene_id}, skippable={skippable}, fade_out={fade_out}, "
                    f"player_id={player_id}, move_to_region={move_region}, move_to_map={game_map})")

        if instruction_index == 5:
            cutscene_id, playback_method, axis_x, axis_z, rotation, y_trans, player_id = req_args
            player_id = 'PLAYER' if player_id == 10000 else player_id
            if not isinstance(playback_method, int):
                # My wrapper instruction cannot wrap a variable cutscene playback type.
                return (f"PlayCutsceneAndRotatePlayer({cutscene_id}, playback_method={playback_method}, "
                        f"axis_x={axis_x}, axis_z={axis_z}, rotation={rotation}, vertical_translation={y_trans}, "
                        f"player_id={player_id})")
            skippable = True if playback_method in (0, 8) else False
            fade_out = True if playback_method in (8, 10) else False
            return (f"PlayCutscene(cutscene_id={cutscene_id}, skippable={skippable}, fade_out={fade_out}, "
                    f"player_id={player_id}, rotation={rotation}, relative_rotation_axis_x={axis_x}, "
                    f"relative_rotation_axis_z={axis_z}, vertical_translation={y_trans})")

    if instruction_class == 2003:  # EVENT

        if instruction_index == 1:
            entity_id, animation_id, loop, wait = req_args
            entity_id = 'PLAYER' if entity_id == 10000 else entity_id
            return (f"RequestAnimation({entity_id}, {animation_id}, loop={boolify(loop)}, "
                    f"wait_for_completion={boolify(wait)})")

        if instruction_index == 2:
            flag, state = req_args
            if state == 1:
                return f"EnableFlag({flag})"
            elif state == 0:
                return f"DisableFlag({flag})"
            return f"SetFlagState({flag}, state={state})"

        if instruction_index == 3:
            spawner_id, state = req_args
            if state == 1:
                return f"EnableSpawner({spawner_id})"
            elif state == 0:
                return f"DisableSpawner({spawner_id})"
            return f"SetSpawnerState({spawner_id}, state={boolify(state)})"

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
            if end_type == 1:
                return f"RestartEvent({event_id}, slot={slot})"
            elif end_type == 0:
                return f"StopEvent({event_id}, slot={slot})"
            return f"SetEventState({event_id}, slot={slot}, end_type={boolify(end_type)})"

        if instruction_index == 11:
            state, boss_id, slot, name = req_args
            if state == 1:
                return f"EnableBossHealthBar({boss_id}, name={name}, slot={slot})"
            elif state == 0:
                # Name and slot are not used here (all health bars are disabled at once).
                return f"DisableBossHealthBar({boss_id}, name={name}, slot={slot})"
            return f"SetBossHealthBarState({boss_id}, name={name}, slot={slot}, state={boolify(state)})"

        if instruction_index == 12:
            game_area_param_id, = req_args
            return f"KillBoss({game_area_param_id})"

        if instruction_index == 13:
            navimesh_id, navimesh_type, bitop = req_args
            navimesh_type = get_enum_name(game_module.NavimeshType, navimesh_type, True)
            if bitop == 2:
                return f"ToggleNavimeshType({navimesh_id}, {navimesh_type})"
            elif bitop == 1:
                return f"DisableNavimeshType({navimesh_id}, {navimesh_type})"
            elif bitop == 0:
                return f"EnableNavimeshType({navimesh_id}, {navimesh_type})"
            return f"SetNavimeshType({navimesh_id}, {navimesh_type}, {bitop})"

        if instruction_index == 14:
            area_id, block_id, destination_player_id = req_args
            game_map = get_game_map_name(area_id, block_id, game_module)
            return f"WarpToMap(game_map={game_map}, destination_player_id={destination_player_id})"

        if instruction_index == 16:
            multiplayer_event_id, = req_args
            return f"TriggerMultiplayerEvent({multiplayer_event_id})"

        if instruction_index == 17:
            first_flag, last_flag, state = req_args
            if state == 1:
                return f"EnableRandomFlagInRange(({first_flag}, {last_flag}))"
            elif state == 0:
                return f"DisableRandomFlagInRange(({first_flag}, {last_flag}))"
            return f"SetRandomFlagInRange(({first_flag}, {last_flag}), state={boolify(state)})"

        if instruction_index == 18:
            entity_id, animation_id, loop, wait, skip_transition = req_args
            entity_id = 'PLAYER' if entity_id == 10000 else entity_id
            keyword_args = []
            if loop != 0:
                keyword_args.append(f'loop={boolify(loop)}')
            if wait != 0:
                keyword_args.append(f'wait_for_completion={boolify(wait)}')
            if skip_transition != 0:
                keyword_args.append(f'skip_transition={boolify(skip_transition)}')
            keyword_args = ', '.join(keyword_args)
            if keyword_args:
                return f"ForceAnimation({entity_id}, {animation_id}, {keyword_args})"
            return f"ForceAnimation({entity_id}, {animation_id})"

        if instruction_index == 19:
            area_id, drawparam_slot = req_args
            return f"SetMapDrawParamSlot({area_id}, slot={drawparam_slot})"

        if instruction_index == 21:
            dummy_arg, = req_args
            return f"IncrementNewGameCycle({dummy_arg})"

        if instruction_index == 22:
            first_flag, last_flag, state = req_args
            if state == 1:
                return f"EnableFlagRange(({first_flag}, {last_flag}))"
            elif state == 0:
                return f"DisableFlagRange(({first_flag}, {last_flag}))"
            return f"SetFlagRange(({first_flag}, {last_flag}), state={boolify(state)})"

        if instruction_index == 23:
            respawn_point_id, = req_args
            return f"SetRespawnPoint({respawn_point_id})"

        if instruction_index == 24:
            item_type, item_id, quantity = req_args
            try:
                item_type = get_enum_name(game_module.ItemType, item_type).split('.')[-1]
            except EnumStringError:
                if quantity > 0:
                    return f"RemoveItemFromPlayer({item_id}, item_type={item_type}, quantity={quantity})"
                return f"RemoveItemFromPlayer({item_id}, item_type={item_type})"
            else:
                if quantity > 0:
                    return f"Remove{item_type}FromPlayer({item_id}, quantity={quantity})"
                return f"Remove{item_type}FromPlayer({item_id})"

        if instruction_index == 25:
            sign_type, character, region, summon_flag, dismissal_flag = req_args
            character = 'PLAYER' if character == 10000 else character
            sign_type = get_enum_name(game_module.SummonSignType, sign_type, True)
            return (f"PlaceSummonSign({sign_type}, {character}, region={region}, summon_flag={summon_flag}, "
                    f"dismissal_flag={dismissal_flag})")

        if instruction_index == 26:
            tip_message_id, state = req_args
            if state == 1:
                return f"EnableDeveloperMessage({tip_message_id})"
            elif state == 0:
                return f"DisableDeveloperMessage({tip_message_id})"
            return f"SetDeveloperMessageState({tip_message_id}, state={boolify(state)})"

        if instruction_index == 28:
            achievement_id, = req_args
            return f"AwardAchievement({achievement_id})"

        if instruction_index == 30:
            spawning_disabled, = req_args
            if spawning_disabled == 1:
                return "DisableVagrantSpawning()"
            elif spawning_disabled == 0:
                return "EnableVagrantSpawning()"
            return f"SetVagrantSpawning(spawning_disabled={boolify(spawning_disabled)})"

        if instruction_index == 31:
            flag, bit_count, max_value = req_args
            return f"IncrementEventValue({flag}, bit_count={bit_count}, max_value={max_value})"

        if instruction_index == 32:
            flag, bit_count = req_args
            return f"ClearEventValue({flag}, bit_count={bit_count})"

        if instruction_index == 33:
            next_snuggly_flag, = req_args
            return f"SetNextSnugglyTrade({next_snuggly_flag})"

        if instruction_index == 34:
            item_lot_id, region, flag, hitbox_id = req_args
            return f"SnugglyItemDrop({item_lot_id}, region={region}, flag={flag}, hitbox={hitbox_id})"

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

    if instruction_class == 2004:  # CHARACTER

        if instruction_index == 1:
            character, state = req_args
            character = 'PLAYER' if character == 10000 else character
            if state == 1:
                return f"EnableAI({character})"
            elif state == 0:
                return f"DisableAI({character})"
            return f"SetAIState({character}, state={state})"

        if instruction_index == 2:
            character, team_type = req_args
            character = 'PLAYER' if character == 10000 else character
            team_type = get_enum_name(game_module.TeamType, team_type, True)
            return f"SetTeamType({character}, {team_type})"

        if instruction_index == 3:
            character, destination_type, destination_id, model_point = req_args
            character = 'PLAYER' if character == 10000 else character
            destination_type = get_enum_name(game_module.CoordEntityType, destination_type, True)
            return (f"Move({character}, destination={destination_id}, model_point={model_point}, "
                    f"destination_type={destination_type})")

        if instruction_index == 4:
            character, award_souls = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"Kill({character}, award_souls={boolify(award_souls)})"

        if instruction_index == 5:
            character, state = req_args
            character = 'PLAYER' if character == 10000 else character
            if state == 1:
                return f"EnableCharacter({character})"
            elif state == 0:
                return f"DisableCharacter({character})"
            return f"SetCharacterState({character}, state={boolify(state)})"

        if instruction_index == 6:
            character, command_id, slot = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"EzstateAIRequest({character}, command_id={command_id}, slot={slot})"

        if instruction_index == 7:
            entity_id, = req_args
            return f"CreateSpawner({entity_id})"

        # 8 is "AddSpecialEffect", which differs from game to game.

        if instruction_index == 9:
            character, standby, damage, cancel, death, standby_return = req_args
            character = 'PLAYER' if character == 10000 else character
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
            character = 'PLAYER' if character == 10000 else character
            if state == 1:
                return f"EnableGravity({character})"
            elif state == 0:
                return f"DisableGravity({character})"
            return f"SetGravityState({character}, state={state})"

        if instruction_index == 11:
            character, region = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"SetCharacterEventTarget({character}, {region})"

        if instruction_index == 12:
            character, state = req_args
            character = 'PLAYER' if character == 10000 else character
            if state == 1:
                return f"EnableImmortality({character})"
            elif state == 0:
                return f"DisableImmortality({character})"
            return f"SetImmortalityState({character}, state={state})"

        if instruction_index == 13:
            character, nest_region = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"SetNest({character}, {nest_region})"

        # 14 is "RotateToFaceEntity", which differs from game to game.

        if instruction_index == 15:
            character, state = req_args
            character = 'PLAYER' if character == 10000 else character
            if state == 1:
                return f"EnableInvincibility({character})"
            elif state == 0:
                return f"DisableInvincibility({character})"
            return f"SetInvincibilityState({character}, state={state})"

        if instruction_index == 16:
            character, = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"ClearTargetList({character})"

        if instruction_index == 17:
            character, command_id, slot = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"AICommand({character}, command_id={command_id}, slot={slot})"

        if instruction_index == 18:
            character, region, reaction_range = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"SetEventPoint({character}, region={region}, reaction_range={reaction_range})"

        if instruction_index == 19:
            character, ai_id = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"SetAIParamID({character}, {ai_id})"

        if instruction_index == 20:
            character, = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"ReplanAI({character})"

        if instruction_index == 21:
            character, special_effect_id = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"CancelSpecialEffect({character}, {special_effect_id})"

        if instruction_index == 22:
            character, npc_part_id, part_index, part_hp, \
                damage_correction, body_damage_correction, invincible, start_in_stop_state = req_args
            part_index = get_enum_name(game_module.NPCPartType, part_index, True)
            character = 'PLAYER' if character == 10000 else character
            return (f"CreateNPCPart({character}, npc_part_id={npc_part_id}, part_index={part_index}, "
                    f"part_health={part_hp}, damage_correction={damage_correction}, "
                    f"body_damage_correction={body_damage_correction}, is_invincible={boolify(invincible)}, "
                    f"start_in_stop_state={boolify(start_in_stop_state)})")

        if instruction_index == 23:
            character, npc_part_id, desired_hp, overwrite_max = req_args
            character = 'PLAYER' if character == 10000 else character
            return (f"SetNPCPartHealth({character}, npc_part_id={npc_part_id}, "
                    f"desired_hp={desired_hp}, overwrite_max={boolify(overwrite_max)})")

        if instruction_index == 24:
            character, npc_part_id, material_special_effect_id, material_fx_id = req_args
            character = 'PLAYER' if character == 10000 else character
            return (f"SetNPCPartEffects({character}, npc_part_id={npc_part_id}, "
                    f"material_special_effect_id={material_special_effect_id}, material_fx_id={material_fx_id})")

        if instruction_index == 25:
            character, npc_part_id, bullet_scaling = req_args
            character = 'PLAYER' if character == 10000 else character
            return (f"SetNPCPartBulletDamageScaling({character}, npc_part_id={npc_part_id}, "
                    f"desired_scaling={bullet_scaling})")

        if instruction_index == 26:
            character, bit_index, switch_type = req_args
            character = 'PLAYER' if character == 10000 else character
            switch_type = get_enum_name(game_module.OnOffChange, switch_type, True)
            return f"SetDisplayMask({character}, bit_index={bit_index}, switch_type={switch_type})"

        if instruction_index == 27:
            character, bit_index, switch_type = req_args
            character = 'PLAYER' if character == 10000 else character
            switch_type = get_enum_name(game_module.OnOffChange, switch_type, True)
            return f"SetHitboxMask({character}, bit_index={bit_index}, switch_type={switch_type})"

        if instruction_index == 28:
            character, update_auth_type = req_args
            character = 'PLAYER' if character == 10000 else character
            update_auth_type = get_enum_name(game_module.UpdateAuthority, update_auth_type, True)
            return f"SetNetworkUpdateAuthority({character}, {update_auth_type})"

        if instruction_index == 29:
            character, remove = req_args
            character = 'PLAYER' if character == 10000 else character
            if remove == 1:
                return f"DisableBackread({character})"
            elif remove == 0:
                return f"EnableBackread({character})"
            return f"SetBackreadState({character}, remove={boolify(remove)})"

        if instruction_index == 30:
            character, state = req_args
            character = 'PLAYER' if character == 10000 else character
            if state == 1:
                return f"EnableHealthBar({character})"
            elif state == 0:
                return f"DisableHealthBar({character})"
            return f"SetHealthBarState({character}, state={state})"

        if instruction_index == 31:
            character, disabled = req_args
            character = 'PLAYER' if character == 10000 else character
            if disabled == 1:
                return f"DisableCollision({character})"
            elif disabled == 0:
                return f"EnableCollision({character})"
            return f"SetCollisionState({character}, is_disabled={disabled})"

        if instruction_index == 32:
            character, command_id, slot, start_flag, end_flag = req_args
            character = 'PLAYER' if character == 10000 else character
            return (f"AIEvent({character}, command_id={command_id}, slot={slot}, "
                    f"first_event_flag={start_flag}, last_event_flag={end_flag})")

        if instruction_index == 33:
            character, target_entity_id = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"ReferDamageToEntity({character}, {target_entity_id})"

        if instruction_index == 34:
            character, is_fixed, update_rate = req_args
            character = 'PLAYER' if character == 10000 else character
            update_rate = get_enum_name(game_module.CharacterUpdateRate, update_rate, True)
            return f"SetNetworkUpdateRate({character}, is_fixed={boolify(is_fixed)}, update_rate={update_rate})"

        if instruction_index == 35:
            character, state = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"SetBackreadStateAlternate({character}, state={boolify(state)})"

        if instruction_index == 36:
            character, object_id, animation_id = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"HellkiteBreathControl({character}, obj={object_id}, animation_id={animation_id})"

        if instruction_index == 37:
            character, = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"DropMandatoryTreasure({character})"

        if instruction_index == 38:
            return "BetrayCurrentCovenant()"

        if instruction_index == 39:
            character, state = req_args
            character = 'PLAYER' if character == 10000 else character
            if state == 1:
                return f"EnableAnimations({character})"
            elif state == 0:
                return f"DisableAnimations({character})"
            return f"SetAnimationsState({character}, state={state})"

        if instruction_index == 40:
            character, destination_type, destination_id, model_point, hitbox_id = req_args
            character = 'PLAYER' if character == 10000 else character
            destination_type = get_enum_name(game_module.CoordEntityType, destination_type, True)
            return (f"Move({character}, destination={destination_id}, destination_type={destination_type}, "
                    f"model_point={model_point}, set_draw_hitbox={hitbox_id})")

        if instruction_index == 41:
            character, destination_type, destination_id, model_point = req_args
            character = 'PLAYER' if character == 10000 else character
            destination_type = get_enum_name(game_module.CoordEntityType, destination_type, True)
            return (f"Move({character}, destination={destination_id}, destination_type={destination_type}, "
                    f"model_point={model_point}, short_move=True)")

        if instruction_index == 42:
            character, destination_type, destination_id, model_point, copy_hitbox = req_args
            character = 'PLAYER' if character == 10000 else character
            copy_hitbox = 'PLAYER' if copy_hitbox == 10000 else copy_hitbox
            destination_type = get_enum_name(game_module.CoordEntityType, destination_type, True)
            return (f"Move({character}, destination={destination_id}, destination_type={destination_type}, "
                    f"model_point={model_point}, copy_draw_hitbox={copy_hitbox})")

        if instruction_index == 43:
            character, disable_interpolation = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"ResetAnimation({character}, disable_interpolation={boolify(disable_interpolation)})"

        if instruction_index == 44:
            character, team_type = req_args
            character = 'PLAYER' if character == 10000 else character
            team_type = get_enum_name(game_module.TeamType, team_type, True)
            return f"SetTeamTypeAndExitStandbyAnimation({character}, {team_type})"

        if instruction_index == 45:
            character, initial_humanity_flag = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"HumanityRegistration({character}, {initial_humanity_flag})"

        if instruction_index == 46:
            return "IncrementPvPSin()"

        if instruction_index == 47:
            return "EqualRecovery()"

    if instruction_class == 2005:  # OBJECT

        if instruction_index == 1:
            obj, slot = req_args
            if slot == 0:
                return f"DestroyObject({obj})"
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
            return f"SetObjectState({obj}, state={state})"

        if instruction_index == 4:
            obj, state = req_args
            if state == 1:
                return f"EnableTreasure({obj})"
            elif state == 0:
                return f"DisableTreasure({obj})"
            return f"SetTreasureState({obj}, state={state})"

        if instruction_index == 5:
            obj, obj_act_id, relative_index = req_args
            return f"ActivateObject({obj}, obj_act_id={obj_act_id}, relative_index={relative_index})"

        if instruction_index == 6:
            obj, obj_act_id, state = req_args
            if state == 1:
                return f"EnableObjectActivation({obj}, obj_act_id={obj_act_id})"
            elif state == 0:
                return f"DisableObjectActivation({obj}, obj_act_id={obj_act_id})"
            return f"SetObjectActivation({obj}, obj_act_id={obj_act_id}, state={boolify(state)})"

        if instruction_index == 7:
            # I have not wrapped this instruction. Just using standard EndOfAnimation (as the game does).
            obj, animation_id = req_args
            return f"EndOfAnimation({obj}, {animation_id})"

        if instruction_index == 8:
            obj, slot = req_args
            return f"PostDestruction({obj}, slot={slot})"

        if instruction_index == 9:
            obj_flag, obj, model_point, behavior_id, anchor_type, radius, life, repetition_time = req_args
            anchor_type = get_enum_name(game_module.DamageTargetType, anchor_type, True)
            return (f"CreateHazard({obj_flag}, {obj}, model_point={model_point}, behavior_param_id={behavior_id}, "
                    f"target_type={anchor_type}, radius={radius}, life={life}, repetition_time={repetition_time})")

        if instruction_index == 10:
            obj, area_id, block_id, statue_type = req_args
            statue_type = get_enum_name(game_module.StatueType, statue_type, True)
            game_map = get_game_map_name(area_id, block_id, game_module)
            return f"RegisterStatue({obj}, game_map={game_map}, statue_type={statue_type})"

        if instruction_index == 11:
            obj, character, model_point = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"MoveObjectToCharacter({obj}, character={character}, model_point={model_point})"

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
            obj, obj_act_id, relative_index, state = req_args
            if state == 1:
                return f"EnableObjectActivation({obj}, obj_act_id={obj_act_id}, relative_index={relative_index})"
            elif state == 0:
                return f"DisableObjectActivation({obj}, obj_act_id={obj_act_id}, relative_index={relative_index})"
            return (f"SetObjectActivationWithIdx({obj}, obj_act_id={obj_act_id}, relative_index={relative_index}, "
                    f"state={boolify(state)})")

        if instruction_index == 15:
            obj, = req_args
            return f"EnableTreasureCollection({obj})"

    if instruction_class == 2006:  # SFX

        if instruction_index == 1:
            fx_id, erase_root_only = req_args
            return f"DeleteFX({fx_id}, erase_root_only={boolify(erase_root_only)})"

        if instruction_index == 2:
            fx_id, = req_args
            return f"CreateFX({fx_id})"

        if instruction_index == 3:
            anchor_type, anchor_entity_id, model_point, fx_id = req_args
            anchor_type = get_enum_name(game_module.CoordEntityType, anchor_type, True)
            return (f"CreateTemporaryFX({fx_id}, anchor_entity={anchor_entity_id}, "
                    f"anchor_type={anchor_type}, model_point={model_point})")

        if instruction_index == 4:
            obj, model_point, fx_id = req_args
            return f"CreateObjectFX({fx_id}, obj={obj}, model_point={model_point})"

        if instruction_index == 5:
            obj, erase_root = req_args
            return f"DeleteObjectFX({obj}, erase_root={boolify(erase_root)})"

    if instruction_class == 2007:  # MESSAGE

        if instruction_index == 1:
            text_id, button_type, number_buttons, entity_id, display_distance = req_args
            button_type = get_enum_name(game_module.ButtonType, button_type)
            number_buttons = get_enum_name(game_module.NumberButtons, number_buttons)
            return (f"DisplayDialog({text_id}, anchor_entity={entity_id}, display_distance={display_distance}, "
                    f"button_type={button_type}, number_buttons={number_buttons})")

        if instruction_index == 2:
            banner_type, = req_args
            banner_type = get_enum_name(game_module.BannerType, banner_type)
            return f"DisplayBanner({banner_type})"

        if instruction_index == 3:
            text_id, pad_enabled = req_args
            return f"DisplayStatus({text_id}, pad_enabled={boolify(pad_enabled)})"

        if instruction_index == 4:
            text_id, location = req_args
            return f"DisplayBattlefieldMessage({text_id}, display_location_index={location})"

        if instruction_index == 5:
            player_id, = req_args
            return f"ArenaSetNametag1({player_id})"

        if instruction_index == 6:
            player_id, = req_args
            return f"ArenaSetNametag2({player_id})"

        if instruction_index == 7:
            player_id, = req_args
            return f"ArenaSetNametag3({player_id})"

        if instruction_index == 8:
            player_id, = req_args
            return f"ArenaSetNametag4({player_id})"

        if instruction_index == 9:
            text_id, = req_args
            return f"DisplayArenaDissolutionMessage({text_id})"

        if instruction_index == 10:
            player_id, = req_args
            return f"ArenaSetNametag5({player_id})"

        if instruction_index == 11:
            player_id, = req_args
            return f"ArenaSetNametag6({player_id})"

    if instruction_class == 2008:  # CAMERA

        if instruction_index == 1:
            normal_camera_id, locked_camera_id = req_args
            return f"ChangeCamera(normal_camera_id={normal_camera_id}, locked_camera_id={locked_camera_id})"

        if instruction_index == 2:
            vibration_id, anchor_type, anchor_entity, model_point, decay_start_distance, decay_end_distance = req_args
            anchor_type = get_enum_name(game_module.CoordEntityType, anchor_type, True)
            return (f"SetCameraVibration(vibration_id={vibration_id}, anchor_entity={anchor_entity}, "
                    f"model_point={model_point}, decay_start_distance={decay_start_distance}, "
                    f"decay_end_distance={decay_end_distance}, anchor_type={anchor_type})")

        if instruction_index == 3:
            area_id, block_id, camera_slot = req_args
            game_map = get_game_map_name(area_id, block_id, game_module)
            return f"SetLockedCameraSlot(game_map={game_map}, camera_slot={camera_slot})"

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

        if instruction_index == 1:
            state, slot, entity, sound_type, sound_id = req_args
            sound_type = get_enum_name(game_module.SoundType, sound_type)
            return (f"SetBackgroundMusic(state={boolify(state)}, slot={slot}, entity={entity}, "
                    f"sound_type={sound_type}, sound_id={sound_id})")

        if instruction_index == 2:
            anchor_entity_id, sound_type, sound_id = req_args
            sound_type = get_enum_name(game_module.SoundType, sound_type, True)
            return f"PlaySoundEffect(anchor_entity={anchor_entity_id}, sound_type={sound_type}, sound_id={sound_id})"

        if instruction_index == 3:
            sound_id, state = req_args
            if state == 1:
                return f"EnableMapSound({sound_id})"
            elif state == 0:
                return f"DisableMapSound({sound_id})"
            return f"SetMapSoundState({sound_id}, state={state})"

    if instruction_class == 2011:  # ヒット

        if instruction_index == 1:
            hitbox_id, state = req_args
            if state == 1:
                return f"EnableHitbox({hitbox_id})"
            elif state == 0:
                return f"DisableHitbox({hitbox_id})"
            return f"SetHitboxState({hitbox_id}, state={boolify(state)})"

        if instruction_index == 2:
            hitbox_id, state = req_args
            if state == 1:
                return f"EnableHitboxBackreadMask({hitbox_id})"
            elif state == 0:
                return f"DisableHitboxBackreadMask({hitbox_id})"
            return f"SetHitboxBackreadMaskState({hitbox_id}, state={boolify(state)})"

    if instruction_class == 2012:  # マップ

        if instruction_index == 1:
            map_part_id, state = req_args
            if state == 1:
                return f"EnableMapPart({map_part_id})"
            elif state == 0:
                return f"DisableMapPart({map_part_id})"
            return f"SetMapPartState({map_part_id}, state={state})"

    if instruction_class == 1000:  # 【実行制御】システム

        if instruction_index == 0:
            state, condition = req_args
            if state == 1:
                return f"AwaitConditionTrue({condition})"
            if state == 0:
                return f"AwaitConditionFalse({condition})"
            return f"AwaitConditionState(state={boolify(state)}, condition={condition})"

        if instruction_index == 1:
            line_count, state, condition = req_args
            if state == 1:
                return f"SkipLinesIfConditionTrue({line_count}, {condition})"
            elif state == 0:
                return f"SkipLinesIfConditionFalse({line_count}, {condition})"
            return f"SkipLinesIfConditionState({line_count}, state={boolify(state)}, condition={condition})"

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
            line_count, = req_args
            return f"SkipLines({line_count})"

        if instruction_index == 4:
            end_type, = req_args
            if end_type == 1:
                return "Restart()"
            elif end_type == 0:
                return "End()"
            return f"Terminate(event_end_type={end_type})"

        if instruction_index == 5:
            line_count, comparison_type, left, right = req_args
            try:
                comparison_type = get_enum_name(game_module.ComparisonType, comparison_type)
            except EnumStringError:
                return (f"SkipLinesIfComparison({line_count}, comparison_type={comparison_type}, "
                        f"left={left}, right={right})")
            else:
                return f"SkipLinesIf{comparison_type.split('.')[-1]}({line_count}, left={left}, right={right})"

        if instruction_index == 6:
            end_type, comparison_type, left, right = req_args
            if end_type == 1:
                try:
                    comparison_type_name = get_enum_name(game_module.ComparisonType, comparison_type)
                except EnumStringError:
                    return (f"TerminateIfComparison(EventEndType.Restart, comparison_type={comparison_type}, "
                            f"left={left}, right={right})")
                else:
                    return f"RestartIf{comparison_type_name.split('.')[-1]}(left={left}, right={right})"
            elif end_type == 0:
                try:
                    comparison_type_name = get_enum_name(game_module.ComparisonType, comparison_type)
                except EnumStringError:
                    return (f"TerminateIfComparison(EventEndType.End, comparison_type={comparison_type}, "
                            f"left={left}, right={right})")
                else:
                    return f"EndIf{comparison_type_name.split('.')[-1]}(left={left}, right={right})"
            else:
                return (f"TerminateIfComparison(event_end_type={end_type}, comparison_type={comparison_type}, "
                        f"left={left}, right={right})")

        if instruction_index == 7:
            line_count, state, condition = req_args
            if state == 1:
                return f"SkipLinesIfFinishedConditionTrue({line_count}, {condition})"
            elif state == 0:
                return f"SkipLinesIfFinishedConditionFalse({line_count}, {condition})"
            return (f"SkipLinesIfFinishedConditionState({line_count}, state={boolify(state)}, "
                    f"input_condition={condition})")

        if instruction_index == 8:
            end_type, state, condition = req_args
            if end_type == 1:
                if state == 1:
                    return f"RestartIfFinishedConditionTrue({condition})"
                elif state == 0:
                    return f"RestartIfFinishedConditionFalse({condition})"
                return (f"TerminateIfFinishedConditionState(EventEndType.Restart, state={boolify(state)}, "
                        f"input_condition={condition})")
            elif end_type == 0:
                if state == 1:
                    return f"EndIfFinishedConditionTrue({condition})"
                elif state == 0:
                    return f"EndIfFinishedConditionFalse({condition})"
                return (f"TerminateIfFinishedConditionState(EventEndType.End, state={boolify(state)}, "
                        f"input_condition={condition})")
            return (f"TerminateIfFinishedConditionState(event_end_type={end_type}, state={boolify(state)}, "
                    f"input_condition={condition})")

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

        if instruction_index == 3:
            min_frames, max_frames = req_args
            return f"WaitRandomFrames(min_frames={min_frames}, max_frames={max_frames})"

    if instruction_class == 1003:  # 【実行制御】イベント

        if instruction_index == 0:
            state, flag_type, flag = req_args
            if flag_type == 0:
                if state == 0:
                    return f"AwaitFlagOff({flag})"
                elif state == 1:
                    return f"AwaitFlagOn({flag})"
                elif state == 2:
                    return f"AwaitFlagChange({flag})"
            elif flag_type == 1:
                if flag == 0:
                    if state == 0:
                        return f"AwaitThisEventOff()"
                    elif state == 1:
                        return f"AwaitThisEventOn()"
            elif flag_type == 2:
                if flag == 0:
                    if state == 0:
                        return f"AwaitThisEventSlotOff()"
                    elif state == 1:
                        return f"AwaitThisEventSlotOn()"
            # No simple instruction found.
            flag_type = get_enum_name(game_module.FlagType, flag_type, True)
            state = get_enum_name(game_module.FlagState, state, True)
            return f"AwaitFlagState(state={state}, flag_type={flag_type}, flag={flag})"

        if instruction_index == 1:
            line_count, state, flag_type, flag = req_args
            if state == 2:
                raise ValueError("Skip instruction should never condition on flag state 'Change'.")
            if flag_type == 0:
                if state == 0:
                    return f"SkipLinesIfFlagOff({line_count}, {flag})"
                elif state == 1:
                    return f"SkipLinesIfFlagOn({line_count}, {flag})"
            elif flag_type == 1 and flag == 0:
                if state == 0:
                    return f"SkipLinesIfThisEventOff({line_count})"
                elif state == 1:
                    return f"SkipLinesIfThisEventOn({line_count})"
            elif flag_type == 2 and flag == 0:
                if state == 0:
                    return f"SkipLinesIfThisEventSlotOff({line_count})"
                elif state == 1:
                    return f"SkipLinesIfThisEventSlotOn({line_count})"
            # No simple instruction found.
            flag_type = get_enum_name(game_module.FlagType, flag_type, True)
            state = get_enum_name(game_module.FlagState, state, True)
            return f"SkipLinesIfFlagState(state={state}, flag_type={flag_type}, flag={flag})"

        if instruction_index == 2:
            end_type, state, flag_type, flag = req_args
            if state == 2:
                raise ValueError("Terminate instruction should never condition on flag state 'Change'.")
            if end_type == 0:
                if flag_type == 0:
                    if state == 0:
                        return f"EndIfFlagOff({flag})"
                    elif state == 1:
                        return f"EndIfFlagOn({flag})"
                elif flag_type == 1 and flag == 0:
                    if state == 0:
                        return f"EndIfThisEventOff()"
                    elif state == 1:
                        return f"EndIfThisEventOn()"
                elif flag_type == 2 and flag == 0:
                    if state == 0:
                        return f"EndIfThisEventSlotOff()"
                    elif state == 1:
                        return f"EndIfThisEventSlotOn()"
            elif end_type == 1:
                if flag_type == 0:
                    if state == 0:
                        return f"RestartIfFlagOff({flag})"
                    elif state == 1:
                        return f"RestartIfFlagOn({flag})"
                elif flag_type == 1 and flag == 0:
                    if state == 0:
                        return f"RestartIfThisEventOff()"
                    elif state == 1:
                        return f"RestartIfThisEventOn()"
                elif flag_type == 2 and flag == 0:
                    if state == 0:
                        return f"RestartIfThisEventSlotOff()"
                    elif state == 1:
                        return f"RestartIfThisEventSlotOn()"
            # No simple instruction found.
            flag_type = get_enum_name(game_module.FlagType, flag_type, True)
            state = get_enum_name(game_module.FlagState, state, True)
            return f"TerminateIfFlagState(event_end_type={end_type}, state={state}, flag_type={flag_type}, flag={flag})"

        if instruction_index == 3:
            line_count, state, flag_type, first_flag, last_flag = req_args
            if flag_type == 0:
                try:
                    state_name = get_enum_name(game_module.RangeState, state)
                except EnumStringError:
                    pass
                else:
                    return f"SkipLinesIfFlagRange{state_name.split('.')[-1]}({line_count}, ({first_flag}, {last_flag}))"
            flag_type = get_enum_name(game_module.FlagType, flag_type, True)
            return (f"SkipLinesIfFlagRangeState({line_count}, state={state}, flag_type={flag_type}, "
                    f"flag_range=({first_flag}, {last_flag}))")

        if instruction_index == 4:
            end_type, state, flag_type, first_flag, last_flag = req_args
            if flag_type == 0:
                try:
                    state_name = get_enum_name(game_module.RangeState, state)
                except EnumStringError:
                    pass
                else:
                    if end_type == 0:
                        return f"EndIfFlagRange{state_name.split('.')[-1]}(({first_flag}, {last_flag}))"
                    elif end_type == 1:
                        return f"RestartIfFlagRange{state_name.split('.')[-1]}(({first_flag}, {last_flag}))"
            state = get_enum_name(game_module.RangeState, state, True)
            flag_type = get_enum_name(game_module.FlagType, flag_type, True)
            return (f"TerminateIfFlagRangeState(event_end_type={end_type}, state={state}, flag_type={flag_type}, "
                    f"flag_range=({first_flag}, {last_flag}))")

        if instruction_index == 5:
            line_count, multiplayer_state = req_args
            try:
                state_name = get_enum_name(game_module.MultiplayerState, multiplayer_state).split('.')[-1]
            except EnumStringError:
                return f"SkipLinesIfMultiplayerState({line_count}, state={multiplayer_state})"
            else:
                return f"SkipLinesIf{state_name}({line_count})"

        if instruction_index == 6:
            end_type, multiplayer_state = req_args
            if end_type == game_module.EventEndType.End:
                try:
                    state_name = get_enum_name(game_module.MultiplayerState, multiplayer_state).split('.')[-1]
                except EnumStringError:
                    pass
                else:
                    return f"EndIf{state_name}()"
            elif end_type == game_module.EventEndType.Restart:
                try:
                    state_name = get_enum_name(game_module.MultiplayerState, multiplayer_state).split('.')[-1]
                except EnumStringError:
                    pass
                else:
                    return f"RestartIf{state_name}()"
            multiplayer_state = get_enum_name(game_module.MultiplayerState, multiplayer_state, True)
            return f"TerminateIfMultiplayerState(event_end_type={end_type}, state={multiplayer_state})"

        if instruction_index == 7:
            line_count, state, area_id, block_id = req_args
            game_map = get_game_map_name(area_id, block_id, game_module)
            if state == 1:
                return f"SkipLinesIfInsideMap({line_count}, game_map={game_map})"
            elif state == 0:
                return f"SkipLinesIfOutsideMap({line_count}, game_map={game_map})"
            return f"SkipLinesIfMapPresenceState({line_count}, state={boolify(state)}, game_map={game_map})"

        if instruction_index == 8:  # マップIDでイベント終了
            end_type, state, area_id, block_id = req_args
            game_map = get_game_map_name(area_id, block_id, game_module)
            if end_type == 0:
                if state == 1:
                    return f"EndIfInsideMap(game_map={game_map})"
                elif state == 0:
                    return f"EndIfOutsideMap(game_map={game_map})"
            elif end_type == 1:
                if state == 1:
                    return f"RestartIfInsideMap(game_map={game_map})"
                elif state == 0:
                    return f"RestartIfOutsideMap(game_map={game_map})"
            return (f"TerminateIfMapPresenceState(event_end_type={end_type}, game_map={game_map}, "
                    f"state={boolify(state)})")

    if instruction_class == 1005:  # 【実行制御】オブジェクト

        if instruction_index == 0:
            state, obj = req_args
            if state == 0:
                return f"AwaitObjectNotDestroyed({obj})"
            if state == 1:
                return f"AwaitObjectDestroyed({obj})"
            return f"AwaitObjectDestructionState(state={boolify(state)}, obj={obj})"

        if instruction_index == 1:
            line_count, state, obj = req_args
            if state == 0:
                return f"SkipLinesIfObjectNotDestroyed({line_count}, {obj})"
            if state == 1:
                return f"SkipLinesIfObjectDestroyed({line_count}, {obj})"
            return f"SkipLinesIfObjectDestructionState({line_count}, {obj}, state={boolify(state)})"

        if instruction_index == 2:
            end_type, state, obj = req_args
            if end_type == 0:
                if state == 1:
                    return f"EndIfObjectDestroyed({obj})"
                elif state == 0:
                    return f"EndIfObjectNotDestroyed({obj})"
            elif end_type == 1:
                if state == 1:
                    return f"RestartIfObjectDestroyed({obj})"
                elif state == 0:
                    return f"RestartIfObjectNotDestroyed({obj})"
            return f"TerminateIfObjectDestructionState(event_end_type={end_type}, obj={obj}, state={boolify(state)})"

    if instruction_class == 0:  # 《条件登録》システム

        if instruction_index == 0:
            condition, state, source_condition = req_args
            if state == 1:
                return f"IfConditionTrue({condition}, input_condition={source_condition})"
            if state == 0:
                return f"IfConditionFalse({condition}, input_condition={source_condition})"
            return f"IfConditionState({condition}, state={boolify(state)}, input_condition={source_condition})"

        if instruction_index == 1:
            condition, comparison_type, left, right = req_args
            comparison_type = get_enum_name(game_module.ComparisonType, comparison_type, True)
            return f"IfValueComparison({condition}, {comparison_type}, left={left}, right={right})"

    if instruction_class == 1:  # 《条件登録》タイマー

        if instruction_index == 0:
            condition, seconds = req_args
            return f"IfTimeElapsed({condition}, {seconds})"

        if instruction_index == 1:
            condition, frames = req_args
            return f"IfFramesElapsed({condition}, {frames})"

        if instruction_index == 2:
            condition, min_seconds, max_seconds = req_args
            return f"IfRandomTimeElapsed({condition}, min_seconds={min_seconds}, max_seconds={max_seconds})"

        if instruction_index == 3:
            condition, min_frames, max_frames = req_args
            return f"IfRandomFramesElapsed({condition}, min_frames={min_frames}, max_frames={max_frames})"

    if instruction_class == 3:  # CONTROL (EVENT)

        if instruction_index == 0:
            condition, state, flag_type, flag = req_args
            try:
                if state == 0:
                    state_name = 'Off'
                elif state == 1:
                    state_name = 'On'
                elif state == 2:
                    state_name = 'Change'
                else:
                    raise ValueError
                if flag_type == 0:
                    return f"IfFlag{state_name}({condition}, {flag})"
                elif flag == 0:
                    if flag_type == 1:
                        return f"IfThisEvent{state_name}({condition})"
                    elif flag_type == 2:
                        return f"IfThisEventSlot{state_name}({condition})"
                raise ValueError
            except ValueError:
                flag_type = get_enum_name(game_module.FlagType, flag_type, True)
                state = get_enum_name(game_module.FlagState, state, True)
                return f"IfFlagState({condition}, state={state}, flag_type={flag_type}, flag={flag})"

        if instruction_index == 1:
            condition, state, flag_type, first_flag, last_flag = req_args
            if flag_type == 0:
                try:
                    state_name = get_enum_name(game_module.RangeState, state)
                except EnumStringError:
                    pass
                else:
                    return f"IfFlagRange{state_name.split('.')[-1]}({condition}, ({first_flag}, {last_flag}))"
            state = get_enum_name(game_module.RangeState, state, True)
            flag_type = get_enum_name(game_module.FlagType, flag_type, True)
            return (f"IfFlagRangeState({condition}, state={state}, flag_type={flag_type}, "
                    f"flag_range=({first_flag}, {last_flag}))")

        if instruction_index == 2:
            condition, state, character, region = req_args
            character = 'PLAYER' if character == 10000 else character
            if state == 1:
                return f"IfCharacterInsideRegion({condition}, {character}, region={region})"
            elif state == 0:
                return f"IfCharacterOutsideRegion({condition}, {character}, region={region})"
            return f"IfCharacterRegionState({condition}, {character}, region={region}, state={boolify(state)}')"

        if instruction_index == 3:
            condition, state, entity, other_entity, radius = req_args
            entity = 'PLAYER' if entity == 10000 else entity
            other_entity = 'PLAYER' if other_entity == 10000 else other_entity
            if state == 1:
                return f"IfEntityWithinDistance({condition}, {entity}, {other_entity}, radius={radius})"
            elif state == 0:
                return f"IfEntityBeyondDistance({condition}, {entity}, {other_entity}, radius={radius})"
            return f"IfEntityDistanceState({condition}, {entity}, {other_entity}, {radius}, state={boolify(state)})"

        if instruction_index == 4:
            condition, item_type, item_id, state = req_args
            if state in {0, 1}:
                state = 'Has' if state else 'DoesNotHave'
                try:
                    item_type = get_enum_name(game_module.ItemType, item_type)
                except EnumStringError:
                    return f"IfPlayer{state}Item({condition}, {item_id}, item_type={item_type}, including_box=False)"
                else:
                    return f"IfPlayer{state}{item_type.split('.')[-1]}({condition}, {item_id}, including_box=False)"
            item_type = get_enum_name(game_module.ItemType, item_type, True)
            return (f"IfPlayerItemState({condition}, state={boolify(state)}, item={item_id}, item_type={item_type}, "
                    f"including_box=False)")

        if instruction_index == 5:
            condition, anchor_type, anchor_entity, reaction_angle, model_point, \
                reaction_distance, text_id, reaction_attribute, pad_id = req_args
            anchor_type = get_enum_name(game_module.CoordEntityType, anchor_type, True)
            model_point_arg = f'model_point={model_point}, ' if model_point != -1 else ''
            button_arg = f'button={pad_id}, ' if pad_id != 0 else ''
            human_or_hollow_only = True if reaction_attribute == 48 else False
            return (f"IfDialogPromptActivated({condition}, prompt_text={text_id}, "
                    f"anchor_entity={anchor_entity}, anchor_type={anchor_type}, facing_angle={reaction_angle}, "
                    f"max_distance={reaction_distance}, {model_point_arg}{button_arg}"
                    f"human_or_hollow_only={human_or_hollow_only})")

        if instruction_index == 6:
            condition, multiplayer_state = req_args
            try:
                state_name = get_enum_name(game_module.MultiplayerState, multiplayer_state).split('.')[-1]
            except EnumStringError:
                return f"IfMultiplayerState({condition}, state={multiplayer_state})"
            else:
                return f"If{state_name}({condition})"

        if instruction_index == 7:
            condition, state, region = req_args
            if state == 1:
                return f"IfAllPlayersInsideRegion({condition}, region={region})"
            elif state == 0:
                return f"IfAllPlayersOutsideRegion({condition}, region={region})"
            return f"IfAllPlayersRegionState({condition}, region={region}, state={boolify(state)}')"

        if instruction_index == 8:
            condition, state, area_id, block_id = req_args
            game_map = get_game_map_name(area_id, block_id, game_module)
            if state == 1:
                return f"IfInsideMap({condition}, game_map={game_map})"
            elif state == 0:
                return f"IfOutsideMap({condition}, game_map={game_map})"
            return f"IfMapPresenceState({condition}, {game_map}, state={boolify(state)})"

        if instruction_index == 9:
            condition, multiplayer_event_id = req_args
            return f"IfMultiplayerEvent({condition}, {multiplayer_event_id})"

        if instruction_index == 10:
            condition, flag_type, first_flag, last_flag, comparison_type, comparison_value = req_args
            if flag_type == 0:
                try:
                    comparison_type = get_enum_name(game_module.ComparisonType, comparison_type)
                except EnumStringError:
                    pass
                else:
                    return (f"IfTrueFlagCount{comparison_type.split('.')[-1]}({condition}, {comparison_value}, "
                            f"({first_flag}, {last_flag}))")
            flag_type = get_enum_name(game_module.FlagType, flag_type, True)
            comparison_type = get_enum_name(game_module.ComparisonType, comparison_type, True)
            return (f"IfTrueFlagCountComparison({condition}, {comparison_value}, {flag_type}, {comparison_type}, "
                    f"({first_flag}, {last_flag}))")

        if instruction_index == 11:
            condition, tendency_type, comparison_type, comparison_value = req_args
            if tendency_type == 0:
                if comparison_type == 4:
                    return f"IfWhiteWorldTendencyGreaterThanOrEqual({condition}, {comparison_value})"
                comparison_type = get_enum_name(game_module.ComparisonType, comparison_type, True)
                return (f"IfWhiteWorldTendencyComparison({condition}, comparison_type={comparison_type}, "
                        f"value={comparison_value})")
            if tendency_type == 1:
                if comparison_type == 4:
                    return f"IfBlackWorldTendencyGreaterThanOrEqual({condition}, {comparison_value})"
                comparison_type = get_enum_name(game_module.ComparisonType, comparison_type, True)
                return (f"IfBlackWorldTendencyComparison({condition}, comparison_type={comparison_type}, "
                        f"value={comparison_value})")
            return (f"IfWorldTendencyComparison({condition}, world_tendency_type={tendency_type}, "
                    f"comparison_type={comparison_type}, value={comparison_value})")

        if instruction_index == 12:
            condition, flag, bit_count, comparison_type, comparison_value = req_args
            if comparison_type == 0:
                return (f"IfEventValueEqual({condition}, {flag}, bit_count={bit_count}, "
                        f"value={comparison_value})")
            if comparison_type == 2:
                return (f"IfEventValueGreaterThan({condition}, {flag}, bit_count={bit_count}, "
                        f"value={comparison_value})")
            comparison_type = get_enum_name(game_module.ComparisonType, comparison_type, True)
            return (f"IfEventValueComparison({condition}, {flag}, bit_count={bit_count}, "
                    f"comparison_type={comparison_type}, value={comparison_value})")

        if instruction_index == 13:
            condition, anchor_type, anchor_entity, reaction_angle, model_point, \
                reaction_distance, text_id, reaction_attribute, pad_id = req_args
            anchor_type = get_enum_name(game_module.CoordEntityType, anchor_type, True)
            model_point_arg = f'model_point={model_point}, ' if model_point != -1 else ''
            button_arg = f'button={pad_id}, ' if pad_id != 0 else ''
            human_or_hollow_only = reaction_attribute == 48
            return (f"IfDialogPromptActivated({condition}, prompt_text={text_id}, "
                    f"anchor_entity={anchor_entity}, anchor_type={anchor_type}, facing_angle={reaction_angle}, "
                    f"max_distance={reaction_distance}, {model_point_arg}{button_arg}"
                    f"human_or_hollow_only={human_or_hollow_only}, boss_version=True)")

        if instruction_index == 14:
            condition, region = req_args
            return f"IfAnyItemDroppedInRegion({condition}, {region})"

        if instruction_index == 15:
            condition, item_type, item_id = req_args
            item_type = get_enum_name(game_module.ItemType, item_type, True)
            return f"IfItemDropped({condition}, {item_id}, item_type={item_type})"

        if instruction_index == 16:
            condition, item_type, item_id, state = req_args
            if state in {0, 1}:
                state = 'Has' if state else 'DoesNotHave'
                try:
                    item_type = get_enum_name(game_module.ItemType, item_type)
                except EnumStringError:
                    return f"IfPlayer{state}Item({condition}, {item_id}, item_type={item_type}, including_box=True)"
                else:
                    return f"IfPlayer{state}{item_type.split('.')[-1]}({condition}, {item_id}, including_box=True)"
            item_type = get_enum_name(game_module.ItemType, item_type, True)
            return (f"IfPlayerItemState({condition}, state={boolify(state)}, item={item_id}, item_type={item_type}, "
                    f"including_box=True)")

        if instruction_index == 17:
            condition, comparison_type, completion_count = req_args
            if comparison_type == 0:
                return f"IfNewGameCycleEqual({condition}, completion_count={completion_count})"
            if comparison_type == 4:
                return f"IfNewGameCycleGreaterThanOrEqual({condition}, completion_count={completion_count})"
            comparison_type = get_enum_name(game_module.ComparisonType, comparison_type, True)
            return (f"IfNewGameCycleComparison({condition}, comparison_type={comparison_type}, "
                    f"completion_count={completion_count})")

        if instruction_index == 18:
            condition, anchor_type, anchor_entity, reaction_angle, model_point, \
                reaction_distance, text_id, reaction_attribute, pad_id, line_intersects = req_args
            anchor_type = get_enum_name(game_module.CoordEntityType, anchor_type, True)
            model_point_arg = f'model_point={model_point}, ' if model_point != -1 else ''
            button_arg = f'button={pad_id}, ' if pad_id != 0 else ''
            human_or_hollow_only = reaction_attribute == 48
            return (f"IfDialogPromptActivated({condition}, prompt_text={text_id}, "
                    f"anchor_entity={anchor_entity}, anchor_type={anchor_type}, facing_angle={reaction_angle}, "
                    f"max_distance={reaction_distance}, {model_point_arg}{button_arg}"
                    f"human_or_hollow_only={human_or_hollow_only}, line_intersects={line_intersects})")

        if instruction_index == 19:
            condition, anchor_type, anchor_entity, reaction_angle, model_point, \
                reaction_distance, text_id, reaction_attribute, pad_id, line_intersects = req_args
            anchor_type = get_enum_name(game_module.CoordEntityType, anchor_type, True)
            model_point_arg = f'model_point={model_point}, ' if model_point != -1 else ''
            button_arg = f'button={pad_id}, ' if pad_id != 0 else ''
            human_or_hollow_only = reaction_attribute == 48
            return (f"IfDialogPromptActivated({condition}, prompt_text={text_id}, "
                    f"anchor_entity={anchor_entity}, anchor_type={anchor_type}, facing_angle={reaction_angle}, "
                    f"max_distance={reaction_distance}, {model_point_arg}{button_arg}"
                    f"human_or_hollow_only={human_or_hollow_only}, line_intersects={line_intersects}, "
                    f"boss_version=True)")

        if instruction_index == 20:
            condition, left_flag, left_bit_count, comparison_type, right_flag, right_bit_count = req_args
            comparison_type = get_enum_name(game_module.ComparisonType, comparison_type, True)
            return (f"IfEventsComparison({condition}, {left_flag}, {left_bit_count}, {comparison_type}, "
                    f"{right_flag}, {right_bit_count})")

        if instruction_index == 21:
            condition, is_owned = req_args
            if is_owned == 1:
                return f"IfDLCOwned({condition})"
            elif is_owned == 0:
                return f"IfDLCNotOwned({condition})"
            return f"IfDLCState({condition}, is_owned={boolify(is_owned)})"

        if instruction_index == 22:
            condition, state = req_args
            if state == 1:
                return f"IfOnline({condition})"
            elif state == 0:
                return f"IfOffline({condition})"
            return f"IfOnlineState({condition}, state={boolify(state)})"

    if instruction_class == 4:  # CONTROL (CHARACTER)

        if instruction_index == 0:
            condition, character, is_dead = req_args
            character = 'PLAYER' if character == 10000 else character
            if is_dead == 1:
                return f"IfCharacterDead({condition}, {character})"
            elif is_dead == 0:
                return f"IfCharacterAlive({condition}, {character})"
            return f"IfCharacterDeathState({condition}, {character}, state={boolify(is_dead)})"

        if instruction_index == 1:
            condition, attacked, attacker = req_args
            attacked = 'PLAYER' if attacked == 10000 else attacked
            attacker = 'PLAYER' if attacker == 10000 else attacker
            return f"IfAttacked({condition}, {attacked}, attacking_character={attacker})"

        if instruction_index == 2:
            condition, character, comparison_type, comparison_value = req_args
            character = 'PLAYER' if character == 10000 else character
            comparison_type = get_enum_name(game_module.ComparisonType, comparison_type, True)
            return f"IfHealth{comparison_type.split('.')[-1]}({condition}, {character}, {comparison_value})"

        if instruction_index == 3:
            condition, character, character_type = req_args
            character = 'PLAYER' if character == 10000 else character
            if character_type == 8:
                return f"IfCharacterHollow({condition}, {character})"
            elif character_type == 0:
                return f"IfCharacterHuman({condition}, {character})"
            character_type = get_enum_name(game_module.CharacterType, character_type, True)
            return f"IfCharacterType({condition}, {character}, {character_type})"

        if instruction_index == 4:
            condition, targeting_character, targeted_character, state = req_args
            targeting_character = 'PLAYER' if targeting_character == 10000 else targeting_character
            targeted_character = 'PLAYER' if targeted_character == 10000 else targeted_character
            if state == 1:
                return f"IfCharacterTargeting({condition}, {targeting_character}, {targeted_character})"
            elif state == 0:
                return f"IfCharacterNotTargeting({condition}, {targeting_character}, {targeted_character})"
            return (f"IfCharacterTargetingState({condition}, {targeting_character}, {targeted_character}, "
                    f"state={boolify(state)})")

        if instruction_index == 5:
            condition, character, special_effect, state = req_args
            character = 'PLAYER' if character == 10000 else character
            if state == 1:
                return f"IfCharacterHasSpecialEffect({condition}, {character}, {special_effect})"
            elif state == 0:
                return f"IfCharacterDoesNotHaveSpecialEffect({condition}, {character}, {special_effect})"
            return f"IfCharacterSpecialEffectState({condition}, {character}, {special_effect}, state={boolify(state)})"

        if instruction_index == 6:
            condition, character, npc_part_id, comparison_value, comparison_type = req_args
            character = 'PLAYER' if character == 10000 else character
            if comparison_type == 5:
                return (f"IfCharacterPartHealthLessThanOrEqual({condition}, {character}, "
                        f"npc_part_id={npc_part_id}, value={comparison_value})")
            comparison_type = get_enum_name(game_module.ComparisonType, comparison_type, True)
            return (f"IfCharacterPartHealthComparison({condition}, {character}, npc_part_id={npc_part_id}, "
                    f"comparison_type={comparison_type}, value={comparison_value})")

        if instruction_index == 7:
            condition, character, state = req_args
            character = 'PLAYER' if character == 10000 else character
            if state == 1:
                return f"IfCharacterBackreadEnabled({condition}, {character})"
            elif state == 0:
                return f"IfCharacterBackreadDisabled({condition}, {character})"
            return f"IfCharacterBackreadState({condition}, {character}, state={boolify(state)})"

        if instruction_index == 8:
            condition, character, tae_event_id, state = req_args
            character = 'PLAYER' if character == 10000 else character
            if state == 1:
                return f"IfHasTAEEvent({condition}, {character}, tae_event_id={tae_event_id})"
            elif state == 0:
                return f"IfDoesNotHaveTAEEvent({condition}, {character}, tae_event_id={tae_event_id})"
            return f"IfTAEEventState({condition}, {character}, tae_event_id={tae_event_id}, state={boolify(state)})"

        if instruction_index == 9:
            condition, character, ai_status = req_args
            character = 'PLAYER' if character == 10000 else character
            ai_status = get_enum_name(game_module.AIStatusType, ai_status, True)
            return f"IfHasAIStatus({condition}, {character}, ai_status={ai_status})"

        if instruction_index == 10:
            condition, state = req_args
            if state == 1:
                return f"IfSkullLanternActive({condition})"
            elif state == 0:
                return f"IfSkullLanternInactive({condition})"
            return f"IfSkullLanternState({condition}, state={boolify(state)})"

        if instruction_index == 11:
            condition, class_type = req_args
            class_type = get_enum_name(game_module.ClassType, class_type, True)
            return f"IfPlayerClass({condition}, {class_type})"

        if instruction_index == 12:
            condition, covenant = req_args
            covenant = get_enum_name(game_module.Covenant, covenant, True)
            return f"IfPlayerCovenant({condition}, {covenant})"

        if instruction_index == 13:
            condition, comparison_type, comparison_value = req_args
            if comparison_type == 4:
                return f"IfPlayerSoulLevelGreaterThanOrEqual({condition}, {comparison_value})"
            if comparison_type == 5:
                return f"IfPlayerSoulLevelLessThanOrEqual({condition}, {comparison_value})"
            comparison_type = get_enum_name(game_module.ComparisonType, comparison_type, True)
            return f"IfPlayerSoulLevelComparison({condition}, {comparison_type}, {comparison_value})"

        if instruction_index == 14:
            condition, character, comparison_type, comparison_value = req_args
            character = 'PLAYER' if character == 10000 else character
            try:
                comparison_type = get_enum_name(game_module.ComparisonType, comparison_type)
            except EnumStringError:
                return f"IfHealthValueComparison({condition}, {character}, {comparison_type}, {comparison_value})"
            else:
                return f"IfHealthValue{comparison_type.split('.')[-1]}({condition}, {character}, {comparison_value})"

    if instruction_class == 5:  # CONTROL (OBJECT)

        if instruction_index == 0:
            condition, state, obj = req_args
            if state == 1:
                return f"IfObjectDestroyed({condition}, {obj})"
            elif state == 0:
                return f"IfObjectNotDestroyed({condition}, {obj})"
            return f"IfObjectDestructionState({condition}, {obj}, state={boolify(state)})"

        if instruction_index == 1:
            condition, obj, attacker = req_args
            return f"IfObjectDamagedBy({condition}, {obj}, attacker={attacker})"

        if instruction_index == 2:
            condition, obj_act_id = req_args
            return f"IfObjectActivated({condition}, obj_act_id={obj_act_id})"

        if instruction_index == 3:
            condition, obj, comparison_type, value = req_args
            comparison_type = get_enum_name(game_module.ComparisonType, comparison_type, True)
            return f"IfObjectHealthValueComparison({condition}, {obj}, {comparison_type}, {value})"

    if instruction_class == 11:  # CONTROL (HITBOX)

        if instruction_index == 0:
            condition, hitbox_id = req_args
            return f"IfMovingOnHitbox({condition}, {hitbox_id})"

        if instruction_index == 1:
            condition, hitbox_id = req_args
            return f"IfRunningOnHitbox({condition}, {hitbox_id})"

        if instruction_index == 2:
            condition, hitbox_id = req_args
            return f"IfStandingOnHitbox({condition}, {hitbox_id})"

    # Failed to find instruction in game's combined decompiler.
    raise InstructionNotFoundError(f"Could not decompile instruction {instruction_class}[{instruction_index:02d}].")
