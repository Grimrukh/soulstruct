from __future__ import annotations

__all__ = [
    # Basic enums
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
    "ALL_PLAYERS",
    "ALL_SPIRIT_SUMMONS",
    "TORRENT",
    "AIStatusType",
    "ArenaMatchType",
    "ArenaResult",
    "BitOperation",
    "BossMusicState",
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
    "NavmeshFlag",
    "NumberButtons",
    "OnOffChange",
    "OnRestBehavior",
    "SoundType",
    "StatueType",
    "SummonSignType",
    "TriggerAttribute",
    "UpdateAuthority",
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
    "SingleplayerSummonSignType",
    "TeamType",
    "Weather",
]

from enum import IntEnum

from soulstruct.base.events.enums import *


ALL_PLAYERS = 20000  # I strongly suspect
ALL_SPIRIT_SUMMONS = 35000
TORRENT = 40000


class AIStatusType(BaseEMEVDEnum):
    Normal = 0
    Caution = 1
    Search = 2
    Battle = 3
    Unknown4 = 4
    Unknown5 = 5
    Unknown6 = 6


class ArenaMatchType(BaseEMEVDEnum):
    Duel = 0
    TwoPlayerBrawl = 1
    FourPlayerBrawl = 2
    SixPlayerBrawl = 3
    OneVersusOne = 4
    TwoVersusTwo = 5
    ThreeVersusThree = 6


class ArenaResult(BaseEMEVDEnum):
    Win = 0
    Draw = 1


class BitOperation(BaseEMEVDEnum):
    Add = 0
    Delete = 1
    Invert = 2


class BossMusicState(BaseEMEVDEnum):
    NormalFadeOut = -2
    LongFadeOut = -1
    Start = 0
    HeatUp = 1
    Unknown = 2  # added in DLC


class ButtonType(BaseEMEVDEnum):
    Yes_or_No = 0
    OK_or_Cancel = 1


class CharacterType(BaseEMEVDEnum):
    Alive = 0
    WhitePhantom = 1
    BlackPhantom = 2
    Unknown3 = 3
    Unknown4 = 4
    Unknown5 = 5
    Unknown6 = 6
    Unknown7 = 7
    GrayPhantom = 8
    Invader = 15
    Invader2 = 16
    BluePhantom = 17
    Invader3 = 18


class CharacterUpdateRate(BaseEMEVDEnum):
    Never = -1
    Always = 0
    EveryTwoFrames = 2
    EveryFiveFrames = 5
    AtLeastEveryTwoFrames = 102
    AtLeastEveryFiveFrames = 105


class ClassType(BaseEMEVDEnum):
    Vagabond = 0
    Warrior = 1
    Hero = 2
    Bandit = 3
    Astrologer = 4
    Prophet = 5
    Confessor = 6
    Samurai = 7
    Prisoner = 8
    Wretch = 9


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
    # TODO: These could have been introduced in Sekiro?
    Unknown16 = 0b0001_0000  # 16
    Unknown32 = 0b0010_0000  # 32
    IsEndingCutscene = 0b0100_0000  # 64


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
    Talisman = 2  # 'Accessory'
    Good = 3
    AshOfWar = 4  # 'Gem'


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
    Asset = 0
    Region = 1
    Character = 2


class NavmeshFlag(BaseEMEVDEnum):
    """Only `Default` and `Disable` appear in EMEVD, since Havok manages navmeshes now (no NVM format)."""
    Default = 0  # no special flags
    Disable = 1  # ignored completely during pathfinding


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
    WhiteSign = 0
    BlackSign = 1
    RedSign = 2
    NPCWhiteSign = 20


class SoundType(BaseEMEVDEnum):
    # The initial letter is prefixed to the sound ID to find the sound file in the FEV.
    # TODO: Used outside EMEVD in MSB, so should be removed from here.
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
    unk_GeometrySet = 14


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


class UpdateAuthority(BaseEMEVDEnum):

    @classmethod
    def get_event_arg_fmt(cls):
        return "i"

    Normal = 0
    Forced = 8192


class ArmorType(BaseEMEVDEnum):
    Head = 0
    Body = 1
    Arms = 2
    Legs = 3


class BannerType(BaseEMEVDEnum):
    YouDied = 2
    HostVanquished = 5
    BloodyFingerVanquished = 7
    LostGraceDiscovered = 13
    Unknown14 = 14
    LegendFelled = 15
    DemigodFelled = 16
    GreatEnemyFelled = 17
    EnemyFelled = 18
    DutyFulfilled = 20
    MapFound = 22
    GreatRuneRestored = 26
    GodSlain = 27
    DuelistVanquished = 28
    RecusantVanquished = 29
    InvaderVanquished = 30
    Commence = 31
    Stalemate = 32
    Victory = 33
    Defeat = 34


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
    Male = 0
    Female = 1


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
    L10 = 10
    L11 = 11
    L12 = 12
    L13 = 13
    L14 = 14
    L15 = 15
    L16 = 16
    L17 = 17
    L18 = 18
    L19 = 19
    L20 = 20


class MultiplayerState(IntEnum):
    Host = 0
    Client = 1
    Multiplayer = 2
    MultiplayerPending = 3
    Singleplayer = 4
    Invasion = 5
    InvasionPending = 6


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

    # Types 19+ are BB and DS3.
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

    # Types 31+ are DS3 only.
    WhiteBerserker = 31
    RedBerserker = 32
    ArchEnemyTeam = 33

    # Types 34+ are ER only.
    Unknown67 = 70
    Unknown70 = 70


class Weather(IntEnum):
    Null = -1
    Default = 0
    Rain = 1
    Snow = 2
    WindyRain = 3
    Fog = 4
    Cloudless = 5
    FlatClouds = 6
    PuffyClouds = 7
    RainyClouds = 8
    WindyFog = 9
    HeavySnow = 10
    HeavyFog = 11
    WindyPuffyClouds = 12
    Default2 = 13
    Default3 = 14
    RainyHeavyFog = 15
    SnowyHeavyFog = 16
    ScatteredRain = 17
    Unknown18 = 18
    Unknown19 = 19
    Unknown20 = 20
    Unknown21 = 21
    Unknown22 = 22
    Unknown23 = 23
