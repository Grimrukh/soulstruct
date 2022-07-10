"""
linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 90005600, args=(1038530000, 1038531950, 5.0, 1038530480), arg_types="IIfI")
    Event_1038532200(0, character=1038530200)
    Event_1038532200(1, character=1038530201)
    Event_1038532200(2, character=1038530202)
    Event_1038532200(3, character=1038530203)
    Event_1038532200(4, character=1038530204)
    Event_1038532200(5, character=1038530205)
    Event_1038532200(6, character=1038530206)
    Event_1038532200(7, character=1038530207)
    Event_1038532200(8, character=1038530208)
    Event_1038532580()
    RunCommonEvent(
        0,
        90005620,
        args=(1038530570, 1038531570, 1038531571, 1038531572, 1038532570, 1038532571, 1038532572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(1038530570, 1038531573), arg_types="II")


@RestartOnRest(1038532580)
def Event_1038532580():
    """Event 1038532580"""
    RegisterLadder(start_climbing_flag=38531580, stop_climbing_flag=38531851, obj=1038531582)


@RestartOnRest(1038532200)
def Event_1038532200(_, character: uint):
    """Event 1038532200"""
    Kill(character)
    End()
