"""
linked:
0
72
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 90005261, args=(1037410200, 1037412200, 3.0, 0.0, 3020), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037410201, 1037412200, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037410202, 1037412200, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037410203, 1037412200, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037410204, 1037412204, 3.0, 0.0, 3020), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037410205, 1037412204, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037410206, 1037412204, 3.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 900005610, args=(1037411680, 100, 800, 0), arg_types="IiiI")
    Event_1037410220(0, 1037410220)


@RestartOnRest(1037410220)
def Event_1037410220(_, character: uint):
    """Event 1037410220"""
    Kill(character)
