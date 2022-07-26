"""
Southwest Mountaintops (NE) (SW)

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


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1050542200(0, character=1050545200)


@RestartOnRest(1050542200)
def Event_1050542200(_, character: uint):
    """Event 1050542200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()
