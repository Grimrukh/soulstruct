"""
linked:
0
82
166

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: N:\\GR\\data\\Param\\event\\m60.emevd
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
    RunCommonEvent(0, 90005261, args=(1038440200, 1038442200, 20.0, 0.0, 3011), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1038440210, 1038442210, 15.0, 1.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1038440211, 1038442210, 15.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1038440210, 30002, 20002, 1038442210, 15.0, 1.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038440211, 30002, 20002, 1038442210, 15.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
