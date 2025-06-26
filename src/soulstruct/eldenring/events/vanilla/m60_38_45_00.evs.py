"""
East Liurnia (SE) (NW)

linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *
from .enums.m60_38_45_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1038450000, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=1038450001, asset=Assets.AEG099_060_9001)
    CommonFunc_90005632(0, flag=580010, asset=Assets.AEG099_385_2000, item_lot=80010)
    CommonFunc_90005570(0, flag=60824, gesture_param_id=54, asset=Assets.AEG099_990_9000, left=2, left_1=1, right=0)
