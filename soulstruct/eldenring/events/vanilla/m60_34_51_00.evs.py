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
    RunCommonEvent(
        0,
        90005605,
        args=(1034511620, 12, 1, 0, 0, 12012480, 0, 1034512620, 1034512621, 1034512622, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    RunCommonEvent(0, 900055278, args=(1034510739, 1034511739, 1506, 9320, 30051, 0, 0, 0), arg_types="IIiiiiii")
    RunCommonEvent(0, 90005920, args=(1034510600, 1034511600, 1034513600), arg_types="III")
    Event_1034512580()


@NeverRestart(1034512580)
def Event_1034512580():
    """Event 1034512580"""
    RegisterLadder(start_climbing_flag=1034510580, stop_climbing_flag=1034510581, obj=1034511580)
