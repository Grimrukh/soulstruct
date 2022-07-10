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
    RegisterGrace(grace_flag=1051390000, obj=1051391950, unknown=5.0)
    RunCommonEvent(0, 90005683, args=(62412, 1051391684, 209, 78494, 78494), arg_types="IIiII")
    RunCommonEvent(0, 900005610, args=(1051391650, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005250, args=(1051390204, 1051392204, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051390250, 1051392280, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051390251, 1051392251, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051390280, 1051392280, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051390400, 1051392400, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051390402, 1051392400, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051390431, 1051392401, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051390432, 1051392401, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051390433, 1051392401, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051390434, 1051392401, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051390435, 1051392401, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051390436, 1051392401, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051390437, 1051392401, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1051390438, 1051392401, 0.0, -1), arg_types="IIfi")
    Event_1051392200(0, character=1051390400)
    Event_1051392200(1, character=1051390402)
    Event_1051392200(2, character=1051390431)
    Event_1051392200(3, character=1051390432)
    Event_1051392200(4, character=1051390433)
    Event_1051392200(5, character=1051390434)
    Event_1051392200(6, character=1051390435)
    Event_1051392200(7, character=1051390436)
    Event_1051392200(8, character=1051390437)
    Event_1051392200(9, character=1051390438)
    Event_1051392580(0, start_climbing_flag=1051390580, stop_climbing_flag=1051390851, obj=1051391580)
    Event_1051392580(1, start_climbing_flag=1051390582, stop_climbing_flag=1051390853, obj=1051391582)
    Event_1051392580(2, 1051390584, 1051390855, 1051391584)


@RestartOnRest(1051392200)
def Event_1051392200(_, character: uint):
    """Event 1051392200"""
    AddSpecialEffect(character, 8081)
    IfHasAIStatus(MAIN, character, ai_status=AIStatusType.Battle)
    CancelSpecialEffect(character, 8081)


@NeverRestart(1051392580)
def Event_1051392580(_, start_climbing_flag: uint, stop_climbing_flag: uint, obj: uint):
    """Event 1051392580"""
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, obj=obj)
