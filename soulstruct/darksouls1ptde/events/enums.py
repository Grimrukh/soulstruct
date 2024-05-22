from __future__ import annotations

__all__ = [
    # Basic enums/types
    "OnRestBehavior",
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
    "CLIENT_PLAYER_6",
    "CLIENT_PLAYER_7",
    "CLIENT_PLAYER_8",
    "CLIENT_PLAYER_9",
    "BaseEMEVDEnum",
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
    "FlagSetting",
    "FlagType",
    "InterpolationState",
    "ItemType",
    "RangeState",
    "CoordEntityType",
    "NavmeshType",
    "NumberButtons",
    "OnOffChange",
    "OnRestBehavior",
    "SoundType",
    "StatueType",
    "SummonSignType",
    "TriggerAttribute",
    "WorldTendencyType",
    "UpdateAuthority",
    "CalculationType",
    "ConditionGroup",
    "Covenant",
    "TeamType",
    "BannerType",
    "MultiplayerState",
    "NPCPartType",
]

from enum import IntEnum

from soulstruct.base.events.enums import *


# Basic obvious booleans are omitted:
# ENUM_ON_OFF, ENUM_CONTAINED, ENUM_OWN_STATE, ENUM_BOOL, ENUM_CONDITION_STATE, ENUM_DEATH_STATUS, ENUM_ENABLE_STATE


class AIStatusType(BaseEMEVDEnum):
    Normal = 0
    Caution = 1
    Search = 2
    Battle = 3


class BitOperation(BaseEMEVDEnum):
    Add = 0
    Delete = 1
    Invert = 2


class ButtonType(BaseEMEVDEnum):
    Yes_or_No = 0
    OK_or_Cancel = 1


class CharacterType(BaseEMEVDEnum):
    Human = 0  # Also called "Survival" in some resources.
    WhitePhantom = 1
    BlackPhantom = 2
    Hollow = 8  # Also called "Gray Ghost" in some resources.
    Intruder = 12


class CharacterUpdateRate(BaseEMEVDEnum):
    Never = -1
    Always = 0
    EveryTwoFrames = 2
    EveryFiveFrames = 5
    Unknown105 = 105  # TODO: Move to `eldenring`


class ClassType(BaseEMEVDEnum):
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


class ComparisonType(BaseNegatableEMEVDEnum):
    Equal = 0
    NotEqual = 1
    GreaterThan = 2
    LessThan = 3
    GreaterThanOrEqual = 4
    LessThanOrEqual = 5

    def negate(self):
        if self == ComparisonType.Equal:
            return ComparisonType.NotEqual
        elif self == ComparisonType.NotEqual:
            return ComparisonType.Equal
        elif self == ComparisonType.GreaterThan:
            return ComparisonType.LessThanOrEqual
        elif self == ComparisonType.LessThan:
            return ComparisonType.GreaterThanOrEqual
        elif self == ComparisonType.GreaterThanOrEqual:
            return ComparisonType.LessThan
        elif self == ComparisonType.LessThanOrEqual:
            return ComparisonType.GreaterThan
        return super().negate()

    def get_operator(self):
        if self == ComparisonType.Equal:
            return "=="
        elif self == ComparisonType.NotEqual:
            return "!="
        elif self == ComparisonType.GreaterThan:
            return ">"
        elif self == ComparisonType.LessThan:
            return "<"
        elif self == ComparisonType.GreaterThanOrEqual:
            return ">="
        elif self == ComparisonType.LessThanOrEqual:
            return "<="


class CutsceneFlags(BaseEMEVDFlags):
    """Bit flags, stored in one byte."""
    Unskippable = 0b0000_0010  # 2
    FadeOut = 0b0000_1000  # 8


class DamageTargetType(BaseEMEVDEnum):
    Character = 1
    Map = 2
    Character_and_Map = 3


class EventReturnType(BaseEMEVDEnum):
    End = 0
    Restart = 1


class FlagSetting(BaseNegatableEMEVDEnum):
    Off = 0
    On = 1
    Change = 2

    def negate(self):
        if self == FlagSetting.Off:
            return FlagSetting.On
        elif self == FlagSetting.On:
            return FlagSetting.Off
        return super().negate()


class FlagType(BaseEMEVDEnum):
    Absolute = 0
    RelativeToThisEvent = 1
    RelativeToThisEventSlot = 2


class InterpolationState(BaseNegatableEMEVDEnum):
    Interpolated = 0
    NotInterpolated = 1

    def negate(self):
        if self == InterpolationState.Interpolated:
            return InterpolationState.NotInterpolated
        elif self == InterpolationState.NotInterpolated:
            return InterpolationState.Interpolated
        return super().negate()


class ItemType(BaseEMEVDEnum):
    Weapon = 0
    Armor = 1
    Ring = 2
    Good = 3


class RangeState(BaseNegatableEMEVDEnum):
    AllOn = 0
    AllOff = 1
    AnyOn = 2  # or "not all off"
    AnyOff = 3  # or "not all on"

    def negate(self):
        if self == RangeState.AllOn:
            return RangeState.AnyOff
        elif self == RangeState.AllOff:
            return RangeState.AnyOn
        elif self == RangeState.AnyOn:
            return RangeState.AllOff
        elif self == RangeState.AnyOff:
            return RangeState.AllOn
        return super().negate()


class CoordEntityType(BaseEMEVDEnum):
    """Originally "Category", which was ambiguous. Used often to identify the type of an MSB part (or region).

    Note that all MSB parts (Map Pieces, Collisions, Navmesh, etc.) technically have `translate` coordinates, but these
    are the big three types/subtypes.
    """
    Object = 0
    Region = 1
    Character = 2


class NavmeshType(BaseEMEVDEnum):
    """Bit flags for Navmesh types.

    NOTE: These EMEVD bit values are in reverse-endian order to the actual NVM triangle flag.
    """
    Default = 0b0000_0000_0000_0000  # no special flags
    Disable = 0b0000_0000_0000_0001  # ignored completely during pathfinding
    Gate = 0b0000_0000_0000_0010  # location of an MCG gate node to connect to another navmesh in the same map
    Obstacle = 0b0000_0000_0000_0100  # will trigger enemies' 'destroy obstacle' animation; can stack with other flags
    Drop = 0b0000_0000_0000_1000  # a drop from one floor section to another; usually extends into air
    Degenerate = 0b0000_0000_0001_0000  # seen on triangles with co-linear vertices and potentially others
    DropAdjacent = 0b0000_0000_0010_0000  # replaces standard floor triangles when they are adjacent to `Drop`
    LandingPoint = 0b0000_0000_0100_0000
    Event = 0b0000_0000_1000_0000
    Edge = 0b0000_0001_0000_0000
    LargeSpace = 0b0000_0010_0000_0000
    Ladder = 0b0000_0100_0000_0000  # used at the bottom and top of ladders (but not on the vertical section itself)
    Hole = 0b0000_1000_0000_0000
    Door = 0b0001_0000_0000_0000
    ClosedDoor = 0b0010_0000_0000_0000
    MapExit = 0b0100_0000_0000_0000  # used to generate dynamic gate nodes to connect to other maps
    InsideWall = 0b1000_0000_0000_0000  # unknown use


class NumberButtons(BaseEMEVDEnum):
    OneButton = 1
    TwoButton = 2
    NoButton = 6


class OnOffChange(BaseNegatableEMEVDEnum):
    On = 0
    Off = 1
    Change = 2

    def negate(self):
        if self == OnOffChange.On:
            return OnOffChange.Off
        elif self == OnOffChange.Off:
            return OnOffChange.On
        return super().negate()


class OnRestBehavior(BaseEMEVDEnum):
    ContinueOnRest = 0
    RestartOnRest = 1
    EndOnRest = 2


class SummonSignType(BaseEMEVDEnum):
    BlueEyeSign = 0  # Used for NPC summons.
    BlackEyeSign = 1  # Used for NPC invasions.
    RedEyeSign = 2
    DetectionSign = 3
    WhiteHelpSign = 4
    BlackHelpSign = 5


class SoundType(BaseEMEVDEnum):
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


class StatueType(BaseEMEVDEnum):
    Stone = 0  # e.g. in the Depths, from Basilisk breath
    Crystal = 1  # e.g. in Crystal Cave, from Seath crystals


class TriggerAttribute(BaseEMEVDFlags):
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


class WorldTendencyType(BaseEMEVDEnum):
    White = 0
    Black = 1


class UpdateAuthority(BaseEMEVDEnum):
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

    def Await(self, condition: bool | int | ConditionGroup):
        """For EVS intellisense. Handled internally.

        Continually evaluate the given condition until it is true, then continue with the next instruction.

        Only permitted for `MAIN`.
        """
        ...

    def Add(self, condition: bool | int | ConditionGroup):
        """For EVS intellisense. Handled internally.

        Add a condition to this condition group for evaluation.
        """
        ...

    # noinspection PyPropertyDefinition
    @property
    def LastResult(self) -> bool:
        """For EVS intellisense. Handled internally.

        Retrieve the result of this condition group from its last evaluation for use in a simple, instantaneous test.
        If the group has never been evaluted, this will be False, except for `MAIN`, which is always True (but you have
        no reason to call this on `MAIN`).
        """
        ...


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


class MultiplayerState(IntEnum):
    Host = 0
    Client = 1
    Multiplayer = 2
    Singleplayer = 3


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
