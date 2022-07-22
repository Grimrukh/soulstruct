"""
Arena (Round Plaza)

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.darksouls3.events import *
from soulstruct.darksouls3.events.instructions import *


@ContinueOnRest(0)
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
    CommonFunc_20005920(0, match_type=0, flag=15405300, message=10020000, message_1=10020010)
    CommonFunc_20005930(0, flag=15405300)
    CommonFunc_20005941(0, flag=15405300)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    CommonFunc_20005920(0, match_type=1, flag=15405300, message=10020001, message_1=10020011)
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    CommonFunc_20005920(0, match_type=2, flag=15405300, message=10020002, message_1=10020012)
    Goto(Label.L9)

    # --- Label 3 --- #
    DefineLabel(3)
    CommonFunc_20005920(0, match_type=3, flag=15405300, message=10020003, message_1=10020013)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    CommonFunc_20005920(0, match_type=4, flag=15405300, message=10020004, message_1=10020014)
    Goto(Label.L9)

    # --- Label 5 --- #
    DefineLabel(5)
    CommonFunc_20005920(0, match_type=5, flag=15405300, message=10020005, message_1=10020015)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    CommonFunc_20005940(0, 15405300)
