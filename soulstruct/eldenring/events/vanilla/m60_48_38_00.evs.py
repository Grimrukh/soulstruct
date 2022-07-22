"""
South Caelid (NW) (SW)

linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_48_38_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1048380000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76418,
        flag_1=76406,
        asset=Assets.AEG099_090_9001,
        source_flag=77400,
        value=4,
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
    RegisterGrace(grace_flag=1048380001, asset=Assets.AEG099_060_9001)
    CommonFunc_90005100(
        0,
        flag=76418,
        flag_1=76407,
        asset=Assets.AEG099_090_9000,
        source_flag=77400,
        value=3,
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
    CommonFunc_90005631(0, anchor_entity=Assets.AEG099_376_1000, text=61040)
    CommonFunc_90005790(
        0,
        right=0,
        flag=1048380180,
        summon_flag=1048382181,
        dismissal_flag=1048382182,
        character=Characters.Millicent,
        sign_type=23,
        region=1048382705,
        region_1=1048382706,
        seconds=0.0,
        right_1=1050389259,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=1048380180, flag_1=1048382181, flag_2=1048382182, character=Characters.Millicent)
    CommonFunc_90005792(
        0,
        flag=1048380180,
        flag_1=1048382181,
        flag_2=1048382182,
        character=Characters.Millicent,
        item_lot=1048380500,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=1048380180,
        flag_1=1048382181,
        flag_2=1048382182,
        character=Characters.Millicent,
        other_entity=1048382705,
        region=0,
        left=0,
    )
    CommonFunc_90005300(0, flag=1048380290, character=Characters.Scarab, item_lot=40402, seconds=0.0, left=0)
    Event_1048382201()
    Event_1048382200(0, source_entity=Assets.AEG099_046_1000, seconds=2.0)
    Event_1048382200(1, source_entity=Assets.AEG099_046_1001, seconds=4.0)
    Event_1048382200(2, source_entity=Assets.AEG099_046_1002, seconds=14.0)
    Event_1048382200(3, source_entity=Assets.AEG099_046_1003, seconds=5.0)
    Event_1048382200(4, source_entity=Assets.AEG099_046_1004, seconds=9.0)
    CommonFunc_90005250(0, character=Characters.MirandaRotFlower0, region=1048382200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.MirandaRotFlower1, region=1048382200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.MirandaRotFlower2, region=1048382200, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.MirandaRotFlower3,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.MirandaRotFlower4,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.MirandaRotFlower5,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.MirandaRotFlower6,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.MirandaRotFlower7,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.MirandaRotFlower8,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.MirandaRotFlower9,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.MirandaRotFlower10,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.MirandaRotFlower11,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.MirandaRotFlower12, radius=12.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.MirandaRotFlower13, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1048380300, region=1048382300, seconds=0.0, animation_id=-1)
    CommonFunc_90005725(
        0,
        flag=4775,
        flag_1=4776,
        flag_2=4778,
        flag_3=1048389205,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        asset=1048386700,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4776,
        flag_1=4777,
        flag_2=1048389206,
        flag_3=4776,
        first_flag=4775,
        last_flag=4779,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4776, flag_1=4775, flag_2=1048389206, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4778, first_flag=4775, last_flag=4779)
    CommonFunc_90005703(
        0,
        character=Characters.NomadMule,
        flag=4776,
        flag_1=4777,
        flag_2=1048389207,
        flag_3=4776,
        first_flag=4775,
        last_flag=4779,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.NomadMule, flag=4776, flag_1=4775, flag_2=1048389207, right=3)
    CommonFunc_90005728(0, attacked_entity=Characters.NomadMule, flag=1048382706, flag_1=1048382707)
    CommonFunc_90005727(
        0,
        flag=4776,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        first_flag=4775,
        last_flag=4778,
    )
    CommonFunc_90005729(0, flag=1048389200, character=Characters.Merchant, distance=54.0, flag_1=1048382702)
    CommonFunc_90005706(0, 1048380701, 930023, 0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Millicent)
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.NomadMule)
    DisableBackread(1048380710)
    DisableBackread(Characters.WanderingNoble)


@RestartOnRest(1048382200)
def Event_1048382200(_, source_entity: uint, seconds: float):
    """Event 1048382200"""
    EnableNetworkSync()
    Wait(8.0)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=source_entity, radius=70.0))
    
    Wait(seconds)
    AND_1.Add(NewGameCycleEqual(completion_count=0))
    SkipLinesIfConditionFalse(2, AND_1)
    ShootProjectile(
        owner_entity=Characters.Dummy,
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
        owner_entity=Characters.Dummy,
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
        owner_entity=Characters.Dummy,
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
        owner_entity=Characters.Dummy,
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
        owner_entity=Characters.Dummy,
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
        owner_entity=Characters.Dummy,
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
        owner_entity=Characters.Dummy,
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
        owner_entity=Characters.Dummy,
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


@RestartOnRest(1048382201)
def Event_1048382201():
    """Event 1048382201"""
    CreateProjectileOwner(entity=Characters.Dummy)
