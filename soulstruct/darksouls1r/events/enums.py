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
from soulstruct.darksouls1ptde.events.enums import *


# DSR extends three enums:


class BannerType(BaseEMEVDEnum):
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


class ConditionGroup(IntEnum):
    # TODO: Check exactly how many slots QLOC added for DSR.
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
    AND_8 = 8  # used by QLOC in new Battle of Stoicism code; unclear how many extra slots have been added

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


class MultiplayerState(BaseEMEVDEnum):
    Host = 0
    Client = 1
    Multiplayer = 2
    Singleplayer = 3
    UnknownPlayerType4 = 4  # REMASTERED ONLY.
    UnknownPlayerType5 = 5  # REMASTERED ONLY.
