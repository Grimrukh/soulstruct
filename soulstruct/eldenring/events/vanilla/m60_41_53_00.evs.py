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
    RunCommonEvent(0, 90005870, args=(1041530800, 904580600, 8), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1041530800, 0, 1041530800, 0, 30320, 0.0), arg_types="IIIIif")
    RunCommonEvent(
        0,
        90005636,
        args=(32058691, 1041530650, 1041531650, 4470, 1041532650, 1041532651, 1041532650, 1041533650, 0),
        arg_types="IIIiIIIIi",
    )
    RunCommonEvent(0, 90005637, args=(32058691, 1041530650, 1041531650), arg_types="III")
    RunCommonEvent(0, 90005300, args=(1041530500, 1041530500, 40308, 0.0, 0), arg_types="IIifi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(1041530362, 1041532362, 3.0, 0.0, 3010), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(1041530365, 30000, 20000, 1041532365, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1041530357, 30001, 20001, 1041532357, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1041530361, 1041532361, 0.0, 3011), arg_types="IIfi")
    RunCommonEvent(0, 90005201, args=(1041530800, 30000, 20000, 15.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
