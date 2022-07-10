"""
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


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 90005300, args=(1033410350, 1033410350, 1033410400, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1033410351, 1033410351, 1033410410, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1033410340, 1033410340, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005920, args=(1033410600, 1033411600, 1033413600), arg_types="III")
    RunCommonEvent(0, 90005920, args=(1033410601, 1033411601, 1033413601), arg_types="III")
    RunCommonEvent(0, 90005920, args=(1033410602, 1033411602, 1033413602), arg_types="III")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(
        0,
        90005211,
        args=(1033410340, 30001, 20001, 1033412340, 20.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005201, args=(1033410350, 30000, 20000, 17.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1033410350, 17.0, 0.0, -1), arg_types="Iffi")
