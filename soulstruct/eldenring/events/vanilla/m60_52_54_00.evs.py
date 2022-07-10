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
    RegisterGrace(grace_flag=1052540000, obj=1052541950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76510, 76506, 1052541980, 77500, 6, 78500, 78501, 78502, 78503, 78504, 78505, 78506, 78507, 78508, 78509),
        arg_types="IIIIIIIIIIIIIII",
    )
    Event_1052542200(0, character=1052545200)
    RunCommonEvent(
        0,
        90005200,
        args=(1052540259, 30003, 20003, 1052542304, 1.7000000476837158, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(1052540260, 30003, 20003, 1052542304, 1.7000000476837158, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(1052540261, 30004, 20004, 1052542304, 1.7000000476837158, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(1052540311, 30003, 20003, 1052542311, 1.899999976158142, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(1052540320, 30005, 20005, 1052542320, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1052540321, 30005, 20005, 1052542321, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1052540322, 30005, 20005, 1052542322, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1052540331, 30003, 20003, 1052542331, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(1052540334, 1052542334, 50.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005300, args=(1052540491, 1052540331, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1052540492, 1052540332, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1052540494, 1052540334, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005771, args=(1052540950, 1052542700), arg_types="II")


@RestartOnRest(1052542200)
def Event_1052542200(_, character: uint):
    """Event 1052542200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()
