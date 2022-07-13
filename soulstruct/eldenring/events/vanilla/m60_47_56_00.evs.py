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
        args=(1047561500, 12, 5, 0, 0, 12052020, 0, 1047562501, 1047562502, 1047562503, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    RunCommonEvent(
        0,
        90005790,
        args=(0, 1047560180, 1047562181, 1047562182, 1047560180, 21, 1047562180, 1047562181, 0.0, 0, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(1047560180, 1047562181, 1047562182, 1047560180), arg_types="IIII")
    RunCommonEvent(
        0,
        90005792,
        args=(1047560180, 1047562181, 1047562182, 1047560180, 1047560700, 0.0),
        arg_types="IIIIif",
    )
    RunCommonEvent(
        0,
        90005793,
        args=(1047560180, 1047562181, 1047562182, 1047560180, 1047562180, 1047562182, 0),
        arg_types="IIIIIIi",
    )
