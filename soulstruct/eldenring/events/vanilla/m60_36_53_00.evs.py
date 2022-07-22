"""
West Altus Plateau (SW) (NW)

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
from .entities.m60_36_53_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005261(0, character=1036530200, region=1036532200, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=1036530200,
        animation_id=30001,
        animation_id_1=20001,
        region=1036532200,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=1036530201, region=1036532200, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=1036530201,
        animation_id=30001,
        animation_id_1=20001,
        region=1036532200,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1036532300()
    Event_1036532500()
    Event_1036532450(0, asset=Assets.AEG007_434_9000)
    Event_1036532450(1, asset=Assets.AEG007_434_9001)
    Event_1036532450(2, asset=Assets.AEG007_434_9002)
    Event_1036533700()


@RestartOnRest(1036532300)
def Event_1036532300():
    """Event 1036532300"""
    RemoveSpecialEffect(1036530300, 5070)
    RemoveSpecialEffect(1036530301, 5070)
    RemoveSpecialEffect(1036530302, 5070)
    RemoveSpecialEffect(1036530303, 5070)
    RemoveSpecialEffect(1036530304, 5070)
    RemoveSpecialEffect(1036530305, 5070)
    RemoveSpecialEffect(1036530306, 5070)
    RemoveSpecialEffect(1036530307, 5070)


@RestartOnRest(1036532450)
def Event_1036532450(_, asset: uint):
    """Event 1036532450"""
    DisableAsset(asset)
    End()


@ContinueOnRest(1036532500)
def Event_1036532500():
    """Event 1036532500"""
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1036532200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1036532200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1036532200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1036532200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1036532200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1036532200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1036532200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1036532200,
            asset=Assets.AEG007_557_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1036532201,
            asset=Assets.AEG007_557_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1036532201,
            asset=Assets.AEG007_557_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1036532201,
            asset=Assets.AEG007_557_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1036532201,
            asset=Assets.AEG007_557_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1036532201,
            asset=Assets.AEG007_557_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1036532201,
            asset=Assets.AEG007_557_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1036532201,
            asset=Assets.AEG007_557_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1036532201,
            asset=Assets.AEG007_557_1001,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1036532202,
            asset=Assets.AEG007_557_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1036532202,
            asset=Assets.AEG007_557_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1036532202,
            asset=Assets.AEG007_557_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1036532202,
            asset=Assets.AEG007_557_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1036532202,
            asset=Assets.AEG007_557_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1036532202,
            asset=Assets.AEG007_557_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1036532202,
            asset=Assets.AEG007_557_1002,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802003210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(0, 1036532202, 1036531202, 200, 0, 802003200, 1.0, 0.0, 1.0)


@RestartOnRest(1036533700)
def Event_1036533700():
    """Event 1036533700"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3670):
        return
    if FlagEnabled(400179):
        return
    AND_1.Add(FlagEnabled(400179))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1035539204)
    End()
