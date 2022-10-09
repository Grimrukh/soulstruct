"""
North Altus Plateau (SE) (SW)

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
from .entities.m60_42_52_00_entities import *


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005201(
        0,
        character=Characters.Bat,
        animation_id=30000,
        animation_id_1=20000,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
