"""
linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 90005251, args=(1037430200, 12.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1037430201, 12.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1037430203, 12.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1037430204, 12.0, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1037430210, 12.0, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1037430211, 12.0, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1037430212, 12.0, 0.0, 1701), arg_types="Iffi")
