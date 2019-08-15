from soulstruct.events.core import boolify, get_enum_name, get_game_map_name, EnumStringError, InstructionNotFoundError
from soulstruct.enums.bloodborne import *


def decompile_instruction(instruction_class, instruction_index, req_args, game_module):
    """ Bloodborne-specific instruction decompiler. Run after the shared decompiler. Raises an error if it fails to
    resolve. """

    if instruction_class == 3:

        if instruction_index == 23:
            condition, attacked_entity, attacking_character, damage_type = req_args
            if attacked_entity == 10000:
                attacked_entity = 'PLAYER'
            if attacking_character == 10000:
                attacking_character = 'PLAYER'
            return (f"IfDamageType({condition}, attacked_entity={attacked_entity}, "
                    f"attacking_character={attacking_character}, damage_type={get_enum_name(DamageType, damage_type)})")

        if instruction_index == 24:
            condition, action_button_id, region = req_args
            return f"IfActionButtonInRegion({condition}, action_button_id={action_button_id}, region={region})"

        if instruction_index == 25:
            condition, armor_type, first, last = req_args
            return (f"IfPlayerArmorType({condition}, armor_type={get_enum_name(ArmorType, armor_type)}, "
                    f"required_armor_range_first={first}, required_armor_range_last={last})")

        if instruction_index == 26:
            condition, value, comp_type = req_args
            try:
                comp_type = get_enum_name(ComparisonType, comp_type)
            except EnumStringError:
                return f"IfPlayerInsightAmountComparison({condition}, {value}, comparison_type={comp_type})"
            else:
                comp_type = comp_type.split('.')[-1]
                return f"IfPlayerInsightAmount{comp_type}({condition}, {value})"

        if instruction_index == 27:
            condition, dialog_result = req_args
            try:
                dialog_result = get_enum_name(DialogResult, dialog_result)
            except EnumStringError:
                pass
            return f"IfDialogChoice({condition}, {dialog_result})"

        if instruction_index == 28:
            condition, playgo_state = req_args
            playgo_state = get_enum_name(PlayGoState, playgo_state, True)
            return f"IfPlayGoState({condition}, {playgo_state})"

        if instruction_index == 29:
            condition, client_type, comp_type, value = req_args
            client_type = get_enum_name(ClientType, client_type, True)
            comp_type = get_enum_name(ComparisonType, comp_type, True)
            return f"IfClientTypeCountComparison({condition}, {client_type}, {comp_type}, value={value})"

    if instruction_class == 4:

        if instruction_index == 15:
            condition, character, state = req_args
            character = 'PLAYER' if character == 10000 else character
            if state == 1:
                return f"IfCharacterDrawGroupActive({condition}, {character})"
            if state == 0:
                return f"IfCharacterDrawGroupInactive({condition}, {character})"
            return f"IfCharacterDrawGroupState({condition}, {character}, state={boolify(state)})"

    if instruction_class == 1000:

        if instruction_index == 101:
            label, state, condition = req_args
            label = get_enum_name(Label, label, True)
            if state == 1:
                return f"GotoIfConditionTrue({label}, input_condition={condition})"
            if state == 0:
                return f"GotoIfConditionFalse({label}, input_condition={condition})"
            return f"GotoIfConditionState({label}, state={boolify(state)}, input_condition={condition})"

        if instruction_index == 103:
            label, = req_args
            label = get_enum_name(Label, label, True)
            return f"Goto({label})"

        if instruction_index == 105:
            label, comp_type, left, right = req_args
            label = get_enum_name(Label, label, True)
            comp_type = get_enum_name(ComparisonType, comp_type, True)
            return f"GotoIfValueComparison({label}, {comp_type}, left={left}, right={right})"

        if instruction_index == 107:
            label, state, condition = req_args
            label = get_enum_name(Label, label, True)
            if state == 1:
                return f"GotoIfFinishedConditionTrue({label}, input_condition={condition})"
            if state == 0:
                return f"GotoIfFinishedConditionFalse({label}, input_condition={condition})"
            return f"GotoIfFinishedConditionState({label}, state={boolify(state)}, input_condition={condition})"

    if instruction_class == 1003:

        if instruction_index == 9:
            skip_lines, comp_type, value = req_args
            comp_type = get_enum_name(ComparisonType, comp_type, True)
            return f"SkipLinesIfCoopClientCountComparison({skip_lines}, {comp_type}, {value})"

        if instruction_index == 10:
            event_end_type, comparison_type, value = req_args
            if event_end_type == 0:
                return f"EndIfCoopClientCountComparison({comparison_type}, {value})"
            if event_end_type == 1:
                return f"RestartIfCoopClientCountComparison({comparison_type}, {value})"
            return f"TerminateIfCoopClientCountComparison({event_end_type}, {comparison_type}, {value})"

        if instruction_index == 11:
            skip_lines, gender = req_args
            gender = get_enum_name(Gender, gender, True)
            return f"SkipLinesIfPlayerGender({skip_lines}, {gender})"

        if instruction_index == 12:
            label, gender = req_args
            label = get_enum_name(Label, label, True)
            gender = get_enum_name(Gender, gender, True)
            return f"GotoIfPlayerGender({label}, {gender})"

        if instruction_index == 13:
            event_end_type, gender = req_args
            gender = get_enum_name(Gender, gender, True)
            if event_end_type == EventEndType.End:
                return f"EndIfPlayerGender({gender})"
            if event_end_type == EventEndType.Restart:
                return f"RestartIfPlayerGender({gender})"
            return f"TerminateIfPlayerGender({event_end_type}, {gender})"

        if instruction_index == 14:
            skip_lines, client_type, comparison_type, value = req_args
            return f"SkipLinesIfClientTypeCountComparison({skip_lines}, {client_type}, {comparison_type}, {value})"

        if instruction_index == 15:
            label, client_type, comparison_type, value = req_args
            label = get_enum_name(Label, label, True)
            return f"GotoIfClientTypeCountComparison({label}, {client_type}, {comparison_type}, {value})"

        if instruction_index == 16:
            event_end_type, client_type, comparison_type, value = req_args
            if event_end_type == 0:
                return f"EndIfClientTypeCountComparison({client_type}, {comparison_type}, {value})"
            if event_end_type == 1:
                return f"RestartIfClientTypeCountComparison({client_type}, {comparison_type}, {value})"
            return f"TerminateIfClientTypeCountComparison({event_end_type}, {client_type}, {comparison_type}, {value})"

        if instruction_index == 101:
            label, state, flag_type, flag = req_args
            label = get_enum_name(Label, label, True)
            if flag_type == FlagType.Absolute:
                if state == 1:
                    return f"GotoIfFlagOn({label}, {flag})"
                if state == 0:
                    return f"GotoIfFlagOff({label}, {flag})"
                raise EnumStringError
            if flag_type == FlagType.RelativeToThisEvent:
                if state == 1:
                    return f"GotoIfThisEventOn({label})"
                if state == 0:
                    return f"GotoIfThisEventOff({label})"
            if flag_type == FlagType.RelativeToThisEventSlot:
                if state == 1:
                    return f"GotoIfThisEventSlotOn({label})"
                if state == 0:
                    return f"GotoIfThisEventSlotOff({label})"
            flag_type = get_enum_name(FlagType, flag_type)
            return f"GotoIfFlagState({label}, {boolify(state)}, flag_type={flag_type}, flag={flag})"

        if instruction_index == 103:
            label, state, flag_type, first_flag, last_flag = req_args
            label = get_enum_name(Label, label, True)
            flag_type = get_enum_name(FlagType, flag_type)
            if flag_type == FlagType.Absolute:
                if state == RangeState.AllOn:
                    return f"GotoIfFlagRangeAllOn({label}, ({first_flag}, {last_flag}))"
                if state == RangeState.AllOff:
                    return f"GotoIfFlagRangeAllOff({label}, ({first_flag}, {last_flag}))"
                if state == RangeState.AnyOn:
                    return f"GotoIfFlagRangeAnyOn({label}, ({first_flag}, {last_flag}))"
                if state == RangeState.AnyOff:
                    return f"GotoIfFlagRangeAnyOff({label}, ({first_flag}, {last_flag}))"
            state = get_enum_name(RangeState, state, True)
            return f"GotoIfFlagRangeState({label}, {state}, {flag_type}, ({first_flag}, {last_flag}))"

        if instruction_index == 105:
            label, state = req_args
            label = get_enum_name(Label, label, True)
            try:
                state_name = get_enum_name(MultiplayerState, state).split('.')[-1]
            except EnumStringError:
                return f"GotoIfMultiplayerState({label}, state={state})"
            else:
                return f"GotoIf{state_name}({label})"

        if instruction_index == 107:
            label, state, area_id, block_id = req_args
            label = get_enum_name(Label, label, True)
            game_map = get_game_map_name(area_id, block_id, game_module)
            if state == 1:
                return f"GotoIfInsideMap({label}, {game_map})"
            if state == 0:
                return f"GotoIfOutsideMap({label}, {game_map})"
            return f"GotoIfMapPresenceState({label}, {game_map}, state={boolify(state)})"

        if instruction_index == 109:
            label, comparison_type, value = req_args
            label = get_enum_name(Label, label, True)
            comparison_type = get_enum_name(ComparisonType, comparison_type, True)
            return f"GotoIfCoopClientCountComparison({label}, {comparison_type}, {value})"

    if instruction_class == 1005:

        if instruction_index == 101:
            label, obj, state = req_args
            label = get_enum_name(Label, label, True)
            if state == 1:
                return f"GotoIfObjectDestroyed({label}, {obj})"
            if state == 0:
                return f"GotoIfObjectNotDestroyed({label}, {obj})"
            return f"GotoIfObjectDestructionState({label}, {obj}, state={boolify(state)})"

    if instruction_class == 1014:

        if 0 <= instruction_index <= 9:
            return f"Label({instruction_index})"
        else:
            raise ValueError("Label instruction index must be between 0 and 9.")

    if instruction_class == 2002:

        if instruction_index == 6:
            cutscene, cutscene_type, region, area_id, block_id, player_id, time_period_id = req_args
            game_map = get_game_map_name(area_id, block_id, game_module)
            cutscene_type = get_enum_name(CutsceneType, cutscene_type, True)
            return (f"PlayCutsceneAndMovePlayerAndSetTimePeriod({cutscene}, {cutscene_type}, {region}, "
                    f"{game_map}, player_id={player_id}, time_period_id={time_period_id})")

        if instruction_index == 7:
            cutscene, cutscene_type, player_id, time_period_id = req_args
            cutscene_type = get_enum_name(CutsceneType, cutscene_type, True)
            return f"PlayCutsceneAndSetTimePeriod({cutscene}, {cutscene_type}, {player_id}, {time_period_id})"

        if instruction_index == 8:
            region, area_id, block_id = req_args
            game_map = get_game_map_name(area_id, block_id, game_module)
            return f"PlayCutsceneAndMovePlayer_Dummy({region}, {game_map})"

    if instruction_class == 2003:

        if instruction_index == 15:
            miniboss_id, = req_args
            return f"HandleMinibossDefeat({miniboss_id})"

        if instruction_index == 27:
            arg1, = req_args
            return f"Unknown_2003_27({arg1})"

        if instruction_index == 41:
            source_flag, source_flag_bit_count, operand, target_flag, target_flag_bit_count, calculation_type = req_args
            calculation_type = get_enum_name(CalculationType, calculation_type, True)
            return (f"EventValueOperation({source_flag}, {source_flag_bit_count}, {operand}, {target_flag}, "
                    f"{target_flag_bit_count}, {calculation_type})")

        if instruction_index == 42:
            item_type, item, flag, bit_count = req_args
            item_type = get_enum_name(ItemType, item_type)
            return f"StoreItemAmountSpecifiedByFlagValue({item_type}, {item}, {flag}, {bit_count})"

        if instruction_index == 43:
            item_type, item, flag, bit_count = req_args
            item_type = get_enum_name(ItemType, item_type)
            return f"GivePlayerItemAmountSpecifiedByFlagValue({item_type}, {item}, {flag}, {bit_count})"

        if instruction_index == 44:
            state, = req_args
            if state == 1:
                return "EnableDirectionDisplay()"
            if state == 0:
                return "DisableDirectionDisplay()"
            return f"SetDirectionDisplayState(state={boolify(state)})"

        if instruction_index == 45:
            hitbox, level, grid_x, grid_y, state = req_args
            if state == 1:
                return f"EnableMapHitGridCorrespondence({hitbox}, {level}, {grid_x}, {grid_y})"
            if state == 0:
                return f"DisableMapHitGridCorrespondence({hitbox}, {level}, {grid_x}, {grid_y})"
            return f"SetMapHitGridCorrespondence({hitbox}, {level}, {grid_x}, {grid_y}, state={boolify(state)})"

        if instruction_index == 46:
            content_image_part_id, state = req_args
            return f"SetMapContentImageDisplayState({content_image_part_id}, {state})"

        if instruction_index == 47:
            hierarchy, grid_x, grid_y, state = req_args
            return f"SetMapBoundariesDisplay({hierarchy}, {grid_x}, {grid_y}, state={state})"

        if instruction_index == 48:
            region, state, duration, wind_id = req_args
            return f"SetAreaWind({region}, state={boolify(state)}, duration={duration}, wind_parameter_id={wind_id})"

        if instruction_index == 49:
            respawn_point_id, = req_args
            return f"MovePlayerToRespawnPoint({respawn_point_id})"

        if instruction_index == 50:
            spawner_id, = req_args
            return f"StartEnemySpawner({spawner_id})"

        if instruction_index == 51:
            sign_type, character, region, summon_flag, dismissal_flag = req_args
            character = 'PLAYER' if character == 10000 else character
            sign_type = get_enum_name(SingleplayerSummonSignType, sign_type, True)
            return (f"SummonNPC({sign_type}, {character}, {region}, summon_flag={summon_flag}, "
                    f"dismissal_flag={dismissal_flag})")

        if instruction_index == 52:
            warp_object_id, = req_args
            return f"InitializeWarpObject({warp_object_id})"

        if instruction_index == 53:
            boss_id, banner_type = req_args
            banner_type = get_enum_name(BannerType, banner_type, True)
            return f"BossDefeat({boss_id}, {banner_type})"

        if instruction_index == 54:
            character, = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"SendNPCSummonHome({character})"

    if instruction_class == 2004:

        if instruction_index == 8:
            character, special_effect_id, affect_npc_part_hp = req_args
            character = 'PLAYER' if character == 10000 else character
            return (f"AddSpecialEffect({character}, {special_effect_id}, "
                    f"affect_npc_part_hp={boolify(affect_npc_part_hp)})")

        if instruction_index == 14:
            character, target_entity, animation, wait_for_completion = req_args
            character = 'PLAYER' if character == 10000 else character
            return (f"RotateToFaceEntity({character}, {target_entity}, animation={animation}, "
                    f"wait_for_completion={boolify(wait_for_completion)})")

        if instruction_index == 48:
            character, bit_count, state_id = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"ChangeCharacterCloth({character}, {bit_count}, state_id={state_id})"

        if instruction_index == 49:
            character, patrol_information_id = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"ChangePatrolBehavior({character}, patrol_information_id={patrol_information_id})"

        if instruction_index == 50:
            character, distance = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"SetDistanceLimitForConversationStateChanges({character}, distance={distance})"

        if instruction_index == 51:
            recipient_character, recipient_target_rigid_index, recipient_model_point, attachment_character, \
                attachment_target_rigid_index, attachment_model_point = req_args
            return (f"Test_RequestRagdollRestraint({recipient_character}, {recipient_target_rigid_index}, "
                    f"{recipient_model_point}, {attachment_character}, {attachment_target_rigid_index}, "
                    f"{attachment_model_point})")

        if instruction_index == 52:
            character_init_param, = req_args
            return f"ChangePlayerCharacterInitParam({character_init_param})"

        if instruction_index == 53:
            character, = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"AdaptSpecialEffectHealthChangeToNPCPart({character})"

        if instruction_index == 54:
            character, state = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"SetGravityAndCollisionExcludingOwnWorld({character}, {boolify(state)})"

        if instruction_index == 55:
            character, speffect, affect_parts = req_args
            character = 'PLAYER' if character == 10000 else character
            return (f"AddSpecialEffect_WithUnknownEffect({character}, {speffect}, "
                    f"affect_npc_parts_hp={boolify(affect_parts)})")

    if instruction_class == 2005:

        if instruction_index == 16:
            obj, objact_id, relative_index, character = req_args
            character = 'PLAYER' if character == 10000 else character
            return (f"ActivateObjectWithSpecificCharacter({obj}, objact_id={objact_id}, "
                    f"relative_index={relative_index}, character={character})")

        if instruction_index == 17:
            obj, state = req_args
            return f"SetObjectDamageShieldState({obj}, state={boolify(state)})"

    if instruction_class == 2009:

        if instruction_index == 5:
            flag, obj, reaction_distance, reaction_angle, initial_sword_number, sword_level = req_args
            return (f"RegisterHealingFountain({flag}, {obj}, {reaction_distance}, reaction_angle={reaction_angle}, "
                    f"initial_sword_number={initial_sword_number}, sword_level={sword_level})")

    if instruction_class == 2010:

        if instruction_index == 4:
            sound_id, state = req_args
            return f"SetBossMusicState({sound_id}, state={boolify(state)})"

        if instruction_index == 5:
            entity_id, state = req_args
            state = get_enum_name(DoorState, state, True)
            return f"NotifyDoorEventSoundDampening({entity_id}, state={state})"

    if instruction_class == 2011:

        if instruction_index == 3:
            hitbox, state = req_args
            return f"SetHitboxResState({hitbox}, state={boolify(state)})"

    if instruction_class == 2013:

        if instruction_index == 1:
            name_string, = req_args
            return f"CreatePlayLog({name_string})"

        if instruction_index == 2:
            measurement_id, name_string, overwrite = req_args
            return f"StartPlayLogMeasurement({measurement_id}, {name_string}, overwrite={boolify(overwrite)})"

        if instruction_index == 3:
            measurement_id, = req_args
            return f"StopPlayLogMeasurement({measurement_id})"

        if instruction_index == 4:
            category, name_string, output_multiplayer_state = req_args
            category = get_enum_name(PlayerPlayLogParameter, category, True)
            output_multiplayer_state = get_enum_name(PlayLogMultiplayerType, output_multiplayer_state, True)
            return f"PlayLogParameterOutput({category}, {name_string}, {output_multiplayer_state})"

    raise InstructionNotFoundError(f"Instruction not decompiled: {instruction_class}[{instruction_index:02d}].")
