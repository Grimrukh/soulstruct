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
    Event_1050532200(0, character=1050535200)
    RunCommonEvent(0, 90005300, args=(1050530210, 1050530210, 1050530700, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 900005610, args=(1050531680, 100, 800, 1050538620), arg_types="IiiI")
    RunCommonEvent(0, 90005683, args=(62511, 1050531600, 211, 78592, 0), arg_types="IIiII")
    RunCommonEvent(0, 900005610, args=(1050531685, 100, 800, 1050538600), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005620,
        args=(1050530570, 1050531570, 1050531571, 1050531572, 1050532570, 1050532571, 1050532572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(1050530570, 1050531573), arg_types="II")
    RunCommonEvent(0, 90005631, args=(1050531500, 61050), arg_types="Ii")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005200, args=(1050530201, 30004, 20004, 1050532201, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")


@RestartOnRest(1050532200)
def Event_1050532200(_, character: uint):
    """Event 1050532200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()
