"""
North Altus Plateau (SE) (SW)

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


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005201(0, 1042520303, 30000, 20000, 15.0, 0.0, 0, 0, 0, 0)
