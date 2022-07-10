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


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(1040550301, 1040552301, 2.0, 0.0, 3005), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040550302, 1040552302, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040550303, 1040552302, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1040550304, 1040552302, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(1040550250, 1040552250, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(
        0,
        90005200,
        args=(1040550403, 30000, 20000, 1040552403, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(1040550403, 30000, 20000, 1040552403, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1040550403, 30000, 20000, 1040552403, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
