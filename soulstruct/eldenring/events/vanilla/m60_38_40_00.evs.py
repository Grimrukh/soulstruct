"""
linked:
0
72
154
238

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\common_macro.emevd
238: N:\\GR\\data\\Param\\event\\m60.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1038400000, obj=1038401950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76206, 76201, 1038401980, 77200, 1, 78200, 78201, 78202, 78203, 78204, 78205, 78206, 78207, 78208, 78209),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005251, args=(1038400210, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005630, args=(61384000, 1038401500, 122), arg_types="IIi")
