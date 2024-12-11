"""
Land of Shadow 13-11 NE NW

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
    CommonFunc_90005221(0, character=2054470209, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005201(
        0,
        character=2054470210,
        animation_id=30002,
        animation_id_1=20002,
        radius=25.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2054470211,
        animation_id=30002,
        animation_id_1=20002,
        radius=25.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
