__all__ = [
    # Names processed directly by EVS parser
    "NeverRestart",
    "RestartOnRest",
    "UnknownRestart",
    "EVENTS",
    "Condition",
    "END",
    "RESTART",
    "Await",
    # Shared tests
    "THIS_FLAG",
    "THIS_SLOT_FLAG",
    "ONLINE",
    "OFFLINE",
    "DLC_OWNED",
    "SKULL_LANTERN_ACTIVE",
    "WHITE_WORLD_TENDENCY",
    "BLACK_WORLD_TENDENCY",
    "NEW_GAME_CYCLE",
    "SOUL_LEVEL",
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
    # Bloodborne tests
    "HOST",
    "CLIENT",
    "SINGLEPLAYER",
    "MULTIPLAYER",
    "IsAttackedWithDamageType",
    "ActionButtonParamActivated",
    "WearingArmorTypeInRange",
    "CharacterDrawGroupActive",
    "CharacterDrawGroupInactive",
    "INSIGHT",
]

from soulstruct.base.events.emevd.utils import *
from soulstruct.base.events.emevd.tests import *
from soulstruct.game_types import *
from . import instructions as instr
from .enums import *


HOST = ConstantCondition(
    if_true_func=instr.IfHost,
    skip_if_true_func=instr.SkipLinesIfHost,
    end_if_true_func=instr.EndIfHost,
    restart_if_true_func=instr.RestartIfHost,
)

CLIENT = ConstantCondition(
    if_true_func=instr.IfClient,
    skip_if_true_func=instr.SkipLinesIfClient,
    end_if_true_func=instr.EndIfClient,
    restart_if_true_func=instr.RestartIfClient,
)

SINGLEPLAYER = ConstantCondition(
    if_true_func=instr.IfSingleplayer,
    skip_if_true_func=instr.SkipLinesIfSingleplayer,
    end_if_true_func=instr.EndIfSingleplayer,
    restart_if_true_func=instr.RestartIfSingleplayer,
)

MULTIPLAYER = ConstantCondition(
    if_true_func=instr.IfMultiplayer,
    skip_if_true_func=instr.SkipLinesIfMultiplayer,
    end_if_true_func=instr.EndIfMultiplayer,
    restart_if_true_func=instr.RestartIfMultiplayer,
)


@no_skip_or_negate_or_return
def IsAttackedWithDamageType(
    attacked_entity: AnimatedTyping, attacker: CharacterTyping, damage_type: DamageType, condition: int
):
    return instr.IfAttackedWithDamageType(condition, attacked_entity, attacker, damage_type)


@no_skip_or_negate_or_return
def ActionButtonParamActivated(action_button_id: int, entity: CoordEntityTyping, condition: int):
    return instr.IfActionButtonParam(condition, action_button_id, entity)


@no_skip_or_negate_or_return
def WearingArmorTypeInRange(
    armor_type: ArmorType, required_armor_range_first: int, required_armor_range_last: int, condition: int
):
    return instr.IfPlayerArmorType(condition, armor_type, required_armor_range_first, required_armor_range_last)


@no_skip_or_negate_or_return
def CharacterDrawGroupActive(character: CharacterTyping, condition: int):
    return instr.IfCharacterDrawGroupActive(condition, character)


@no_skip_or_negate_or_return
def CharacterDrawGroupInactive(character: CharacterTyping, condition: int):
    return instr.IfCharacterDrawGroupInactive(condition, character)


@negate_only
def INSIGHT(op_node, comparison_value, condition: int, negate: bool = False):
    comparison_type = NEG_COMPARISON_NODES[op_node] if negate else COMPARISON_NODES[op_node]
    return instr.IfPlayerInsightAmountComparison(condition, comparison_value, comparison_type)
