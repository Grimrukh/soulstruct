__all__ = [
    # Basic enums/types
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
    # Enums in Dark Souls 1 (both PTD and DSR) only
    "CalculationType",
    "ConditionGroup",
    "Covenant",
    "TeamType",
    "BannerType",
    "MultiplayerState",
    "NPCPartType",
]

from enum import IntEnum

from soulstruct.base.events.emevd.enums import *


class ProtectedEntities(IntEnum):
    """Hard-coded entity IDs used in EMEVD instructions. Used by decompiler; you can use global names above instead."""
    PLAYER = PLAYER
    CLIENT_PLAYER_1 = 10001
    CLIENT_PLAYER_2 = 10002
    CLIENT_PLAYER_3 = 10003
    CLIENT_PLAYER_4 = 10004
    CLIENT_PLAYER_5 = 10005


# Basic obvious booleans are omitted:
# ENUM_ON_OFF, ENUM_CONTAINED, ENUM_OWN_STATE, ENUM_BOOL, ENUM_CONDITION_STATE, ENUM_DEATH_STATUS, ENUM_ENABLE_STATE


class AIStatusType(IntEnum):
    Normal = 0
    Caution = 1
    Search = 2
    Battle = 3


class BitOperation(IntEnum):
    Add = 0
    Delete = 1
    Invert = 2


class ButtonType(IntEnum):
    Yes_or_No = 0
    OK_or_Cancel = 1


class CharacterType(IntEnum):
    Human = 0  # Also called "Survival" in some resources.
    WhitePhantom = 1
    BlackPhantom = 2
    Hollow = 8  # Also called "Gray Ghost" in some resources.
    Intruder = 12


class CharacterUpdateRate(IntEnum):
    Never = -1
    Always = 0
    EveryTwoFrames = 2
    EveryFiveFrames = 5
    Unknown105 = 105  # TODO: Move to `eldenring`


class ClassType(IntEnum):
    Warrior = 0
    Knight = 1
    Wanderer = 2
    Thief = 3
    Bandit = 4
    Hunter = 5
    Sorcerer = 6
    Pyromancer = 7
    Cleric = 8
    Deprived = 9
    # Prototype classes (unused):
    Temp_Warrior = 20
    Temp_Knight = 21
    Temp_Sorcerer = 22
    Temp_Pyromancer = 23
    Chi_Warrior = 24
    Chi_Knight = 25
    Chi_Sorcerer = 26
    Chi_Pyromancer = 27


class ComparisonType(IntEnum):
    Equal = 0
    NotEqual = 1
    GreaterThan = 2
    LessThan = 3
    GreaterThanOrEqual = 4
    LessThanOrEqual = 5


class CutsceneFlags(IntEnum):
    """Bit flags, stored in one byte."""
    Unskippable = 0b0000_0010  # 2
    FadeOut = 0b0000_1000  # 8
    # TODO: Move these to `eldenring` (or `sekiro` if appropriate)
    Unknown16 = 0b0001_0000  # 16
    Unknown32 = 0b0010_0000  # 32
    Unknown64 = 0b0100_0000  # 64


class DamageTargetType(IntEnum):
    Character = 1
    Map = 2
    Character_and_Map = 3


class EventReturnType(IntEnum):
    End = 0
    Restart = 1


class FlagState(IntEnum):
    Off = 0
    On = 1
    Change = 2


class FlagType(IntEnum):
    Absolute = 0
    RelativeToThisEvent = 1
    RelativeToThisEventSlot = 2


class InterpolationState(IntEnum):
    Interpolated = 0
    NotInterpolated = 1


class ItemType(IntEnum):
    Weapon = 0
    Armor = 1
    Ring = 2
    Good = 3


class RangeState(IntEnum):
    AllOn = 0
    AllOff = 1
    AnyOn = 2  # or "not all off"
    AnyOff = 3  # or "not all on"


class CoordEntityType(IntEnum):
    """Originally "Category", which was ambiguous. Used often to identify the type of an MSB part (or region).

    Note that all MSB parts (Map Pieces, Collisions, Navmesh, etc.) technically have `translate` coordinates, but these
    are the big three types/subtypes.
    """
    Object = 0
    Region = 1
    Character = 2


class NavmeshType(IntEnum):
    """Bit flags for Navmesh types."""

    Solid = 0b00000000000001
    Exit = 0b00000000000010
    Obstacle = 0b00000000000100
    Wall = 0b00000000001000
    # Note enum 16 (fifth bit) is missing.
    WallTouchingFloor = 0b00000000100000
    LandingPoint = 0b00000001000000
    Event = 0b00000010000000
    Cliff = 0b00000100000000
    WideSpace = 0b00001000000000
    Ladder = 0b00010000000000
    Hole = 0b00100000000000
    Door = 0b01000000000000
    ClosedDoor = 0b10000000000000


class NumberButtons(IntEnum):
    OneButton = 1
    TwoButton = 2
    NoButton = 6


class OnOffChange(IntEnum):
    On = 0
    Off = 1
    Change = 2


class RestartType(IntEnum):
    NeverRestart = 0
    RestartOnRest = 1
    UnknownRestart = 2


class SummonSignType(IntEnum):
    BlueEyeSign = 0  # Used for NPC summons.
    BlackEyeSign = 1  # Used for NPC invasions.
    RedEyeSign = 2
    DetectionSign = 3
    WhiteHelpSign = 4
    BlackHelpSign = 5


class SoundType(IntEnum):
    # The initial letter is prefixed to the sound ID to find the sound file in the FEV.
    a_Ambient = 0
    c_CharacterMotion = 1
    f_MenuEffect = 2
    o_Object = 3
    p_Cutscene = 4  # the 'p' stands for 'poly play' or 'poly-scn'.
    s_SFX = 5
    m_Music = 6
    v_Voice = 7
    x_FloorMaterialDependent = 8
    b_ArmorMaterialDependent = 9
    g_Ghost = 10


class StatueType(IntEnum):
    Stone = 0  # e.g. in the Depths, from Basilisk breath
    Crystal = 1  # e.g. in Crystal Cave, from Seath crystals


class TriggerAttribute(IntEnum):
    """Bit flags that determine which categories of player are able to use a given action button trigger.

    If you want multiple player types to be able to use it, simply add those enums together. The vanilla events almost
    always use Human + Hollow (48), for which I have provided a shortcut enum name, or All (255).

    Fairly confident that these are base by all games, but not completely confirmed.
    """

    Session = 0b00000001
    NoSession = 0b00000010
    Host = 0b00000100
    Client = 0b00001000
    Human = 0b00010000  # "Live"
    Hollow = 0b00100000  # "Gray"
    WhitePhantom = 0b01000000
    BlackPhantom = 0b10000000
    All = 0b11111111

    Human_or_Hollow = Human + Hollow  # Shortcut


class WorldTendencyType(IntEnum):
    White = 0
    Black = 1


class UpdateAuthority(IntEnum):
    Normal = 0
    Forced = 4095


# EXTRA ENUMS (unused in EMEVD)

LOCAL_PLAYER = 10000
NET_PLAYER = 10001


class MessageCategory(IntEnum):
    Sample = 0
    Talk = 1
    Soapstone = 2
    Item = 10
    Weapon = 11
    Armor = 12
    Ring = 13
    GoodExp = 14
    WeaponExp = 15
    ArmorExp = 16
    RingExp = 17
    Event = 30
    Dialog = 78  # Not sure how this differs from 'Talk'.


class InfoMenuType(IntEnum):
    List = 0
    Simple = 1


class TalkAttribute(IntEnum):
    """Bit flags with unknown purpose. Doc in Demon's Souls suggests they are "conversation setting relation" flags."""

    Repeat = 0b00000001
    Pad = 0b00000010
    Draw = 0b00000100
    Voice = 0b00001000
    # Fifth through eighth flags are unused/unknown.
    All = 0b11111111


class PlayerDeathType(IntEnum):
    """Type of player death. Originally called "DEATH_STATE". Original value names:

    DEATH_STATE_Normal = 0
    DEATH_STATE_MagicResurrection = 1
    DEATH_STATE_RingNormalResurrection = 2
    DEATH_STATE_RingCurseResurrection = 3
    """

    Normal = 0
    MagicRevival = 1  # from unused 'Escape Death' miracle
    RingRevival = 2
    RareRingRevival = 3


class SummonParamType(IntEnum):
    NoType = 0
    White = -1
    Black = -2
    ForceJoinBlack = -3  # Fixed typo in original ("FroceJoinBlack")
    DetectBlack = -4
    InvadeNito = -7  # Gravelord Servant
    Dragonewt = -10  # Path of the Dragon
    InvadeBounty = -11  # Darkmoon Blades
    Coliseum = -12


class InvadeType(IntEnum):
    NoType = 0
    NormalWhite = 1
    NormalBlack = 2
    ForceJoinBlack = 3
    DetectBlack = 4
    WhiteRescue = 5  # Unused covenant?
    BlackRescue = 6  # Unused covenant?
    Nito = 7
    ThievesGuilds = 8  # Unused covenant?
    OtoutoUmbasa = 9  # Unused covenant?
    Dragonewt = 10
    InvadeBounty = 11
    ColiseumOneB = 12  # 1v1
    ColiseumTwoA2 = 13  # 2v2
    ColiseumTwoB1 = 14
    ColiseumTwoB2 = 15
    ColiseumBrB = 16  # Battle Royale
    ColiseumBrC = 17
    ColiseumBrD = 18


class CalculationType(IntEnum):
    Add = 0
    Subtract = 1
    Multiply = 2
    Divide = 3
    Modulus = 4


class ConditionGroup(IntEnum):
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


class Covenant(IntEnum):
    NoCovenant = 0
    WayOfWhite = 1
    PrincessGuard = 2
    WarriorOfSunlight = 3
    Darkwraith = 4
    PathOfTheDragon = 5
    GravelordServant = 6
    ForestHunter = 7
    DarkmoonBlade = 8
    ChaosServant = 9


class TeamType(IntEnum):
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
    RedChild = 11  # Seems identical to Enemy.
    FightingAlly = 12  # Targets Enemy/Boss, targeted by Enemy/Boss.
    Intruder = 13  # Targets and targeted by Human/WhitePhantom/Hollow
    Neutral = 14
    Charm = 15  # Seems to target and hurt everyone, but can't be locked onto, and keeps attacking dead (Charm) enemies.


class BannerType(IntEnum):
    VictoryAchieved = 1
    YouDied = 2
    HumanityRestored = 3
    SoulsRetrieved = 4
    TargetDestroyed = 5
    YouDiedPhantom = 6  # Phantom version of "YOU DIED"
    BlackPhantomDestroyed = 7
    AreaName = 8  # Name determined by current floor collision.
    MagicRevival = 9
    RingRevival = 10
    RareRingRevival = 11
    Congratulations = 12  # Bugged texture.
    BonfireLit = 13
    YouWin = 15
    YouLose = 16
    Draw = 17
    BeginMatch = 18  # REMASTERED ONLY.


class MultiplayerState(IntEnum):
    Host = 0
    Client = 1
    Multiplayer = 2
    Singleplayer = 3
    UnknownPlayerType4 = 4  # REMASTERED ONLY.
    UnknownPlayerType5 = 5  # REMASTERED ONLY.


class NPCPartType(IntEnum):
    """Used in definining different behavior for parts of NPC models, e.g. tails that can be cut or Smough's invincible
    hammer."""
    Part1 = 1
    Part2 = 2
    Part3 = 3
    Part4 = 4
    Part5 = 5
    Part6 = 6
    WeakPoint = 7
    Part7 = 8
    Part8 = 9
