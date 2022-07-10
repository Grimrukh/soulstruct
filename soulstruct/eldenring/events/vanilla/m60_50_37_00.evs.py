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
    RunCommonEvent(0, 90005251, args=(1050370299, 100.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005300, args=(1050370299, 1050370299, 0, 0.0, 0), arg_types="IIifi")
