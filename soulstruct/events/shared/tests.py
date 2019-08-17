"""EMEVD tests shared by all FromSoft games supported by Soulstruct.

DO NOT IMPORT THIS FILE. Import the specific game package (e.g. "from soulstruct.events.darksouls1 import *") to get the
full set of instructions, enums, game types, etc. for that game.
"""
from soulstruct.events.core import no_skip_or_negate_or_terminate, negate_only, skip_and_negate_and_terminate, \
    ConstantCondition, COMPARISON_NODES, NEG_COMPARISON_NODES
import soulstruct.events.shared.instructions as instr
from soulstruct.enums.shared import *
import soulstruct.game_types as gt

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

ONLINE = ConstantCondition(if_true_func=instr.IfOnline,
                           if_false_func=instr.IfOffline)

OFFLINE = ConstantCondition(if_true_func=instr.IfOffline,
                            if_false_func=instr.IfOnline)

DLC_OWNED = ConstantCondition(if_true_func=instr.IfDLCOwned,
                              if_false_func=instr.IfDLCNotOwned)

SKULL_LANTERN_ACTIVE = ConstantCondition(if_true_func=instr.IfSkullLanternActive,
                                         if_false_func=instr.IfSkullLanternInactive)

COMPARISON_VARIABLES = ['WHITE_WORLD_TENDENCY', 'BLACK_WORLD_TENDENCY', 'NEW_GAME_CYCLE', 'SOUL_LEVEL']


@negate_only
def WHITE_WORLD_TENDENCY(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfWhiteWorldTendencyComparison(condition, comparison_type, comparison_value)


@negate_only
def BLACK_WORLD_TENDENCY(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfBlackWorldTendencyComparison(condition, comparison_type, comparison_value)


@negate_only
def NEW_GAME_CYCLE(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfNewGameCycleComparison(condition, comparison_type, comparison_value)


@negate_only
def SOUL_LEVEL(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfPlayerSoulLevelComparison(condition, comparison_type, comparison_value)


@skip_and_negate_and_terminate
def FlagEnabled(flag: gt.Flag, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False):
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


@skip_and_negate_and_terminate
def FlagDisabled(flag: gt.Flag, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False):
    return FlagEnabled(flag=flag, condition=condition, negate=not negate, skip_lines=skip_lines,
                       end_event=end_event, restart_event=restart_event)


@no_skip_or_negate_or_terminate
def SecondsElapsed(elapsed_seconds, condition):
    return instr.IfTimeElapsed(condition, elapsed_seconds)


@no_skip_or_negate_or_terminate
def FramesElapsed(elapsed_frames, condition):
    return instr.IfFramesElapsed(condition, elapsed_frames)


@negate_only
def CharacterInsideRegion(entity: gt.CoordEntity, region: gt.Region, condition, negate=False):
    return instr.IfCharacterRegionState(condition, entity, region, not negate)


@negate_only
def CharacterOutsideRegion(entity: gt.CoordEntity, region: gt.Region, condition, negate=False):
    return instr.IfCharacterRegionState(condition, entity, region, negate)


@negate_only
def PlayerInsideRegion(region: gt.Region, condition, negate=False):
    return instr.IfCharacterRegionState(condition, PLAYER, region, not negate)


@negate_only
def PlayerOutsideRegion(region: gt.Region, condition, negate=False):
    return instr.IfCharacterRegionState(condition, PLAYER, region, negate)


@negate_only
def AllPlayersInsideRegion(region: gt.Region, condition, negate=False):
    return instr.IfAllPlayersRegionState(condition, region, not negate)


@negate_only
def AllPlayersOutsideRegion(region: gt.Region, condition, negate=False):
    return instr.IfAllPlayersRegionState(condition, region, negate)


@skip_and_negate_and_terminate
def InsideMap(game_map: gt.MapOrSequence, condition=None, negate=False,
              skip_lines=0, end_event=False, restart_event=False):
    if skip_lines > 0:
        return instr.SkipLinesIfMapPresenceState(skip_lines, negate, game_map)
    if end_event:
        return instr.TerminateIfMapPresenceState(EventEndType.End, not negate, game_map)
    if restart_event:
        return instr.SkipLinesIfMapPresenceState(EventEndType.Restart, not negate, game_map)
    return instr.IfMapPresenceState(condition, not negate, game_map)


@skip_and_negate_and_terminate
def OutsideMap(game_map: gt.MapOrSequence, sub_index=None, condition=None, negate=False, skip_lines=0,
               end_event=False, restart_event=False):
    return InsideMap(game_map, sub_index, condition=condition, negate=not negate, skip_lines=skip_lines,
                     end_event=end_event, restart_event=restart_event)


@negate_only
def EntityWithinDistance(first_entity: gt.CoordEntity, second_entity: gt.CoordEntity, max_distance, condition,
                         negate=False):
    return instr.IfEntityDistanceState(condition, first_entity, second_entity, max_distance, not negate)


@negate_only
def EntityBeyondDistance(first_entity: gt.CoordEntity, second_entity: gt.CoordEntity, min_distance, condition,
                         negate=False):
    return instr.IfEntityDistanceState(condition, first_entity, second_entity, min_distance, negate)


@negate_only
def PlayerWithinDistance(entity: gt.CoordEntity, max_distance, condition, negate=False):
    return instr.IfEntityDistanceState(condition, PLAYER, entity, max_distance, not negate)


@negate_only
def PlayerBeyondDistance(entity: gt.CoordEntity, min_distance, condition, negate=False):
    return instr.IfEntityDistanceState(condition, PLAYER, entity, min_distance, negate)


@negate_only
def HasItem(item: gt.Item, condition, negate=False):
    try:
        item_type = item.item_type
    except AttributeError:
        raise ValueError("Can only use auto-detecting HasItem() on declared item types (Weapon, Armor, Ring, Good).")
    return instr.IfPlayerItemStateNoBox(condition, item_type, item, not negate)


@negate_only
def HasWeapon(weapon: gt.Weapon, condition, negate=False):
    return instr.IfPlayerItemStateNoBox(condition, ItemType.Weapon, weapon, not negate)


@negate_only
def HasArmor(armor: gt.Armor, condition, negate=False):
    return instr.IfPlayerItemStateNoBox(condition, ItemType.Armor, armor, not negate)


@negate_only
def HasRing(ring: gt.Ring, condition, negate=False):
    return instr.IfPlayerItemStateNoBox(condition, ItemType.Ring, ring, not negate)


@negate_only
def HasGood(good: gt.Good, condition, negate=False):
    return instr.IfPlayerItemStateNoBox(condition, ItemType.Good, good, not negate)


@no_skip_or_negate_or_terminate
def DialogPromptActivated(prompt_text, anchor_entity: gt.CoordEntity, facing_angle=None, max_distance=None,
                          model_point=-1, human_or_hollow_only=True, button=0, boss_version=False,
                          line_intersects=None, anchor_type=None, condition=None):
    return instr.IfDialogPromptActivated(condition, prompt_text, anchor_entity, facing_angle, max_distance,
                                         model_point, human_or_hollow_only, button, boss_version, line_intersects,
                                         anchor_type)


@no_skip_or_negate_or_terminate
def MultiplayerEvent(multiplayer_event, condition):
    return instr.IfMultiplayerEvent(condition, multiplayer_event)


@negate_only
def TrueFlagCount(op_node, comparison_value, flag_range: gt.FlagRangeOrSequence, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfTrueFlagCountComparison(condition, comparison_value, FlagType.Absolute,
                                           comparison_type, flag_range)


@negate_only
def EventValue(op_node, comparison_value, start_flag, bit_count, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfEventValueComparison(condition, start_flag, bit_count, comparison_type, comparison_value)


# TODO: The EVS syntax for this will involve comparing two flags, which I haven't implemented yet.
#  Until then, you will need to use line-for-line-style 'IfEventFlagValue...()' directly.
@negate_only
def EventFlagValue(op_node, left_start_flag, left_bit_count, right_start_flag, right_bit_count,
                   condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfEventsComparison(condition, left_start_flag, left_bit_count, comparison_type,
                                    right_start_flag, right_bit_count)


@no_skip_or_negate_or_terminate
def AnyItemDroppedInRegion(region: gt.Region, condition):
    return instr.IfAnyItemDroppedInRegion(condition, region)


@no_skip_or_negate_or_terminate
def ItemDropped(item: gt.Item, condition):
    try:
        item_type = item.item_type
    except AttributeError:
        raise ValueError("Can only use HasItem() on declared item types (Weapon, Armor, Ring, Good).")
    return instr.IfItemDropped(condition, item, item_type)


@negate_only
def OwnsItem(item: gt.Item, condition, negate=False):
    try:
        item_type = item.type
    except AttributeError:
        raise ValueError("Can only use OwnsItem() on declared item types (Weapon, Armor, Ring, Good).")
    return instr.IfPlayerItemStateBox(condition, item_type, item, not negate)


@negate_only
def OwnsWeapon(weapon: gt.Weapon, condition, negate=False):
    return instr.IfPlayerItemStateBox(condition, ItemType.Weapon, weapon, not negate)


@negate_only
def OwnsArmor(armor: gt.Armor, condition, negate=False):
    return instr.IfPlayerItemStateBox(condition, ItemType.Armor, armor, not negate)


@negate_only
def OwnsRing(ring: gt.Ring, condition, negate=False):
    return instr.IfPlayerItemStateBox(condition, ItemType.Ring, ring, not negate)


@negate_only
def OwnsGood(good: gt.Good, condition, negate=False):
    return instr.IfPlayerItemStateBox(condition, ItemType.Good, good, not negate)


@negate_only
def IsAlive(character: gt.Character, condition, negate=False):
    return instr.IfCharacterDeathState(condition, character, negate)


@negate_only
def IsDead(character: gt.Character, condition, negate=False):
    return instr.IfCharacterDeathState(condition, character, not negate)


@no_skip_or_negate_or_terminate
def IsAttacked(attacked_entity, attacking_character, condition):
    return instr.IfAttacked(condition, attacked_entity, attacking_character)


@negate_only
def HealthRatio(op_node, comparison_value, character: gt.Character, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfHealthComparison(condition, character, comparison_type, comparison_value)


@negate_only
def PartHealthValue(op_node, comparison_value, character: gt.Character, part_type, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfCharacterPartHealthComparison(condition, character, part_type, comparison_value, comparison_type)


@no_skip_or_negate_or_terminate
def IsCharacterType(character: gt.Character, character_type: CharacterType, condition):
    return instr.IfCharacterType(condition, character, character_type)


@no_skip_or_negate_or_terminate
def IsHollow(character: gt.Character, condition):
    return instr.IfCharacterHollow(condition, character)


@no_skip_or_negate_or_terminate
def IsHuman(character: gt.Character, condition):
    return instr.IfCharacterHuman(condition, character)


@no_skip_or_negate_or_terminate
def IsInvader(character: gt.Character, condition):
    return instr.IfCharacterType(condition, character, CharacterType.Intruder)


@no_skip_or_negate_or_terminate
def IsBlackPhantom(character: gt.Character, condition):
    return instr.IfCharacterType(condition, character, CharacterType.BlackPhantom)


@no_skip_or_negate_or_terminate
def IsWhitePhantom(character: gt.Character, condition):
    return instr.IfCharacterType(condition, character, CharacterType.WhitePhantom)


@negate_only
def IsTargeting(targeting_chr, targeted_chr, condition, negate=False):
    return instr.IfCharacterTargetingState(condition, targeting_chr, targeted_chr, not negate)


@negate_only
def HasSpecialEffect(character: gt.Character, special_effect, condition, negate=False):
    return instr.IfCharacterSpecialEffectState(condition, character, special_effect, not negate)


@negate_only
def BackreadEnabled(character: gt.Character, condition, negate=False):
    return instr.IfCharacterBackreadState(condition, character, not negate)


@negate_only
def BackreadDisabled(character: gt.Character, condition, negate=False):
    return instr.IfCharacterBackreadState(condition, character, negate)


@negate_only
def HasTaeEvent(character: gt.Character, tae_event_id, condition, negate=False):
    return instr.IfTAEEventState(condition, character, tae_event_id, not negate)


@no_skip_or_negate_or_terminate
def HasAiStatus(character: gt.Character, ai_state, condition):
    return instr.IfHasAIStatus(condition, character, ai_state)


@no_skip_or_negate_or_terminate
def AiStatusIsNormal(character: gt.Character, condition):
    return instr.IfHasAIStatus(condition, character, AIStatusType.Normal)


@no_skip_or_negate_or_terminate
def AiStatusIsRecognition(character: gt.Character, condition):
    return instr.IfHasAIStatus(condition, character, AIStatusType.Caution)


@no_skip_or_negate_or_terminate
def AiStatusIsAlert(character: gt.Character, condition):
    return instr.IfHasAIStatus(condition, character, AIStatusType.Search)


@no_skip_or_negate_or_terminate
def AiStatusIsBattle(character: gt.Character, condition):
    return instr.IfHasAIStatus(condition, character, AIStatusType.Battle)


@no_skip_or_negate_or_terminate
def PlayerIsClass(class_type: ClassType, condition):
    return instr.IfPlayerClass(condition, class_type)


@no_skip_or_negate_or_terminate
def PlayerInCovenant(covenant_type: Covenant, condition):
    return instr.IfPlayerCovenant(condition, covenant_type)


@negate_only
def HealthValue(op_node, comparison_value, character: gt.Character, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfHealthValueComparison(condition, character, comparison_type, comparison_value)


@no_skip_or_negate_or_terminate
def IsDamaged(attacked_obj: gt.Object, attacking_character, condition):
    return instr.IfObjectDamagedBy(condition, attacked_obj, attacking_character)


@skip_and_negate_and_terminate
def IsDestroyed(obj: gt.Object, condition, negate=False, skip_lines=0, end_event=False, restart_event=False):
    if skip_lines > 0:
        return instr.SkipLinesIfObjectDestructionState(skip_lines, obj, negate)
    if end_event:
        return instr.TerminateIfObjectDestructionState(EventEndType.End, obj, not negate)
    if restart_event:
        return instr.TerminateIfObjectDestructionState(EventEndType.Restart, obj, not negate)
    return instr.IfObjectDestructionState(condition, obj, not negate)


@no_skip_or_negate_or_terminate
def IsActivated(obj: gt.Object, condition):
    return instr.IfObjectActivated(condition, obj)


@no_skip_or_negate_or_terminate
def PlayerStandingOnHitbox(hitbox: gt.Hitbox, condition):
    return instr.IfStandingOnHitbox(condition, hitbox)


@no_skip_or_negate_or_terminate
def PlayerMovingOnHitbox(hitbox: gt.Hitbox, condition):
    return instr.IfMovingOnHitbox(condition, hitbox)


@no_skip_or_negate_or_terminate
def PlayerRunningOnHitbox(hitbox: gt.Hitbox, condition):
    return instr.IfRunningOnHitbox(condition, hitbox)
