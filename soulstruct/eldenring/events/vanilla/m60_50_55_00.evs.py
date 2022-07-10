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
        90005211,
        args=(1050550300, 30000, 20000, 1050552300, 0.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1050550301, 30000, 20000, 1050552300, 0.0, 1.5, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1050550302, 30000, 20000, 1050552302, 0.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 900005610, args=(1050551680, 100, 800, 1050558600), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005636,
        args=(1050558600, 1050550600, 1050551600, 4470, 1050552600, 1050552601, 1050552600, 1050553600, 0),
        arg_types="IIIiIIIIi",
    )
    RunCommonEvent(0, 90005637, args=(1050558600, 1050550600, 1050552601), arg_types="III")
