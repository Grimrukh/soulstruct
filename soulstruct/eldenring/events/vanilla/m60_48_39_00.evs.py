"""
South Caelid (NW) (NW)

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
from .enums.m60_48_39_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.PutridCorpse1, region=1048392203, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.PutridCorpse2, region=1048392203, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.PutridCorpse3, region=1048392203, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.PutridCorpseBare0, region=1048392203, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.PutridCorpseBare1, region=1048392203, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.PutridCorpseBare2, region=1048392203, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.PutridCorpseBare3, region=1048392203, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.PutridCorpseBare4, region=1048392203, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.PutridCorpseBare5, region=1048392203, seconds=0.0, animation_id=-1)
    RegisterGrace(grace_flag=1048390000, asset=Assets.AEG099_060_9001)
    CommonFunc_90005100(
        0,
        flag=76418,
        flag_1=76409,
        asset=Assets.AEG099_090_9000,
        source_flag=77400,
        value=2,
        flag_2=78400,
        flag_3=78401,
        flag_4=78402,
        flag_5=78403,
        flag_6=78404,
        flag_7=78405,
        flag_8=78406,
        flag_9=78407,
        flag_10=78408,
        flag_11=78409,
    )
    CommonFunc_90005630(0, far_view_id=61483900, asset=Assets.AEG099_130_9000, dummy_id=123)
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1048392501,
            asset=Assets.AEG007_470_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004070,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005694(
            0,
            asset_flag=1048392501,
            asset=Assets.AEG007_470_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004060,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005694(
            0,
            asset_flag=1048392501,
            asset=Assets.AEG007_470_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004050,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005694(
            0,
            asset_flag=1048392501,
            asset=Assets.AEG007_470_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004040,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005694(
            0,
            asset_flag=1048392501,
            asset=Assets.AEG007_470_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004030,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005694(
            0,
            asset_flag=1048392501,
            asset=Assets.AEG007_470_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004020,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005694(
            0,
            asset_flag=1048392501,
            asset=Assets.AEG007_470_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004010,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005694(
            0,
            asset_flag=1048392501,
            asset=Assets.AEG007_470_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004000,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    CommonFunc_90005705(0, character=Characters.FingerReader)
    CommonFunc_90005706(0, character=Characters.PutridCorpse0, animation_id=930027, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1048390700)
    DisableBackread(Characters.PutridCorpse0)
    DisableBackread(Characters.FingerReader)
