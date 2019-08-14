from soulstruct.emevd.core import get_game_map_name, InstructionNotFoundError


def decompile_instruction(instruction_class, instruction_index, req_args, game_module):
    """ DS1 or DSR-specific instruction decompiler. Run after the shared decompiler. Raises an error if it fails to
    resolve. """

    if instruction_class == 2003:

        if instruction_index == 41:
            area_id, block_id, y, target_model_id = req_args
            game_map = get_game_map_name(area_id, block_id, game_module)
            return f"ActivateKillplaneForModel(game_map={game_map}, y_threshold={y}, target_model_id={target_model_id})"

    if instruction_class == 2004:

        if instruction_index == 8:
            character, special_effect_id = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"AddSpecialEffect({character}, {special_effect_id})"

        if instruction_index == 14:
            character, target_entity_id = req_args
            character = 'PLAYER' if character == 10000 else character
            return f"RotateToFaceEntity({character}, {target_entity_id})"

    raise InstructionNotFoundError(f"Could not decompile instruction {instruction_class:04d}[{instruction_index:02d}].")
