"""
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
from .entities.m60_34_51_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=12,
        block_id=1,
        cc_id=0,
        dd_id=0,
        player_start=12012480,
        unk_8_12=0,
        flag=1034512620,
        left_flag=1034512621,
        cancel_flag__right_flag=1034512622,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    CommonFunc_900055278(
        0,
        flag=1034510739,
        asset=Assets.AEG099_251_2000,
        model_point=1506,
        action_button_id=9320,
        text=30051,
        left=0,
        left_1=0,
        left_2=0,
    )
    CommonFunc_90005920(0, flag=1034510600, asset=1034511600, obj_act_id=1034513600)
    Event_1034512580()


@NeverRestart(1034512580)
def Event_1034512580():
    """Event 1034512580"""
    RegisterLadder(start_climbing_flag=1034510580, stop_climbing_flag=1034510581, asset=Assets.AEG110_119_2000)
