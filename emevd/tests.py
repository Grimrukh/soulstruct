from emevd.ds_types import *
from pydses import *


_THIS_FLAG = ConstantCondition(
    if_true_func=if_this_event_on,
    if_false_func=if_this_event_off,
    skip_if_true_func=skip_if_this_event_on,
    skip_if_false_func=skip_if_this_event_off,
    end_if_true_func=end_if_this_event_on,
    end_if_false_func=end_if_this_event_off,
    restart_if_true_func=restart_if_this_event_on,
    restart_if_false_func=restart_if_this_event_off,
)

_THIS_SLOT_FLAG = ConstantCondition(
    if_true_func=if_this_event_slot_on,
    if_false_func=if_this_event_slot_off,
    skip_if_true_func=skip_if_this_event_slot_on,
    skip_if_false_func=skip_if_this_event_slot_off,
    end_if_true_func=end_if_this_event_slot_on,
    end_if_false_func=end_if_this_event_slot_off,
    restart_if_true_func=restart_if_this_event_slot_on,
    restart_if_false_func=restart_if_this_event_slot_off,
)

_HOST = ConstantCondition(
    if_true_func=if_host,
    if_false_func=if_client,
    skip_if_true_func=skip_if_host,
    skip_if_false_func=skip_if_client,
    end_if_true_func=end_if_host,
    end_if_false_func=end_if_client,
    restart_if_true_func=restart_if_host,
    restart_if_false_func=restart_if_client,
)

_CLIENT = ConstantCondition(
    if_true_func=if_client,
    if_false_func=if_host,
    skip_if_true_func=skip_if_client,
    skip_if_false_func=skip_if_host,
    end_if_true_func=end_if_client,
    end_if_false_func=end_if_host,
    restart_if_true_func=restart_if_client,
    restart_if_false_func=restart_if_host,
)

_SINGLEPLAYER = ConstantCondition(
    if_true_func=if_singleplayer,
    if_false_func=if_multiplayer,
    skip_if_true_func=skip_if_singleplayer,
    skip_if_false_func=skip_if_multiplayer,
    end_if_true_func=end_if_singleplayer,
    end_if_false_func=end_if_multiplayer,
    restart_if_true_func=restart_if_singleplayer,
    restart_if_false_func=restart_if_multiplayer,
)

_MULTIPLAYER = ConstantCondition(
    if_true_func=if_multiplayer,
    if_false_func=if_singleplayer,
    skip_if_true_func=skip_if_multiplayer,
    skip_if_false_func=skip_if_singleplayer,
    end_if_true_func=end_if_multiplayer,
    end_if_false_func=end_if_singleplayer,
    restart_if_true_func=restart_if_multiplayer,
    restart_if_false_func=restart_if_singleplayer,
)

_ONLINE = ConstantCondition(if_true_func=if_online, if_false_func=if_offline)

_OFFLINE = ConstantCondition(if_true_func=if_offline, if_false_func=if_online)

_DLC_OWNED = ConstantCondition(if_true_func=if_owns_dlc, if_false_func=if_does_not_own_dlc)

_SKULL_LANTERN_ACTIVE = ConstantCondition(
    if_true_func=if_skull_lantern_activated, if_false_func=if_skull_lantern_not_activated)


def __no_skip_or_negate_or_terminate(func):
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines != 0:
            raise NoSkipOrTerminateError
        if negate:
            raise NoNegateError
        if end_event or restart_event:
            raise NoSkipOrTerminateError
        if condition is None:
            raise ValueError("Condition index must be specified (-7 to 7).")
        return func(*args, condition=condition, **kwargs)

    return decorated


def __negate_only(func):
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines != 0:
            raise NoSkipOrTerminateError
        if end_event or restart_event:
            raise NoSkipOrTerminateError
        if condition is None:
            raise ValueError("Condition index must be specified (-7 to 7).")
        return func(*args, condition=condition, negate=negate, **kwargs)

    return decorated


def __skip_and_negate_and_terminate(func):
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines > 0:
            if condition is not None or end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, skip_lines=skip_lines, negate=negate, **kwargs)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            if condition not in range(-7, 8):
                raise ValueError("Condition register index must be in range [-7, 7], inclusive.")
            return func(*args, condition=condition, negate=negate, **kwargs)

        if end_event:
            if restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, end_event=True, negate=negate, **kwargs)

        if restart_event:
            return func(*args, restart_event=True, negate=negate, **kwargs)

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")

    return decorated


def emevd_variables_comparison(name, op_node, comparison_value, condition, negate=False):
    """ Resolve a comparison with one of the four EMEVD 'variable' names below. """
    if name in ['WHITE_WORLD_TENDENCY', 'BLACK_WORLD_TENDENCY', 'NEW_GAME_CYCLE', 'SOUL_LEVEL']:
        return globals()['_' + name](op_node, comparison_value, condition, negate=negate)
    raise TypeError(f"INTERNAL ERROR: Name {name} is not an internal EMEVD variable name.")


@__negate_only
def _WHITE_WORLD_TENDENCY(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return if_world_tendency_comparison(condition, 0, comparison_type, comparison_value)


@__negate_only
def _BLACK_WORLD_TENDENCY(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return if_world_tendency_comparison(condition, 1, comparison_type, comparison_value)


@__negate_only
def _NEW_GAME_CYCLE(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return if_new_game_count_comparison(condition, comparison_type, comparison_value)


@__negate_only
def _SOUL_LEVEL(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return if_player_soul_level_comparison(condition, comparison_type, comparison_value)


@__skip_and_negate_and_terminate
def _FlagEnabled(flag: Flag, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False):
    if condition:
        if negate:
            return if_event_flag_off(condition, flag)
        return if_event_flag_on(condition, flag)
    if skip_lines > 0:
        if negate:
            return skip_if_event_flag_on(skip_lines, flag)
        return skip_if_event_flag_off(skip_lines, flag)
    if end_event:
        if negate:
            return end_if_event_flag_off(flag)
        return end_if_event_flag_on(flag)
    if restart_event:
        if negate:
            return restart_if_event_flag_off(flag)
        return restart_if_event_flag_on(flag)


@__skip_and_negate_and_terminate
def _FlagDisabled(flag: Flag, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False):
    return _FlagEnabled(flag=flag, condition=condition, negate=not negate, skip_lines=skip_lines,
                        end_event=end_event, restart_event=restart_event)


@__no_skip_or_negate_or_terminate
def _SecondsElapsed(elapsed_seconds, condition):
    return if_time_elapsed(condition, elapsed_seconds)


@__no_skip_or_negate_or_terminate
def _FramesElapsed(elapsed_frames, condition):
    return if_time_elapsed(condition, elapsed_frames)


@__negate_only
def _EntityInsideRegion(entity: MapEntity, region: Region, condition, negate=False):
    return if_entity_inside_or_outside_region(condition, entity, region, not negate)


@__negate_only
def _EntityOutsideRegion(entity: MapEntity, region: Region, condition, negate=False):
    return if_entity_inside_or_outside_region(condition, entity, region, negate)


@__negate_only
def _PlayerInsideRegion(region: Region, condition, negate=False):
    return if_entity_inside_or_outside_region(condition, PLAYER, region, not negate)


@__negate_only
def _PlayerOutsideRegion(region: Region, condition, negate=False):
    return if_entity_inside_or_outside_region(condition, PLAYER, region, negate)


@__negate_only
def _AllPlayersInsideRegion(region: Region, condition, negate=False):
    return if_all_players_inside_or_outside_region(condition, region, not negate)


@__negate_only
def _AllPlayersOutsideRegion(region: Region, condition, negate=False):
    return if_all_players_inside_or_outside_region(condition, region, negate)


@__skip_and_negate_and_terminate
def _InsideMap(game_map, sub_index=None, condition=None, negate=False,
               skip_lines=0, end_event=False, restart_event=False):
    if isinstance(game_map, Map):
        if sub_index is not None:
            raise ValueError("Do not specify the map sub-block if using a declared Map instance.")
        sub_index = game_map.sub_id
        game_map = game_map.block_id
    if skip_lines > 0:
        return skip_if_area_state(skip_lines, negate, game_map, sub_index)
    if end_event:
        return terminate_if_area_state(0, not negate, game_map, sub_index)
    if restart_event:
        return terminate_if_area_state(1, not negate, game_map, sub_index)
    return if_world_area_state(condition, game_map, sub_index, not negate)


@__skip_and_negate_and_terminate
def _OutsideMap(game_map, sub_index=None, condition=None, negate=False, skip_lines=0,
                end_event=False, restart_event=False):
    return _InsideMap(game_map, sub_index, condition=condition, negate=not negate, skip_lines=skip_lines,
                      end_event=end_event, restart_event=restart_event)


@__negate_only
def _EntityWithinDistance(first_entity: MapEntity, second_entity: MapEntity, max_distance, condition, negate=False):
    return if_entity_within_or_beyond_distance(condition, first_entity, second_entity, max_distance, not negate)


@__negate_only
def _EntityBeyondDistance(first_entity: MapEntity, second_entity: MapEntity, min_distance, condition, negate=False):
    return if_entity_within_or_beyond_distance(condition, first_entity, second_entity, min_distance, negate)


@__negate_only
def _PlayerWithinDistance(entity: MapEntity, max_distance, condition, negate=False):
    return if_entity_within_or_beyond_distance(condition, PLAYER, entity, max_distance, not negate)


@__negate_only
def _PlayerBeyondDistance(entity: MapEntity, min_distance, condition, negate=False):
    return if_entity_within_or_beyond_distance(condition, PLAYER, entity, min_distance, negate)


@__negate_only
def _HasItem(item: Item, condition, negate=False):
    try:
        item_type = item.item_type
    except AttributeError:
        raise ValueError("Can only use auto-detecting HasItem() on declared item types (Weapon, Armor, Ring, Good).")
    return if_player_has_or_does_not_have_item(condition, item_type, item, not negate)


@__negate_only
def _HasWeapon(weapon: Weapon, condition, negate=False):
    return if_player_has_or_does_not_have_item(condition, 0, weapon, not negate)


@__negate_only
def _HasArmor(armor: Armor, condition, negate=False):
    return if_player_has_or_does_not_have_item(condition, 1, armor, not negate)


@__negate_only
def _HasRing(ring: Ring, condition, negate=False):
    return if_player_has_or_does_not_have_item(condition, 2, ring, not negate)


@__negate_only
def _HasGood(good: Good, condition, negate=False):
    return if_player_has_or_does_not_have_item(condition, 3, good, not negate)


@__no_skip_or_negate_or_terminate
def _DialogPromptActivated(prompt_text, anchor_entity: MapEntity, facing_angle=None, max_distance=None,
                           model_point=-1, human_or_hollow_only=True, button=0, boss_version=False,
                           line_intersects=None, condition=None):
    try:
        category = anchor_entity.category
    except AttributeError:
        raise ValueError("Target entity must be an Object, Region, or Character instance.")

    if human_or_hollow_only:
        reaction_attribute = ReactionAttribute.human_or_hollow
    else:
        reaction_attribute = ReactionAttribute.all

    if facing_angle is None and category != category.Region:
        raise ValueError("Facing angle must be greater than zero for Object and Character targets.")
    else:
        facing_angle = 0.0

    if max_distance is None and category != Category.region:
        raise ValueError("Max distance must be greater than zero for Object and Character targets.")
    else:
        max_distance = 0.0

    args = [condition, category, anchor_entity, facing_angle, model_point, max_distance,
            prompt_text, reaction_attribute, button]

    if boss_version:
        if line_intersects is None:
            return if_action_button_state_in_boss(*args)
        else:
            return if_action_button_state_and_line_segment_in_boss(*args, line_intersects)
    else:
        if line_intersects is None:
            return if_action_button_state(*args)
        else:
            return if_action_button_state_and_line_segment(*args, line_intersects)


@__no_skip_or_negate_or_terminate
def _MultiplayerEvent(multiplayer_event, condition):
    return if_multiplayer_event(condition, multiplayer_event)


@__negate_only
def _TrueFlagCount(op_node, comparison_value, flag_range, condition, negate=False):
    if isinstance(flag_range, FlagRange):
        first = flag_range.first
        last = flag_range.last
    else:
        try:
            first, last = flag_range
        except ValueError:
            raise ValueError("Flag range must be a FlagRange or two-value sequence (first, last).")

    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]

    return if_count_true_event_flags_in_range(
        condition, FlagType.event_flag, start_event_flag_id=first, end_event_flag_id=last,
        comparison_type=comparison_type, count_comparison=comparison_value)


@__negate_only
def _EventValue(op_node, comparison_value, start_flag, bit_count, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return if_event_value_comparison(condition, start_flag, bit_count, comparison_type, comparison_value)


# TODO: This involves comparing two flags, which I haven't implemented.
@__negate_only
def _EventFlagValue(op_node, left_start_flag, left_bit_count, right_start_flag, right_bit_count,
                    condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return if_event_flag_value_comparison(condition, left_start_flag, left_bit_count, comparison_type, right_start_flag,
                                          right_bit_count)


@__no_skip_or_negate_or_terminate
def _AnyItemDroppedInRegion(region: Region, condition):
    return if_any_item_dropped_in_region(condition, region)


@__no_skip_or_negate_or_terminate
def _ItemDropped(item: Item, condition):
    try:
        item_type = item.item_type
    except AttributeError:
        raise ValueError("Can only use HasItem() on declared item types (Weapon, Armor, Ring, Good).")
    return if_item_dropped(condition, item_type, item)


@__negate_only
def _OwnsItem(item: Item, condition, negate=False):
    try:
        item_type = item.type
    except AttributeError:
        raise ValueError("Can only use OwnsItem() on declared item types (Weapon, Armor, Ring, Good).")
    return if_player_has_or_does_not_have_item(condition, item_type, item, not negate)


@__negate_only
def _OwnsWeapon(weapon: Weapon, condition, negate=False):
    return if_player_has_or_does_not_have_item(condition, 0, weapon, not negate)


@__negate_only
def _OwnsArmor(armor: Armor, condition, negate=False):
    return if_player_has_or_does_not_have_item(condition, 1, armor, not negate)


@__negate_only
def _OwnsRing(ring: Ring, condition, negate=False):
    return if_player_has_or_does_not_have_item(condition, 2, ring, not negate)


@__negate_only
def _OwnsGood(good: Good, condition, negate=False):
    return if_player_has_or_does_not_have_item(condition, 3, good, not negate)


@__negate_only
def _IsAlive(character: Character, condition, negate=False):
    return if_entity_death_state(condition, character, negate)


@__negate_only
def _IsDead(character: Character, condition, negate=False):
    return if_entity_death_state(condition, character, not negate)


@__no_skip_or_negate_or_terminate
def _IsAttacked(attacked_entity, attacking_character, condition):
    return if_entity_attacked_by(condition, attacked_entity, attacking_character)


@__negate_only
def _HealthRatio(op_node, comparison_value, character: Character, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return if_entity_health_comparison(condition, character, comparison_type, comparison_value)


@__negate_only
def _PartHealthValue(op_node, comparison_value, character: Character, part_type, condition, negate=False):
    # TODO: Not 100% sure this is health value rather than health ratio, as it is only used to compare to 0.
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return if_body_part_health_comparison(condition, character, part_type, comparison_value, comparison_type)


@__no_skip_or_negate_or_terminate
def _IsChrType(character: Character, character_type, condition):
    return if_character_type(condition, character, character_type)


@__no_skip_or_negate_or_terminate
def _IsHollow(character: Character, condition):
    return if_character_type(condition, character, CharacterType.hollow)


@__no_skip_or_negate_or_terminate
def _IsHuman(character: Character, condition):
    return if_character_type(condition, character, CharacterType.human)


@__no_skip_or_negate_or_terminate
def _IsInvader(character: Character, condition):
    return if_character_type(condition, character, CharacterType.intruder)


@__no_skip_or_negate_or_terminate
def _IsBlackPhantom(character: Character, condition):
    return if_character_type(condition, character, CharacterType.black_phantom)


@__no_skip_or_negate_or_terminate
def _IsWhitePhantom(character: Character, condition):
    return if_character_type(condition, character, CharacterType.white_phantom)


@__negate_only
def _IsTargeting(targeting_chr, targeted_chr, condition, negate=False):
    return if_entity_target_state(condition, targeting_chr, targeted_chr, not negate)


@__negate_only
def _HasSpecialEffect(character: Character, special_effect, condition, negate=False):
    return if_entity_special_effect_state(condition, character, special_effect, not negate)


@__negate_only
def _BackreadEnabled(character: Character, condition, negate=False):
    return if_entity_backread_state(condition, character, not negate)


@__negate_only
def _BackreadDisabled(character: Character, condition, negate=False):
    return if_entity_backread_state(condition, character, negate)


@__negate_only
def _HasTaeEvent(character: Character, tae_event_id, condition, negate=False):
    return if_tae_event_state(condition, character, tae_event_id, not negate)


@__no_skip_or_negate_or_terminate
def _HasAiStatus(character: Character, ai_state, condition):
    return if_ai_state(condition, character, ai_state)


@__no_skip_or_negate_or_terminate
def _AiStatusIsNormal(character: Character, condition):
    return if_ai_state(condition, character, AIStatusType.normal)


@__no_skip_or_negate_or_terminate
def _AiStatusIsRecognition(character: Character, condition):
    return if_ai_state(condition, character, AIStatusType.recognition)


@__no_skip_or_negate_or_terminate
def _AiStatusIsAlert(character: Character, condition):
    return if_ai_state(condition, character, AIStatusType.alert)


@__no_skip_or_negate_or_terminate
def _AiStatusIsBattle(character: Character, condition):
    return if_ai_state(condition, character, AIStatusType.battle)


@__no_skip_or_negate_or_terminate
def _PlayerIsClass(class_type: ClassType, condition):
    return if_player_class(condition, class_type)


@__no_skip_or_negate_or_terminate
def _PlayerInCovenant(covenant_type: Covenant, condition):
    return if_player_covenant(condition, covenant_type)


@__negate_only
def _HealthValue(op_node, comparison_value, character: Character, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return if_entity_health_value_comparison(condition, character, comparison_type, comparison_value)


@__no_skip_or_negate_or_terminate
def _IsDamaged(attacked_obj: Object, attacking_character, condition):
    return if_object_damaged_by(condition, attacked_obj, attacking_character)


@__skip_and_negate_and_terminate
def _IsDestroyed(obj: Object, condition, negate=False, skip_lines=0, end_event=False, restart_event=False):
    if skip_lines > 0:
        return skip_if_object_destruction_state(skip_lines, negate, obj)
    if end_event:
        return terminate_if_object_destruction_state(0, not negate, obj)
    if restart_event:
        return terminate_if_object_destruction_state(1, not negate, obj)
    return if_object_destruction_state(condition, not negate, obj)


@__no_skip_or_negate_or_terminate
def _IsActivated(obj: Object, condition):
    return if_object_activated(condition, obj)


@__no_skip_or_negate_or_terminate
def _PlayerStandingOnHitbox(hitbox: Hitbox, condition):
    return if_player_standing_on_hitbox(condition, hitbox)


@__no_skip_or_negate_or_terminate
def _PlayerMovingOnHitbox(hitbox: Hitbox, condition):
    return if_player_moving_on_hitbox(condition, hitbox)


@__no_skip_or_negate_or_terminate
def _PlayerRunningOnHitbox(hitbox: Hitbox, condition):
    return if_player_running_on_hitbox(condition, hitbox)
