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

# Boolean constants.
HOST = ...
CLIENT = ...
IN_OWN_WORLD = ...

def ActionButtonInRegion(action_button_id: int, region: RegionInt): ...
def IsAttackedWithDamageType(attacked_entity: CharacterInt, attacking_character: CharacterInt,
                             damage_type: DamageType): ...
def CharacterDrawGroupActive(character: CharacterInt): ...
def CharacterDrawGroupInactive(character: CharacterInt): ...
