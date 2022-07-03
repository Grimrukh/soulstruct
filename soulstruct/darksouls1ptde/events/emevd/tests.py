__all__ = [
    # Names processed directly by EVS parser
    "NeverRestart",
    "RestartOnRest",
    "UnknownRestart",
    "EVENTS",
    "Condition",
    "HeldCondition",
    "END",
    "RESTART",
    "Await",

    "THIS_FLAG",
    "THIS_SLOT_FLAG",
    "ONLINE",
    "OFFLINE",
    "DLC_OWNED",
    "SKULL_LANTERN_ACTIVE",
    "WHITE_WORLD_TENDENCY",
    "BLACK_WORLD_TENDENCY",
    "NEW_GAME_CYCLE",
    "PLAYER_LEVEL",
    "FlagEnabled",
    "FlagDisabled",
    "SecondsElapsed",
    "FramesElapsed",
    "CharacterInsideRegion",
    "CharacterOutsideRegion",
    "PlayerInsideRegion",
    "PlayerOutsideRegion",
    "AllPlayersInsideRegion",
    "AllPlayersOutsideRegion",
    "InsideMap",
    "OutsideMap",
    "EntityWithinDistance",
    "EntityBeyondDistance",
    "PlayerWithinDistance",
    "PlayerBeyondDistance",
    "HasItem",
    "HasWeapon",
    "HasArmor",
    "HasRing",
    "HasGood",
    "ActionButton",
    "MultiplayerEvent",
    "TrueFlagCount",
    "EventValue",
    "EventFlagValue",
    "AnyItemDroppedInRegion",
    "ItemDropped",
    "OwnsItem",
    "OwnsWeapon",
    "OwnsArmor",
    "OwnsRing",
    "OwnsGood",
    "IsAlive",
    "IsDead",
    "IsAttacked",
    "HealthRatio",
    "HealthValue",
    "PartHealthValue",
    "IsCharacterType",
    "IsHollow",
    "IsHuman",
    "IsInvader",
    "IsBlackPhantom",
    "IsWhitePhantom",
    "HasSpecialEffect",
    "BackreadEnabled",
    "BackreadDisabled",
    "HasTaeEvent",
    "IsTargeting",
    "HasAiStatus",
    "AiStatusIsNormal",
    "AiStatusIsRecognition",
    "AiStatusIsAlert",
    "AiStatusIsBattle",
    "PlayerIsClass",
    "PlayerInCovenant",
    "IsDamaged",
    "IsDestroyed",
    "IsActivated",
    "PlayerStandingOnCollision",
    "PlayerMovingOnCollision",
    "PlayerRunningOnCollision",
    "HOST",
    "CLIENT",
    "SINGLEPLAYER",
    "MULTIPLAYER",
]
import typing as tp

from soulstruct.base.events.emevd.compiler import BooleanTestCompiler
from soulstruct.base.events.emevd.utils import *
from soulstruct.darksouls1ptde.game_types import *

from .compiler import compile_instruction
from .enums import *


# Dummy names parsed directly in `EVSParser` (correct EVS signatures given in `tests.pyi` stub file).


def NeverRestart(event_id_or_func: tp.Union[tp.Callable, int]):
    return event_id_or_func


def RestartOnRest(event_id_or_func: tp.Union[tp.Callable, int]):
    return event_id_or_func


def UnknownRestart(event_id_or_func: tp.Union[tp.Callable, int]):
    return event_id_or_func


class EVENTS:
    pass


class Condition:
    pass


class HeldCondition:
    pass


def Await(_):
    pass


END = None
RESTART = None


# Special constant conditions.


THIS_FLAG = BooleanTestCompiler(
    compile_instruction=compile_instruction,
    if_true="IfThisEventFlagEnabled",
    if_false="IfThisEventFlagDisabled",
    skip_if_true="SkipLinesIfThisEventFlagEnabled",
    skip_if_false="SkipLinesIfThisEventFlagDisabled",
    end_if_true="EndIfThisEventFlagEnabled",
    end_if_false="EndIfThisEventFlagDisabled",
    restart_if_true="RestartIfThisEventFlagEnabled",
    restart_if_false="RestartIfThisEventFlagDisabled",
)

THIS_SLOT_FLAG = BooleanTestCompiler(
    compile_instruction=compile_instruction,
    if_true="IfThisEventSlotFlagEnabled",
    if_false="IfThisEventSlotFlagDisabled",
    skip_if_true="SkipLinesIfThisEventSlotFlagEnabled",
    skip_if_false="SkipLinesIfThisEventSlotFlagDisabled",
    end_if_true="EndIfThisEventSlotFlagEnabled",
    end_if_false="EndIfThisEventSlotFlagDisabled",
    restart_if_true="RestartIfThisEventSlotFlagEnabled",
    restart_if_false="RestartIfThisEventSlotFlagDisabled",
)

ONLINE = BooleanTestCompiler(
    compile_instruction=compile_instruction,
    if_true="IfOnline",
    if_false="IfOffline",
)

OFFLINE = BooleanTestCompiler(
    compile_instruction=compile_instruction,
    if_true="IfOffline",
    if_false="IfOnline",
)

DLC_OWNED = BooleanTestCompiler(
    compile_instruction=compile_instruction,
    if_true="IfDLCOwned",
    if_false="IfDLCNotOwned",
)

SKULL_LANTERN_ACTIVE = BooleanTestCompiler(
    compile_instruction=compile_instruction,
    if_true="IfSkullLanternActive",
    if_false="IfSkullLanternInactive",
)


# Special comparator values.


@negate_only
def WHITE_WORLD_TENDENCY(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return compile_instruction("IfWhiteWorldTendencyComparison", condition, comparison_type, comparison_value)


@negate_only
def BLACK_WORLD_TENDENCY(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return compile_instruction("IfBlackWorldTendencyComparison", condition, comparison_type, comparison_value)


@negate_only
def NEW_GAME_CYCLE(op_node, completion_count, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return compile_instruction("IfNewGameCycleComparison", condition, comparison_type, completion_count)


@negate_only
def PLAYER_LEVEL(op_node, comparison_value, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return compile_instruction("IfPlayerLevelComparison", condition, comparison_type, comparison_value)


# All other tests.


@skip_and_negate_and_return
def FlagEnabled(flag: Flag, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False):
    if condition is not None:
        if negate:
            return compile_instruction("IfFlagDisabled", condition, flag)
        return compile_instruction("IfFlagEnabled", condition, flag)
    if skip_lines > 0:
        if negate:
            return compile_instruction("SkipLinesIfFlagEnabled", skip_lines, flag)
        return compile_instruction("SkipLinesIfFlagDisabled", skip_lines, flag)
    if end_event:
        if negate:
            return compile_instruction("EndIfFlagDisabled", flag)
        return compile_instruction("EndIfFlagEnabled", flag)
    if restart_event:
        if negate:
            return compile_instruction("RestartIfFlagDisabled", flag)
        return compile_instruction("RestartIfFlagEnabled", flag)


@skip_and_negate_and_return
def FlagDisabled(flag: Flag, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False):
    if condition is not None:
        if not negate:
            return compile_instruction("IfFlagDisabled", condition, flag)
        return compile_instruction("IfFlagEnabled", condition, flag)
    if skip_lines > 0:
        if not negate:
            return compile_instruction("SkipLinesIfFlagEnabled", skip_lines, flag)
        return compile_instruction("SkipLinesIfFlagDisabled", skip_lines, flag)
    if end_event:
        if not negate:
            return compile_instruction("EndIfFlagDisabled", flag)
        return compile_instruction("EndIfFlagEnabled", flag)
    if restart_event:
        if not negate:
            return compile_instruction("RestartIfFlagDisabled", flag)
        return compile_instruction("RestartIfFlagEnabled", flag)


@no_skip_or_negate_or_return
def SecondsElapsed(elapsed_seconds, condition):
    return compile_instruction("IfTimeElapsed", condition, elapsed_seconds)


@no_skip_or_negate_or_return
def FramesElapsed(elapsed_frames, condition):
    return compile_instruction("IfFramesElapsed", condition, elapsed_frames)


@negate_only
def CharacterInsideRegion(entity: AnimatedEntityTyping, region: Region, condition, negate=False):
    return compile_instruction("IfCharacterRegionState", condition, not negate, entity, region)


@negate_only
def CharacterOutsideRegion(entity: AnimatedEntityTyping, region: Region, condition, negate=False):
    return compile_instruction("IfCharacterRegionState", condition, negate, entity, region)


@negate_only
def PlayerInsideRegion(region: Region, condition, negate=False):
    return compile_instruction("IfCharacterRegionState", condition, not negate, PLAYER, region)


@negate_only
def PlayerOutsideRegion(region: Region, condition, negate=False):
    return compile_instruction("IfCharacterRegionState", condition, negate, PLAYER, region)


@negate_only
def AllPlayersInsideRegion(region: Region, condition, negate=False):
    return compile_instruction("IfAllPlayersRegionState", condition, not negate, region)


@negate_only
def AllPlayersOutsideRegion(region: Region, condition, negate=False):
    return compile_instruction("IfAllPlayersRegionState", condition, negate, region)


@skip_and_negate_and_return
def InsideMap(
    game_map: MapTyping, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False
):
    if skip_lines > 0:
        return compile_instruction("SkipLinesIfMapPresenceState", skip_lines, negate, game_map)
    if end_event:
        return compile_instruction("ReturnIfMapPresenceState", EventReturnType.End, not negate, game_map)
    if restart_event:
        return compile_instruction("SkipLinesIfMapPresenceState", EventReturnType.Restart, not negate, game_map)
    return compile_instruction("IfMapPresenceState", condition, not negate, game_map)


@skip_and_negate_and_return
def OutsideMap(
    game_map: MapTyping, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False
):
    if skip_lines > 0:
        return compile_instruction("SkipLinesIfMapPresenceState", skip_lines, not negate, game_map)
    if end_event:
        return compile_instruction("ReturnIfMapPresenceState", EventReturnType.End, negate, game_map)
    if restart_event:
        return compile_instruction("SkipLinesIfMapPresenceState", EventReturnType.Restart, negate, game_map)
    return compile_instruction("IfMapPresenceState", condition, negate, game_map)


@negate_only
def EntityWithinDistance(
    first_entity: CoordEntityTyping,
    second_entity: CoordEntityTyping,
    max_distance,
    condition,
    negate=False,
):
    return compile_instruction(
        "IfEntityDistanceState", condition, not negate, first_entity, second_entity, max_distance
    )


@negate_only
def EntityBeyondDistance(
    first_entity: CoordEntityTyping,
    second_entity: CoordEntityTyping,
    min_distance,
    condition,
    negate=False,
):
    return compile_instruction("IfEntityDistanceState", condition, negate, first_entity, second_entity, min_distance)


@negate_only
def PlayerWithinDistance(entity: CoordEntityTyping, max_distance, condition, negate=False):
    return compile_instruction("IfEntityDistanceState", condition, not negate, PLAYER, entity, max_distance)


@negate_only
def PlayerBeyondDistance(entity: CoordEntityTyping, min_distance, condition, negate=False):
    return compile_instruction("IfEntityDistanceState", condition, negate, PLAYER, entity, min_distance)


@negate_only
def HasItem(item: ItemTyping, condition, item_type=None, negate=False):
    if item_type is None:
        try:
            item_type = item.get_item_enum()
        except AttributeError:
            raise ValueError(
                "Can only use auto-detecting HasItem() on declared item types (Weapon, Armor, Ring, Good)."
            )
    return compile_instruction("IfPlayerItemStateExcludingStorage", condition, item, not negate, item_type)


@negate_only
def HasWeapon(weapon: WeaponParam, condition, negate=False):
    return compile_instruction("IfPlayerItemStateExcludingStorage", condition, weapon, not negate, ItemType.Weapon)


@negate_only
def HasArmor(armor: ArmorParam, condition, negate=False):
    return compile_instruction("IfPlayerItemStateExcludingStorage", condition, armor, not negate, ItemType.Armor, )


@negate_only
def HasRing(ring: AccessoryParam, condition, negate=False):
    return compile_instruction("IfPlayerItemStateExcludingStorage", condition, ring, not negate, ItemType.Ring)


@negate_only
def HasGood(good: GoodParam, condition, negate=False):
    return compile_instruction("IfPlayerItemStateExcludingStorage", condition, good, not negate, ItemType.Good)


@no_skip_or_negate_or_return
def ActionButton(
    prompt_text,
    anchor_entity: CoordEntityTyping,
    anchor_type=None,
    facing_angle=None,
    max_distance=None,
    model_point=-1,
    trigger_attribute: TriggerAttribute = TriggerAttribute.Human_or_Hollow,
    button=0,
    boss_version=False,
    line_intersects=None,
    condition=None,
):
    return compile_instruction(
        "IfActionButton",
        condition,
        prompt_text=prompt_text,
        anchor_entity=anchor_entity,
        anchor_type=anchor_type,
        facing_angle=facing_angle,
        max_distance=max_distance,
        model_point=model_point,
        trigger_attribute=trigger_attribute,
        button=button,
        boss_version=boss_version,
        line_intersects=line_intersects,
    )


@no_skip_or_negate_or_return
def MultiplayerEvent(multiplayer_event, condition):
    return compile_instruction("IfMultiplayerEvent", condition, multiplayer_event)


@negate_only
def TrueFlagCount(op_node, comparison_value, flag_range: FlagRangeTyping, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return compile_instruction(
        "IfTrueFlagCountComparison", condition, FlagType.Absolute, comparison_type, flag_range, comparison_value
    )


@negate_only
def EventValue(op_node, comparison_value, start_flag, bit_count, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return compile_instruction(
        "IfEventValueComparison", condition, start_flag, bit_count, comparison_type, comparison_value
    )


# TODO: The EVS syntax for this will involve comparing two flags, which I haven't implemented yet.
#  Until then, you will need to use line-for-line-style 'IfEventFlagValue...()' directly.
@negate_only
def EventFlagValue(
    op_node, left_start_flag, left_bit_count, right_start_flag, right_bit_count, condition, negate=False
):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return compile_instruction(
        "IfEventsComparison",
        condition,
        left_start_flag,
        left_bit_count,
        comparison_type,
        right_start_flag,
        right_bit_count,
    )


@no_skip_or_negate_or_return
def AnyItemDroppedInRegion(region: Region, condition):
    return compile_instruction("IfAnyItemDroppedInRegion", condition, region)


@no_skip_or_negate_or_return
def ItemDropped(item: ItemTyping, condition, item_type=None):
    if item_type is None:
        try:
            item_type = item.get_item_enum()
        except AttributeError:
            raise ValueError("Can only use ItemDropped() on declared item types (Weapon, Armor, Ring, Good).")
    return compile_instruction("IfItemDropped", condition, item, item_type)


@negate_only
def OwnsItem(item: ItemTyping, condition, item_type=None, negate=False):
    if item_type is None:
        try:
            item_type = item.get_item_enum()
        except AttributeError:
            raise ValueError("Can only use OwnsItem() on declared item types (Weapon, Armor, Ring, Good).")
    return compile_instruction("IfPlayerItemStateIncludingStorage", condition, item, not negate, item_type)


@negate_only
def OwnsWeapon(weapon: WeaponParam, condition, negate=False):
    return compile_instruction("IfPlayerItemStateIncludingStorage", condition, weapon, not negate, ItemType.Weapon)


@negate_only
def OwnsArmor(armor: ArmorParam, condition, negate=False):
    return compile_instruction("IfPlayerItemStateIncludingStorage", condition, armor, not negate, ItemType.Armor)


@negate_only
def OwnsRing(ring: AccessoryParam, condition, negate=False):
    return compile_instruction("IfPlayerItemStateIncludingStorage", condition, ring, not negate, ItemType.Ring)


@negate_only
def OwnsGood(good: GoodParam, condition, negate=False):
    return compile_instruction("IfPlayerItemStateIncludingStorage", condition, good, not negate, ItemType.Good)


@negate_only
def IsAlive(character: Character, condition, negate=False):
    return compile_instruction("IfCharacterDeathState", condition, character, negate)


@negate_only
def IsDead(character: Character, condition, negate=False):
    return compile_instruction("IfCharacterDeathState", condition, character, not negate)


@no_skip_or_negate_or_return
def IsAttacked(attacked_entity, attacker, condition):
    return compile_instruction("IfAttacked", condition, attacked_entity, attacker)


@negate_only
def HealthRatio(op_node, comparison_value, character: Character, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return compile_instruction("IfHealthComparison", condition, character, comparison_type, comparison_value)


@negate_only
def HealthValue(op_node, comparison_value, character: Character, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return compile_instruction("IfHealthValueComparison", condition, character, comparison_type, comparison_value)


@negate_only
def PartHealthValue(op_node, comparison_value, character: Character, npc_part_id, condition, negate=False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return compile_instruction(
        "IfCharacterPartHealthComparison", condition, character, npc_part_id, comparison_type, comparison_value
    )


@no_skip_or_negate_or_return
def IsCharacterType(character: Character, character_type: CharacterType, condition):
    return compile_instruction("IfCharacterType", condition, character, character_type)


@no_skip_or_negate_or_return
def IsHollow(character: Character, condition):
    return compile_instruction("IfCharacterHollow", condition, character)


@no_skip_or_negate_or_return
def IsHuman(character: Character, condition):
    return compile_instruction("IfCharacterHuman", condition, character)


@no_skip_or_negate_or_return
def IsInvader(character: Character, condition):
    return compile_instruction("IfCharacterType", condition, character, CharacterType.Intruder)


@no_skip_or_negate_or_return
def IsBlackPhantom(character: Character, condition):
    return compile_instruction("IfCharacterType", condition, character, CharacterType.BlackPhantom)


@no_skip_or_negate_or_return
def IsWhitePhantom(character: Character, condition):
    return compile_instruction("IfCharacterType", condition, character, CharacterType.WhitePhantom)


@negate_only
def HasSpecialEffect(character: Character, special_effect, condition, negate=False):
    return compile_instruction("IfCharacterSpecialEffectState", condition, character, special_effect, not negate)


@negate_only
def BackreadEnabled(character: Character, condition, negate=False):
    return compile_instruction("IfCharacterBackreadState", condition, character, not negate)


@negate_only
def BackreadDisabled(character: Character, condition, negate=False):
    return compile_instruction("IfCharacterBackreadState", condition, character, negate)


@negate_only
def HasTaeEvent(character: Character, tae_event_id, condition, negate=False):
    return compile_instruction("IfCharacterTAEEventState", condition, character, tae_event_id, not negate)


@negate_only
def IsTargeting(targeting_chr, targeted_chr, condition, negate=False):
    return compile_instruction("IfCharacterTargetingState", condition, targeting_chr, targeted_chr, not negate)


@no_skip_or_negate_or_return
def HasAiStatus(character: Character, ai_status, condition):
    return compile_instruction("IfHasAIStatus", condition, character, ai_status)


@no_skip_or_negate_or_return
def AiStatusIsNormal(character: Character, condition):
    return compile_instruction("IfHasAIStatus", condition, character, AIStatusType.Normal)


@no_skip_or_negate_or_return
def AiStatusIsRecognition(character: Character, condition):
    return compile_instruction("IfHasAIStatus", condition, character, AIStatusType.Caution)


@no_skip_or_negate_or_return
def AiStatusIsAlert(character: Character, condition):
    return compile_instruction("IfHasAIStatus", condition, character, AIStatusType.Search)


@no_skip_or_negate_or_return
def AiStatusIsBattle(character: Character, condition):
    return compile_instruction("IfHasAIStatus", condition, character, AIStatusType.Battle)


@no_skip_or_negate_or_return
def PlayerIsClass(class_type: ClassType, condition):
    return compile_instruction("IfPlayerClass", condition, class_type)


@no_skip_or_negate_or_return
def PlayerInCovenant(covenant_type: Covenant, condition):
    return compile_instruction("IfPlayerCovenant", condition, covenant_type)


@no_skip_or_negate_or_return
def IsDamaged(attacked_obj: Object, attacker, condition):
    return compile_instruction("IfObjectDamagedBy", condition, attacked_obj, attacker)


@skip_and_negate_and_return
def IsDestroyed(obj: Object, condition, negate=False, skip_lines=0, end_event=False, restart_event=False):
    if skip_lines > 0:
        return compile_instruction("SkipLinesIfObjectDestructionState", skip_lines, negate, obj)
    if end_event:
        return compile_instruction("ReturnIfObjectDestructionState", EventReturnType.End, not negate, obj)
    if restart_event:
        return compile_instruction("ReturnIfObjectDestructionState", EventReturnType.Restart, not negate, obj)
    return compile_instruction("IfObjectDestructionState", condition, not negate, obj)


@no_skip_or_negate_or_return
def IsActivated(obj_act_flag: Flag, condition):
    return compile_instruction("IfObjectActivated", condition, obj_act_flag)


@no_skip_or_negate_or_return
def PlayerStandingOnCollision(collision: Collision, condition):
    return compile_instruction("IfStandingOnCollision", condition, collision)


@no_skip_or_negate_or_return
def PlayerMovingOnCollision(collision: Collision, condition):
    return compile_instruction("IfMovingOnCollision", condition, collision)


@no_skip_or_negate_or_return
def PlayerRunningOnCollision(collision: Collision, condition):
    return compile_instruction("IfRunningOnCollision", condition, collision)


HOST = BooleanTestCompiler(
    compile_instruction=compile_instruction,
    if_true="IfHost",
    skip_if_true="SkipLinesIfHost",
    end_if_true="EndIfHost",
    restart_if_true="RestartIfHost",
)

CLIENT = BooleanTestCompiler(
    compile_instruction=compile_instruction,
    if_true="IfClient",
    skip_if_true="SkipLinesIfClient",
    end_if_true="EndIfClient",
    restart_if_true="RestartIfClient",
)

SINGLEPLAYER = BooleanTestCompiler(
    compile_instruction=compile_instruction,
    if_true="IfSingleplayer",
    skip_if_true="SkipLinesIfSingleplayer",
    end_if_true="EndIfSingleplayer",
    restart_if_true="RestartIfSingleplayer",
)

MULTIPLAYER = BooleanTestCompiler(
    compile_instruction=compile_instruction,
    if_true="IfMultiplayer",
    skip_if_true="SkipLinesIfMultiplayer",
    end_if_true="EndIfMultiplayer",
    restart_if_true="RestartIfMultiplayer",
)
