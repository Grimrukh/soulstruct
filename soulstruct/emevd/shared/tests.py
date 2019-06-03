from soulstruct.emevd.game_types import *  # IDE may wrongly mark this import as unused.
from soulstruct.emevd.shared.instructions import *


_THIS_FLAG = ConstantCondition(
    if_true_func=IfThisEventOn,
    if_false_func=IfThisEventOff,
    skip_if_true_func=SkipLinesIfThisEventOn,
    skip_if_false_func=SkipLinesIfThisEventOff,
    end_if_true_func=EndIfThisEventOn,
    end_if_false_func=EndIfThisEventOff,
    restart_if_true_func=RestartIfThisEventOn,
    restart_if_false_func=RestartIfThisEventOff,
)

_THIS_SLOT_FLAG = ConstantCondition(
    if_true_func=IfThisEventSlotOn,
    if_false_func=IfThisEventSlotOff,
    skip_if_true_func=SkipLinesIfThisEventSlotOn,
    skip_if_false_func=SkipLinesIfThisEventSlotOff,
    end_if_true_func=EndIfThisEventSlotOn,
    end_if_false_func=EndIfThisEventSlotOff,
    restart_if_true_func=RestartIfThisEventSlotOn,
    restart_if_false_func=RestartIfThisEventSlotOff,
)


_ONLINE = ConstantCondition(if_true_func=IfOnline, if_false_func=IfOffline)

_OFFLINE = ConstantCondition(if_true_func=IfOffline, if_false_func=IfOnline)

_DLC_OWNED = ConstantCondition(if_true_func=IfDLCOwned, if_false_func=IfDLCNotOwned)

_SKULL_LANTERN_ACTIVE = ConstantCondition(if_true_func=IfSkullLanternActive, if_false_func=IfSkullLanternNotActive)

_COMPARISON_VARIABLES = ['WHITE_WORLD_TENDENCY', 'BLACK_WORLD_TENDENCY', 'NEW_GAME_CYCLE', 'SOUL_LEVEL']


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


@__negate_only
def _WHITE_WORLD_TENDENCY(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return IfWhiteWorldTendencyComparison(condition, comparison_type, comparison_value)


@__negate_only
def _BLACK_WORLD_TENDENCY(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return IfBlackWorldTendencyComparison(condition, comparison_type, comparison_value)


@__negate_only
def _NEW_GAME_CYCLE(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return IfNewGameCycleComparison(condition, comparison_type, comparison_value)


@__negate_only
def _SOUL_LEVEL(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return IfPlayerSoulLevelComparison(condition, comparison_type, comparison_value)


@__skip_and_negate_and_terminate
def _FlagEnabled(flag: Flag, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False):
    if condition is not None:
        if negate:
            return IfFlagOff(condition, flag)
        return IfFlagOn(condition, flag)
    if skip_lines > 0:
        if negate:
            return SkipLinesIfFlagOn(skip_lines, flag)
        return SkipLinesIfFlagOff(skip_lines, flag)
    if end_event:
        if negate:
            return EndIfFlagOff(flag)
        return EndIfFlagOn(flag)
    if restart_event:
        if negate:
            return RestartIfFlagOff(flag)
        return RestartIfFlagOn(flag)


@__skip_and_negate_and_terminate
def _FlagDisabled(flag: Flag, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False):
    return _FlagEnabled(flag=flag, condition=condition, negate=not negate, skip_lines=skip_lines,
                        end_event=end_event, restart_event=restart_event)


@__no_skip_or_negate_or_terminate
def _SecondsElapsed(elapsed_seconds, condition):
    return IfTimeElapsed(condition, elapsed_seconds)


@__no_skip_or_negate_or_terminate
def _FramesElapsed(elapsed_frames, condition):
    return IfFramesElapsed(condition, elapsed_frames)


@__negate_only
def _EntityInsideRegion(entity: MapEntity, region: Region, condition, negate=False):
    return IfEntityRegionState(condition, entity, region, not negate)


@__negate_only
def _EntityOutsideRegion(entity: MapEntity, region: Region, condition, negate=False):
    return IfEntityRegionState(condition, entity, region, negate)


@__negate_only
def _PlayerInsideRegion(region: Region, condition, negate=False):
    return IfEntityRegionState(condition, PLAYER, region, not negate)


@__negate_only
def _PlayerOutsideRegion(region: Region, condition, negate=False):
    return IfEntityRegionState(condition, PLAYER, region, negate)


@__negate_only
def _AllPlayersInsideRegion(region: Region, condition, negate=False):
    return IfAllPlayersRegionState(condition, region, not negate)


@__negate_only
def _AllPlayersOutsideRegion(region: Region, condition, negate=False):
    return IfAllPlayersRegionState(condition, region, negate)


@__skip_and_negate_and_terminate
def _InsideMap(game_map: GameMap, condition=None, negate=False,
               skip_lines=0, end_event=False, restart_event=False):
    if skip_lines > 0:
        return SkipLinesIfMapPresenceState(skip_lines, negate, game_map)
    if end_event:
        return TerminateIfMapPresenceState(EventEndType.End, not negate, game_map)
    if restart_event:
        return SkipLinesIfMapPresenceState(EventEndType.Restart, not negate, game_map)
    return IfMapPresenceState(condition, not negate, game_map)


@__skip_and_negate_and_terminate
def _OutsideMap(game_map: GameMap, sub_index=None, condition=None, negate=False, skip_lines=0,
                end_event=False, restart_event=False):
    return _InsideMap(game_map, sub_index, condition=condition, negate=not negate, skip_lines=skip_lines,
                      end_event=end_event, restart_event=restart_event)


@__negate_only
def _EntityWithinDistance(first_entity: MapEntity, second_entity: MapEntity, max_distance, condition, negate=False):
    return IfEntityDistanceState(condition, first_entity, second_entity, max_distance, not negate)


@__negate_only
def _EntityBeyondDistance(first_entity: MapEntity, second_entity: MapEntity, min_distance, condition, negate=False):
    return IfEntityDistanceState(condition, first_entity, second_entity, min_distance, negate)


@__negate_only
def _PlayerWithinDistance(entity: MapEntity, max_distance, condition, negate=False):
    return IfEntityDistanceState(condition, PLAYER, entity, max_distance, not negate)


@__negate_only
def _PlayerBeyondDistance(entity: MapEntity, min_distance, condition, negate=False):
    return IfEntityDistanceState(condition, PLAYER, entity, min_distance, negate)


@__negate_only
def _HasItem(item: Item, condition, negate=False):
    try:
        item_type = item.item_type
    except AttributeError:
        raise ValueError("Can only use auto-detecting HasItem() on declared item types (Weapon, Armor, Ring, Good).")
    return IfPlayerItemStateNoBox(condition, item_type, item, not negate)


@__negate_only
def _HasWeapon(weapon: Weapon, condition, negate=False):
    return IfPlayerItemStateNoBox(condition, ItemType.Weapon, weapon, not negate)


@__negate_only
def _HasArmor(armor: Armor, condition, negate=False):
    return IfPlayerItemStateNoBox(condition, ItemType.Armor, armor, not negate)


@__negate_only
def _HasRing(ring: Ring, condition, negate=False):
    return IfPlayerItemStateNoBox(condition, ItemType.Ring, ring, not negate)


@__negate_only
def _HasGood(good: Good, condition, negate=False):
    return IfPlayerItemStateNoBox(condition, ItemType.Good, good, not negate)


@__no_skip_or_negate_or_terminate
def _DialogPromptActivated(prompt_text, anchor_entity: MapEntity, facing_angle=None, max_distance=None,
                           model_point=-1, human_or_hollow_only=True, button=0, boss_version=False,
                           line_intersects=None, anchor_type=None, condition=None):
    return IfDialogPromptActivated(condition, prompt_text, anchor_entity, facing_angle, max_distance,
                                   model_point, human_or_hollow_only, button, boss_version, line_intersects,
                                   anchor_type)


@__no_skip_or_negate_or_terminate
def _MultiplayerEvent(multiplayer_event, condition):
    return IfMultiplayerEvent(condition, multiplayer_event)


@__negate_only
def _TrueFlagCount(op_node, comparison_value, flag_range: FlagRangeOrSequence, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return IfTrueFlagCountComparison(condition, comparison_value, FlagType.Absolute, comparison_type, flag_range)


@__negate_only
def _EventValue(op_node, comparison_value, start_flag, bit_count, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return IfEventValueComparison(condition, start_flag, bit_count, comparison_type, comparison_value)


# TODO: This involves comparing two flags, which I haven't implemented.
@__negate_only
def _EventFlagValue(op_node, left_start_flag, left_bit_count, right_start_flag, right_bit_count,
                    condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return IfEventsComparison(condition, left_start_flag, left_bit_count, comparison_type,
                              right_start_flag, right_bit_count)


@__no_skip_or_negate_or_terminate
def _AnyItemDroppedInRegion(region: Region, condition):
    return IfAnyItemDroppedInRegion(condition, region)


@__no_skip_or_negate_or_terminate
def _ItemDropped(item: Item, condition):
    try:
        item_type = item.item_type
    except AttributeError:
        raise ValueError("Can only use HasItem() on declared item types (Weapon, Armor, Ring, Good).")
    return IfItemDropped(condition, item, item_type)


@__negate_only
def _OwnsItem(item: Item, condition, negate=False):
    try:
        item_type = item.type
    except AttributeError:
        raise ValueError("Can only use OwnsItem() on declared item types (Weapon, Armor, Ring, Good).")
    return IfPlayerItemStateBox(condition, item_type, item, not negate)


@__negate_only
def _OwnsWeapon(weapon: Weapon, condition, negate=False):
    return IfPlayerItemStateBox(condition, ItemType.Weapon, weapon, not negate)


@__negate_only
def _OwnsArmor(armor: Armor, condition, negate=False):
    return IfPlayerItemStateBox(condition, ItemType.Armor, armor, not negate)


@__negate_only
def _OwnsRing(ring: Ring, condition, negate=False):
    return IfPlayerItemStateBox(condition, ItemType.Ring, ring, not negate)


@__negate_only
def _OwnsGood(good: Good, condition, negate=False):
    return IfPlayerItemStateBox(condition, ItemType.Good, good, not negate)


@__negate_only
def _IsAlive(character: Character, condition, negate=False):
    return IfCharacterDeathState(condition, character, negate)


@__negate_only
def _IsDead(character: Character, condition, negate=False):
    return IfCharacterDeathState(condition, character, not negate)


@__no_skip_or_negate_or_terminate
def _IsAttacked(attacked_entity, attacking_character, condition):
    return IfAttacked(condition, attacked_entity, attacking_character)


@__negate_only
def _HealthRatio(op_node, comparison_value, character: Character, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return IfHealthComparison(condition, character, comparison_type, comparison_value)


@__negate_only
def _PartHealthValue(op_node, comparison_value, character: Character, part_type, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return IfCharacterPartHealthComparison(condition, character, part_type, comparison_value, comparison_type)


@__no_skip_or_negate_or_terminate
def _IsCharacterType(character: Character, character_type: CharacterType, condition):
    return IfCharacterType(condition, character, character_type)


@__no_skip_or_negate_or_terminate
def _IsHollow(character: Character, condition):
    return IfCharacterHollow(condition, character)


@__no_skip_or_negate_or_terminate
def _IsHuman(character: Character, condition):
    return IfCharacterHuman(condition, character)


@__no_skip_or_negate_or_terminate
def _IsInvader(character: Character, condition):
    return IfCharacterType(condition, character, CharacterType.Intruder)


@__no_skip_or_negate_or_terminate
def _IsBlackPhantom(character: Character, condition):
    return IfCharacterType(condition, character, CharacterType.BlackPhantom)


@__no_skip_or_negate_or_terminate
def _IsWhitePhantom(character: Character, condition):
    return IfCharacterType(condition, character, CharacterType.WhitePhantom)


@__negate_only
def _IsTargeting(targeting_chr, targeted_chr, condition, negate=False):
    return IfCharacterTargetingState(condition, targeting_chr, targeted_chr, not negate)


@__negate_only
def _HasSpecialEffect(character: Character, special_effect, condition, negate=False):
    return IfCharacterSpecialEffectState(condition, character, special_effect, not negate)


@__negate_only
def _BackreadEnabled(character: Character, condition, negate=False):
    return IfBackreadState(condition, character, not negate)


@__negate_only
def _BackreadDisabled(character: Character, condition, negate=False):
    return IfBackreadState(condition, character, negate)


@__negate_only
def _HasTaeEvent(character: Character, tae_event_id, condition, negate=False):
    return IfTAEEventState(condition, character, tae_event_id, not negate)


@__no_skip_or_negate_or_terminate
def _HasAiStatus(character: Character, ai_state, condition):
    return IfHasAIStatus(condition, character, ai_state)


@__no_skip_or_negate_or_terminate
def _AiStatusIsNormal(character: Character, condition):
    return IfHasAIStatus(condition, character, AIStatusType.Normal)


@__no_skip_or_negate_or_terminate
def _AiStatusIsRecognition(character: Character, condition):
    return IfHasAIStatus(condition, character, AIStatusType.Recognition)


@__no_skip_or_negate_or_terminate
def _AiStatusIsAlert(character: Character, condition):
    return IfHasAIStatus(condition, character, AIStatusType.Alert)


@__no_skip_or_negate_or_terminate
def _AiStatusIsBattle(character: Character, condition):
    return IfHasAIStatus(condition, character, AIStatusType.Battle)


@__no_skip_or_negate_or_terminate
def _PlayerIsClass(class_type: ClassType, condition):
    return IfPlayerClass(condition, class_type)


@__no_skip_or_negate_or_terminate
def _PlayerInCovenant(covenant_type: Covenant, condition):
    return IfPlayerCovenant(condition, covenant_type)


@__negate_only
def _HealthValue(op_node, comparison_value, character: Character, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return IfHealthValueComparison(condition, character, comparison_type, comparison_value)


@__no_skip_or_negate_or_terminate
def _IsDamaged(attacked_obj: Object, attacking_character, condition):
    return IfObjectDamagedBy(condition, attacked_obj, attacking_character)


@__skip_and_negate_and_terminate
def _IsDestroyed(obj: Object, condition, negate=False, skip_lines=0, end_event=False, restart_event=False):
    if skip_lines > 0:
        return SkipLinesIfObjectDestructionState(skip_lines, obj, negate)
    if end_event:
        return TerminateIfObjectDestructionState(EventEndType.End, obj, not negate)
    if restart_event:
        return TerminateIfObjectDestructionState(EventEndType.Restart, obj, not negate)
    return IfObjectDestructionState(condition, obj, not negate)


@__no_skip_or_negate_or_terminate
def _IsActivated(obj: Object, condition):
    return IfObjectActivated(condition, obj)


@__no_skip_or_negate_or_terminate
def _PlayerStandingOnHitbox(hitbox: Hitbox, condition):
    return IfStandingOnHitbox(condition, hitbox)


@__no_skip_or_negate_or_terminate
def _PlayerMovingOnHitbox(hitbox: Hitbox, condition):
    return IfMovingOnHitbox(condition, hitbox)


@__no_skip_or_negate_or_terminate
def _PlayerRunningOnHitbox(hitbox: Hitbox, condition):
    return IfRunningOnHitbox(condition, hitbox)
