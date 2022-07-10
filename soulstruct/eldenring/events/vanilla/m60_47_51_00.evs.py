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
    RegisterGrace(grace_flag=1047510000, obj=1047511950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76510, 76500, 1047511980, 77500, 0, 78500, 78501, 78502, 78503, 78504, 78505, 78506, 78507, 78508, 78509),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 900005610, args=(1047511600, 100, 800, 0), arg_types="IiiI")
