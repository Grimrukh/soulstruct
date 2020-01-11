import soulstruct.events.darksouls3.instructions as instr
from soulstruct.events.internal import no_skip_or_negate_or_terminate, ConstantCondition
from soulstruct.events.shared.tests import *
from soulstruct.enums.darksouls3 import *
from soulstruct.game_types import *

__all__ = [
    # Names processed directly by EVS parser
    "NeverRestart", "RestartOnRest", "UnknownRestart", "EVENTS", "Condition", "END", "RESTART", "Await",

    # Shared tests
    "THIS_FLAG", "THIS_SLOT_FLAG",
    "ONLINE", "OFFLINE", "DLC_OWNED", "SKULL_LANTERN_ACTIVE",
    "WHITE_WORLD_TENDENCY", "BLACK_WORLD_TENDENCY", "NEW_GAME_CYCLE", "SOUL_LEVEL",
    "FlagEnabled", "FlagDisabled",
    "SecondsElapsed", "FramesElapsed",
    "CharacterInsideRegion", "CharacterOutsideRegion",
    "PlayerInsideRegion", "PlayerOutsideRegion", "AllPlayersInsideRegion", "AllPlayersOutsideRegion",
    "InsideMap", "OutsideMap",
    "EntityWithinDistance", "EntityBeyondDistance", "PlayerWithinDistance", "PlayerBeyondDistance",
    "HasItem", "HasWeapon", "HasArmor", "HasRing", "HasGood",
    "DialogPromptActivated",
    "MultiplayerEvent", "TrueFlagCount", "EventValue", "EventFlagValue",
    "AnyItemDroppedInRegion", "ItemDropped",
    "OwnsItem", "OwnsWeapon", "OwnsArmor", "OwnsRing", "OwnsGood",
    "IsAlive", "IsDead", "IsAttacked",
    "HealthRatio", "HealthValue", "PartHealthValue",
    "IsCharacterType", "IsHollow", "IsHuman", "IsInvader", "IsBlackPhantom", "IsWhitePhantom",
    "HasSpecialEffect",
    "BackreadEnabled", "BackreadDisabled",
    "HasTaeEvent",
    "IsTargeting", "HasAiStatus", "AiStatusIsNormal", "AiStatusIsRecognition", "AiStatusIsAlert", "AiStatusIsBattle",
    "PlayerIsClass", "PlayerInCovenant",
    "IsDamaged", "IsDestroyed", "IsActivated",
    "PlayerStandingOnCollision", "PlayerMovingOnCollision", "PlayerRunningOnCollision",

    # Dark Souls 3 tests
    "HOST", "CLIENT", "IN_OWN_WORLD", "ActionButtonInRegion", "IsAttackedWithDamageType",
    "CharacterDrawGroupActive", "CharacterDrawGroupInactive",
]


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

IN_OWN_WORLD = ConstantCondition(
    if_true_func=instr.IfPlayerInOwnWorld,
    if_false_func=instr.IfPlayerNotInOwnWorld,
    end_if_true_func=instr.EndIfPlayerInOwnWorld,
    end_if_false_func=instr.EndIfPlayerNotInOwnWorld,
    restart_if_true_func=instr.RestartIfPlayerInOwnWorld,
    restart_if_false_func=instr.RestartIfPlayerNotInOwnWorld,
)


@no_skip_or_negate_or_terminate
def ActionButtonInRegion(action_button_id: int, region: RegionInt, condition: int):
    return instr.IfActionButtonInRegion(condition, action_button_id, region)


@no_skip_or_negate_or_terminate
def IsAttackedWithDamageType(attacked_entity: AnimatedInt, attacking_character: CharacterInt,
                             damage_type: DamageType, condition: int):
    return instr.IfDamageType(condition, attacked_entity, attacking_character, damage_type)


@no_skip_or_negate_or_terminate
def CharacterDrawGroupActive(character: CharacterInt, condition: int):
    return instr.IfCharacterDrawGroupActive(condition, character)


@no_skip_or_negate_or_terminate
def CharacterDrawGroupInactive(character: CharacterInt, condition: int):
    return instr.IfCharacterDrawGroupInactive(condition, character)
