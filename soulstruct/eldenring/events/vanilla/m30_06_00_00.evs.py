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
    RunCommonEvent(
        0,
        90005646,
        args=(30060800, 30062840, 30062841, 30061840, 30062840, 30, 6, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RegisterGrace(grace_flag=300600, obj=30061950, unknown=5.0)
    Event_30062800()
    Event_30062810()
    Event_30062849()
    Event_30062811()
    RunCommonEvent(
        0,
        90005501,
        args=(30060510, 30060511, 0, 30061510, 30061511, 30061512, 30060512),
        arg_types="IIIIIII",
    )
    Event_30062510()
    RunCommonEvent(0, 90005650, args=(30060540, 30061540, 30061541, 30063541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30060540, 30061540), arg_types="II")
    RunCommonEvent(
        0,
        30062400,
        args=(30060600, 30061600, 30062600, 0, 30062601, 30062602, 30062603),
        arg_types="IIIiIII",
    )
    RunCommonEvent(
        1,
        30062400,
        args=(30060605, 30061605, 30062605, 0, 30062606, 30062607, 30062608),
        arg_types="IIIiIII",
    )
    RunCommonEvent(
        2,
        30062400,
        args=(30060610, 30061610, 30062610, 0, 30062611, 30062612, 30062613),
        arg_types="IIIiIII",
    )
    RunCommonEvent(
        3,
        30062400,
        args=(30060615, 30061615, 30062615, 0, 30062616, 30062617, 30062618),
        arg_types="IIIiIII",
    )
    Event_30062580()
    RunCommonEvent(0, 90005410, args=(30062100, 30061100, 30065100), arg_types="III")
    RunCommonEvent(0, 90005411, args=(30061100, 30060100, 10), arg_types="III")
    RunCommonEvent(
        0,
        90005620,
        args=(30060570, 30061570, 30061571, 0, 30062570, 30062571, 30062572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(30060570, 30061573), arg_types="II")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_30060519()
    RunCommonEvent(0, 90005211, args=(30060200, 30009, 20009, 30062200, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005251, args=(30060201, 20.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(30060202, 30062202, 5.0, 1.0, 3002), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(30060203, 30000, 20000, 30062203, 2.0, 2.5999999046325684, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005250, args=(30060204, 30062204, 0.0, 0), arg_types="IIfi")
    Event_30062206()
    RunCommonEvent(0, 90005200, args=(30060205, 30000, 20000, 30062205, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_30062211(0, 30060206, 30010, 20010, 5.0, 0.0, 0, 0, 0, 0)
    Event_30062211(1, 30060207, 30010, 20010, 5.0, 0.0, 0, 0, 0, 0)
    RunCommonEvent(
        0,
        90005211,
        args=(30060208, 30002, 20002, 30062208, 5.0, 2.799999952316284, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(30060209, 30010, 20010, 30062208, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(30060210, 30010, 20010, 30062210, 2.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(30060211, 30010, 20010, 30062210, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30060212, 30003, 20003, 30062212, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005201, args=(30060213, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005211, args=(30060214, 30004, 20004, 30062214, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005201, args=(30060215, 30002, 20002, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005261, args=(30060216, 30062216, 2.0, 0.4000000059604645, 3005), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(0, 0, 0.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005201, args=(30060300, 30001, 20001, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005261, args=(30060301, 30062301, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(30060302, 30000, 20000, 30062302, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 30062300, args=(30060303, 30000, 20000, 30062303, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(30060304, 30062304, 5.0, 0.0, -1), arg_types="IIffi")
    Event_30062304()
    RunCommonEvent(0, 90005200, args=(30060305, 30000, 20000, 30062305, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")


@RestartOnRest(30062206)
def Event_30062206():
    """Event 30062206"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(OR_11, character=PLAYER, region=30062294)
    IfEntityWithinDistance(OR_11, entity=PLAYER, other_entity=30060204, radius=3.0)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfCharacterHasSpecialEffect(AND_4, 30060204, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 30060204, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 30060204, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 30060204, 90160)
    IfCharacterHasSpecialEffect(AND_5, 30060204, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 30060204, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 30060204, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 30060204, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 30060204, 90162)
    IfCharacterHasSpecialEffect(AND_6, 30060204, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 30060204, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 30060204, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 30060204, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 30060204, 90161)
    IfCharacterHasSpecialEffect(AND_7, 30060204, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 30060204, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 30060204, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 30060204, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 30060204, 90162)
    IfCharacterHasSpecialEffect(AND_8, 30060204, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 30060204, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 30060204, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 30060204, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=30060204, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=30060204, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=30060204, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=30060204, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=30060204, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=30060204, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    ForceAnimation(30060204, 3004, loop=True, unknown2=1.0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(30062211)
def Event_30062211(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 30062211"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    IfHasAIStatus(AND_14, 30060301, ai_status=AIStatusType.Battle)
    IfConditionTrue(OR_2, input_condition=AND_14)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterHasSpecialEffect(OR_11, character, 5080)
    IfCharacterHasSpecialEffect(OR_11, character, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfUnsignedEqual(AND_9, left=left_1, right=0)
    IfUnsignedEqual(AND_9, left=left_2, right=0)
    IfUnsignedEqual(AND_9, left=left_3, right=0)
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Battle)
    SkipLinesIfUnsignedEqual(1, left=left_2, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown5)
    SkipLinesIfUnsignedEqual(1, left=left_3, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown4)
    IfConditionTrue(AND_1, input_condition=OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    IfCharacterHasSpecialEffect(AND_4, character, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90160)
    IfCharacterHasSpecialEffect(AND_5, character, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90162)
    IfCharacterHasSpecialEffect(AND_6, character, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90161)
    IfCharacterHasSpecialEffect(AND_7, character, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90162)
    IfCharacterHasSpecialEffect(AND_8, character, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(30062304)
def Event_30062304():
    """Event 30062304"""
    IfCharacterDead(AND_1, 30060304)
    DisableHealthBar(30060304)
    AddSpecialEffect(30060304, 4403)
    Wait(1.0)
    EnableHealthBar(30060304)


@NeverRestart(30062400)
def Event_30062400(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
):
    """Event 30062400"""
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Wait(0.5)
    SkipLinesIfValueEqual(4, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    SkipLinesIfFlagDisabled(3, 50)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 51)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 52)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 53)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 54)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 55)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 56)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 57)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(4, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L1)
    SkipLinesIfFlagDisabled(3, 50)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 51)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 52)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 53)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 54)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 55)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 56)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 57)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(4, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    SkipLinesIfFlagDisabled(3, 50)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 51)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 52)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 53)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 54)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 55)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 56)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 57)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(3.0)
    IfAllPlayersOutsideRegion(MAIN, region=region)
    ForceAnimation(entity, 3, wait_for_completion=True, unknown2=1.0)
    Restart()


@RestartOnRest(30062300)
def Event_30062300(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 30062300"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    DisableAI(character)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterHasSpecialEffect(OR_11, character, 5080)
    IfCharacterHasSpecialEffect(OR_11, character, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfUnsignedEqual(AND_9, left=left_1, right=0)
    IfUnsignedEqual(AND_9, left=left_2, right=0)
    IfUnsignedEqual(AND_9, left=left_3, right=0)
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Battle)
    SkipLinesIfUnsignedEqual(1, left=left_2, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown5)
    SkipLinesIfUnsignedEqual(1, left=left_3, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown4)
    IfConditionTrue(AND_1, input_condition=OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    IfCharacterHasSpecialEffect(AND_4, character, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90160)
    IfCharacterHasSpecialEffect(AND_5, character, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90162)
    IfCharacterHasSpecialEffect(AND_6, character, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90161)
    IfCharacterHasSpecialEffect(AND_7, character, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90162)
    IfCharacterHasSpecialEffect(AND_8, character, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableAI(character)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@NeverRestart(30062510)
def Event_30062510():
    """Event 30062510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            30060510,
            30060511,
            0,
            30061510,
            30061511,
            30063511,
            30061512,
            30063512,
            30062511,
            30062512,
            30060512,
            30060513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(30060519)
def Event_30060519():
    """Event 30060519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(30060510)


@RestartOnRest(30062520)
def Event_30062520(_, flag: uint, obj: uint, flag_1: uint):
    """Event 30062520"""
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


@NeverRestart(30062580)
def Event_30062580():
    """Event 30062580"""
    RegisterLadder(start_climbing_flag=30060580, stop_climbing_flag=30060581, obj=30061580)


@RestartOnRest(30062800)
def Event_30062800():
    """Event 30062800"""
    EndIfFlagEnabled(30060800)
    IfHealthValueLessThanOrEqual(MAIN, 30060800, value=0)
    Wait(4.0)
    PlaySoundEffect(30060800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30060800)
    KillBossAndDisplayBanner(character=30060800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30060800)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61207)
    EnableFlag(9207)


@RestartOnRest(30062810)
def Event_30062810():
    """Event 30062810"""
    GotoIfFlagDisabled(Label.L0, flag=30060800)
    DisableCharacter(30060800)
    DisableAnimations(30060800)
    Kill(30060800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30060800)
    IfFlagEnabled(AND_2, 30062805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30062800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableAI(30060800)
    SetNetworkUpdateRate(30060800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30060800, name=904260302)


@RestartOnRest(30062811)
def Event_30062811():
    """Event 30062811"""
    EndIfFlagEnabled(30060800)
    IfHealthLessThanOrEqual(AND_1, 30060800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30062802)


@RestartOnRest(30062849)
def Event_30062849():
    """Event 30062849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30060800, 30061800, 30062800, 30062805, 30065800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30060800, 30061800, 30062800, 30062805, 30062806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30060800, 30061800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30060800, 930000, 30062805, 30062806, 0, 30062802, 0, 0), arg_types="IiIIIIii")
