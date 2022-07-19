"""
East Limgrave (NE) (SE)

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
from .entities.m60_47_38_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1047382210()
    Event_1047382211(0, source_entity=Assets.AEG099_046_9000, seconds=2.0)
    Event_1047382211(1, source_entity=Assets.AEG099_046_9001, seconds=7.0)
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=60,
        block_id=50,
        cc_id=36,
        dd_id=0,
        player_start=1050360602,
        unk_8_12=0,
        flag=1047382650,
        left_flag=1047382654,
        cancel_flag__right_flag=1047382655,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    CommonFunc_90005620(
        0,
        flag=1047380570,
        asset=Assets.AEG027_078_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=Assets.AEG027_217_9000,
        left_flag=1047382570,
        cancel_flag__right_flag=1047382571,
        right=1047382572,
    )
    Event_1047382569(0, flag=1047380570, asset=Assets.AEG099_271_9000)
    if FlagEnabled(57):
        CommonFunc_90005694(
            0,
            asset_flag=1047382500,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047382500,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047382500,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047382500,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047382500,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047382500,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047382500,
            asset=Assets.AEG007_470_2000,
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
            asset_flag=1047382500,
            asset=Assets.AEG007_470_2000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802004000,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005636(
        0,
        flag=31218690,
        character=Characters.WanderingNoble,
        entity=Assets.AEG099_374_9000,
        special_effect_id=4470,
        destination=1047382627,
        region=1047382625,
        flag_1=1047382630,
        patrol_information_id=1047383620,
        right=0,
    )
    CommonFunc_90005637(0, flag=31218690, character=Characters.WanderingNoble, region=1047382625)
    CommonFunc_90005251(0, 1047380294, 8.0, 0.0, -1)
    CommonFunc_90005250(0, 1047380296, 1047382296, 0.0, -1)
    CommonFunc_90005300(
        0,
        flag=1047380299,
        character=Characters.LionGuardian,
        item_lot_param_id=1047380700,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005250(0, 1047380301, 1047382453, 0.0, -1)
    CommonFunc_90005250(0, 1047380302, 1047382302, 0.0, -1)
    CommonFunc_90005250(0, 1047380306, 1047382302, 0.0, -1)
    CommonFunc_90005251(0, 1047380307, 8.0, 0.0, -1)
    CommonFunc_90005250(0, 1047380312, 1047382302, 0.0, -1)
    CommonFunc_90005250(0, 1047380450, 1047382450, 0.0, -1)
    CommonFunc_90005251(0, 1047382459, 15.0, 0.0, -1)
    CommonFunc_90005250(0, 1047380474, 1047382474, 0.0, -1)
    CommonFunc_90005513(
        0,
        flag=1047380540,
        asset=Assets.AEG030_605_2000,
        asset_1=Assets.AEG099_026_2000,
        obj_act_id=1047383541,
        obj_act_id_1=99026,
        animation_id=1,
        animation_id_1=2,
    )
    Event_1047381580()
    CommonFunc_90005706(0, 1047380701, 930025, 1047381700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1047380700)
    DisableBackread(Characters.Commoner)


@RestartOnRest(1047382210)
def Event_1047382210():
    """Event 1047382210"""
    CreateProjectileOwner(entity=Characters.Human)


@RestartOnRest(1047382211)
def Event_1047382211(_, source_entity: uint, seconds: float):
    """Event 1047382211"""
    EnableNetworkSync()
    Wait(8.0)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=source_entity, radius=70.0))
    
    Wait(seconds)
    AND_1.Add(NewGameCycleEqual(completion_count=0))
    SkipLinesIfConditionFalse(2, AND_1)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_2.Add(NewGameCycleEqual(completion_count=1))
    SkipLinesIfConditionFalse(2, AND_2)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_3.Add(NewGameCycleEqual(completion_count=2))
    SkipLinesIfConditionFalse(2, AND_3)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_4.Add(NewGameCycleEqual(completion_count=3))
    SkipLinesIfConditionFalse(2, AND_4)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_5.Add(NewGameCycleEqual(completion_count=4))
    SkipLinesIfConditionFalse(2, AND_5)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_6.Add(NewGameCycleEqual(completion_count=5))
    SkipLinesIfConditionFalse(2, AND_6)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_7.Add(NewGameCycleEqual(completion_count=6))
    SkipLinesIfConditionFalse(2, AND_7)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_8.Add(NewGameCycleGreaterThanOrEqual(completion_count=7))
    SkipLinesIfConditionFalse(2, AND_8)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@NeverRestart(1047382569)
def Event_1047382569(_, flag: uint, asset: uint):
    """Event 1047382569"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAsset(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, vfx_id=101, model_point=806043)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    DeleteAssetVFX(asset)
    PlaySoundEffect(asset, 90011, sound_type=SoundType.s_SFX)
    Wait(0.5)
    DisableAsset(asset)


@NeverRestart(1047381580)
def Event_1047381580():
    """Event 1047381580"""
    RegisterLadder(start_climbing_flag=1047380580, stop_climbing_flag=1047380581, asset=Assets.AEG030_017_2000)
    RegisterLadder(start_climbing_flag=1047380582, stop_climbing_flag=1047380583, asset=Assets.AEG030_902_2001)
    RegisterLadder(start_climbing_flag=1047380584, stop_climbing_flag=1047380585, asset=Assets.AEG030_017_2001)
