"""
Northeast Mountaintops (SW) (NW)

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
from .enums.m60_52_57_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1052570000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76510,
        flag_1=76504,
        asset=Assets.AEG099_090_9000,
        source_flag=77500,
        value=3,
        flag_2=78500,
        flag_3=78501,
        flag_4=78502,
        flag_5=78503,
        flag_6=78504,
        flag_7=78505,
        flag_8=78506,
        flag_9=78507,
        flag_10=78508,
        flag_11=78509,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton4,
        animation_id=30018,
        animation_id_1=20018,
        region=0,
        radius=3.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton10,
        animation_id=30019,
        animation_id_1=20019,
        region=0,
        radius=3.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Avionette0, region=1052572240, seconds=0.0, animation_id=3010)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Avionette1, region=1052572240, seconds=0.5, animation_id=3010)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Avionette2, region=1052572243, seconds=0.0, animation_id=3032)
    Event_1052572200(0, character=1052575200)
    CommonFunc_90005261(0, character=1052570320, region=1052572320, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=1052570321, region=1052572321, radius=3.0, seconds=0.0, animation_id=0)
    Event_1052572210()
    Event_1052572220()
    Event_1052572230()
    CommonFunc_90005560(0, flag=1052570490, asset=Assets.AEG099_635_9000, left=0)
    Event_1052572510()
    CommonFunc_90005501(
        0,
        flag=1052570510,
        flag_1=1052570511,
        left=0,
        asset=Assets.AEG110_112_2000,
        asset_1=Assets.AEG099_182_2001,
        asset_2=Assets.AEG099_182_2000,
        flag_2=1052570512,
    )
    CommonFunc_90005630(0, far_view_id=65525700, asset=Assets.AEG099_130_9000, dummy_id=125)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_1052570519()


@RestartOnRest(1052572200)
def Event_1052572200(_, character: uint):
    """Event 1052572200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    End()


@RestartOnRest(1052572210)
def Event_1052572210():
    """Event 1052572210"""
    GotoIfFlagEnabled(Label.L0, flag=1052570210)
    DeleteAssetVFX(Assets.AEG099_251_9000)
    CreateAssetVFX(Assets.AEG099_251_9000, vfx_id=200, dummy_id=1500)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1052572210))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1052570210)
    DisplayDialog(text=20210, anchor_entity=0, display_distance=5.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG099_251_9000)
    DeleteAssetVFX(Assets.AEG099_251_9000)
    PlaySoundEffect(Assets.AEG099_251_9000, 1500, sound_type=SoundType.s_SFX)
    End()


@RestartOnRest(1052572220)
def Event_1052572220():
    """Event 1052572220"""
    DisableNetworkSync()
    if FlagEnabled(1052570210):
        return
    OR_1.Add(ActionButtonParamActivated(action_button_id=9320, entity=Assets.AEG099_251_9000))
    OR_1.Add(FlagEnabled(1052570210))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(1052570210):
        return
    DisplayDialog(text=20200, anchor_entity=Assets.AEG099_251_9000)
    Wait(1.0)
    Restart()


@RestartOnRest(1052572230)
def Event_1052572230():
    """Event 1052572230"""
    DisableNetworkSync()
    AND_1.Add(ActionButtonParamActivated(action_button_id=9210, entity=Assets.AEG099_023_2000))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=60051, anchor_entity=Assets.AEG099_023_2000)
    Wait(1.0)
    Restart()


@ContinueOnRest(1052572510)
def Event_1052572510():
    """Event 1052572510"""
    CommonFunc_90005500(
        0,
        flag=1052570510,
        flag_1=1052570511,
        left=0,
        asset=Assets.AEG110_112_2000,
        asset_1=Assets.AEG099_182_2001,
        obj_act_id=1052573511,
        asset_2=Assets.AEG099_182_2000,
        obj_act_id_1=1052573512,
        region=1052572511,
        region_1=1052572512,
        flag_2=1052570512,
        flag_3=1052570513,
        left_1=0,
    )


@ContinueOnRest(1052570519)
def Event_1052570519():
    """Event 1052570519"""
    if ThisEventSlotFlagEnabled():
        return
    DisableFlag(1052570510)
