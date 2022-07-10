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
    RunCommonEvent(
        0,
        90005633,
        args=(580360, 580060, 1051400298, 30017, 20017, 1051401500, 1051401501),
        arg_types="IIIiiII",
    )
    RunCommonEvent(0, 90005870, args=(1051400800, 904811601, 18), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1051400800, 0, 1051400800, 0, 30415, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1051400800, 18, 0), arg_types="III")
    RunCommonEvent(0, 90005250, args=(1051400200, 1051402200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051400201, 1051402200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051400202, 1051402200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051400299, 1051402300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1051400300, 7.0, 0.0, -1), arg_types="Iffi")
