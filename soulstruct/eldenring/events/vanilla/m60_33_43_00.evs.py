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
    RunCommonEvent(0, 90005870, args=(1033430800, 904810600, 18), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1033430800, 0, 1033430800, 0, 30205, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005251, args=(1033430800, 20.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005872, args=(1033430800, 18, 0), arg_types="III")
    RunCommonEvent(0, 900005610, args=(1033431680, 100, 800, 1033438600), arg_types="IiiI")
    RunCommonEvent(0, 90005300, args=(1033430200, 1033430200, 40238, 0.0, 0), arg_types="IIifi")
