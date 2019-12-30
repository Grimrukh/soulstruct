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
from soulstruct.events.darksouls3 import *


def Constructor():
    """ 0: Event 0 """
    GotoIfHollowArenaMatchType(Label.L0, match_type=HollowArenaMatchType.Duel)
    GotoIfHollowArenaMatchType(Label.L1, match_type=HollowArenaMatchType.TwoPlayerBrawl)
    GotoIfHollowArenaMatchType(Label.L2, match_type=HollowArenaMatchType.FourPlayerBrawl)
    GotoIfHollowArenaMatchType(Label.L3, match_type=HollowArenaMatchType.SixPlayerBrawl)
    GotoIfHollowArenaMatchType(Label.L4, match_type=HollowArenaMatchType.TwoVsTwo)
    GotoIfHollowArenaMatchType(Label.L5, match_type=HollowArenaMatchType.ThreeVsThree)

    # --- 0 --- #
    DefineLabel(0)
    RunCommonEvent(20005920, args=(0, 15405300, 10020000, 10020010))
    RunCommonEvent(20005930, args=(15405300,))
    RunCommonEvent(20005941, args=(15405300,))
    End()

    # --- 1 --- #
    DefineLabel(1)
    RunCommonEvent(20005920, args=(1, 15405300, 10020001, 10020011))
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    RunCommonEvent(20005920, args=(2, 15405300, 10020002, 10020012))
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    RunCommonEvent(20005920, args=(3, 15405300, 10020003, 10020013))
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    RunCommonEvent(20005920, args=(4, 15405300, 10020004, 10020014))
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    RunCommonEvent(20005920, args=(5, 15405300, 10020005, 10020015))
    Goto(Label.L9)

    # --- 9 --- #
    DefineLabel(9)
    RunCommonEvent(20005940, args=(15405300,))
