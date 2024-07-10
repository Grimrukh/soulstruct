"""
South Altus Plateau (NE) (SW)

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
from .enums.m60_42_50_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005300(
        0,
        flag=1042500300,
        character=Characters.UlceratedTreeSpirit,
        item_lot=1042500020,
        seconds=0.0,
        left=0,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005201(
        0,
        character=Characters.UlceratedTreeSpirit,
        animation_id=30000,
        animation_id_1=20000,
        radius=30.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellFootSoldier1,
        animation_id=30001,
        animation_id_1=20001,
        radius=30.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=1042500351, radius=100.0, seconds=0.0, animation_id=0)
