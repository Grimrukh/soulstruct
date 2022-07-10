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
    Event_1052402200()
    Event_1052402210()


@RestartOnRest(1052402200)
def Event_1052402200():
    """Event 1052402200"""
    RunCommonEvent(0, 9005811, args=(1252380800, 1052401800, 5, 0), arg_types="IIiI")


@RestartOnRest(1052402210)
def Event_1052402210():
    """Event 1052402210"""
    EndIfFlagEnabled(1052408600)
    GotoIfFlagEnabled(Label.L0, flag=1252380800)
    DisableObjectActivation(1052401550, obj_act_id=-1)
    IfFlagEnabled(MAIN, 1252380800)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObjectActivation(1052401550, obj_act_id=-1)
