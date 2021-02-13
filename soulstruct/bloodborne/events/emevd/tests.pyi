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

from soulstruct.base.events.emevd.tests import *
from soulstruct.game_types import *


# Boolean constants.
HOST = ...
CLIENT = ...
SINGLEPLAYER = ...
MULTIPLAYER = ...

# Numeric comparison.
INSIGHT = ...

def IsAttackedWithDamageType(attacked_entity: CharacterTyping, attacker: CharacterTyping, damage_type): ...
def ActionButtonParamActivated(action_button_id: int, entity: CoordEntityTyping): ...
def WearingArmorTypeInRange(armor_type, required_armor_range_first, required_armor_range_last): ...
def CharacterDrawGroupActive(character: CharacterTyping): ...
def CharacterDrawGroupInactive(character: CharacterTyping): ...
