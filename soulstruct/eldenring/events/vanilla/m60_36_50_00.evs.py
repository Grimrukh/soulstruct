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
    RegisterGrace(grace_flag=1036500000, obj=1036501950, unknown=5.0)
    RunCommonEvent(
        0,
        90005880,
        args=(1036500800, 1036500805, 1036502800, 1036500800, 30255, 60, 36, 50, 0, 1036502805),
        arg_types="IIIIiBBbbI",
    )
    RunCommonEvent(
        0,
        90005881,
        args=(1036500800, 1036500805, 1036502801, 1036502802, 20300, 1036501805, 60, 36, 50, 0, 1036502805),
        arg_types="IIIIiIBBbbI",
    )
    RunCommonEvent(
        0,
        90005882,
        args=(
            1036500800,
            1036500805,
            1036502800,
            1036500800,
            1036502806,
            1036505810,
            1036501800,
            1036500810,
            1036502810,
            903600520,
            -1,
            20001,
        ),
        arg_types="IIIIIIIIIiii",
    )
    RunCommonEvent(0, 90005883, args=(1036500800, 1036500805, 1036501805), arg_types="III")
    RunCommonEvent(0, 90005885, args=(1036500800, 0, 1036502806, 1036502807, 0, 1), arg_types="IiIIii")
    RunCommonEvent(0, 90005300, args=(1036500340, 1036500340, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(
        0,
        90005633,
        args=(580310, 580010, 1036500600, 30016, 20016, 1036501600, 1036501610),
        arg_types="IIIiiII",
    )


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(1036500210, 1036502210, 1.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036500211, 1036502210, 1.0, 0.5, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036500213, 1036502210, 1.0, 1.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036500214, 1036502214, 1.0, 1.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036500215, 1036502214, 1.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036500216, 1036502214, 1.0, 0.5, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036500217, 1036502214, 1.0, 2.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036500218, 1036502218, 1.0, 1.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036500219, 1036502218, 1.0, 0.5, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036500220, 1036502218, 1.0, 0.0, 1700), arg_types="IIffi")
