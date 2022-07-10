"""
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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1038450000, obj=1038451950, unknown=5.0)
    RegisterGrace(grace_flag=1038450001, obj=1038451951, unknown=5.0)
    RunCommonEvent(0, 90005632, args=(580010, 1038451600, 80010), arg_types="IIi")
    RunCommonEvent(0, 90005570, args=(60824, 54, 1038451500, 2, 1, 0), arg_types="IiIiii")
