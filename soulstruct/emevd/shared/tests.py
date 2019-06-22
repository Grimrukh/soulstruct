from soulstruct.emevd.game_types import *  # IDE may wrongly mark this import as unused.
import soulstruct.emevd.shared.instructions as instr


THIS_FLAG = ConstantCondition(
    if_true_func=instr.IfThisEventOn,
    if_false_func=instr.IfThisEventOff,
    skip_if_true_func=instr.SkipLinesIfThisEventOn,
    skip_if_false_func=instr.SkipLinesIfThisEventOff,
    end_if_true_func=instr.EndIfThisEventOn,
    end_if_false_func=instr.EndIfThisEventOff,
    restart_if_true_func=instr.RestartIfThisEventOn,
    restart_if_false_func=instr.RestartIfThisEventOff,
)

THIS_SLOT_FLAG = ConstantCondition(
    if_true_func=instr.IfThisEventSlotOn,
    if_false_func=instr.IfThisEventSlotOff,
    skip_if_true_func=instr.SkipLinesIfThisEventSlotOn,
    skip_if_false_func=instr.SkipLinesIfThisEventSlotOff,
    end_if_true_func=instr.EndIfThisEventSlotOn,
    end_if_false_func=instr.EndIfThisEventSlotOff,
    restart_if_true_func=instr.RestartIfThisEventSlotOn,
    restart_if_false_func=instr.RestartIfThisEventSlotOff,
)


ONLINE = ConstantCondition(if_true_func=instr.IfOnline, if_false_func=instr.IfOffline)

OFFLINE = ConstantCondition(if_true_func=instr.IfOffline, if_false_func=instr.IfOnline)

DLC_OWNED = ConstantCondition(if_true_func=instr.IfDLCOwned, if_false_func=instr.IfDLCNotOwned)

SKULL_LANTERN_ACTIVE = ConstantCondition(if_true_func=instr.IfSkullLanternActive,
                                         if_false_func=instr.IfSkullLanternInactive)

COMPARISON_VARIABLES = ['WHITE_WORLD_TENDENCY', 'BLACK_WORLD_TENDENCY', 'NEW_GAME_CYCLE', 'SOUL_LEVEL']


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
def WHITE_WORLD_TENDENCY(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfWhiteWorldTendencyComparison(condition, comparison_type, comparison_value)


@__negate_only
def BLACK_WORLD_TENDENCY(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfBlackWorldTendencyComparison(condition, comparison_type, comparison_value)


@__negate_only
def NEW_GAME_CYCLE(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfNewGameCycleComparison(condition, comparison_type, comparison_value)


@__negate_only
def SOUL_LEVEL(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfPlayerSoulLevelComparison(condition, comparison_type, comparison_value)


@__skip_and_negate_and_terminate
def FlagEnabled(flag: Flag, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False):
    if condition is not None:
        if negate:
            return instr.IfFlagOff(condition, flag)
        return instr.IfFlagOn(condition, flag)
    if skip_lines > 0:
        if negate:
            return instr.SkipLinesIfFlagOn(skip_lines, flag)
        return instr.SkipLinesIfFlagOff(skip_lines, flag)
    if end_event:
        if negate:
            return instr.EndIfFlagOff(flag)
        return instr.EndIfFlagOn(flag)
    if restart_event:
        if negate:
            return instr.RestartIfFlagOff(flag)
        return instr.RestartIfFlagOn(flag)


@__skip_and_negate_and_terminate
def FlagDisabled(flag: Flag, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False):
    return FlagEnabled(flag=flag, condition=condition, negate=not negate, skip_lines=skip_lines,
                       end_event=end_event, restart_event=restart_event)


@__no_skip_or_negate_or_terminate
def SecondsElapsed(elapsed_seconds, condition):
    return instr.IfTimeElapsed(condition, elapsed_seconds)


@__no_skip_or_negate_or_terminate
def FramesElapsed(elapsed_frames, condition):
    return instr.IfFramesElapsed(condition, elapsed_frames)


@__negate_only
def CharacterInsideRegion(entity: MapEntity, region: Region, condition, negate=False):
    return instr.IfCharacterRegionState(condition, entity, region, not negate)

@__negate_only
def CharacterOutsideRegion(entity: MapEntity, region: Region, condition, negate=False):
    return instr.IfCharacterRegionState(condition, entity, region, negate)

@__negate_only
def PlayerInsideRegion(region: Region, condition, negate=False):
    return instr.IfCharacterRegionState(condition, PLAYER, region, not negate)

@__negate_only
def PlayerOutsideRegion(region: Region, condition, negate=False):
    return instr.IfCharacterRegionState(condition, PLAYER, region, negate)


@__negate_only
def AllPlayersInsideRegion(region: Region, condition, negate=False):
    return instr.IfAllPlayersRegionState(condition, region, not negate)

@__negate_only
def AllPlayersOutsideRegion(region: Region, condition, negate=False):
    return instr.IfAllPlayersRegionState(condition, region, negate)


@__skip_and_negate_and_terminate
def InsideMap(game_map: GameMap, condition=None, negate=False,
              skip_lines=0, end_event=False, restart_event=False):
    if skip_lines > 0:
        return instr.SkipLinesIfMapPresenceState(skip_lines, negate, game_map)
    if end_event:
        return instr.TerminateIfMapPresenceState(EventEndType.End, not negate, game_map)
    if restart_event:
        return instr.SkipLinesIfMapPresenceState(EventEndType.Restart, not negate, game_map)
    return instr.IfMapPresenceState(condition, not negate, game_map)


@__skip_and_negate_and_terminate
def OutsideMap(game_map: GameMap, sub_index=None, condition=None, negate=False, skip_lines=0,
               end_event=False, restart_event=False):
    return InsideMap(game_map, sub_index, condition=condition, negate=not negate, skip_lines=skip_lines,
                     end_event=end_event, restart_event=restart_event)


@__negate_only
def EntityWithinDistance(first_entity: MapEntity, second_entity: MapEntity, max_distance, condition, negate=False):
    return instr.IfEntityDistanceState(condition, first_entity, second_entity, max_distance, not negate)


@__negate_only
def EntityBeyondDistance(first_entity: MapEntity, second_entity: MapEntity, min_distance, condition, negate=False):
    return instr.IfEntityDistanceState(condition, first_entity, second_entity, min_distance, negate)


@__negate_only
def PlayerWithinDistance(entity: MapEntity, max_distance, condition, negate=False):
    return instr.IfEntityDistanceState(condition, PLAYER, entity, max_distance, not negate)


@__negate_only
def PlayerBeyondDistance(entity: MapEntity, min_distance, condition, negate=False):
    return instr.IfEntityDistanceState(condition, PLAYER, entity, min_distance, negate)


@__negate_only
def HasItem(item: Item, condition, negate=False):
    try:
        item_type = item.item_type
    except AttributeError:
        raise ValueError("Can only use auto-detecting HasItem() on declared item types (Weapon, Armor, Ring, Good).")
    return instr.IfPlayerItemStateNoBox(condition, item_type, item, not negate)


@__negate_only
def HasWeapon(weapon: Weapon, condition, negate=False):
    return instr.IfPlayerItemStateNoBox(condition, ItemType.Weapon, weapon, not negate)


@__negate_only
def HasArmor(armor: Armor, condition, negate=False):
    return instr.IfPlayerItemStateNoBox(condition, ItemType.Armor, armor, not negate)


@__negate_only
def HasRing(ring: Ring, condition, negate=False):
    return instr.IfPlayerItemStateNoBox(condition, ItemType.Ring, ring, not negate)


@__negate_only
def HasGood(good: Good, condition, negate=False):
    return instr.IfPlayerItemStateNoBox(condition, ItemType.Good, good, not negate)


@__no_skip_or_negate_or_terminate
def DialogPromptActivated(prompt_text, anchor_entity: MapEntity, facing_angle=None, max_distance=None,
                          model_point=-1, human_or_hollow_only=True, button=0, boss_version=False,
                          line_intersects=None, anchor_type=None, condition=None):
    return instr.IfDialogPromptActivated(condition, prompt_text, anchor_entity, facing_angle, max_distance,
                                         model_point, human_or_hollow_only, button, boss_version, line_intersects,
                                         anchor_type)


@__no_skip_or_negate_or_terminate
def MultiplayerEvent(multiplayer_event, condition):
    return instr.IfMultiplayerEvent(condition, multiplayer_event)


@__negate_only
def TrueFlagCount(op_node, comparison_value, flag_range: FlagRangeOrSequence, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfTrueFlagCountComparison(condition, comparison_value, FlagType.Absolute, comparison_type, flag_range)


@__negate_only
def EventValue(op_node, comparison_value, start_flag, bit_count, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfEventValueComparison(condition, start_flag, bit_count, comparison_type, comparison_value)


# TODO: This involves comparing two flags, which I haven't implemented in the EVS parser yet.
@__negate_only
def EventFlagValue(op_node, left_start_flag, left_bit_count, right_start_flag, right_bit_count,
                   condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfEventsComparison(condition, left_start_flag, left_bit_count, comparison_type,
                                    right_start_flag, right_bit_count)


@__no_skip_or_negate_or_terminate
def AnyItemDroppedInRegion(region: Region, condition):
    return instr.IfAnyItemDroppedInRegion(condition, region)


@__no_skip_or_negate_or_terminate
def ItemDropped(item: Item, condition):
    try:
        item_type = item.item_type
    except AttributeError:
        raise ValueError("Can only use HasItem() on declared item types (Weapon, Armor, Ring, Good).")
    return instr.IfItemDropped(condition, item, item_type)


@__negate_only
def OwnsItem(item: Item, condition, negate=False):
    try:
        item_type = item.type
    except AttributeError:
        raise ValueError("Can only use OwnsItem() on declared item types (Weapon, Armor, Ring, Good).")
    return instr.IfPlayerItemStateBox(condition, item_type, item, not negate)


@__negate_only
def OwnsWeapon(weapon: Weapon, condition, negate=False):
    return instr.IfPlayerItemStateBox(condition, ItemType.Weapon, weapon, not negate)


@__negate_only
def OwnsArmor(armor: Armor, condition, negate=False):
    return instr.IfPlayerItemStateBox(condition, ItemType.Armor, armor, not negate)


@__negate_only
def OwnsRing(ring: Ring, condition, negate=False):
    return instr.IfPlayerItemStateBox(condition, ItemType.Ring, ring, not negate)


@__negate_only
def OwnsGood(good: Good, condition, negate=False):
    return instr.IfPlayerItemStateBox(condition, ItemType.Good, good, not negate)


@__negate_only
def IsAlive(character: Character, condition, negate=False):
    return instr.IfCharacterDeathState(condition, character, negate)


@__negate_only
def IsDead(character: Character, condition, negate=False):
    return instr.IfCharacterDeathState(condition, character, not negate)


@__no_skip_or_negate_or_terminate
def IsAttacked(attacked_entity, attacking_character, condition):
    return instr.IfAttacked(condition, attacked_entity, attacking_character)


@__negate_only
def HealthRatio(op_node, comparison_value, character: Character, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfHealthComparison(condition, character, comparison_type, comparison_value)


@__negate_only
def PartHealthValue(op_node, comparison_value, character: Character, part_type, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfCharacterPartHealthComparison(condition, character, part_type, comparison_value, comparison_type)


@__no_skip_or_negate_or_terminate
def IsCharacterType(character: Character, character_type: CharacterType, condition):
    return instr.IfCharacterType(condition, character, character_type)


@__no_skip_or_negate_or_terminate
def IsHollow(character: Character, condition):
    return instr.IfCharacterHollow(condition, character)


@__no_skip_or_negate_or_terminate
def IsHuman(character: Character, condition):
    return instr.IfCharacterHuman(condition, character)


@__no_skip_or_negate_or_terminate
def IsInvader(character: Character, condition):
    return instr.IfCharacterType(condition, character, CharacterType.Intruder)


@__no_skip_or_negate_or_terminate
def IsBlackPhantom(character: Character, condition):
    return instr.IfCharacterType(condition, character, CharacterType.BlackPhantom)


@__no_skip_or_negate_or_terminate
def IsWhitePhantom(character: Character, condition):
    return instr.IfCharacterType(condition, character, CharacterType.WhitePhantom)


@__negate_only
def IsTargeting(targeting_chr, targeted_chr, condition, negate=False):
    return instr.IfCharacterTargetingState(condition, targeting_chr, targeted_chr, not negate)


@__negate_only
def HasSpecialEffect(character: Character, special_effect, condition, negate=False):
    return instr.IfCharacterSpecialEffectState(condition, character, special_effect, not negate)


@__negate_only
def BackreadEnabled(character: Character, condition, negate=False):
    return instr.IfCharacterBackreadState(condition, character, not negate)


@__negate_only
def BackreadDisabled(character: Character, condition, negate=False):
    return instr.IfCharacterBackreadState(condition, character, negate)


@__negate_only
def HasTaeEvent(character: Character, tae_event_id, condition, negate=False):
    return instr.IfTAEEventState(condition, character, tae_event_id, not negate)


@__no_skip_or_negate_or_terminate
def HasAiStatus(character: Character, ai_state, condition):
    return instr.IfHasAIStatus(condition, character, ai_state)


@__no_skip_or_negate_or_terminate
def AiStatusIsNormal(character: Character, condition):
    return instr.IfHasAIStatus(condition, character, AIStatusType.Normal)


@__no_skip_or_negate_or_terminate
def AiStatusIsRecognition(character: Character, condition):
    return instr.IfHasAIStatus(condition, character, AIStatusType.Recognition)


@__no_skip_or_negate_or_terminate
def AiStatusIsAlert(character: Character, condition):
    return instr.IfHasAIStatus(condition, character, AIStatusType.Alert)


@__no_skip_or_negate_or_terminate
def AiStatusIsBattle(character: Character, condition):
    return instr.IfHasAIStatus(condition, character, AIStatusType.Battle)


@__no_skip_or_negate_or_terminate
def PlayerIsClass(class_type: ClassType, condition):
    return instr.IfPlayerClass(condition, class_type)


@__no_skip_or_negate_or_terminate
def PlayerInCovenant(covenant_type: Covenant, condition):
    return instr.IfPlayerCovenant(condition, covenant_type)


@__negate_only
def HealthValue(op_node, comparison_value, character: Character, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfHealthValueComparison(condition, character, comparison_type, comparison_value)


@__no_skip_or_negate_or_terminate
def IsDamaged(attacked_obj: Object, attacking_character, condition):
    return instr.IfObjectDamagedBy(condition, attacked_obj, attacking_character)


@__skip_and_negate_and_terminate
def IsDestroyed(obj: Object, condition, negate=False, skip_lines=0, end_event=False, restart_event=False):
    if skip_lines > 0:
        return instr.SkipLinesIfObjectDestructionState(skip_lines, obj, negate)
    if end_event:
        return instr.TerminateIfObjectDestructionState(EventEndType.End, obj, not negate)
    if restart_event:
        return instr.TerminateIfObjectDestructionState(EventEndType.Restart, obj, not negate)
    return instr.IfObjectDestructionState(condition, obj, not negate)


@__no_skip_or_negate_or_terminate
def IsActivated(obj: Object, condition):
    return instr.IfObjectActivated(condition, obj)


@__no_skip_or_negate_or_terminate
def PlayerStandingOnHitbox(hitbox: Hitbox, condition):
    return instr.IfStandingOnHitbox(condition, hitbox)


@__no_skip_or_negate_or_terminate
def PlayerMovingOnHitbox(hitbox: Hitbox, condition):
    return instr.IfMovingOnHitbox(condition, hitbox)


@__no_skip_or_negate_or_terminate
def PlayerRunningOnHitbox(hitbox: Hitbox, condition):
    return instr.IfRunningOnHitbox(condition, hitbox)
