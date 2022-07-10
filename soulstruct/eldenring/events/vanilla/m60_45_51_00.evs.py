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
    Event_1045512620()
    RunCommonEvent(0, 900005610, args=(1045511680, 100, 800, 1045518620), arg_types="IiiI")


@RestartOnRest(1045512620)
def Event_1045512620():
    """Event 1045512620"""
    GotoIfFlagEnabled(Label.L0, flag=1045510620)
    IfObjectActivated(MAIN, obj_act_id=1145513620)
    EnableFlag(1045510620)
    Wait(3.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObjectActivation(1145511620, obj_act_id=-1)
    EndOfAnimation(obj=1145511620, animation_id=0)
    End()
