"""
linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 90005300, args=(1040510500, 1040510500, 40310, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005706, args=(1040510700, 930023, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1040510700)
    RunCommonEvent(0, 90005250, args=(1040510407, 1040512407, 0.0, 3003), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1040510408, 1040512407, 0.0, 3003), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1040510407, 1040512408, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1040510408, 1040512408, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005201, args=(1040510406, 30001, 20001, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
