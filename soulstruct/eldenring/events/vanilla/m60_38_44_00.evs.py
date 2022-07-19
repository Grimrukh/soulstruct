"""
East Liurnia (SE) (SW)

linked:
0
82
166

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: N:\\GR\\data\\Param\\event\\m60.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_38_44_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005261(
        0,
        character=Characters.WolfPackLeader,
        region=1038442200,
        radius=20.0,
        seconds=0.0,
        animation_id=3011,
    )
    CommonFunc_90005261(0, 1038440210, 1038442210, 15.0, 1.0, -1)
    CommonFunc_90005261(0, 1038440211, 1038442210, 15.0, 0.0, -1)
    CommonFunc_90005211(
        0,
        character=Characters.Albinauric0,
        animation_id=30002,
        animation_id_1=20002,
        region=1038442210,
        radius=15.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(0, 1038440211, 30002, 20002, 1038442210, 15.0, 0.0, 0, 0, 0, 0)
