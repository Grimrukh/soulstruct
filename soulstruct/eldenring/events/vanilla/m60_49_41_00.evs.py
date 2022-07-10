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
    RunCommonEvent(0, 90005300, args=(1049410299, 1049410299, 40426, 0.0, 0), arg_types="IIifi")
    Event_1049412580()
    RunCommonEvent(0, 900005610, args=(1049411650, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(1049411651, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(1049411652, 100, 800, 0), arg_types="IiiI")


@RestartOnRest(1049412580)
def Event_1049412580():
    """Event 1049412580"""
    RegisterLadder(start_climbing_flag=1049410580, stop_climbing_flag=1049410581, obj=1049411580)
    RegisterLadder(start_climbing_flag=1049410582, stop_climbing_flag=1049410583, obj=1049411582)
    RegisterLadder(start_climbing_flag=1049410584, stop_climbing_flag=1049410585, obj=1049411584)
    RegisterLadder(start_climbing_flag=1049410586, stop_climbing_flag=1049410587, obj=1049411586)
    RegisterLadder(start_climbing_flag=1049410588, stop_climbing_flag=1049410589, obj=1049411588)
    RegisterLadder(start_climbing_flag=1049410590, stop_climbing_flag=1049410591, obj=1049411590)
    RegisterLadder(start_climbing_flag=1049410592, stop_climbing_flag=1049410593, obj=1049411592)
    RegisterLadder(start_climbing_flag=1049410594, stop_climbing_flag=1049410595, obj=1049411594)
    RegisterLadder(start_climbing_flag=1049410596, stop_climbing_flag=1049410597, obj=1049411596)
