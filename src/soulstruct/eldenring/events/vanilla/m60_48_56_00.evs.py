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
from soulstruct.eldenring.game_types import *
from .enums.m60_48_56_00_enums import *


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
    Event_1048562350(2, character=Characters.AlbinauricArcher0, character_1=Characters.BigWolf0)
    Event_1048562350(5, character=Characters.AlbinauricArcher2, character_1=Characters.BigWolf1)
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
        item_lot=1048560800,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=1048560180,
        flag_1=1048562181,
        flag_2=1048562182,
        character=Characters.AnastasiaTarnishedEater,
        other_entity=1048562180,
        region=1048562182,
        left=0,
    )


@RestartOnRest(1048562350)
def Event_1048562350(_, character: uint, character_1: uint):
    """Event 1048562350"""
    if ThisEventSlotFlagDisabled():
        SetCharacterEventTarget(character_1, entity=character)
    AND_1.Add(CharacterHasSpecialEffect(character_1, 11893))
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterAlive(character_1))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=283,
        set_draw_parent=0,
    )
    WaitFrames(frames=1)
    ForceAnimation(character_1, 20003)
    AddSpecialEffect(character, 11880)
    AddSpecialEffect(character_1, 11880)
    ReplanAI(character)
    Wait(5.0)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(character_1, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Restart()


@ContinueOnRest(100)
def Event_100():
    """Event 100"""
    CommonFunc_90005300(0, flag=1148560200, character=Characters.Scarab, item_lot=40524, seconds=0.0, left=0)
