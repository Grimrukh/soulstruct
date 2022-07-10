"""
linked:
0
82
166

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: N:\\GR\\data\\Param\\event\\m60.emevd
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
    RunCommonEvent(0, 90005251, args=(1043400200, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005300, args=(1043400200, 1043400200, 0, 0.0, 0), arg_types="IIifi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1043402200()


@RestartOnRest(1043402200)
def Event_1043402200():
    """Event 1043402200"""
    EndIfFlagEnabled(1043400200)
    DisableHealthBar(1043400200)
    AddSpecialEffect(1043400200, 12189)
    Wait(3.0)
    CancelSpecialEffect(1043400200, 12189)
    EnableHealthBar(1043400200)
