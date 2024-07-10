"""
Southwest Liurnia (SW) (NE)

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
from .enums.m60_33_41_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005300(
        0,
        flag=1033410350,
        character=Characters.GlintstoneDragon0,
        item_lot=1033410400,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005300(
        0,
        flag=1033410351,
        character=Characters.GlintstoneDragon1,
        item_lot=1033410410,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005300(0, flag=1033410340, character=Characters.RedWolf, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005920(0, flag=1033410600, asset=1033411600, obj_act_id=1033413600)
    CommonFunc_90005920(0, flag=1033410601, asset=1033411601, obj_act_id=1033413601)
    CommonFunc_90005920(0, flag=1033410602, asset=1033411602, obj_act_id=1033413602)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005211(
        0,
        character=Characters.RedWolf,
        animation_id=30001,
        animation_id_1=20001,
        region=1033412340,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.GlintstoneDragon0,
        animation_id=30000,
        animation_id_1=20000,
        radius=17.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.GlintstoneDragon0, radius=17.0, seconds=0.0, animation_id=-1)
