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
    RunCommonEvent(0, 90005250, args=(1048390203, 1048392203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1048390204, 1048392203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1048390205, 1048392203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1048390402, 1048392203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1048390403, 1048392203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1048390404, 1048392203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1048390405, 1048392203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1048390406, 1048392203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1048390407, 1048392203, 0.0, -1), arg_types="IIfi")
    RegisterGrace(grace_flag=1048390000, obj=1048391950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76418, 76409, 1048391980, 77400, 2, 78400, 78401, 78402, 78403, 78404, 78405, 78406, 78407, 78408, 78409),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005630, args=(61483900, 1048391500, 123), arg_types="IIi")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1048392501, 1048391501, 200, 0, 802004070, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1048392501, 1048391501, 200, 0, 802004060, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1048392501, 1048391501, 200, 0, 802004050, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1048392501, 1048391501, 200, 0, 802004040, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1048392501, 1048391501, 200, 0, 802004030, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1048392501, 1048391501, 200, 0, 802004020, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1048392501, 1048391501, 200, 0, 802004010, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1048392501, 1048391501, 200, 0, 802004000, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    RunCommonEvent(0, 90005705, args=(1048390705,))
    RunCommonEvent(0, 90005706, args=(1048390701, 930027, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1048390700)
    DisableBackread(1048390701)
    DisableBackread(1048390705)
