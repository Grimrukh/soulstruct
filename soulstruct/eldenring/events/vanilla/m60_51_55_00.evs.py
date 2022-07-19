"""
Southwest Mountaintops (NE) (NE)

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


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005300(0, 1051550300, 1051550300, 0, 0.0, 0)


@NeverRestart(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005485(0, 1051550300)
