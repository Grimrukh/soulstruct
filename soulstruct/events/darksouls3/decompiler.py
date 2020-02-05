from soulstruct.events.internal import InstructionNotFoundError, get_enum_name, EnumStringError, boolify, \
    get_game_map_variable_name
from soulstruct.enums.darksouls3 import *


def get_target_args(target_comparison_type, target_count):
    """ Determine the arg string for the fairly useless extra DS3 arguments. """
    if target_comparison_type != 0 or target_count != 1:
        target_comparison_type = get_enum_name(ComparisonType, target_comparison_type, True)
        return f', target_comparison_type={target_comparison_type}, target_count={target_count}'
    return ''


def decompile_instruction(instruction_class, instruction_index, req_args, game_module):
    """ Bloodborne-specific instruction decompiler. Run after the shared decompiler. Raises an error if it fails to
    resolve. """

    # TODO: Probably easier to call the game-specific decompiler before trying the shared one, in case I forget to
    #  remove one from shared that turns out to differ in one or more games.

    if instruction_class == 3:

        if instruction_index == 2:
            condition, state, character, region, min_target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            min_target_arg = f', min_target_count={min_target_count}' if min_target_count != 1 else ''
            if state == 1:
                return f"IfCharacterInsideRegion({condition}, {character}, region={region}{min_target_arg})"
            elif state == 0:
                return f"IfCharacterOutsideRegion({condition}, {character}, region={region}{min_target_arg})"
            return f"IfCharacterRegionState({condition}, {character}, region={region}, state={boolify(state)}{min_target_arg})"

        if instruction_index == 3:
            condition, state, entity, other_entity, radius, min_target_count = req_args
            min_target_arg = f', min_target_count={min_target_count}' if min_target_count != 1 else ''
            entity = 'PLAYER' if entity == 10000 else entity
            other_entity = 'PLAYER' if other_entity == 10000 else other_entity
            if state == 1:
                return f"IfEntityWithinDistance({condition}, {entity}, {other_entity}, radius={radius}{min_target_arg})"
            elif state == 0:
                return f"IfEntityBeyondDistance({condition}, {entity}, {other_entity}, radius={radius}{min_target_arg})"
            return f"IfEntityDistanceState({condition}, {entity}, {other_entity}, {radius}, state={boolify(state)}{min_target_arg})"

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

        if instruction_index == 26:
            condition, not_in_own_world = req_args
            if not_in_own_world == 1:
                return f"IfPlayerNotInOwnWorld({condition})"
            if not_in_own_world == 0:
                return f"IfPlayerInOwnWorld({condition})"
            return f"IfPlayerOwnWorldState({condition}, not_in_own_world={not_in_own_world}"

        if instruction_index == 28:
            condition, state, area_id, block_id, ceremony = req_args
            game_map = get_game_map_variable_name(area_id, block_id, game_module)
            if state == 1:
                return f"IfMapInCeremony({condition}, game_map={game_map}, ceremony_id={ceremony})"
            if state == 0:
                return f"IfMapNotInCeremony({condition}, game_map={game_map}, ceremony_id={ceremony})"
            return f"IfMapCeremonyState({condition}, state={state}, game_map={game_map}, ceremony_id={ceremony})"

        if instruction_index == 29:
            condition, = req_args
            return f"IfMultiplayerNetworkPenalized({condition})"

        if instruction_index == 30:
            condition, gender = req_args
            gender = get_enum_name(Gender, gender, True)
            return f"IfPlayerGender({condition}, {gender})"

        if instruction_index == 31:
            condition, cutscene = req_args
            return f"IfOngoingCutsceneFinished({condition}, {cutscene})"

        if instruction_index == 32:
            condition, is_ready = req_args
            return f"IfHollowArenaMatchReadyState({condition}, is_ready={boolify(is_ready)})"

        if instruction_index == 33:
            condition, result = req_args
            result = get_enum_name(HollowArenaResult, result)
            return f"IfHollowArenaSoloResults({condition}, {result})"

        if instruction_index == 34:
            condition, comparison_type, value = req_args
            comparison_type = get_enum_name(ComparisonType, comparison_type, True)
            return f"IfHollowArenaSoloScoreComparison({condition}, comparison_type={comparison_type}, value={value})"

        if instruction_index == 35:
            condition, result = req_args
            result = get_enum_name(HollowArenaResult, result, True)
            return f"IfHollowArenaTeamResults({condition}, result={result})"

        if instruction_index == 38:
            condition, is_disconnected = req_args
            return f"IfSteamDisconnected({condition}, is_disconnected={boolify(is_disconnected)})"

        if instruction_index == 39:
            condition, comparison_state, comparison_type, value = req_args
            comparison_type = get_enum_name(ComparisonType, comparison_type, True)
            return (f"IfAllyPhantomCountComparison({condition}, comparison_state={boolify(comparison_state)}, "
                    f"comparison_type={comparison_type}, value={value})")

    if instruction_class == 4:

        if instruction_index == 0:
            condition, character, state, target_comparison_type, target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            target_args = get_target_args(target_comparison_type, target_count)
            if state == 1:
                return f"IfCharacterDead({condition}, {character}{target_args})"
            elif state == 0:
                return f"IfCharacterAlive({condition}, {character}{target_args})"
            return f"IfCharacterDeathState({condition}, character={character}, state={state}{target_args})"
                
        if instruction_index == 2:
            condition, character, comparison_type, value, target_comparison_type, target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            comparison_type = get_enum_name(ComparisonType, comparison_type, True)
            target_args = get_target_args(target_comparison_type, target_count)
            if comparison_type == ComparisonType.Equal:
                return f"IfHealthEqual({condition}, character={character}, value={value}{target_args})"
            elif comparison_type == ComparisonType.NotEqual:
                return f"IfHealthNotEqual({condition}, character={character}, value={value}{target_args})"
            elif comparison_type == ComparisonType.GreaterThan:
                return f"IfHealthGreaterThan({condition}, character={character}, value={value}{target_args})"
            elif comparison_type == ComparisonType.LessThan:
                return f"IfHealthLessThan({condition}, character={character}, value={value}{target_args})"
            elif comparison_type == ComparisonType.GreaterThanOrEqual:
                return f"IfHealthGreaterThanOrEqual({condition}, character={character}, value={value}{target_args})"
            elif comparison_type == ComparisonType.LessThanOrEqual:
                return f"IfHealthLessThanOrEqual({condition}, character={character}, value={value}{target_args})"
            return f"IfHealthComparison({condition}, character={character}, comparison_type={comparison_type}, value={value}{target_args})"

        if instruction_index == 3:
            condition, character, character_type, target_comparison_type, target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            character_type = get_enum_name(CharacterType, character_type, True)
            target_args = get_target_args(target_comparison_type, target_count)
            return f"IfCharacterType({condition}, character={character}, character_type={character_type}{target_args})"

        if instruction_index == 5:
            condition, character, special_effect, state, target_comparison_type, target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            target_args = get_target_args(target_comparison_type, target_count)
            if state == 1:
                return f"IfCharacterHasSpecialEffect({condition}, character={character}, special_effect={special_effect}{target_args})"
            elif state == 0:
                return f"IfCharacterDoesNotHaveSpecialEffect({condition}, character={character}, special_effect={special_effect}{target_args})"
            return f"IfCharacterSpecialEffectState({condition}, character={character}, special_effect={special_effect}, state={state}{target_args})"

        if instruction_index == 7:
            condition, character, state, target_comparison_type, target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            target_args = get_target_args(target_comparison_type, target_count)
            if state == 1:
                return f"IfCharacterBackreadEnabled({condition}, character={character}{target_args})"
            elif state == 0:
                return f"IfCharacterBackreadDisabled({condition}, character={character}{target_args})"
            return f"IfCharacterBackreadState({condition}, character={character}, state={state}{target_args})"

        if instruction_index == 8:
            condition, character, tae_event_id, state, target_comparison_type, target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            target_args = get_target_args(target_comparison_type, target_count)
            if state == 1:
                return f"IfHasTAEEvent({condition}, character={character}, tae_event_id={tae_event_id}{target_args})"
            elif state == 0:
                return f"IfDoesNotHaveTAEEvent({condition}, character={character}, tae_event_id={tae_event_id}{target_args})"
            return f"IfTAEEventState({condition}, character={character}, tae_event_id={tae_event_id}, state={state}{target_args})"

        if instruction_index == 9:
            condition, character, ai_status, target_comparison_type, target_count = req_args
            ai_status = get_enum_name(AIStatusType, ai_status, True)
            target_args = get_target_args(target_comparison_type, target_count)
            return f"IfHasAIStatus({condition}, character={character}, ai_status={ai_status}{target_args})"

        if instruction_index == 14:
            condition, character, comparison_type, value, target_comparison_type, target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            target_args = get_target_args(target_comparison_type, target_count)
            if comparison_type == ComparisonType.Equal:
                return f"IfHealthValueEqual({condition}, character={character}, value={value}{target_args})"
            elif comparison_type == ComparisonType.NotEqual:
                return f"IfHealthValueNotEqual({condition}, character={character}, value={value}{target_args})"
            elif comparison_type == ComparisonType.GreaterThan:
                return f"IfHealthValueGreaterThan({condition}, character={character}, value={value}{target_args})"
            elif comparison_type == ComparisonType.LessThan:
                return f"IfHealthValueLessThan({condition}, character={character}, value={value}{target_args})"
            elif comparison_type == ComparisonType.GreaterThanOrEqual:
                return f"IfHealthValueGreaterThanOrEqual({condition}, character={character}, value={value}{target_args})"
            elif comparison_type == ComparisonType.LessThanOrEqual:
                return f"IfHealthValueLessThanOrEqual({condition}, character={character}, value={value}{target_args})"
            return f"IfHealthValueComparison({condition}, character={character}, comparison_type={comparison_type}, value={value}{target_args})"

        if instruction_index == 15:
            condition, character, state, target_comparison_type, target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            target_args = get_target_args(target_comparison_type, target_count)
            if state == 1:
                return f"IfCharacterDrawGroupActive({condition}, {character}{target_args})"
            if state == 0:
                return f"IfCharacterDrawGroupInactive({condition}, {character}{target_args})"
            return f"IfCharacterDrawGroupState({condition}, character={character}, state={state}{target_args})"

        if instruction_index == 26:
            condition, comparison_type, value = req_args
            comparison_type = get_enum_name(ComparisonType, comparison_type, True)
            return f"IfPlayerRemainingYoelLevelComparison({condition}, comparison_type={comparison_type}, value={value})"

        if instruction_index == 27:
            condition, character, invade_type, target_comparison_type, target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            target_args = get_target_args(target_comparison_type, target_count)
            return f"IfCharacterInvadeType({condition}, character={character}, invade_type={invade_type}{target_args})"

        if instruction_index == 28:
            condition, character, chameleon_fx_id, is_transformed = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"IfCharacterChameleonState({condition}, character={character}, chameleon_fx_id={chameleon_fx_id}, is_transformed={boolify(is_transformed)})"

    if instruction_class == 5:

        if instruction_index == 0:
            condition, state, obj, target_comparison_type, target_count = req_args
            target_args = get_target_args(target_comparison_type, target_count)
            if state == 1:
                return f"IfObjectDestroyed({condition}, obj={obj}{target_args})"
            elif state == 0:
                return f"IfObjectNotDestroyed({condition}, obj={obj}{target_args})"
            return f"IfObjectDestructionState({condition}, state={boolify(state)}, obj={obj}{target_args})"

        if instruction_index == 9:
            condition, obj, comparison_type, state, target_comparison_type, target_count = req_args
            comparison_type = get_enum_name(ComparisonType, comparison_type, True)
            target_args = get_target_args(target_comparison_type, target_count)
            return f"IfObjectBurnState({condition}, obj={obj}, comparison_type={comparison_type}, state={boolify(state)}{target_args})"

        if instruction_index == 10:
            condition, obj, state, target_comparison_type, target_count = req_args
            target_args = get_target_args(target_comparison_type, target_count)
            if state == 1:
                return f"IfObjectBackreadEnabled({condition}, obj={obj}{target_args})"
            elif state == 0:
                return f"IfObjectBackreadDisabled({condition}, obj={obj}{target_args})"
            return f"IfObjectBackreadState({condition}, obj={obj}, state={state}{target_args})"

        if instruction_index == 11:
            condition, obj, state, target_comparison_type, target_count = req_args
            target_args = get_target_args(target_comparison_type, target_count)
            if state == 1:
                return f"IfObjectBackreadEnabled_Alternate({condition}, obj={obj}{target_args})"
            elif state == 0:
                return f"IfObjectBackreadDisabled_Alternate({condition}, obj={obj}{target_args})"
            return f"IfObjectBackreadState_Alternate({condition}, obj={obj}, state={state}{target_args})"

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

    if instruction_class == 1001:

        if instruction_index == 4:
            match_type, is_second_half = req_args
            return f"WaitHollowArenaHalftime(match_type={match_type}, is_second_half={boolify(is_second_half)})"

    if instruction_class == 1003:

        if instruction_index == 5:
            line_count, state = req_args
            try:
                state_name = get_enum_name(MultiplayerState, state).split('.')[-1]
            except EnumStringError:
                return f"SkipLinesIfMultiplayerState({line_count}, state={state})"
            else:
                return f"SkipLinesIf{state_name}({line_count})"

        if instruction_index == 6:
            event_end_type, state = req_args
            if event_end_type == EventEndType.End:
                try:
                    state_name = get_enum_name(MultiplayerState, state).split('.')[-1]
                except EnumStringError:
                    pass
                else:
                    return f"EndIf{state_name}()"
            elif event_end_type == EventEndType.Restart:
                try:
                    state_name = get_enum_name(MultiplayerState, state).split('.')[-1]
                except EnumStringError:
                    pass
                else:
                    return f"RestartIf{state_name}()"
            return f"TerminateIfMultiplayerState(event_end_type={event_end_type}, state={state})"

        if instruction_index == 9:
            line_count, comp_type, value = req_args
            comp_type = get_enum_name(ComparisonType, comp_type, True)
            return f"SkipLinesIfCoopClientCountComparison({line_count}, {comp_type}, {value})"

        if instruction_index == 10:
            event_end_type, comparison_type, value = req_args
            if event_end_type == 0:
                return f"EndIfCoopClientCountComparison({comparison_type}, {value})"
            if event_end_type == 1:
                return f"RestartIfCoopClientCountComparison({comparison_type}, {value})"
            return f"TerminateIfCoopClientCountComparison({event_end_type}, {comparison_type}, {value})"

        if instruction_index == 11:
            label, character, special_effect, state, target_comparison_type, target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            label = get_enum_name(Label, label, True)
            target_args = get_target_args(target_comparison_type, target_count)
            if state == 1:
                return f"GotoIfCharacterHasSpecialEffect({label}, character={character}, special_effect={special_effect}{target_args})"
            elif state == 0:
                return f"GotoIfCharacterDoesNotHaveSpecialEffect({label}, character={character}, special_effect={special_effect}{target_args})"
            return f"GotoIfCharacterSpecialEffectState({label}, character={character}, special_effect={special_effect}, state={state}{target_args})"

        if instruction_index == 12:
            label, not_in_own_world = req_args
            label = get_enum_name(Label, label, True)
            if not_in_own_world == 1:
                return f"GotoIfPlayerNotInOwnWorld({label})"
            elif not_in_own_world == 0:
                return f"GotoIfPlayerInOwnWorld({label})"
            return f"GotoIfPlayerOwnWorldState({label}, not_in_own_world={boolify(not_in_own_world)})"

        if instruction_index == 13:
            event_end_type, not_in_own_world = req_args
            if event_end_type == 0:
                if not_in_own_world == 1:
                    return f"EndIfPlayerNotInOwnWorld()"
                elif not_in_own_world == 0:
                    return f"EndIfPlayerInOwnWorld()"
                return f"EndIfPlayerOwnWorldState(not_in_own_world={not_in_own_world})"
            elif event_end_type == 1:
                if not_in_own_world == 1:
                    return f"RestartIfPlayerNotInOwnWorld()"
                elif not_in_own_world == 0:
                    return f"RestartIfPlayerInOwnWorld()"
                return f"RestartIfPlayerOwnWorldState(not_in_own_world={not_in_own_world})"
            return f"TerminateIfPlayerOwnWorldState(event_end_type={event_end_type}, state={not_in_own_world})"

        if instruction_index == 14:
            line_count, client_type, comparison_type, value = req_args
            client_type = get_enum_name(ClientType, client_type, True)
            comparison_type = get_enum_name(ComparisonType, comparison_type, True)
            return f"SkipLinesIfClientTypeCountComparison({line_count}, client_type={client_type}, comparison_type={comparison_type}, value={value})"

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
            if flag_type == FlagType.Absolute:
                if state == RangeState.AllOn:
                    return f"GotoIfFlagRangeAllOn({label}, ({first_flag}, {last_flag}))"
                if state == RangeState.AllOff:
                    return f"GotoIfFlagRangeAllOff({label}, ({first_flag}, {last_flag}))"
                if state == RangeState.AnyOn:
                    return f"GotoIfFlagRangeAnyOn({label}, ({first_flag}, {last_flag}))"
                if state == RangeState.AnyOff:
                    return f"GotoIfFlagRangeAnyOff({label}, ({first_flag}, {last_flag}))"
            flag_type = get_enum_name(FlagType, flag_type)
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
            game_map = get_game_map_variable_name(area_id, block_id, game_module)
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

        if instruction_index == 111:
            event_end_type, character, special_effect, state, target_comparison_type, target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            target_args = get_target_args(target_comparison_type, target_count)
            if event_end_type == EventEndType.End:
                if state == 1:
                    return f"EndIfCharacterHasSpecialEffect(character={character}, special_effect={special_effect}{target_args})"
                elif state == 0:
                    return f"EndIfCharacterDoesNotHaveSpecialEffect(character={character}, special_effect={special_effect}{target_args})"
            elif event_end_type == EventEndType.Restart:
                if state == 1:
                    return f"RestartIfCharacterHasSpecialEffect(character={character}, special_effect={special_effect}{target_args})"
                elif state == 0:
                    return f"RestartIfCharacterDoesNotHaveSpecialEffect(character={character}, special_effect={special_effect}{target_args})"
            return f"TerminateIfCharacterSpecialEffectState(event_end_type={event_end_type}, character={character}, special_effect={special_effect}, state={state}{target_args})"

        if instruction_index == 112:
            line_count, character, special_effect, state, target_comparison_type, target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            target_args = get_target_args(target_comparison_type, target_count)
            if state == 1:
                return f"SkipLinesIfCharacterHasSpecialEffect({line_count}, character={character}, special_effect={special_effect}{target_args})"
            elif state == 0:
                return f"SkipLinesIfCharacterDoesNotHaveSpecialEffect({line_count}, character={character}, special_effect={special_effect}{target_args})"
            return f"SkipLinesIfCharacterSpecialEffectState({line_count}, character={character}, special_effect={special_effect}, state={state}{target_args})"

        if instruction_index == 200:
            label, state, character, region, min_target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            label = get_enum_name(Label, label, True)
            min_target_arg = f', min_target_count={min_target_count}' if min_target_count != 1 else ''
            if state == 1:
                return f"GotoIfCharacterInsideRegion({label}, character={character}, region={region}{min_target_arg})"
            elif state == 0:
                return f"GotoIfCharacterOutsideRegion({label}, character={character}, region={region}{min_target_arg})"
            return f"GotoIfCharacterRegionState({label}, state={boolify(state)}, character={character}, region={region}{min_target_arg})"

        if instruction_index == 201:
            event_end_type, state, character, region, min_target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            min_target_arg = f', min_target_count={min_target_count}' if min_target_count != 1 else ''
            if event_end_type == EventEndType.End:
                if state == 1:
                    return f"EndIfCharacterInsideRegion(character={character}, region={region}{min_target_arg})"
                elif state == 0:
                    return f"EndIfCharacterOutsideRegion(character={character}, region={region}{min_target_arg})"
                return f"EndIfCharacterRegionState(state={boolify(state)}, character={character}, region={region}{min_target_arg})"
            elif event_end_type == EventEndType.Restart:
                if state == 1:
                    return f"RestartIfCharacterInsideRegion(character={character}, region={region}{min_target_arg})"
                elif state == 0:
                    return f"RestartIfCharacterOutsideRegion(character={character}, region={region}{min_target_arg})"
                return f"RestartIfCharacterRegionState(state={boolify(state)}, character={character}, region={region}{min_target_arg})"
            return f"TerminateIfCharacterRegionState(event_end_type={event_end_type}, state={boolify(state)}, character={character}, region={region}{min_target_arg})"

        if instruction_index == 202:
            line_count, state, character, region, min_target_count = req_args
            character = 'PLAYER' if character == 10000 else character
            min_target_arg = f', min_target_count={min_target_count}' if min_target_count != 1 else ''
            if state == 1:
                return f"SkipLinesIfCharacterInsideRegion({line_count}, character={character}, region={region}{min_target_arg})"
            elif state == 0:
                return f"SkipLinesIfCharacterOutsideRegion({line_count}, character={character}, region={region}{min_target_arg})"
            return f"SkipLinesIfCharacterRegionState({line_count}, state={boolify(state)}, character={character}, region={region}{min_target_arg})"

        if instruction_index == 211:
            label, match_type = req_args
            label = get_enum_name(Label, label, True)
            match_type = get_enum_name(HollowArenaMatchType, match_type, True)
            return f"GotoIfHollowArenaMatchType({label}, match_type={match_type})"

    if instruction_class == 1005:

        if instruction_index == 1:
            line_count, state, obj, target_comparison_type, target_count = req_args
            target_args = get_target_args(target_comparison_type, target_count)
            if state == 1:
                return f"SkipLinesIfObjectDestroyed({line_count}, obj={obj}{target_args})"
            elif state == 0:
                return f"SkipLinesIfObjectNotDestroyed({line_count}, obj={obj}{target_args})"
            return f"SkipLinesIfObjectDestructionState({line_count}, obj={obj}, state={state}{target_args})"

        if instruction_index == 2:
            event_end_type, state, obj, target_comparison_type, target_count = req_args
            target_args = get_target_args(target_comparison_type, target_count)
            if event_end_type == EventEndType.End:
                if state == 1:
                    return f"EndIfObjectDestroyed({obj}{target_args})"
                elif state == 0:
                    return f"EndIfObjectNotDestroyed({obj}{target_args})"
            elif event_end_type == EventEndType.Restart:
                if state == 1:
                    return f"RestartIfObjectDestroyed({obj}{target_args})"
                elif state == 0:
                    return f"RestartIfObjectNotDestroyed({obj}{target_args})"
            return f"TerminateIfObjectDestructionState(event_end_type={event_end_type}, obj={obj}, state={state}{target_args})"

        if instruction_index == 101:
            label, state, obj, target_comparison_type, target_count = req_args
            label = get_enum_name(Label, label, True)
            target_args = get_target_args(target_comparison_type, target_count)
            if state == 1:
                return f"GotoIfObjectDestroyed({label}, obj={obj}{target_args})"
            if state == 0:
                return f"GotoIfObjectNotDestroyed({label}, obj={obj}{target_args})"
            return f"GotoIfObjectDestructionState({label}, obj={obj}, state={state}{target_args})"

    if instruction_class == 1014:

        if 0 <= instruction_index <= 20:
            return f"DefineLabel({instruction_index})"
        else:
            raise ValueError("Label instruction index must be between 0 and 9.")

    if instruction_class == 2002:

        if instruction_index == 6:
            cutscene, cutscene_type, region, area_id, block_id, player_id, time_period_id = req_args
            game_map = get_game_map_variable_name(area_id, block_id, game_module)
            cutscene_type = get_enum_name(CutsceneType, cutscene_type, True)
            return (f"PlayCutsceneAndMovePlayerAndSetTimePeriod({cutscene}, {cutscene_type}, {region}, "
                    f"{game_map}, player_id={player_id}, time_period_id={time_period_id})")

        if instruction_index == 7:
            cutscene, cutscene_type, player_id, time_period_id = req_args
            cutscene_type = get_enum_name(CutsceneType, cutscene_type, True)
            return f"PlayCutsceneAndSetTimePeriod({cutscene}, {cutscene_type}, {player_id}, {time_period_id})"

        if instruction_index == 8:
            region, area_id, block_id = req_args
            game_map = get_game_map_variable_name(area_id, block_id, game_module)
            return f"PlayCutsceneAndMovePlayer_Dummy({region}, {game_map})"

        if instruction_index == 9:
            cutscene, cutscene_type, ceremony_id, unknown, region, area_id, block_id, player_id = req_args
            game_map = get_game_map_variable_name(area_id, block_id, game_module)
            cutscene_type = get_enum_name(CutsceneType, cutscene_type, True)
            return (f"PlayCutsceneAndMovePlayerAndSetMapCeremony({cutscene}, cutscene_type={cutscene_type}, "
                    f"ceremony_id={ceremony_id}, unknown={unknown}, region={region}, game_map={game_map}, "
                    f"player_id={player_id})")

        if instruction_index == 10:
            cutscene, cutscene_type, ceremony_id, unknown, player_id = req_args
            cutscene_type = get_enum_name(CutsceneType, cutscene_type, True)
            return f"PlayCutsceneAndSetMapCeremony(cutscene={cutscene}, cutscene_type={cutscene_type}, ceremony_id={ceremony_id}, unknown={unknown}, player_id={player_id})"

        if instruction_index == 11:
            cutscene, cutscene_type, region, area_id, block_id, player_id, unknown1, unknown2 = req_args
            game_map = get_game_map_variable_name(area_id, block_id, game_module)
            cutscene_type = get_enum_name(CutsceneType, cutscene_type, True)
            return f"PlayCutsceneAndMovePlayer_WithUnknowns(cutscene={cutscene}, cutscene_type={cutscene_type}, region={region}, game_map={game_map}, player_id={player_id}, unknown1={unknown1}, unknown2={unknown2})"

        if instruction_index == 12:
            cutscene, cutscene_type, region, area_id, block_id, player_id, other_region = req_args
            game_map = get_game_map_variable_name(area_id, block_id, game_module)
            cutscene_type = get_enum_name(CutsceneType, cutscene_type, True)
            return f"PlayCutsceneAndMovePlayer_WithSecondRegion(cutscene={cutscene}, cutscene_type={cutscene_type}, region={region}, game_map={game_map}, player_id={player_id}, other_region={other_region})"

    if instruction_class == 2003:

        if instruction_index == 11:
            state, character, slot, name = req_args
            character = 'PLAYER' if character == 10000 else character
            slot_arg = f', slot={slot}' if slot != 0 else ''
            if state == 1:
                return f"EnableBossHealthBar({character}, name={name}{slot_arg})"
            elif state == 0:
                return f"DisableBossHealthBar({character}, name={name}{slot_arg})"
            return f"SetBossHealthBarState({character}, name={name}, slot={slot}, state={state})"

        if instruction_index == 15:
            miniboss_id, = req_args
            return f"HandleMinibossDefeat(miniboss_id={miniboss_id})"

        if instruction_index == 18:
            entity, animation_id, loop, wait, skip_transition, unknown1, unknown2 = req_args
            entity_id = 'PLAYER' if entity == 10000 else entity
            keyword_args = []
            if loop != 0:
                keyword_args.append(f'loop={boolify(loop)}')
            if wait != 0:
                keyword_args.append(f'wait_for_completion={boolify(wait)}')
            if skip_transition != 0:
                keyword_args.append(f'skip_transition={boolify(skip_transition)}')
            if unknown1 != 0:
                keyword_args.append(f'unknown1={unknown1}')
            if unknown2 != 1.0:
                keyword_args.append(f'unknown2={unknown2}')
            keyword_args = ', '.join(keyword_args)
            if keyword_args:
                return f"ForceAnimation({entity_id}, {animation_id}, {keyword_args})"
            return f"ForceAnimation({entity_id}, {animation_id})"

        if instruction_index == 27:
            arg1, = req_args
            return f"Unknown_2003_27(arg1={arg1})"

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
            collision, level, grid_x, grid_y, state = req_args
            if state == 1:
                return f"EnableMapHitGridCorrespondence({collision}, {level}, {grid_x}, {grid_y})"
            if state == 0:
                return f"DisableMapHitGridCorrespondence({collision}, {level}, {grid_x}, {grid_y})"
            return f"SetMapHitGridCorrespondence({collision}, {level}, {grid_x}, {grid_y}, state={boolify(state)})"

        if instruction_index == 46:
            content_image_part_id, state = req_args
            return f"SetMapContentImageDisplayState(content_image_part_id={content_image_part_id}, state={state})"

        if instruction_index == 47:
            hierarchy, grid_coord_x, grid_coord_y, state = req_args
            return f"SetMapBoundariesDisplay(hierarchy={hierarchy}, grid_coord_x={grid_coord_x}, grid_coord_y={grid_coord_y}, state={state})"

        if instruction_index == 48:
            region, state, duration, wind_parameter_id = req_args
            return f"SetAreaWind(region={region}, state={state}, duration={duration}, wind_parameter_id={wind_parameter_id})"

        if instruction_index == 49:
            respawn_point_id, = req_args
            return f"MovePlayerToRespawnPoint(respawn_point_id={respawn_point_id})"

        if instruction_index == 50:
            spawner_id, = req_args
            return f"StartEnemySpawner(spawner_id={spawner_id})"

        if instruction_index == 51:
            sign_type, character, region, summon_flag, dismissal_flag = req_args
            sign_type = get_enum_name(SingleplayerSummonSignType, sign_type, True)
            return (f"SummonNPC({sign_type}, {character}, {region}, summon_flag={summon_flag}, "
                    f"dismissal_flag={dismissal_flag})")

        if instruction_index == 52:
            warp_object_id, = req_args
            return f"InitializeWarpObject(warp_object_id={warp_object_id})"

        if instruction_index == 54:
            character, = req_args
            return f"MakeEnemyAppear({character})"

        if instruction_index == 57:
            ceremony_id, = req_args
            return f"SetCurrentMapCeremony(ceremony_id={ceremony_id})"

        if instruction_index == 59:
            area_id, block_id, ceremony_id = req_args
            game_map = get_game_map_variable_name(area_id, block_id, game_module)
            return f"SetMapCeremony(game_map={game_map}, ceremony_id={ceremony_id})"

        if instruction_index == 61:
            message, = req_args
            return f"DisplayEpitaphMessage(message={message})"

        if instruction_index == 62:
            flag, state = req_args
            state = get_enum_name(FlagState, state, True)
            return f"SetNetworkConnectedFlagState(flag={flag}, state={boolify(state)})"

        if instruction_index == 63:
            first_flag, last_flag, state = req_args
            state = get_enum_name(RangeState, state, True)
            return f"SetNetworkConnectedFlagRangeState(flag_range=({first_flag}, {last_flag}), state={state})"

        if instruction_index == 64:
            level_1_count, level_2_count = req_args
            return f"SetOmissionModeCounts(level_1_count={level_1_count}, level_2_count={level_2_count})"

        if instruction_index == 65:
            return f"ResetOmissionModeCountsToDefault()"

        if instruction_index == 66:
            item_type, item_id, item_lot_id, trade_completed_flag, crow_response_flag = req_args
            item_type = get_enum_name(ItemType, item_type, True)
            return f"InitializeCrowTrade(item_type={item_type}, item_id={item_id}, item_lot_id={item_lot_id}, trade_completed_flag={trade_completed_flag}, crow_response_flag={crow_response_flag})"

        if instruction_index == 67:
            region, = req_args
            return f"InitializeCrowTradeRegion(region={region})"

        if instruction_index == 70:
            state, = req_args
            return f"SetNetworkInteractionState(state={boolify(state)})"

        if instruction_index == 71:
            is_invisible, = req_args
            if is_invisible == 1:
                return f"DisableHUDVisibility()"
            elif is_invisible == 0:
                return f"EnableHUDVisibility()"
            return f"SetHUDVisibility(is_invisible={is_invisible})"

        if instruction_index == 72:
            bonfire, animation, state = req_args
            if state == 1:
                return f"EnableBonfireWarping(bonfire={bonfire}, animation={animation})"
            if state == 0:
                return f"DisableBonfireWarping(bonfire={bonfire}, animation={animation})"
            return f"SetBonfireWarpingState(bonfire={bonfire}, animation={animation}, state={state})"

        if instruction_index == 73:
            unknown1, unknown2 = req_args
            return f"SetAutogeneratedEventSpecificFlag_1(unknown1={unknown1}, unknown2={unknown2})"

        if instruction_index == 74:
            boss, banner = req_args
            banner = get_enum_name(BannerType, banner, True)
            return f"HandleBossDefeatAndDisplayBanner(boss={boss}, banner={banner})"

        if instruction_index == 75:
            unknown1, unknown2 = req_args
            return f"SetAutogeneratedEventSpecificFlag_2(unknown1={unknown1}, unknown2={unknown2})"

        if instruction_index == 76:
            tips_disabled, = req_args
            if tips_disabled == 1:
                return "DisableLoadingScreenTips()"
            elif tips_disabled == 0:
                return "EnableLoadingScreenTips()"
            return f"SetLoadingScreenTipsState(tips_disabled={tips_disabled})"

        if instruction_index == 77:
            gesture_id, item_type, item_id = req_args
            item_type = get_enum_name(ItemType, item_type, True)
            return f"AwardGestureItem(gesture_id={gesture_id}, item_type={item_type}, item_id={item_id})"

        if instruction_index == 78:
            character, = req_args
            return f"SendNPCSummonHome({character})"

        if instruction_index == 79:
            unknown1, = req_args
            return f"Unknown_2003_79(unknown1={unknown1})"

        if instruction_index == 80:
            state, character, slot, name, decoration = req_args
            if state == 1:
                return f"EnableDecoratedBossHealthBar({character}, slot={slot}, name={name}, decoration={decoration})"
            if state == 0:
                return f"DisableDecoratedBossHealthBar({character}, slot={slot}, name={name}, decoration={decoration})"
            return f"SetDecoratedBossHealthBarState(state={state}, character={character}, slot={slot}, name={name}, decoration={decoration})"

        if instruction_index == 81:
            sign_type, character, region, summon_flag, dismissal_flag = req_args
            sign_type = get_enum_name(SummonSignType, sign_type, True)
            return f"PlaceNPCSummonSign_WithoutEmber(sign_type={sign_type}, character={character}, region={region}, summon_flag={summon_flag}, dismissal_flag={dismissal_flag})"

    if instruction_class == 2004:

        if instruction_index == 8:
            character, special_effect_id = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"AddSpecialEffect({character}, {special_effect_id})"

        if instruction_index == 14:
            character, target_entity, animation, wait_for_completion = req_args
            character = 'PLAYER' if character == 10000 else character
            target_entity = 'PLAYER' if target_entity == 10000 else target_entity
            return (f"RotateToFaceEntity({character}, {target_entity}, animation={animation}, "
                    f"wait_for_completion={boolify(wait_for_completion)})")

        if instruction_index == 48:
            character, bit_count, state_id = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"ChangeCharacterCloth({character}, bit_count={bit_count}, state_id={state_id})"

        if instruction_index == 49:
            character, patrol_information_id = req_args
            return f"ChangePatrolBehavior({character}, patrol_information_id={patrol_information_id})"

        if instruction_index == 50:
            character, lock_on_model_point, state = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"SetLockOnPoint({character}, lock_on_model_point={lock_on_model_point}, state={boolify(state)})"

        if instruction_index == 51:
            recipient_character, recipient_target_rigid_index, recipient_model_point, attachment_character, attachment_target_rigid_index, attachment_model_point = req_args
            return f"Test_RequestRagdollRestraint(recipient_character={recipient_character}, recipient_target_rigid_index={recipient_target_rigid_index}, recipient_model_point={recipient_model_point}, attachment_character={attachment_character}, attachment_target_rigid_index={attachment_target_rigid_index}, attachment_model_point={attachment_model_point})"

        if instruction_index == 52:
            character_init_param, = req_args
            return f"ChangePlayerCharacterInitParam(character_init_param={character_init_param})"

        if instruction_index == 53:
            character, = req_args
            return f"AdaptSpecialEffectHealthChangeToNPCPart({character})"

        if instruction_index == 54:
            character, state = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"ImmediateActivate({character}, state={boolify(state)})"

        if instruction_index == 55:
            character, distance = req_args
            return f"SetCharacterTalkRange({character}, distance={distance})"

        if instruction_index == 57:
            character, = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"IncrementCharacterNewGameCycle({character})"

        if instruction_index == 58:
            character, state = req_args
            return f"SetMultiplayerBuffs_NonBoss({character}, state={boolify(state)})"

        if instruction_index == 59:
            character, state = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"Unknown_2004_59({character}, state={boolify(state)})"
        
        if instruction_index == 60:
            level_count, = req_args
            return f"SetPlayerRemainingYoelLevels(level_count={level_count})"

    if instruction_class == 2005:

        if instruction_index == 16:
            return f"ExtinguishBurningObjects()"

        if instruction_index == 17:
            obj, ceremony_id, unknown = req_args
            return f"ShowObjectByMapCeremony(obj={obj}, ceremony_id={ceremony_id}, unknown={unknown})"

        if instruction_index == 19:
            obj, = req_args
            return f"DestroyObject_NoSlot(obj={obj})"

    if instruction_class == 2007:

        if instruction_index == 10:
            message, button_type, number_buttons, anchor_entity, display_distance, left_flag, right_flag, cancel_flag = req_args
            button_type = get_enum_name(ButtonType, button_type, True)
            number_buttons = get_enum_name(NumberButtons, number_buttons, True)
            return f"DisplayDialogAndSetFlags(message={message}, button_type={button_type}, number_buttons={number_buttons}, anchor_entity={anchor_entity}, display_distance={display_distance}, left_flag={left_flag}, right_flag={right_flag}, cancel_flag={cancel_flag})"

        if instruction_index == 11:
            message, = req_args
            return f"DisplayAreaWelcomeMessage(message={message})"

        if instruction_index == 12:
            message, unknown, pad_enabled = req_args
            return f"DisplayHollowArenaMessage(message={message}, unknown={unknown}, pad_enabled={boolify(pad_enabled)})"

    if instruction_class == 2009:

        if instruction_index == 5:
            flag, obj, reaction_distance, reaction_angle, initial_sword_number, sword_level = req_args
            return f"RegisterHealingFountain(flag={flag}, obj={obj}, reaction_distance={reaction_distance}, reaction_angle={reaction_angle}, initial_sword_number={initial_sword_number}, sword_level={sword_level})"

        if instruction_index == 8:
            unknown, = req_args
            return f"BanishInvaders(unknown={unknown})"

        if instruction_index == 10:
            unknown, = req_args
            return f"BanishPhantomsAndUpdateServerPvPStats(unknown={unknown})"

        if instruction_index == 11:
            unknown, = req_args
            return f"BanishPhantoms(unknown={unknown})"

    if instruction_class == 2010:

        if instruction_index == 4:
            sound_id, state = req_args
            if state == 1:
                return f"EnableBossMusic({sound_id})"
            elif state == 0:
                return f"DisableBossMusic({sound_id})"
            return f"SetBossMusicState(sound_id={sound_id}, state={boolify(state)})"

        if instruction_index == 5:
            entity_id, state = req_args
            state = get_enum_name(DoorState, state, True)
            return f"NotifyDoorEventSoundDampening(entity_id={entity_id}, state={boolify(state)})"

        if instruction_index == 6:
            sound_id, state, fade_duration = req_args
            if state == 1:
                return f"EnableSoundEventWithFade(sound_id={sound_id}, fade_duration={fade_duration})"
            elif state == 0:
                return f"DisableSoundEventWithFade(sound_id={sound_id}, fade_duration={fade_duration})"
            return f"SetMapSoundWithFade(sound_id={sound_id}, state={state}, fade_duration={fade_duration})"

        if instruction_index == 7:
            entity, = req_args
            return f"Unknown_2010_07(entity={entity})"

    if instruction_class == 2011:

        if instruction_index == 3:
            collision, state = req_args
            return f"SetCollisionResStatecollisionsn={collision}, state={boolify(state)})"

        if instruction_index == 4:
            collision, state = req_args
            return f"ActivateCollisionAndCreateNavmesh(collision={collision}, state={boolify(state)})"

    if instruction_class == 2012:

        if instruction_index == 8:
            state, = req_args
            if state == 1:
                return "EnableAreaWelcomeMessage()"
            elif state == 0:
                return "DisableAreaWelcomeMessage()"
            return f"SetAreaWelcomeMessageState(state={boolify(state)})"

    if instruction_class == 2013:

        if instruction_index == 1:
            name, = req_args
            return f"CreatePlayLog(name={name})"

        if instruction_index == 2:
            measurement_id, name, overwrite = req_args
            return f"StartPlayLogMeasurement(measurement_id={measurement_id}, name={name}, overwrite={overwrite})"

        if instruction_index == 3:
            measurement_id, = req_args
            return f"StopPlayLogMeasurement(measurement_id={measurement_id})"

        if instruction_index == 4:
            category, name, output_multiplayer_state = req_args
            category = get_enum_name(PlayerPlayLogParameter, category, True)
            output_multiplayer_state = get_enum_name(PlayLogMultiplayerType, output_multiplayer_state, True)
            return f"PlayLogParameterOutput(category={category}, name={name}, output_multiplayer_state={output_multiplayer_state})"

    raise InstructionNotFoundError(f"Instruction not decompiled: {instruction_class}[{instruction_index:02d}].")
