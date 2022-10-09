"""
Southeast Altus Plateau (NW) (NE)

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_45_51_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1045512620()
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=1045518620)


@RestartOnRest(1045512620)
def Event_1045512620():
    """Event 1045512620"""
    GotoIfFlagEnabled(Label.L0, flag=1045510620)
    
    MAIN.Await(AssetActivated(obj_act_id=1145513620))
    
    EnableFlag(1045510620)
    Wait(3.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAssetActivation(Assets.AEG110_064_2000, obj_act_id=-1)
    EndOfAnimation(asset=Assets.AEG110_064_2000, animation_id=0)
    End()
