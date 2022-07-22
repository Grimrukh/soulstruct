"""
Northwest Mountaintops (SW) (SW)

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
from .entities.m60_48_56_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005220(
        0,
        character=Characters.KaidenSellsword,
        animation_id=30004,
        animation_id_1=20004,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=1,
    )
    Event_1048562350(2, character__region=1048560352, character=Characters.BigWolf0)
    Event_1048562350(5, character__region=1048560355, character=Characters.BigWolf1)
    CommonFunc_90005790(
        0,
        right=0,
        flag=1048560180,
        summon_flag=1048562181,
        dismissal_flag=1048562182,
        character=Characters.AnastasiaTarnishedEater,
        sign_type=22,
        region=1048562180,
        region_1=1048562181,
        seconds=0.0,
        right_1=0,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(
        0,
        flag=1048560180,
        flag_1=1048562181,
        flag_2=1048562182,
        character=Characters.AnastasiaTarnishedEater,
    )
    CommonFunc_90005792(
        0,
        flag=1048560180,
        flag_1=1048562181,
        flag_2=1048562182,
        character=Characters.AnastasiaTarnishedEater,
        item_lot_param_id=1048560800,
        seconds=0.0,
    )
    CommonFunc_90005793(0, 1048560180, 1048562181, 1048562182, 1048560700, 1048562180, 1048562182, 0)


@RestartOnRest(1048562350)
def Event_1048562350(_, character__region: uint, character: uint):
    """Event 1048562350"""
    if ThisEventSlotFlagDisabled():
        SetCharacterEventTarget(character, region=character__region)
    AND_1.Add(CharacterHasSpecialEffect(character, 11893))
    AND_1.Add(CharacterAlive(character__region))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(character__region, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        character,
        destination=character__region,
        destination_type=CoordEntityType.Character,
        model_point=283,
        set_draw_parent=0,
    )
    WaitFrames(frames=1)
    ForceAnimation(character, 20003)
    AddSpecialEffect(character__region, 11880)
    AddSpecialEffect(character, 11880)
    ReplanAI(character__region)
    Wait(5.0)
    SetNetworkUpdateRate(character__region, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Restart()


@ContinueOnRest(100)
def Event_100():
    """Event 100"""
    CommonFunc_90005300(0, 1148560200, 1148560200, 40524, 0.0, 0)
