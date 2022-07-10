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
    RunCommonEvent(0, 90005600, args=(1051350000, 1051351950, 10.0, 1051350480), arg_types="IIfI")
    RunCommonEvent(0, 90005300, args=(1051350290, 1051350290, 40408, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005261, args=(1051350200, 1051352200, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1051350201, 1051352200, 10.0, 0.0, 0), arg_types="IIffi")
