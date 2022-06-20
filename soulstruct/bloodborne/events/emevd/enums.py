__all__ = [
    # Basic enums
    "RestartType",
    "uint",
    "short",
    "ushort",
    "char",
    "uchar",
    "PLAYER",
    "CLIENT_PLAYER_1",
    "CLIENT_PLAYER_2",
    "CLIENT_PLAYER_3",
    "CLIENT_PLAYER_4",
    "CLIENT_PLAYER_5",
    "PlayerEntity",
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
    "FlagState",
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
    # Enums in Bloodborne only
    "ArmorType",
    "BannerType",
    "CalculationType",
    "ClientType",
    "ConditionGroup",
    "DamageType",
    "DeleteOrAdd",
    "DialogResult",
    "DisplayState",
    "DoorState",
    "Gender",
    "Label",
    "MultiplayerState",
    "NPCPartType",
    "PlayGoState",
    "PlayLogMultiplayerType",
    "PlayerPlayLogParameter",
    "SingleplayerSummonSignType",
    "TeamType",
]

from enum import IntEnum
from soulstruct.base.events.emevd.enums import *


class ArmorType(IntEnum):
    Head = 0
    Body = 1
    Arms = 2
    Legs = 3


class BannerType(IntEnum):
    PreySlaughtered = 1
    YouDied = 2
    Revival = 3
    SoulRecovery = 4
    TargetedDefeated = 5
    PhantomDeath = 6  # Phantom version of "YOU DIED"
    BlackPhantomDestroyed = 7
    AreaName = 8  # Name determined by current floor Collision.
    Congratulations = 12  # Not sure if this is still bugged from DS1.
    YouWin = 15
    YouLose = 16
    NightmareSlain = 17


class CalculationType(IntEnum):
    Add = 0
    Subtract = 1
    Multiply = 2
    Divide = 3
    Modulus = 4
    Assign = 5


class ClientType(IntEnum):
    Coop = 0
    Invader = 1
    BetrayalInvader = 2


class ConditionGroup(IntEnum):
    OR_15 = -15
    OR_14 = -14
    OR_13 = -13
    OR_12 = -12
    OR_11 = -11
    OR_10 = -10
    OR_9 = -9
    OR_8 = -8
    OR_7 = -7
    OR_6 = -6
    OR_5 = -5
    OR_4 = -4
    OR_3 = -3
    OR_2 = -2
    OR_1 = -1
    MAIN = 0
    AND_1 = 1
    AND_2 = 2
    AND_3 = 3
    AND_4 = 4
    AND_5 = 5
    AND_6 = 6
    AND_7 = 7
    AND_8 = 8
    AND_9 = 9
    AND_10 = 10
    AND_11 = 11
    AND_12 = 12
    AND_13 = 13
    AND_14 = 14
    AND_15 = 15


class DamageType(IntEnum):
    Unspecified = 0
    Fire = 1
    Magic = 2
    Lightning = 3
    Blunt = 4
    Slash = 5
    Thrust = 6
    NoType = 7
    AllPhysical = 8


class DeleteOrAdd(IntEnum):
    Delete = 0
    Add = 1


class DialogResult(IntEnum):
    Cancel = 0
    Left = 1
    Right = 2
    Leave = 3


class DisplayState(IntEnum):
    Hide = 0
    Display = 1


class DoorState(IntEnum):
    DoorClosed = 0
    DoorOpen = 1
    DoorClosing = 2
    DoorOpening = 3


class Gender(IntEnum):
    Female = 0
    Male = 1


class Label(IntEnum):
    L0 = 0
    L1 = 1
    L2 = 2
    L3 = 3
    L4 = 4
    L5 = 5
    L6 = 6
    L7 = 7
    L8 = 8
    L9 = 9


class MultiplayerState(IntEnum):
    Host = 0
    Client = 1
    Multiplayer = 2
    ConnectingMultiplayer = 3
    Singleplayer = 4


class NPCPartType(IntEnum):
    """Used to define different behavior for different parts of NPC models."""

    Part1 = 1
    Part2 = 2
    Part3 = 3
    Part4 = 4
    Part5 = 5
    Part6 = 6
    Part7 = 7
    Part8 = 8
    Part9 = 9
    Part10 = 10
    Part11 = 11
    Part12 = 12
    Part13 = 13
    Part14 = 14
    Part15 = 15
    Part16 = 16
    Part17 = 17
    Part18 = 18
    Part19 = 19
    Part20 = 20
    Part21 = 21
    Part22 = 22
    Part23 = 23
    Part24 = 24
    Part25 = 25
    Part26 = 26
    Part27 = 27
    Part28 = 28
    Part29 = 29
    Part30 = 30
    WeakPoint = 31


class PlayGoState(IntEnum):
    DownloadedFirstChunk = 0
    BDInstalling = 1
    Installed = 2


class PlayLogMultiplayerType(IntEnum):
    HostOnly = 0
    GuestOnly = 1
    BothHostAndGuest = 2


class PlayerPlayLogParameter(IntEnum):
    PrimaryParameters = 0
    TemporaryParameters = 1
    Weapon = 2
    Armor = 3


class SingleplayerSummonSignType(IntEnum):
    NormalCoop = 0
    ScriptedInvasion = 1
    ScriptedInvasionWideArea = 2


class TeamType(IntEnum):
    # Types -1 to 15 are base in DS1 and BB, at least.
    Default = -1
    NoTeam = 0
    Human = 1
    WhitePhantom = 2
    BlackPhantom = 3
    Hollow = 4
    Vagrant = 5
    Enemy = 6
    Boss = 7
    Ally = 8  # Targets no one, targeted by Enemy/Boss. (Not sure about HostileAlly.)
    HostileAlly = 9  # Targets and targeted by everyone.
    Decoy = 10
    RedChild = 11
    FightingAlly = 12  # Targets Enemy/Boss, targeted by Enemy/Boss.
    Intruder = 13  # Targets and targeted by Human/WhitePhantom/Hollow
    Neutral = 14
    Charm = 15

    # Types 19+ are BB only (maybe DS3).
    Host = 19
    Coop = 20
    Hostile = 21
    WanderingPhantom = 22
    Enemy1 = 23
    Enemy2 = 24
    StrongEnemy1 = 25  # Probably boss.
    FriendlyNPC = 26
    HostileNPC = 27
    CoopNPC = 28
    Indiscriminate = 29
    Object = 30
