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
    RunCommonEvent(0, 90005261, args=(1040330200, 1040332200, 5.0, 0.0, 1701), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040330201, 1040332200, 5.0, 1.0, 1701), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040330202, 1040332200, 5.0, 2.0, 1702), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040330203, 1040332200, 5.0, 0.0, 1702), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040330204, 1040332200, 5.0, 1.0, 1701), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040330205, 1040332200, 5.0, 2.0, 1702), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040330206, 1040332200, 5.0, 0.0, 1701), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040330207, 1040332200, 5.0, 1.0, 1702), arg_types="IIffi")
