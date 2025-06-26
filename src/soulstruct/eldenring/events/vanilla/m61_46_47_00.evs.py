"""
Land of Shadow 11-11 NE NW

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
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76941, asset=2046471950)
    CommonFunc_90005102(
        0,
        flag=76945,
        flag_1=76941,
        asset=2046471980,
        source_flag=77900,
        value=3,
        flag_2=78900,
        flag_3=78901,
        flag_4=78902,
        flag_5=78903,
        flag_6=78904,
        flag_7=78905,
        flag_8=78906,
        flag_9=78907,
        flag_10=78908,
        flag_11=78909,
        flag_12=9146,
    )
    CommonFunc_90005221(0, character=2046470300, animation_id=30013, animation_id_1=20013, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470305, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470310, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470311, animation_id=30013, animation_id_1=20013, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470312, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470313, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470314, animation_id=30013, animation_id_1=20013, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470315, animation_id=30013, animation_id_1=20013, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470316, animation_id=30013, animation_id_1=20013, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470317, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470318, animation_id=30013, animation_id_1=20013, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470319, animation_id=30013, animation_id_1=20013, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470323, animation_id=30013, animation_id_1=20013, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470327, animation_id=30013, animation_id_1=20013, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470346, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470348, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470349, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470350, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470351, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470365, animation_id=30014, animation_id_1=20014, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470366, animation_id=30013, animation_id_1=20013, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046470367, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    Event_2046472540(
        0,
        flag=2046478540,
        asset=2046471540,
        asset_1=2046471541,
        obj_act_id=2046473541,
        obj_act_id_1=1464026,
        animation_id=10,
        animation_id_1=2,
        obj_act_id_2=2046473540,
        obj_act_id_3=464057,
    )
    CommonFunc_900005580(0, flag=580600, asset=2046471500, flag_1=9146)
    CommonFunc_90005748(0, entity=2046471700, action_button_id=206020, text=1030026, display_distance=30.0, flag=4916)


@RestartOnRest(2046472540)
def Event_2046472540(
    _,
    flag: Flag | int,
    asset: uint,
    asset_1: Asset | int,
    obj_act_id: uint,
    obj_act_id_1: int,
    animation_id: int,
    animation_id_1: int,
    obj_act_id_2: uint,
    obj_act_id_3: int,
):
    """Event 2046472540"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    DisableAssetActivation(asset, obj_act_id=obj_act_id_3)
    EndOfAnimation(asset=asset, animation_id=animation_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(AssetActivated(obj_act_id=obj_act_id))
    OR_3.Add(AND_2)
    AND_3.Add(AssetActivated(obj_act_id=obj_act_id_2))
    OR_3.Add(AND_3)
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_3)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    DisableAssetActivation(asset, obj_act_id=obj_act_id_3)
    ForceAnimation(asset, animation_id)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    DisableAssetActivation(asset, obj_act_id=obj_act_id_3)
    End()
