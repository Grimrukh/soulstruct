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
    RunCommonEvent(0, 90005261, args=(1053550202, 1053552202, 5.0, 0.0, 0), arg_types="IIffi")
    Event_1053552200(0, 1053555200)


@RestartOnRest(1053552200)
def Event_1053552200(_, character: uint):
    """Event 1053552200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()
