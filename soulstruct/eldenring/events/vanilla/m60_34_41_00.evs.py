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
    RegisterGrace(grace_flag=1034410000, obj=1034411950, unknown=5.0)
    RunCommonEvent(
        0,
        90005501,
        args=(1034410510, 1034410511, 1, 1034411510, 1034411511, 1034411512, 1034410512),
        arg_types="IIIIIII",
    )
    Event_1034412510()
    RunCommonEvent(0, 90005640, args=(1034410540, 1034411540), arg_types="II")


@NeverRestart(1034412510)
def Event_1034412510():
    """Event 1034412510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1034410510,
            1034410511,
            1,
            1034411510,
            1034411511,
            1034413511,
            1034411512,
            1034413512,
            1034412511,
            1034412512,
            1034410512,
            1034412513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(1034410519)
def Event_1034410519():
    """Event 1034410519"""
    EndIfFlagEnabled(1034410519)
    DisableFlag(1034410510)
