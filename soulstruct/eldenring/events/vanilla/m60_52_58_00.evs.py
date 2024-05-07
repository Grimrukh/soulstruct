"""
Northeast Mountaintops (NW) (SW)

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
from .enums.m60_52_58_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton,
        animation_id=30018,
        animation_id_1=20018,
        region=0,
        radius=10.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
