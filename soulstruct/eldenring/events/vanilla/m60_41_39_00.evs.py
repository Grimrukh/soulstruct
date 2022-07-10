"""
linked:
0
82
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1041392340(0, character=1041390705)
    Event_1041392340(1, character=1041390706)
    Event_1041392340(2, character=1041390707)
    Event_1041392340(3, character=1041390708)
    RunCommonEvent(0, 90005705, args=(1041390700,))
    RunCommonEvent(0, 90005706, args=(1041390720, 30023, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1041390700)
    DisableBackread(1041390720)
    RunCommonEvent(0, 90005261, args=(1041390200, 1041382200, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1041390201, 1041382200, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1041390202, 1041382200, 10.0, 0.0, -1), arg_types="IIffi")


@RestartOnRest(1041392340)
def Event_1041392340(_, character: uint):
    """Event 1041392340"""
    Kill(character, award_souls=True)
