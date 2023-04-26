"""
Northeast Caelid (NW) (SW)

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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .enums.m60_52_42_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1052420000, asset=Assets.AEG099_060_9000)
