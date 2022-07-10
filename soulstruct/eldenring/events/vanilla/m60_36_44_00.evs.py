"""
linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1036442203(0, character=1036440203)
    Event_1036442203(1, character=1036440204)
    Event_1036442203(2, character=1036440205)
    Event_1036442203(3, character=1036440206)
    RunCommonEvent(0, 90005300, args=(1036440250, 1036440250, 40202, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1036440260, 1036440260, 1036440200, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005920, args=(1036440600, 1036441600, 1036443600), arg_types="III")
    RunCommonEvent(0, 90005705, args=(1036440700,))


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1036440700)
    RunCommonEvent(0, 90005201, args=(1036440210, 30002, 20002, 7.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005261, args=(1036440220, 1036442220, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036440230, 1036442220, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036440231, 1036442220, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(1036440241, 15.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1036440242, 15.0, 0.0, 0), arg_types="Iffi")


@RestartOnRest(1036442203)
def Event_1036442203(_, character: uint):
    """Event 1036442203"""
    Kill(character)
    End()
