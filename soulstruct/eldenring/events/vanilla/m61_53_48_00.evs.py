"""
Land of Shadow 13-12 SW SE

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
    CommonFunc_90005200(
        0,
        character=2053480290,
        animation_id=30005,
        animation_id_1=20005,
        region=2053482290,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005570(0, flag=60861, gesture_param_id=112, asset=2053481699, left=0, left_1=1, right=0)
