"""
Land of Shadow 12-09 NW NW

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
    RegisterGrace(grace_flag=2048390000, asset=2048391950)
    RegisterGrace(grace_flag=2048390001, asset=2048391951)
    CommonFunc_90005211(
        0,
        character=2048390200,
        animation_id=30014,
        animation_id_1=20014,
        region=0,
        radius=18.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390201,
        animation_id=30014,
        animation_id_1=20014,
        region=0,
        radius=18.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390202,
        animation_id=30014,
        animation_id_1=20014,
        region=0,
        radius=18.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390203,
        animation_id=30014,
        animation_id_1=20014,
        region=0,
        radius=18.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390204,
        animation_id=30016,
        animation_id_1=20016,
        region=0,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390205,
        animation_id=30016,
        animation_id_1=20016,
        region=0,
        radius=15.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390206,
        animation_id=30016,
        animation_id_1=20016,
        region=0,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390207,
        animation_id=30016,
        animation_id_1=20016,
        region=0,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390208,
        animation_id=30016,
        animation_id_1=20016,
        region=0,
        radius=15.0,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390209,
        animation_id=30016,
        animation_id_1=20016,
        region=0,
        radius=15.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390210,
        animation_id=30016,
        animation_id_1=20016,
        region=0,
        radius=15.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390216,
        animation_id=30014,
        animation_id_1=20014,
        region=0,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390218,
        animation_id=30014,
        animation_id_1=20014,
        region=0,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390219,
        animation_id=30014,
        animation_id_1=20014,
        region=0,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390220,
        animation_id=30019,
        animation_id_1=20019,
        region=0,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048390221,
        animation_id=30019,
        animation_id_1=20019,
        region=0,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=2048390300, region=2048392300, seconds=0.30000001192092896, animation_id=-1)
    CommonFunc_90005250(0, character=2048390301, region=2048392300, seconds=0.10000000149011612, animation_id=-1)
    CommonFunc_90005250(0, character=2048390303, region=2048392300, seconds=0.699999988079071, animation_id=-1)
    CommonFunc_90005250(0, character=2048390305, region=2048392300, seconds=0.800000011920929, animation_id=-1)
    CommonFunc_90005250(0, character=2048390306, region=2048392300, seconds=0.4000000059604645, animation_id=-1)
    CommonFunc_90005250(0, character=2048390307, region=2048392300, seconds=0.0, animation_id=-1)
    Event_2048390700()


@RestartOnRest(2048390700)
def Event_2048390700():
    """Event 2048390700"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    DisableFlag(2051459751)
    if FlagEnabled(2048380850):
        return
    AND_1.Add(FlagDisabled(2051459708))
    AND_1.Add(FlagDisabled(2051459719))
    AND_1.Add(FlagDisabled(2051459720))
    if AND_1:
        return
    OR_1.Add(FlagEnabled(25000800))
    if OR_1:
        return
    EnableFlag(2051459751)
    OR_10.Add(FlagEnabled(2048380850))
    OR_10.Add(FlagEnabled(25000800))
    
    MAIN.Await(OR_10)
    
    DisableFlag(2051459751)
