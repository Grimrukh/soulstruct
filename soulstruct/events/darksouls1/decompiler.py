from soulstruct.events.internal import InstructionNotFoundError, get_game_map_variable_name, get_enum_name, boolify


def decompile_instruction(instruction_class, instruction_index, req_args, game_module):
    """ DS1 or DSR-specific instruction decompiler. Run after the shared decompiler. Raises an error if it fails to
    resolve. """

    if instruction_class == 3:

        if instruction_index == 23:
            condition, arg1, arg2 = req_args
            return f"Unknown_3_23(condition={condition}, arg1={arg1}, arg2={arg2})"

        if instruction_index == 24:
            condition, arg1, arg2 = req_args
            return f"IfMultiplayerCount(condition={condition}, arg1={arg1}, arg2={arg2})"

    if instruction_class == 4:

        if instruction_index == 15:
            condition, arg1 = req_args
            return f"Unknown_4_15(condition={condition}, arg1={arg1})"

        if instruction_index == 16:
            condition, arg1, arg2, arg3 = req_args
            return f"Unknown_4_16(condition={condition}, arg1={arg1}, arg2={arg2}, arg3={arg3})"

        if instruction_index == 17:
            (condition,) = req_args
            return f"IfArenaMatchmaking({condition})"

    if instruction_class == 2000:

        if instruction_index == 6:
            (arg1,) = req_args
            return f"Unknown_2000_06(arg1={arg1})"

    if instruction_class == 2002:

        if instruction_index == 6:
            condition, playback_method, first_region, last_region, area_id, block_id = req_args
            playback_method = get_enum_name(game_module.CutsceneType, playback_method, True)
            game_map = get_game_map_variable_name(area_id, block_id, game_module)
            return (
                f"PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect1(condition={condition}, playback_method="
                f"{playback_method}, first_region={first_region}, last_region={last_region}, game_map={game_map})"
            )

        if instruction_index == 7:
            condition, playback_method, first_region, last_region, area_id, block_id = req_args
            playback_method = get_enum_name(game_module.CutsceneType, playback_method, True)
            game_map = get_game_map_variable_name(area_id, block_id, game_module)
            return (
                f"PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect2(condition={condition}, playback_method="
                f"{playback_method}, first_region={first_region}, last_region={last_region}, game_map={game_map})"
            )

    if instruction_class == 2003:

        if instruction_index == 41:
            area_id, block_id, y, target_model_id = req_args
            game_map = get_game_map_variable_name(area_id, block_id, game_module)
            return f"ActivateKillplaneForModel(game_map={game_map}, y_threshold={y}, target_model_id={target_model_id})"

        if instruction_index == 42:
            source_flag, destination_flag, bit_count = req_args
            return (
                f"CopyEventValue(source_flag={source_flag}, destination_flag={destination_flag}, "
                f"bit_count={bit_count})"
            )

        if instruction_index == 43:
            flag, bit_count, arg1, arg2 = req_args
            return f"Unknown_2003_43(flag={flag}, bit_count={bit_count}, arg1={arg1}, arg2={arg2})"

        if instruction_index == 44:
            entity, animation, loop, wait_for_completion, skip_transition, arg1 = req_args
            return (
                f"ForceAnimation_WithUnknownEffect1(entity={entity}, animation={animation}, loop={boolify(loop)}, "
                f"wait_for_completion={boolify(wait_for_completion)}, skip_transition={boolify(skip_transition)}, "
                f"arg1={arg1})"
            )

        if instruction_index == 46:
            entity, animation, loop, wait_for_completion, skip_transition, arg1 = req_args
            return (
                f"ForceAnimation_WithUnknownEffect2(entity={entity}, animation={animation}, loop={boolify(loop)}, "
                f"wait_for_completion={boolify(wait_for_completion)}, skip_transition={boolify(skip_transition)}, "
                f"arg1={arg1})"
            )

        if instruction_index == 47:
            return f"Unknown_2003_47()"

        if instruction_index == 48:
            entity, arg1, model_point, magic_id, shoot_angle_x, shoot_angle_y, shoot_angle_z = req_args
            return (
                f"Unknown_2003_48(entity={entity}, arg1={arg1}, model_point={model_point}, magic_id={magic_id}, "
                f"shoot_angle_x={shoot_angle_x}, shoot_angle_y={shoot_angle_y}, shoot_angle_z={shoot_angle_z})"
            )

        if instruction_index == 49:
            (summoned_character,) = req_args
            return f"EraseNPCSummonSign(summoned_character={summoned_character})"

    if instruction_class == 2004:

        if instruction_index == 8:
            character, special_effect_id = req_args
            character = "PLAYER" if character == 10000 else character
            return f"AddSpecialEffect({character}, {special_effect_id})"

        if instruction_index == 14:
            character, target_entity_id = req_args
            character = "PLAYER" if character == 10000 else character
            target_entity_id = "PLAYER" if target_entity_id == 10000 else target_entity_id
            return f"RotateToFaceEntity({character}, {target_entity_id})"

        if instruction_index == 48:
            character, duration = req_args
            character = "PLAYER" if character == 10000 else character
            return f"FadeOutCharacter({character}, duration={duration})"

        if instruction_index == 49:
            character, duration = req_args
            character = "PLAYER" if character == 10000 else character
            return f"FadeInCharacter({character}, duration={duration})"

        if instruction_index == 50:
            return "Unknown_2004_50()"

        if instruction_index == 51:
            (arg1,) = req_args
            return f"Unknown_2004_51(arg1={arg1})"

        if instruction_index == 52:
            return "Unknown_2004_52()"

    if instruction_class == 2007:

        if instruction_index == 12:
            message_id, pad_enabled, concatenator_base_flag, bit_count = req_args
            return (
                f"DisplayConcatenatedMessage(message_id={message_id}, pad_enabled={boolify(pad_enabled)}, "
                f"concatenator_base_flag={concatenator_base_flag}, bit_count={bit_count})"
            )

        if instruction_index == 13:
            (arg1,) = req_args
            return f"Unknown_2007_13(arg1={arg1})"

    if instruction_class == 2008:

        if instruction_index == 4:
            return "Unknown_2008_4()"

    raise InstructionNotFoundError(f"Could not decompile instruction {instruction_class:04d}[{instruction_index:02d}].")
