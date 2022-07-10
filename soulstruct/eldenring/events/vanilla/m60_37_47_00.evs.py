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
    RunCommonEvent(0, 90005261, args=(1037470200, 1037472200, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005201, args=(1037470211, 30005, 20021, 15.0, 2.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1037470212, 30000, 20000, 10.0, 1.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1037470211, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1037470212, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 900005610, args=(1037471680, 100, 800, 0), arg_types="IiiI")
