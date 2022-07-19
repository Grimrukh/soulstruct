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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m30_19_00_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=301900, asset=Assets.AEG099_060_9000)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005200(
        0,
        character=Characters.Imp2,
        animation_id=30003,
        animation_id_1=20003,
        region=30192201,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Imp1, region=30192207, seconds=0.0, animation_id=3004)
    CommonFunc_90005211(
        0,
        character=Characters.Imp8,
        animation_id=30010,
        animation_id_1=20010,
        region=30192203,
        radius=7.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Imp4, region=30192220, seconds=0.0, animation_id=3004)
    CommonFunc_90005250(0, 30190210, 30192210, 0.0, -1)
    CommonFunc_90005250(0, 30190211, 30192210, 0.0, -1)
    CommonFunc_90005201(
        0,
        character=30190212,
        animation_id=30001,
        animation_id_1=20001,
        radius=6.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp6,
        animation_id=30010,
        animation_id_1=20010,
        region=30192210,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp7,
        animation_id=30002,
        animation_id_1=20002,
        region=30192210,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp5,
        animation_id=30002,
        animation_id_1=20002,
        region=30192210,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp3,
        animation_id=30002,
        animation_id_1=20002,
        region=30192210,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=30190214, region=30192210, seconds=0.0, animation_id=3005)
    CommonFunc_90005250(0, 30190225, 30192225, 1.5, -1)
    CommonFunc_90005250(0, 30190226, 30192225, 2.0, -1)
    CommonFunc_90005250(0, 30190227, 30192225, 0.0, -1)
    CommonFunc_90005250(0, 30190228, 30192225, 0.5, -1)
    CommonFunc_90005200(
        0,
        character=30190225,
        animation_id=30000,
        animation_id_1=20000,
        region=30192225,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30190226,
        animation_id=30000,
        animation_id_1=20000,
        region=30192225,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30190227,
        animation_id=30000,
        animation_id_1=20000,
        region=30192225,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30190228,
        animation_id=30000,
        animation_id_1=20000,
        region=30192225,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 30190222, 30192203, 0.0, -1)
    CommonFunc_90005250(0, character=Characters.Imp9, region=30192204, seconds=0.0, animation_id=3003)
    CommonFunc_90005250(0, 30190303, 30192302, 0.0, -1)
    CommonFunc_90005200(
        0,
        character=30190235,
        animation_id=30001,
        animation_id_1=20001,
        region=30192209,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.ErdtreeBurialWatchdog0, region=30192301, seconds=0.0, animation_id=3025)
    Event_30192201()
    CommonFunc_90005211(
        0,
        character=30190202,
        animation_id=30010,
        animation_id_1=20010,
        region=30192300,
        radius=7.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=30190237,
        animation_id=30002,
        animation_id_1=20002,
        region=30192214,
        radius=7.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Imp0, region=30192208, seconds=0.0, animation_id=3006)
    CommonFunc_90005211(
        0,
        character=Characters.Imp10,
        animation_id=30000,
        animation_id_1=20000,
        region=30192211,
        radius=7.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=30190230,
        animation_id=30001,
        animation_id_1=20001,
        region=30192206,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 30190403, 30192400, 0.0, -1)
    CommonFunc_90005250(0, 30190302, 30192400, 0.0, -1)
    CommonFunc_90005200(
        1,
        character=Characters.CleanrotKnight1,
        animation_id=30000,
        animation_id_1=20000,
        region=30192400,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 301900401, 30192401, 0.0, -1)
    CommonFunc_90005650(
        0,
        flag=30190540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_0500,
        obj_act_id=30193541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30190540, anchor_entity=Assets.AEG027_041_0500)
    CommonFunc_90005680(
        0,
        flag=30190505,
        flag_1=30190506,
        flag_2=30190507,
        flag_3=30190508,
        asset=Assets.AEG027_156_0500,
    )
    CommonFunc_90005681(
        0,
        flag=30190505,
        flag_1=30190506,
        flag_2=30190507,
        flag_3=30190508,
        attacked_entity=Assets.AEG027_156_0500,
    )
    CommonFunc_90005680(
        0,
        flag=30190505,
        flag_1=30190506,
        flag_2=30190507,
        flag_3=30190508,
        asset=Assets.AEG027_156_0500,
    )
    CommonFunc_90005680(
        0,
        flag=30190500,
        flag_1=30190501,
        flag_2=30190502,
        flag_3=30190503,
        asset=Assets.AEG027_215_0500,
    )
    CommonFunc_90005681(
        0,
        flag=30190500,
        flag_1=30190501,
        flag_2=30190502,
        flag_3=30190503,
        attacked_entity=Assets.AEG027_215_0500,
    )
    CommonFunc_90005680(
        0,
        flag=30190500,
        flag_1=30190501,
        flag_2=30190502,
        flag_3=30190503,
        asset=Assets.AEG027_215_0500,
    )
    Event_30192600()
    Event_30192500(
        0,
        flag=30190503,
        source_entity=Assets.AEG027_215_0500,
        region=30192500,
        owner_entity=Characters.TalkDummy0,
        behavior_id=801110000,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0,
    )
    Event_30192501(
        0,
        flag=30190503,
        source_entity=Assets.AEG027_215_0500,
        region=30192500,
        owner_entity=Characters.TalkDummy0,
        behavior_id=801110010,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0,
    )
    Event_30192502(
        0,
        flag=30190503,
        source_entity=Assets.AEG027_215_0500,
        region=30192500,
        owner_entity=Characters.TalkDummy0,
        behavior_id=801110020,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0,
    )
    Event_30192503(
        0,
        flag=30190503,
        source_entity=Assets.AEG027_215_0500,
        region=30192500,
        owner_entity=Characters.TalkDummy0,
        behavior_id=801110030,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0,
    )
    Event_30192504(
        0,
        flag=30190503,
        source_entity=Assets.AEG027_215_0500,
        region=30192500,
        owner_entity=Characters.TalkDummy0,
        behavior_id=801110040,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0,
    )
    Event_30192505(
        0,
        flag=30190503,
        source_entity=Assets.AEG027_215_0500,
        region=30192500,
        owner_entity=Characters.TalkDummy0,
        behavior_id=801110050,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0,
    )
    Event_30192506(
        0,
        flag=30190503,
        source_entity=Assets.AEG027_215_0500,
        region=30192500,
        owner_entity=Characters.TalkDummy0,
        behavior_id=801110060,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0,
    )
    Event_30192507(
        0,
        flag=30190503,
        source_entity=Assets.AEG027_215_0500,
        region=30192500,
        owner_entity=Characters.TalkDummy0,
        behavior_id=801110070,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0,
    )
    Event_30190050()
    Event_30192800()
    Event_30192801()
    Event_30192849()
    Event_30192811()
    CommonFunc_90005646(
        0,
        flag=30190800,
        left_flag=30192840,
        cancel_flag__right_flag=30192841,
        asset=Assets.AEG099_065_9000,
        player_start=30192840,
        area_id=30,
        block_id=19,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_91005600(0, 30192800, 30191695, 5)


@NeverRestart(30190050)
def Event_30190050():
    """Event 30190050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30190505)
    EnableFlag(30190500)
    EnableFlag(30190503)


@NeverRestart(30192210)
def Event_30192210(_, flag: uint, entity: uint):
    """Event 30192210"""
    if FlagEnabled(flag):
        ForceAnimation(entity, 11)
        End()
    ForceAnimation(entity, 1)
    
    MAIN.Await(AssetActivated(obj_act_id=30193200))
    
    ForceAnimation(entity, 13)


@RestartOnRest(30192201)
def Event_30192201():
    """Event 30192201"""
    if ThisEventSlotFlagEnabled():
        return
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.ErdtreeBurialWatchdog0, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=Characters.ErdtreeBurialWatchdog0, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.ErdtreeBurialWatchdog0, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.ErdtreeBurialWatchdog0, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.ErdtreeBurialWatchdog0, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.ErdtreeBurialWatchdog0, state_info=260))
    
    MAIN.Await(OR_2)
    
    ClearTargetList(Characters.ErdtreeBurialWatchdog0)
    ForceAnimation(Characters.ErdtreeBurialWatchdog0, 3025, loop=True)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    if ValueNotEqual(left=3025, right=-1):
        ForceAnimation(Characters.ErdtreeBurialWatchdog0, 3025, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)


@NeverRestart(30192500)
def Event_30192500(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    model_point: int,
    model_point_1: int,
    model_point_2: int,
    model_point_3: int,
    model_point_4: int,
    model_point_5: int,
    model_point_6: int,
    model_point_7: int,
):
    """Event 30192500"""
    OR_1.Add(FlagDisabled(50))
    OR_1.Add(FlagEnabled(51))
    OR_1.Add(FlagEnabled(52))
    OR_1.Add(FlagEnabled(53))
    OR_1.Add(FlagEnabled(54))
    OR_1.Add(FlagEnabled(55))
    OR_1.Add(FlagEnabled(56))
    OR_1.Add(FlagEnabled(57))
    if OR_1:
        return
    AND_1.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=region, right=0):
        AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    Wait(2.0)
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=model_point_1, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=model_point_2, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfValueComparison(Label.L5, comparison_type=ComparisonType.Equal, left=model_point_4, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfValueComparison(Label.L6, comparison_type=ComparisonType.Equal, left=model_point_5, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfValueComparison(Label.L7, comparison_type=ComparisonType.Equal, left=model_point_6, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfValueComparison(Label.L8, comparison_type=ComparisonType.Equal, left=model_point_7, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 8 --- #
    DefineLabel(8)
    Wait(5.199999809265137)
    Restart()


@NeverRestart(30192501)
def Event_30192501(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    model_point: int,
    model_point_1: int,
    model_point_2: int,
    model_point_3: int,
    model_point_4: int,
    model_point_5: int,
    model_point_6: int,
    model_point_7: int,
):
    """Event 30192501"""
    OR_1.Add(FlagDisabled(50))
    OR_1.Add(FlagDisabled(51))
    OR_1.Add(FlagEnabled(52))
    OR_1.Add(FlagEnabled(53))
    OR_1.Add(FlagEnabled(54))
    OR_1.Add(FlagEnabled(55))
    OR_1.Add(FlagEnabled(56))
    OR_1.Add(FlagEnabled(57))
    if OR_1:
        return
    AND_1.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=region, right=0):
        AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=model_point_1, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=model_point_2, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfValueComparison(Label.L5, comparison_type=ComparisonType.Equal, left=model_point_4, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfValueComparison(Label.L6, comparison_type=ComparisonType.Equal, left=model_point_5, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfValueComparison(Label.L7, comparison_type=ComparisonType.Equal, left=model_point_6, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfValueComparison(Label.L8, comparison_type=ComparisonType.Equal, left=model_point_7, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 8 --- #
    DefineLabel(8)
    Wait(7.199999809265137)
    Restart()


@NeverRestart(30192502)
def Event_30192502(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    model_point: int,
    model_point_1: int,
    model_point_2: int,
    model_point_3: int,
    model_point_4: int,
    model_point_5: int,
    model_point_6: int,
    model_point_7: int,
):
    """Event 30192502"""
    OR_1.Add(FlagDisabled(50))
    OR_1.Add(FlagDisabled(51))
    OR_1.Add(FlagDisabled(52))
    OR_1.Add(FlagEnabled(53))
    OR_1.Add(FlagEnabled(54))
    OR_1.Add(FlagEnabled(55))
    OR_1.Add(FlagEnabled(56))
    OR_1.Add(FlagEnabled(57))
    if OR_1:
        return
    AND_1.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=region, right=0):
        AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=model_point_1, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=model_point_2, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfValueComparison(Label.L5, comparison_type=ComparisonType.Equal, left=model_point_4, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfValueComparison(Label.L6, comparison_type=ComparisonType.Equal, left=model_point_5, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfValueComparison(Label.L7, comparison_type=ComparisonType.Equal, left=model_point_6, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfValueComparison(Label.L8, comparison_type=ComparisonType.Equal, left=model_point_7, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 8 --- #
    DefineLabel(8)
    Wait(7.199999809265137)
    Restart()


@NeverRestart(30192503)
def Event_30192503(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    model_point: int,
    model_point_1: int,
    model_point_2: int,
    model_point_3: int,
    model_point_4: int,
    model_point_5: int,
    model_point_6: int,
    model_point_7: int,
):
    """Event 30192503"""
    OR_1.Add(FlagDisabled(50))
    OR_1.Add(FlagDisabled(51))
    OR_1.Add(FlagDisabled(52))
    OR_1.Add(FlagDisabled(53))
    OR_1.Add(FlagEnabled(54))
    OR_1.Add(FlagEnabled(55))
    OR_1.Add(FlagEnabled(56))
    OR_1.Add(FlagEnabled(57))
    if OR_1:
        return
    AND_1.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=region, right=0):
        AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=model_point_1, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=model_point_2, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfValueComparison(Label.L5, comparison_type=ComparisonType.Equal, left=model_point_4, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfValueComparison(Label.L6, comparison_type=ComparisonType.Equal, left=model_point_5, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfValueComparison(Label.L7, comparison_type=ComparisonType.Equal, left=model_point_6, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfValueComparison(Label.L8, comparison_type=ComparisonType.Equal, left=model_point_7, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 8 --- #
    DefineLabel(8)
    Wait(7.199999809265137)
    Restart()


@NeverRestart(30192504)
def Event_30192504(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    model_point: int,
    model_point_1: int,
    model_point_2: int,
    model_point_3: int,
    model_point_4: int,
    model_point_5: int,
    model_point_6: int,
    model_point_7: int,
):
    """Event 30192504"""
    OR_1.Add(FlagDisabled(50))
    OR_1.Add(FlagDisabled(51))
    OR_1.Add(FlagDisabled(52))
    OR_1.Add(FlagDisabled(53))
    OR_1.Add(FlagDisabled(54))
    OR_1.Add(FlagEnabled(55))
    OR_1.Add(FlagEnabled(56))
    OR_1.Add(FlagEnabled(57))
    if OR_1:
        return
    AND_1.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=region, right=0):
        AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=model_point_1, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=model_point_2, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfValueComparison(Label.L5, comparison_type=ComparisonType.Equal, left=model_point_4, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfValueComparison(Label.L6, comparison_type=ComparisonType.Equal, left=model_point_5, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfValueComparison(Label.L7, comparison_type=ComparisonType.Equal, left=model_point_6, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfValueComparison(Label.L8, comparison_type=ComparisonType.Equal, left=model_point_7, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 8 --- #
    DefineLabel(8)
    Wait(7.199999809265137)
    Restart()


@NeverRestart(30192505)
def Event_30192505(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    model_point: int,
    model_point_1: int,
    model_point_2: int,
    model_point_3: int,
    model_point_4: int,
    model_point_5: int,
    model_point_6: int,
    model_point_7: int,
):
    """Event 30192505"""
    OR_1.Add(FlagDisabled(50))
    OR_1.Add(FlagDisabled(51))
    OR_1.Add(FlagDisabled(52))
    OR_1.Add(FlagDisabled(53))
    OR_1.Add(FlagDisabled(54))
    OR_1.Add(FlagDisabled(55))
    OR_1.Add(FlagEnabled(56))
    OR_1.Add(FlagEnabled(57))
    if OR_1:
        return
    AND_1.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=region, right=0):
        AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=model_point_1, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=model_point_2, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfValueComparison(Label.L5, comparison_type=ComparisonType.Equal, left=model_point_4, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfValueComparison(Label.L6, comparison_type=ComparisonType.Equal, left=model_point_5, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfValueComparison(Label.L7, comparison_type=ComparisonType.Equal, left=model_point_6, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfValueComparison(Label.L8, comparison_type=ComparisonType.Equal, left=model_point_7, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 8 --- #
    DefineLabel(8)
    Wait(7.199999809265137)
    Restart()


@NeverRestart(30192506)
def Event_30192506(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    model_point: int,
    model_point_1: int,
    model_point_2: int,
    model_point_3: int,
    model_point_4: int,
    model_point_5: int,
    model_point_6: int,
    model_point_7: int,
):
    """Event 30192506"""
    OR_1.Add(FlagDisabled(50))
    OR_1.Add(FlagDisabled(51))
    OR_1.Add(FlagDisabled(52))
    OR_1.Add(FlagDisabled(53))
    OR_1.Add(FlagDisabled(54))
    OR_1.Add(FlagDisabled(55))
    OR_1.Add(FlagDisabled(56))
    OR_1.Add(FlagEnabled(57))
    if OR_1:
        return
    AND_1.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=region, right=0):
        AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=model_point_1, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=model_point_2, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfValueComparison(Label.L5, comparison_type=ComparisonType.Equal, left=model_point_4, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfValueComparison(Label.L6, comparison_type=ComparisonType.Equal, left=model_point_5, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfValueComparison(Label.L7, comparison_type=ComparisonType.Equal, left=model_point_6, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfValueComparison(Label.L8, comparison_type=ComparisonType.Equal, left=model_point_7, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 8 --- #
    DefineLabel(8)
    Wait(7.199999809265137)
    Restart()


@NeverRestart(30192507)
def Event_30192507(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    model_point: int,
    model_point_1: int,
    model_point_2: int,
    model_point_3: int,
    model_point_4: int,
    model_point_5: int,
    model_point_6: int,
    model_point_7: int,
):
    """Event 30192507"""
    OR_1.Add(FlagDisabled(50))
    OR_1.Add(FlagDisabled(51))
    OR_1.Add(FlagDisabled(52))
    OR_1.Add(FlagDisabled(53))
    OR_1.Add(FlagDisabled(54))
    OR_1.Add(FlagDisabled(55))
    OR_1.Add(FlagDisabled(56))
    OR_1.Add(FlagDisabled(57))
    if OR_1:
        return
    AND_1.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=region, right=0):
        AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=model_point_1, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=model_point_2, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfValueComparison(Label.L5, comparison_type=ComparisonType.Equal, left=model_point_4, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_4,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfValueComparison(Label.L6, comparison_type=ComparisonType.Equal, left=model_point_5, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_5,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfValueComparison(Label.L7, comparison_type=ComparisonType.Equal, left=model_point_6, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_6,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfValueComparison(Label.L8, comparison_type=ComparisonType.Equal, left=model_point_7, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_7,
            behavior_id=102102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 8 --- #
    DefineLabel(8)
    Wait(7.199999809265137)
    Restart()


@RestartOnRest(30192520)
def Event_30192520(_, flag: uint, asset: uint, flag_1: uint):
    """Event 30192520"""
    if FlagEnabled(flag):
        return
    DisableAssetActivation(asset, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    EnableAssetActivation(asset, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableAssetActivation(asset, obj_act_id=-1)


@NeverRestart(30192600)
def Event_30192600():
    """Event 30192600"""
    CommonFunc_90005681(
        0,
        flag=30190505,
        flag_1=30190506,
        flag_2=30190507,
        flag_3=30190508,
        attacked_entity=Assets.AEG027_156_0500,
    )
    if FlagEnabled(57):
        CommonFunc_90005682(
            0,
            flag=30190507,
            source_entity=Assets.AEG027_156_0500,
            region=30192505,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801110070,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005682(
            0,
            flag=30190507,
            source_entity=Assets.AEG027_156_0500,
            region=30192505,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801110060,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005682(
            0,
            flag=30190507,
            source_entity=Assets.AEG027_156_0500,
            region=30192505,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801110050,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005682(
            0,
            flag=30190507,
            source_entity=Assets.AEG027_156_0500,
            region=30192505,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801110040,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005682(
            0,
            flag=30190507,
            source_entity=Assets.AEG027_156_0500,
            region=30192505,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801110030,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005682(
            0,
            flag=30190507,
            source_entity=Assets.AEG027_156_0500,
            region=30192505,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801110020,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005682(
            0,
            flag=30190507,
            source_entity=Assets.AEG027_156_0500,
            region=30192505,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801110010,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005682(
            0,
            flag=30190507,
            source_entity=Assets.AEG027_156_0500,
            region=30192505,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801110000,
            behavior_id_1=801110005,
            model_point=101,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    CommonFunc_90005681(
        0,
        flag=30190500,
        flag_1=30190501,
        flag_2=30190502,
        flag_3=30190503,
        attacked_entity=Assets.AEG027_215_0500,
    )
    if FlagEnabled(57):
        CommonFunc_90005682(
            0,
            flag=30190502,
            source_entity=Assets.AEG027_215_0500,
            region=30192500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801110070,
            behavior_id_1=801110005,
            model_point=104,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005682(
            0,
            flag=30190502,
            source_entity=Assets.AEG027_215_0500,
            region=30192500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801110060,
            behavior_id_1=801110005,
            model_point=104,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005682(
            0,
            flag=30190502,
            source_entity=Assets.AEG027_215_0500,
            region=30192500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801110050,
            behavior_id_1=801110005,
            model_point=104,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005682(
            0,
            flag=30190502,
            source_entity=Assets.AEG027_215_0500,
            region=30192500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801110040,
            behavior_id_1=801110005,
            model_point=104,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005682(
            0,
            flag=30190502,
            source_entity=Assets.AEG027_215_0500,
            region=30192500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801110030,
            behavior_id_1=801110005,
            model_point=104,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005682(
            0,
            flag=30190502,
            source_entity=Assets.AEG027_215_0500,
            region=30192500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801110020,
            behavior_id_1=801110005,
            model_point=104,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005682(
            0,
            flag=30190502,
            source_entity=Assets.AEG027_215_0500,
            region=30192500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801110010,
            behavior_id_1=801110005,
            model_point=104,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005682(0, 30190502, 30191500, 30192500, 30190500, 801110000, 801110005, 104, 0, 0, 0)


@RestartOnRest(30192800)
def Event_30192800():
    """Event 30192800"""
    if FlagEnabled(30190800):
        return
    
    MAIN.Await(HealthValue(Characters.GraveWardenDuelist) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.GraveWardenDuelist, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.GraveWardenDuelist))
    
    KillBossAndDisplayBanner(character=Characters.GraveWardenDuelist, banner_type=BannerType.EnemyFelled)
    EnableFlag(30190800)
    EnableFlag(9219)
    if PlayerInOwnWorld():
        EnableFlag(61219)


@RestartOnRest(30192801)
def Event_30192801():
    """Event 30192801"""
    GotoIfFlagDisabled(Label.L0, flag=30190800)
    DisableCharacter(Characters.GraveWardenDuelist)
    DisableAnimations(Characters.GraveWardenDuelist)
    Kill(Characters.GraveWardenDuelist)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.GraveWardenDuelist)
    AND_2.Add(FlagEnabled(30192805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30192800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.GraveWardenDuelist)
    SetNetworkUpdateRate(Characters.GraveWardenDuelist, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.GraveWardenDuelist, name=903400302)


@RestartOnRest(30192811)
def Event_30192811():
    """Event 30192811"""
    if FlagEnabled(30190800):
        return
    AND_1.Add(HealthRatio(Characters.GraveWardenDuelist) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30192802)


@RestartOnRest(30192849)
def Event_30192849():
    """Event 30192849"""
    CommonFunc_9005800(
        0,
        flag=30190800,
        entity=Assets.AEG099_001_9000,
        region=30192800,
        flag_1=30192805,
        character=30195800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30190800,
        entity=Assets.AEG099_001_9000,
        region=30192800,
        flag_1=30192805,
        flag_2=30192806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30190800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(0, 30190800, 930000, 30192805, 30192806, 0, 30192802, 0, 0)
