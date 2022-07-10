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
    RunCommonEvent(0, 90005560, args=(1049400600, 1049401600, 0), arg_types="IIi")
    RunCommonEvent(0, 90005251, args=(1049400390, 0.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1049400391, 0.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1049400392, 0.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1049400393, 0.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1049400394, 0.0, 0.0, -1), arg_types="Iffi")
    Event_1049402390()
    RunCommonEvent(0, 90005250, args=(1049400381, 1049402381, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 900005610, args=(1049401610, 100, 800, 0), arg_types="IiiI")
    RunEvent(1049402650, slot=0, args=(0,))
    Event_1049400500()
    RunCommonEvent(0, 90005511, args=(1049400560, 1049404550, 1049405560, 257013, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(1049400560, 1049402550, 1049402551), arg_types="III")
    RunCommonEvent(0, 90005640, args=(1049400540, 1049401540), arg_types="II")
    RunCommonEvent(0, 90005706, args=(1049400700, 90100, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1049400700)
    Event_1046400510()


@RestartOnRest(1049402390)
def Event_1049402390():
    """Event 1049402390"""
    Kill(1049400390)
    Kill(1049400391)
    Kill(1049400392)
    Kill(1049400393)
    Kill(1049400394)


@NeverRestart(1046400510)
def Event_1046400510():
    """Event 1046400510"""
    EndIfThisEventSlotFlagEnabled()


@RestartOnRest(1049400500)
def Event_1049400500():
    """Event 1049400500"""
    EndIfFlagEnabled(12020570)
    Wait(0.5)
    DisableObjectActivation(1049401521, obj_act_id=227050)
    IfFlagEnabled(MAIN, 12020570)
    EnableObjectActivation(1049401521, obj_act_id=227050)
