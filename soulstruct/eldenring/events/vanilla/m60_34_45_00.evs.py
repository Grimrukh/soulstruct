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
    RunCommonEvent(0, 90005870, args=(1034450800, 904502600, 25), arg_types="IiI")
    RunCommonEvent(0, 90005861, args=(1034450800, 0, 1034450800, 1, 30210, 30061, 0.0), arg_types="IIIIiif")
    Event_1034452800()
    Event_1034452805()
    RunCommonEvent(
        0,
        90005211,
        args=(1034450800, 30000, 20000, 1034452800, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(1034450800, 1034452800, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(1034450227, 7.0, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1034450228, 7.0, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1034450229, 7.0, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1034450230, 7.0, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1034450231, 7.0, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1034450223, 7.0, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1034450224, 7.0, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1034450225, 7.0, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1034450226, 7.0, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005460, args=(1034450200,))
    RunCommonEvent(0, 90005460, args=(1034450201,))
    RunCommonEvent(0, 90005460, args=(1034450202,))
    RunCommonEvent(0, 90005460, args=(1034450203,))
    RunCommonEvent(0, 90005460, args=(1034450204,))
    RunCommonEvent(0, 90005461, args=(1034450200,))
    RunCommonEvent(0, 90005462, args=(1034450200,))
    RunCommonEvent(0, 90005461, args=(1034450201,))
    RunCommonEvent(0, 90005462, args=(1034450201,))
    RunCommonEvent(0, 90005461, args=(1034450202,))
    RunCommonEvent(0, 90005462, args=(1034450202,))
    RunCommonEvent(0, 90005461, args=(1034450203,))
    RunCommonEvent(0, 90005462, args=(1034450203,))
    RunCommonEvent(0, 90005461, args=(1034450204,))
    RunCommonEvent(0, 90005462, args=(1034450204,))
    RunCommonEvent(0, 90005201, args=(1034450200, 30010, -1, 0.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 900005610, args=(1034451680, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005620,
        args=(1034450570, 1034451570, 1034451571, 1034451572, 1034452571, 1034452572, 1034452573),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(1034450570, 1034451573), arg_types="II")


@RestartOnRest(1034452800)
def Event_1034452800():
    """Event 1034452800"""
    EndIfFlagEnabled(1034450800)
    AddSpecialEffect(1034450800, 10247)


@RestartOnRest(1034452805)
def Event_1034452805():
    """Event 1034452805"""
    EndIfFlagEnabled(1034450800)
    SetNest(1034450800, region=1034452810)
    Wait(1.0)
    Restart()
