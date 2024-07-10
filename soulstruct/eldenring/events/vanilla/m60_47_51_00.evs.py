"""
Southeast Altus Plateau (NE) (NE)

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
from .enums.m60_47_51_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1047510000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76510,
        flag_1=76500,
        asset=Assets.AEG099_090_9000,
        source_flag=77500,
        value=0,
        flag_2=78500,
        flag_3=78501,
        flag_4=78502,
        flag_5=78503,
        flag_6=78504,
        flag_7=78505,
        flag_8=78506,
        flag_9=78507,
        flag_10=78508,
        flag_11=78509,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, dummy_id=100, vfx_id=800, right=0)
