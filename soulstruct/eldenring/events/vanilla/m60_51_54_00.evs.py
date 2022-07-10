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
    RunCommonEvent(0, 90005261, args=(1051540245, 1051542245, 0.0, 0.0, 0), arg_types="IIffi")
    Event_1051542200(0, character=1049535200)
    RunCommonEvent(0, 90005300, args=(1051540210, 1051540210, 40512, 0.0, 0), arg_types="IIifi")


@RestartOnRest(1051542200)
def Event_1051542200(_, character: uint):
    """Event 1051542200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()
