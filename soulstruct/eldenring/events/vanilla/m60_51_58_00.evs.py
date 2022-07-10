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
        90005501,
        args=(1051580510, 1051580511, 1, 1051581510, 1051581511, 1051581512, 1051580512),
        arg_types="IIIIIII",
    )
    Event_1051582510()
    RunCommonEvent(0, 90005706, args=(1051580700, 930023, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1051580700)


@NeverRestart(1051582510)
def Event_1051582510():
    """Event 1051582510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1051580510,
            1051580511,
            1,
            1051581510,
            1051581511,
            1051583511,
            1051581512,
            1051583512,
            1051582511,
            1051582512,
            1051580512,
            1051580513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(1051580519)
def Event_1051580519():
    """Event 1051580519"""
    EndIfThisEventSlotFlagEnabled()
    DisableFlag(1051580510)
