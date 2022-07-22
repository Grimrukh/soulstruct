"""
Northeast Caelid (SW) (SW)

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_52_40_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1052402200()
    Event_1052402210()


@RestartOnRest(1052402200)
def Event_1052402200():
    """Event 1052402200"""
    CommonFunc_9005811(0, 1252380800, 1052401800, 5, 0)


@RestartOnRest(1052402210)
def Event_1052402210():
    """Event 1052402210"""
    if FlagEnabled(1052408600):
        return
    GotoIfFlagEnabled(Label.L0, flag=1252380800)
    DisableAssetActivation(Assets.AEG110_063_1000, obj_act_id=-1)
    
    MAIN.Await(FlagEnabled(1252380800))

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAssetActivation(Assets.AEG110_063_1000, obj_act_id=-1)
