"""
linked:
0

strings:
0: N:\\FDP\\data\\Param\\event\\common_func.events
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.events.darksouls3 import *


@NeverRestart
def Constructor():
    """ 0: Event 0 """
    GotoIfHollowArenaMatchType(Label.L0, match_type=HollowArenaMatchType.Duel)
    GotoIfHollowArenaMatchType(Label.L1, match_type=HollowArenaMatchType.TwoPlayerBrawl)
    GotoIfHollowArenaMatchType(Label.L2, match_type=HollowArenaMatchType.FourPlayerBrawl)
    GotoIfHollowArenaMatchType(Label.L3, match_type=HollowArenaMatchType.SixPlayerBrawl)
    GotoIfHollowArenaMatchType(Label.L4, match_type=HollowArenaMatchType.TwoVsTwo)
    GotoIfHollowArenaMatchType(Label.L5, match_type=HollowArenaMatchType.ThreeVsThree)
    Label(0)
    RunCommonEvent(20005920, args=(0, 14605300, 10020000, 10020010))
    RunCommonEvent(20005930, args=(14605300,))
    RunCommonEvent(20005941, args=(14605300,))
    End()
    Label(1)
    RunCommonEvent(20005920, args=(1, 14605300, 10020001, 10020011))
    Goto(Label.L9)
    Label(2)
    RunCommonEvent(20005920, args=(2, 14605300, 10020002, 10020012))
    Goto(Label.L9)
    Label(3)
    RunCommonEvent(20005920, args=(3, 14605300, 10020003, 10020013))
    Goto(Label.L9)
    Label(4)
    RunCommonEvent(20005920, args=(4, 14605300, 10020004, 10020014))
    Goto(Label.L9)
    Label(5)
    RunCommonEvent(20005920, args=(5, 14605300, 10020005, 10020015))
    Goto(Label.L9)
    Label(9)
    RunCommonEvent(20005940, args=(14605300,))


@NeverRestart
def Event14605200(ARG_0_3: float, ARG_4_7: float, ARG_8_11: float):
    """ 14605200: Event 14605200 """
    IfPlayerInOwnWorld(1)
    IfHollowArenaMatchReadyState(1, is_ready=True)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    Wait(ARG_0_3)
    IfPlayerInOwnWorld(0)
    SkipLinesIfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    Wait(ARG_4_7)
    IfPlayerInOwnWorld(0)
    Wait(ARG_8_11)
    BanishPhantomsAndUpdateServerPvPStats(unknown=0)
