"""
linked:
0

strings:
0: N:\\FDP\\data\\Param\\event\\common_func.emevd
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.darksouls3.events import *
from soulstruct.darksouls3.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    GotoIfHollowArenaMatchType(Label.L0, match_type=HollowArenaMatchType.Duel)
    GotoIfHollowArenaMatchType(Label.L1, match_type=HollowArenaMatchType.TwoPlayerBrawl)
    GotoIfHollowArenaMatchType(Label.L2, match_type=HollowArenaMatchType.FourPlayerBrawl)
    GotoIfHollowArenaMatchType(Label.L3, match_type=HollowArenaMatchType.SixPlayerBrawl)
    GotoIfHollowArenaMatchType(Label.L4, match_type=HollowArenaMatchType.TwoVsTwo)
    GotoIfHollowArenaMatchType(Label.L5, match_type=HollowArenaMatchType.ThreeVsThree)

    # --- Label 0 --- #
    DefineLabel(0)
    RunCommonEvent(20005920, args=(0, 14705300, 10020000, 10020010), arg_types="Biii")
    RunCommonEvent(20005930, args=(14705300,))
    RunCommonEvent(20005941, args=(14705300,))
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    RunCommonEvent(20005920, args=(1, 14705300, 10020001, 10020011), arg_types="Biii")
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    RunCommonEvent(20005920, args=(2, 14705300, 10020002, 10020012), arg_types="Biii")
    Goto(Label.L9)

    # --- Label 3 --- #
    DefineLabel(3)
    RunCommonEvent(20005920, args=(3, 14705300, 10020003, 10020013), arg_types="Biii")
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    RunCommonEvent(20005920, args=(4, 14705300, 10020004, 10020014), arg_types="Biii")
    Goto(Label.L9)

    # --- Label 5 --- #
    DefineLabel(5)
    RunCommonEvent(20005920, args=(5, 14705300, 10020005, 10020015), arg_types="Biii")
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    RunCommonEvent(20005940, args=(14705300,))
