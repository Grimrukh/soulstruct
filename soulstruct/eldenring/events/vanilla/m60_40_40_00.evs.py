"""
linked:
0
72
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 90005261, args=(1040400206, 1040402206, 10.0, 0.0, 3011), arg_types="IIffi")
    Event_1040402200(0, character=1040400210)
    Event_1040402200(1, character=1040400211)
    Event_1040402200(2, character=1040400212)
    Event_1040402200(3, character=1040400213)
    Event_1040402200(4, character=1040400214)
    Event_1040402200(5, character=1040400215)
    Event_1040402200(6, character=1040400216)
    Event_1040402200(7, character=1040400217)
    Event_1040402200(8, character=1040400218)
    Event_1040402220(0, character=1040400220)
    RunCommonEvent(0, 90005423, args=(1040400220,))


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005422, args=(1040408500, 1040401500, 1040403500), arg_types="III")


@RestartOnRest(1040402200)
def Event_1040402200(_, character: uint):
    """Event 1040402200"""
    Kill(character)
    End()


@RestartOnRest(1040402220)
def Event_1040402220(_, character: uint):
    """Event 1040402220"""
    AddSpecialEffect(character, 5551)
    End()
