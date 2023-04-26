"""
East Limgrave (NE) (NE)

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
from .enums.m60_47_39_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1047390000, asset=Assets.AEG099_060_9000)
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1047392600,
            asset=Assets.AEG007_431_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004070,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1047392600,
            asset=Assets.AEG007_431_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004060,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1047392600,
            asset=Assets.AEG007_431_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004050,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1047392600,
            asset=Assets.AEG007_431_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004040,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1047392600,
            asset=Assets.AEG007_431_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004030,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1047392600,
            asset=Assets.AEG007_431_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004020,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1047392600,
            asset=Assets.AEG007_431_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004010,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1047392600,
            asset=Assets.AEG007_431_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004000,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1047392601,
            asset=Assets.AEG007_432_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004070,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1047392601,
            asset=Assets.AEG007_432_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004060,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1047392601,
            asset=Assets.AEG007_432_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004050,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1047392601,
            asset=Assets.AEG007_432_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004040,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1047392601,
            asset=Assets.AEG007_432_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004030,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1047392601,
            asset=Assets.AEG007_432_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004020,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1047392601,
            asset=Assets.AEG007_432_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004010,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1047392601,
            asset=Assets.AEG007_432_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004000,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1047392602,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004070,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1047392602,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004060,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1047392602,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004050,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1047392602,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004040,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1047392602,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004030,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1047392602,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004020,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1047392602,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004010,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1047392602,
            asset=Assets.AEG007_432_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004000,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    CommonFunc_90005300(0, flag=1047390299, character=Characters.Scarab0, item_lot=40410, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1047390298, character=Characters.Scarab1, item_lot=40422, seconds=0.0, left=0)
    CommonFunc_90005261(
        0,
        character=Characters.MonstrousCrow0,
        region=1047392304,
        radius=35.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MonstrousCrow1,
        region=1047392304,
        radius=25.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005250(0, character=Characters.RadahnSoldier0, region=1047392450, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnSoldier1, region=1047392450, seconds=2.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.RadahnSoldier2,
        region=1047392406,
        radius=8.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005250(0, character=Characters.RadahnSoldier3, region=1047392406, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnSoldier4, region=1047392406, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.TunnelMiner0, region=1047392450, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.TunnelMiner1, region=1047392450, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.TunnelMiner2, region=1047392450, seconds=0.0, animation_id=-1)
