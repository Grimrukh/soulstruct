"""
linked:
0
72
154

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\common_macro.emevd
238: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 90005261, args=(1042340210, 1042342210, 15.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1042340211, 1042342210, 5.0, 1.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005460, args=(1042340220,))
    RunCommonEvent(0, 90005461, args=(1042340220,))
    RunCommonEvent(0, 90005462, args=(1042340220,))
    RunCommonEvent(0, 90005706, args=(1043340700, 30025, 0), arg_types="IiI")
