"""
Land of Shadow 12-11 NE NE

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
    RegisterGrace(grace_flag=2051470000, asset=2051471950)
    CommonFunc_90005638(0, flag=2051470600, asset=2051471600, asset_1=2051471601)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005200(
        0,
        character=2051470200,
        animation_id=30003,
        animation_id_1=20003,
        region=2051472200,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
