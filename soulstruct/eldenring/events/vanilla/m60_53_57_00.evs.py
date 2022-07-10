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
    Event_1053572200(0, character=1053575200)
    RunCommonEvent(0, 90005300, args=(1053570210, 1053570210, 40510, 0.0, 0), arg_types="IIifi")


@RestartOnRest(1053572200)
def Event_1053572200(_, character: uint):
    """Event 1053572200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()
