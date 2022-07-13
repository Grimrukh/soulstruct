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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=301900, obj=30191950, unknown=5.0)
    RunCommonEvent(0, 900005610, args=(30191150, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005200, args=(30190200, 30003, 20003, 30192201, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30190201, 30192207, 0.0, 3004), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(30190203, 30010, 20010, 30192203, 7.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(30190206, 30192220, 0.0, 3004), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30190210, 30192210, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30190211, 30192210, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005201, args=(30190212, 30001, 20001, 6.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(30190236, 30010, 20010, 30192210, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(30190210, 30002, 20002, 30192210, 0.10000000149011612, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(30190204, 30002, 20002, 30192210, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30190205, 30002, 20002, 30192210, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30190214, 30192210, 0.0, 3005), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30190225, 30192225, 1.5, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30190226, 30192225, 2.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30190227, 30192225, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30190228, 30192225, 0.5, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30190225, 30000, 20000, 30192225, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30190226, 30000, 20000, 30192225, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30190227, 30000, 20000, 30192225, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30190228, 30000, 20000, 30192225, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30190222, 30192203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30190220, 30192204, 0.0, 3003), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30190303, 30192302, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30190235, 30001, 20001, 30192209, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30190301, 30192301, 0.0, 3025), arg_types="IIfi")
    Event_30192201()
    RunCommonEvent(0, 90005211, args=(30190202, 30010, 20010, 30192300, 7.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30190237, 30002, 20002, 30192214, 7.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(30190234, 30192208, 0.0, 3006), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(30190223, 30000, 20000, 30192211, 7.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(1, 90005200, args=(30190230, 30001, 20001, 30192206, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30190403, 30192400, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30190302, 30192400, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(1, 90005200, args=(30190402, 30000, 20000, 30192400, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(301900401, 30192401, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005650, args=(30190540, 30191540, 30191541, 30193541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30190540, 30191540), arg_types="II")
    RunCommonEvent(0, 90005680, args=(30190505, 30190506, 30190507, 30190508, 30191505), arg_types="IIIII")
    RunCommonEvent(0, 90005681, args=(30190505, 30190506, 30190507, 30190508, 30191505), arg_types="IIIII")
    RunCommonEvent(0, 90005680, args=(30190505, 30190506, 30190507, 30190508, 30191505), arg_types="IIIII")
    RunCommonEvent(0, 90005680, args=(30190500, 30190501, 30190502, 30190503, 30191500), arg_types="IIIII")
    RunCommonEvent(0, 90005681, args=(30190500, 30190501, 30190502, 30190503, 30191500), arg_types="IIIII")
    RunCommonEvent(0, 90005680, args=(30190500, 30190501, 30190502, 30190503, 30191500), arg_types="IIIII")
    Event_30192600()
    Event_30192500(
        0,
        flag=30190503,
        source_entity=30191500,
        region=30192500,
        owner_entity=30190500,
        behavior_id=801110000,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0
    )
    Event_30192501(
        0,
        flag=30190503,
        source_entity=30191500,
        region=30192500,
        owner_entity=30190500,
        behavior_id=801110010,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0
    )
    Event_30192502(
        0,
        flag=30190503,
        source_entity=30191500,
        region=30192500,
        owner_entity=30190500,
        behavior_id=801110020,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0
    )
    Event_30192503(
        0,
        flag=30190503,
        source_entity=30191500,
        region=30192500,
        owner_entity=30190500,
        behavior_id=801110030,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0
    )
    Event_30192504(
        0,
        flag=30190503,
        source_entity=30191500,
        region=30192500,
        owner_entity=30190500,
        behavior_id=801110040,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0
    )
    Event_30192505(
        0,
        flag=30190503,
        source_entity=30191500,
        region=30192500,
        owner_entity=30190500,
        behavior_id=801110050,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0
    )
    Event_30192506(
        0,
        flag=30190503,
        source_entity=30191500,
        region=30192500,
        owner_entity=30190500,
        behavior_id=801110060,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0
    )
    Event_30192507(
        0,
        flag=30190503,
        source_entity=30191500,
        region=30192500,
        owner_entity=30190500,
        behavior_id=801110070,
        behavior_id_1=801110005,
        model_point=102,
        model_point_1=0,
        model_point_2=105,
        model_point_3=107,
        model_point_4=0,
        model_point_5=0,
        model_point_6=0,
        model_point_7=0
    )
    Event_30190050()
    Event_30192800()
    Event_30192801()
    Event_30192849()
    Event_30192811()
    RunCommonEvent(
        0,
        90005646,
        args=(30190800, 30192840, 30192841, 30191840, 30192840, 30, 19, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 91005600, args=(30192800, 30191695, 5), arg_types="IIi")


@NeverRestart(30190050)
def Event_30190050():
    """Event 30190050"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(30190505)
    EnableFlag(30190500)
    EnableFlag(30190503)


@NeverRestart(30192210)
def Event_30192210(_, flag: uint, entity: uint):
    """Event 30192210"""
    SkipLinesIfFlagDisabled(2, flag)
    ForceAnimation(entity, 11, unknown2=1.0)
    End()
    ForceAnimation(entity, 1, unknown2=1.0)
    IfObjectActivated(MAIN, obj_act_id=30193200)
    ForceAnimation(entity, 13, unknown2=1.0)


@RestartOnRest(30192201)
def Event_30192201():
    """Event 30192201"""
    EndIfThisEventSlotFlagEnabled()
    IfAttackedWithDamageType(OR_2, attacked_entity=30190301, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=30190301, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=30190301, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=30190301, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=30190301, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=30190301, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    ClearTargetList(30190301)
    ForceAnimation(30190301, 3025, loop=True, unknown2=1.0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    SkipLinesIfValueEqual(1, left=3025, right=-1)
    ForceAnimation(30190301, 3025, loop=True, unknown2=1.0)

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
    IfFlagDisabled(OR_1, 50)
    IfFlagEnabled(OR_1, 51)
    IfFlagEnabled(OR_1, 52)
    IfFlagEnabled(OR_1, 53)
    IfFlagEnabled(OR_1, 54)
    IfFlagEnabled(OR_1, 55)
    IfFlagEnabled(OR_1, 56)
    IfFlagEnabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagDisabled(AND_1, flag)
    SkipLinesIfUnsignedEqual(1, left=region, right=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(2.0)
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    IfFlagDisabled(OR_1, 50)
    IfFlagDisabled(OR_1, 51)
    IfFlagEnabled(OR_1, 52)
    IfFlagEnabled(OR_1, 53)
    IfFlagEnabled(OR_1, 54)
    IfFlagEnabled(OR_1, 55)
    IfFlagEnabled(OR_1, 56)
    IfFlagEnabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagDisabled(AND_1, flag)
    SkipLinesIfUnsignedEqual(1, left=region, right=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    IfFlagDisabled(OR_1, 50)
    IfFlagDisabled(OR_1, 51)
    IfFlagDisabled(OR_1, 52)
    IfFlagEnabled(OR_1, 53)
    IfFlagEnabled(OR_1, 54)
    IfFlagEnabled(OR_1, 55)
    IfFlagEnabled(OR_1, 56)
    IfFlagEnabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagDisabled(AND_1, flag)
    SkipLinesIfUnsignedEqual(1, left=region, right=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    IfFlagDisabled(OR_1, 50)
    IfFlagDisabled(OR_1, 51)
    IfFlagDisabled(OR_1, 52)
    IfFlagDisabled(OR_1, 53)
    IfFlagEnabled(OR_1, 54)
    IfFlagEnabled(OR_1, 55)
    IfFlagEnabled(OR_1, 56)
    IfFlagEnabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagDisabled(AND_1, flag)
    SkipLinesIfUnsignedEqual(1, left=region, right=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    IfFlagDisabled(OR_1, 50)
    IfFlagDisabled(OR_1, 51)
    IfFlagDisabled(OR_1, 52)
    IfFlagDisabled(OR_1, 53)
    IfFlagDisabled(OR_1, 54)
    IfFlagEnabled(OR_1, 55)
    IfFlagEnabled(OR_1, 56)
    IfFlagEnabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagDisabled(AND_1, flag)
    SkipLinesIfUnsignedEqual(1, left=region, right=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    IfFlagDisabled(OR_1, 50)
    IfFlagDisabled(OR_1, 51)
    IfFlagDisabled(OR_1, 52)
    IfFlagDisabled(OR_1, 53)
    IfFlagDisabled(OR_1, 54)
    IfFlagDisabled(OR_1, 55)
    IfFlagEnabled(OR_1, 56)
    IfFlagEnabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagDisabled(AND_1, flag)
    SkipLinesIfUnsignedEqual(1, left=region, right=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    IfFlagDisabled(OR_1, 50)
    IfFlagDisabled(OR_1, 51)
    IfFlagDisabled(OR_1, 52)
    IfFlagDisabled(OR_1, 53)
    IfFlagDisabled(OR_1, 54)
    IfFlagDisabled(OR_1, 55)
    IfFlagDisabled(OR_1, 56)
    IfFlagEnabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagDisabled(AND_1, flag)
    SkipLinesIfUnsignedEqual(1, left=region, right=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    IfFlagDisabled(OR_1, 50)
    IfFlagDisabled(OR_1, 51)
    IfFlagDisabled(OR_1, 52)
    IfFlagDisabled(OR_1, 53)
    IfFlagDisabled(OR_1, 54)
    IfFlagDisabled(OR_1, 55)
    IfFlagDisabled(OR_1, 56)
    IfFlagDisabled(OR_1, 57)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagDisabled(AND_1, flag)
    SkipLinesIfUnsignedEqual(1, left=region, right=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=102100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
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
def Event_30192520(_, flag: uint, obj: uint, flag_1: uint):
    """Event 30192520"""
    EndIfFlagEnabled(flag)
    DisableObjectActivation(obj, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    EnableObjectActivation(obj, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    EnableObjectActivation(obj, obj_act_id=-1)


@NeverRestart(30192600)
def Event_30192600():
    """Event 30192600"""
    RunCommonEvent(0, 90005681, args=(30190505, 30190506, 30190507, 30190508, 30191505), arg_types="IIIII")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(
        0,
        90005682,
        args=(30190507, 30191505, 30192505, 30190505, 801110070, 801110005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(
        0,
        90005682,
        args=(30190507, 30191505, 30192505, 30190505, 801110060, 801110005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(
        0,
        90005682,
        args=(30190507, 30191505, 30192505, 30190505, 801110050, 801110005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(
        0,
        90005682,
        args=(30190507, 30191505, 30192505, 30190505, 801110040, 801110005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(
        0,
        90005682,
        args=(30190507, 30191505, 30192505, 30190505, 801110030, 801110005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(
        0,
        90005682,
        args=(30190507, 30191505, 30192505, 30190505, 801110020, 801110005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(
        0,
        90005682,
        args=(30190507, 30191505, 30192505, 30190505, 801110010, 801110005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(
        0,
        90005682,
        args=(30190507, 30191505, 30192505, 30190505, 801110000, 801110005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    RunCommonEvent(0, 90005681, args=(30190500, 30190501, 30190502, 30190503, 30191500), arg_types="IIIII")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(
        0,
        90005682,
        args=(30190502, 30191500, 30192500, 30190500, 801110070, 801110005, 104, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(
        0,
        90005682,
        args=(30190502, 30191500, 30192500, 30190500, 801110060, 801110005, 104, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(
        0,
        90005682,
        args=(30190502, 30191500, 30192500, 30190500, 801110050, 801110005, 104, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(
        0,
        90005682,
        args=(30190502, 30191500, 30192500, 30190500, 801110040, 801110005, 104, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(
        0,
        90005682,
        args=(30190502, 30191500, 30192500, 30190500, 801110030, 801110005, 104, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(
        0,
        90005682,
        args=(30190502, 30191500, 30192500, 30190500, 801110020, 801110005, 104, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(
        0,
        90005682,
        args=(30190502, 30191500, 30192500, 30190500, 801110010, 801110005, 104, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(
        0,
        90005682,
        args=(30190502, 30191500, 30192500, 30190500, 801110000, 801110005, 104, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )


@RestartOnRest(30192800)
def Event_30192800():
    """Event 30192800"""
    EndIfFlagEnabled(30190800)
    IfHealthValueLessThanOrEqual(MAIN, 30190800, value=0)
    Wait(4.0)
    PlaySoundEffect(30190800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30190800)
    KillBossAndDisplayBanner(character=30190800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30190800)
    EnableFlag(9219)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61219)


@RestartOnRest(30192801)
def Event_30192801():
    """Event 30192801"""
    GotoIfFlagDisabled(Label.L0, flag=30190800)
    DisableCharacter(30190800)
    DisableAnimations(30190800)
    Kill(30190800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30190800)
    IfFlagEnabled(AND_2, 30192805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30192800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30190800)
    SetNetworkUpdateRate(30190800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30190800, name=903400302)


@RestartOnRest(30192811)
def Event_30192811():
    """Event 30192811"""
    EndIfFlagEnabled(30190800)
    IfHealthRatioLessThanOrEqual(AND_1, 30190800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30192802)


@RestartOnRest(30192849)
def Event_30192849():
    """Event 30192849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30190800, 30191800, 30192800, 30192805, 30195800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30190800, 30191800, 30192800, 30192805, 30192806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30190800, 30191800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30190800, 930000, 30192805, 30192806, 0, 30192802, 0, 0), arg_types="IiIIIIii")
