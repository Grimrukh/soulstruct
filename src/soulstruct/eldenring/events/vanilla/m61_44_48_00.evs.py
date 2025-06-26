"""
Land of Shadow 11-12 SW SW

linked:
0
82

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: 
168: 
170: 
172: 
174: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005780(
        0,
        flag=2044470800,
        summon_flag=2044482160,
        dismissal_flag=2044482161,
        character=2044480700,
        sign_type=0,
        region=2044482701,
        right=2046429391,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=2044470800, flag_1=2044482160, flag_2=2044482161, character=2044480700)
    CommonFunc_90005785(
        0,
        flag=2044470800,
        flag_1=2044482160,
        flag_2=2044482161,
        character=2044480700,
        other_entity=2044482700,
        region=2044482400,
        radius=0.0,
    )
    Event_2044480700(0, flag=2046429378, flag_1=2046429391, flag_2=4897)
    Event_2044480701(
        0,
        flag=2044482160,
        flag_1=2044482161,
        flag_2=2046422723,
        flag_3=2046429370,
        flag_4=2044470800,
        flag_5=9290,
        flag_6=9291,
    )


@RestartOnRest(2044480700)
def Event_2044480700(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2044480700"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_2))
    SkipLinesIfConditionFalse(2, OR_1)
    DisableFlag(flag_1)
    SkipLines(1)
    EnableFlag(flag_1)
    End()


@RestartOnRest(2044480701)
def Event_2044480701(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
):
    """Event 2044480701"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_4):
        return
    GotoIfFlagDisabled(Label.L0, flag=flag_2)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    OR_1.Add(FlagEnabled(flag_5))
    OR_1.Add(FlagEnabled(flag_6))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    Wait(1.0)
    EnableFlag(flag_2)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(flag_2))
    AND_2.Add(FlagEnabled(flag_4))
    
    MAIN.Await(AND_2)
    
    EnableFlag(flag_3)
    End()
