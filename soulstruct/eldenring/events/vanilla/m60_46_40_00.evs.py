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
    RegisterGrace(grace_flag=1046400000, obj=1046401950, unknown=5.0)
    RegisterGrace(grace_flag=1046400001, obj=1046401951, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76418, 76401, 1046401981, 77400, 0, 78400, 78401, 78402, 78403, 78404, 78405, 78406, 78407, 78408, 78409),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005790,
        args=(0, 1046400180, 1046402181, 1046402182, 1046400701, 22, 1046402701, 1046402700, 0.0, 0, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(1046400180, 1046402181, 1046402182, 1046400701), arg_types="IIII")
    RunCommonEvent(
        0,
        90005792,
        args=(1046400180, 1046402181, 1046402182, 1046400701, 1046400700, 0.0),
        arg_types="IIIIif",
    )
    RunCommonEvent(
        0,
        90005793,
        args=(1046400180, 1046402181, 1046402182, 1046400701, 1046402701, 1046402182, 0),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005250, args=(1046400300, 1046402303, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1046400301, 1046402301, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1046400303, 1046402303, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1046400304, 1046402303, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1046400400, 2.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005706, args=(1046400710, 930025, 0), arg_types="IiI")
    RunCommonEvent(0, 90005631, args=(1046401640, 61011), arg_types="Ii")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1046400700)
    DisableBackread(1046400710)
