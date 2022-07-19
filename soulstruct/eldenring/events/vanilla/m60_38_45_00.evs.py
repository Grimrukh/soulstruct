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
from .entities.m60_38_45_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1038450000, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=1038450001, asset=Assets.AEG099_060_9001)
    CommonFunc_90005632(0, flag=580010, asset=Assets.AEG099_385_2000, item_lot_param_id=80010)
    CommonFunc_90005570(0, 60824, 54, 1038451500, 2, 1, 0)
