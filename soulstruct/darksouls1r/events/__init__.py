"""Inherits a lot from DS1PTDE."""

__all__ = [
    # EMEVD and EMEVDDirectory classes
    "EMEVD",
    "EMEVDDirectory",
    # Sub-packages / package attributes (contents of constants, instructions, and tests are also in this namespace)
    "constants",
    "instructions",
    "tests",
    "enums",
    "decompiler",
    # File utilities
    "convert_events",
    "compare_events",
    # Dark Souls 1 map constants
    "COMMON",
    "DEPTHS",
    "UNDEAD_BURG",
    "FIRELINK_SHRINE",
    "PAINTED_WORLD",
    "DARKROOT_GARDEN",
    "OOLACILE",
    "CATACOMBS",
    "TOMB_OF_THE_GIANTS",
    "ASH_LAKE",
    "BLIGHTTOWN",
    "LOST_IZALITH",
    "SENS_FORTRESS",
    "ANOR_LONDO",
    "NEW_LONDO_RUINS",
    "DUKES_ARCHIVES",
    "KILN_OF_THE_FIRST_FLAME",
    "UNDEAD_ASYLUM",
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
    "Alive",
    "Dead",
    "Attacked",
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
    "CharacterHasTAEEvent",
    "CharacterTargeting",
    "HasAIStatus",
    "HasNormalAIStatus",
    "HasRecognitionAIStatus",
    "HasAlertAIStatus",
    "HasBattleAIStatus",
    "PlayerIsClass",
    "PlayerInCovenant",
    "ObjectDamaged",
    "ObjectDestroyed",
    "ObjectActivated",
    "PlayerStandingOnCollision",
    "PlayerMovingOnCollision",
    "PlayerRunningOnCollision",
    # Dark Souls 1 specific tests
    "HOST",
    "CLIENT",
    "SINGLEPLAYER",
    "MULTIPLAYER",
    # Basic enums
    "RestartType",
    "uint",
    "short",
    "ushort",
    "char",
    "uchar",
    "PLAYER",
    "ProtectedEntities",
    # Enums identical in all games
    "AIStatusType",
    "BitOperation",
    "ButtonType",
    "CharacterType",
    "CharacterUpdateRate",
    "ClassType",
    "ComparisonType",
    "CutsceneFlags",
    "DamageTargetType",
    "EventReturnType",
    "FlagType",
    "InterpolationState",
    "ItemType",
    "RangeState",
    "CoordEntityType",
    "NavmeshType",
    "NumberButtons",
    "OnOffChange",
    "RestartType",
    "SoundType",
    "StatueType",
    "SummonSignType",
    "TriggerAttribute",
    "WorldTendencyType",
    "UpdateAuthority",
    # Enums for Dark Souls 1 (both PTD and DSR) only
    "CalculationType",
    "ConditionGroup",
    "Covenant",
    "TeamType",
    "BannerType",
    "MultiplayerState",
    "NPCPartType",
]

from soulstruct.darksouls1ptde.maps import constants
from soulstruct.darksouls1ptde.maps.constants import *
from .emevd import EMEVD, decompiler, enums, tests
from .emevd.enums import *
from .emevd.tests import *
from .emevd_directory import EMEVDDirectory
from .utilities import convert_events, compare_events
