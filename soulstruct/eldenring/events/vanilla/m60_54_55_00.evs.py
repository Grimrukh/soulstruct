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
    RegisterGrace(grace_flag=1054550000, obj=1054551950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76510, 76505, 1054551980, 77500, 4, 78500, 78501, 78502, 78503, 78504, 78505, 78506, 78507, 78508, 78509),
        arg_types="IIIIIIIIIIIIIII",
    )
    Event_1054552200(0, character=1054555200)
    RunCommonEvent(0, 90005630, args=(65545500, 1054551500, 119), arg_types="IIi")
    RunCommonEvent(0, 90005771, args=(1054550950, 1054552700), arg_types="II")
    RunCommonEvent(0, 90005771, args=(1054550950, 1054552701), arg_types="II")


@RestartOnRest(1054552200)
def Event_1054552200(_, character: uint):
    """Event 1054552200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()
