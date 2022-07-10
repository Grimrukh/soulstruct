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
    RunCommonEvent(0, 90005600, args=(76357, 1037531950, 5.0, 0), arg_types="IIfI")
    RunCommonEvent(0, 90005870, args=(1037530800, 904130600, 16), arg_types="IiI")
    Event_1037532345()
    Event_1037532350()
    RunCommonEvent(0, 90005860, args=(1037530800, 1037530800, 1037530800, 0, 30395, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1037530800, 16, 0), arg_types="III")
    Event_1037532450(0, 1037530800, 1037532400, 10.0, 0.0, -1)
    RunCommonEvent(1, 90005261, args=(1037530350, 1037532400, 5.0, 2.0, -1), arg_types="IIffi")
    RunCommonEvent(2, 90005261, args=(1037530351, 1037532400, 5.0, 2.0, -1), arg_types="IIffi")
    RunCommonEvent(3, 90005261, args=(1037530352, 1037532400, 5.0, 10.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005300, args=(1037530400, 1037530400, 40332, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(
        0,
        90005211,
        args=(1037540370, 30001, 20001, 1037542370, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(1037540370, 1037542370, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(
        1,
        90005211,
        args=(1037540371, 30002, 20002, 1037542370, 5.0, 1.5, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(1, 90005261, args=(1037540371, 1037542370, 5.0, 1.5, -1), arg_types="IIffi")
    RunCommonEvent(
        2,
        90005211,
        args=(1037540372, 30002, 20002, 1037542370, 5.0, 4.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(2, 90005261, args=(1037540372, 1037542370, 5.0, 4.0, -1), arg_types="IIffi")
    RunCommonEvent(
        3,
        90005211,
        args=(1037540373, 30001, 20001, 1037542370, 5.0, 1.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(3, 90005261, args=(1037540373, 1037542370, 5.0, 1.0, -1), arg_types="IIffi")
    RunCommonEvent(
        4,
        90005211,
        args=(1037540374, 30001, 20001, 1037542370, 5.0, 2.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(4, 90005261, args=(1037540374, 1037542370, 5.0, 2.0, -1), arg_types="IIffi")
    RunCommonEvent(
        5,
        90005211,
        args=(1037540375, 30001, 20001, 1037542370, 5.0, 3.299999952316284, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(5, 90005261, args=(1037540375, 1037542370, 5.0, 3.299999952316284, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1037530360, 30000, 20010, 1037532360, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005201, args=(1037530365, 30000, 20000, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1037530366, 30000, 20000, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    Event_1037532400(0, character=1037530300, region=1037532300, owner_entity=1037530310)
    Event_1037532400(1, character=1037530301, region=1037532300, owner_entity=1037530310)
    Event_1037532400(2, character=1037530302, region=1037532300, owner_entity=1037530310)
    Event_1037532400(3, character=1037530303, region=1037532300, owner_entity=1037530310)
    Event_1037532201()
    Event_1037532200(0, 1037531200, 4.199999809265137)
    Event_1037532200(1, 1037531201, 4.599999904632568)
    Event_1037532200(2, 1037531202, 1.7999999523162842)
    Event_1037532200(3, 1037531203, 5.0)
    Event_1037532200(4, 1037531204, 1.899999976158142)
    Event_1037532200(5, 1037531205, 2.0)
    Event_1037532200(6, 1037531206, 3.0)
    Event_1037532200(7, 1037531207, 11.0)
    Event_1037532200(8, 1037531208, 2.5)
    Event_1037532200(9, 1037531209, 1.5)
    Event_1037532200(10, 1037531210, 2.0)
    Event_1037532200(11, 1037531211, 7.099999904632568)
    Event_1037532200(12, 1037531212, 2.200000047683716)
    Event_1037532200(13, 1037531213, 2.299999952316284)
    Event_1037532200(14, 1037531214, 1.899999976158142)
    Event_1037532200(15, 1037531215, 4.599999904632568)
    Event_1037532200(16, 1037531216, 4.0)
    RunCommonEvent(0, 900005610, args=(1037531680, 100, 800, 1037538620), arg_types="IiiI")
    Event_1037533700(0, 1037530700)


@RestartOnRest(1037532300)
def Event_1037532300():
    """Event 1037532300"""
    CancelSpecialEffect(1037530210, 5070)
    CancelSpecialEffect(1037530211, 5070)
    CancelSpecialEffect(1037530212, 5070)
    CancelSpecialEffect(1037530213, 5070)
    CancelSpecialEffect(1037530214, 5070)
    CancelSpecialEffect(1037530215, 5070)
    CancelSpecialEffect(1037530216, 5070)
    CancelSpecialEffect(1037530217, 5070)
    CancelSpecialEffect(1037530218, 5070)
    CancelSpecialEffect(1037530219, 5070)
    CancelSpecialEffect(1037530220, 5070)
    CancelSpecialEffect(1037530221, 5070)
    CancelSpecialEffect(1037530222, 5070)
    CancelSpecialEffect(1037530223, 5070)
    CancelSpecialEffect(1037530224, 5070)
    CancelSpecialEffect(1037530225, 5070)
    CancelSpecialEffect(1037530226, 5070)
    CancelSpecialEffect(1037530227, 5070)
    CancelSpecialEffect(1037530228, 5070)


@RestartOnRest(1037532345)
def Event_1037532345():
    """Event 1037532345"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(1037530800, 8087)
    DisableThisSlotFlag()
    End()


@RestartOnRest(1037532350)
def Event_1037532350():
    """Event 1037532350"""
    GotoIfFlagEnabled(Label.L0, flag=1037530800)
    IfFlagEnabled(MAIN, 1037530800)
    Kill(1037530350, award_souls=True)
    Kill(1037530351, award_souls=True)
    Kill(1037530352, award_souls=True)
    Kill(1037530353, award_souls=True)
    Kill(1037530354, award_souls=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(1037530350)
    DisableCharacter(1037530351)
    DisableCharacter(1037530352)
    DisableCharacter(1037530353)
    DisableCharacter(1037530354)
    End()


@RestartOnRest(1037532200)
def Event_1037532200(_, source_entity: uint, seconds: float):
    """Event 1037532200"""
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=source_entity, radius=70.0)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    Wait(seconds)
    DisableThisSlotFlag()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=1037530299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803200,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=1037530299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803210,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=1037530299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803220,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=1037530299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803230,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=1037530299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803240,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=1037530299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803250,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=1037530299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803260,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=1037530299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803270,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(6.0)
    RestartIfConditionTrue(input_condition=MAIN)


@RestartOnRest(1037532201)
def Event_1037532201():
    """Event 1037532201"""
    CreateProjectileOwner(entity=1037530299)


@RestartOnRest(1037532400)
def Event_1037532400(_, character: uint, region: uint, owner_entity: uint):
    """Event 1037532400"""
    IfCharacterDead(AND_10, character)
    EndIfConditionTrue(input_condition=AND_10)
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    DisableCharacter(character)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=PLAYER)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    PlaySoundEffect(region, 407008100, sound_type=SoundType.c_CharacterMotion)
    Wait(1.0)
    IfCharacterHollow(OR_7, PLAYER)
    IfCharacterWhitePhantom(OR_7, PLAYER)
    IfCharacterOutsideRegion(AND_11, character=PLAYER, region=region)
    IfConditionTrue(AND_11, input_condition=OR_7)
    GotoIfConditionTrue(Label.L0, input_condition=AND_11)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=0.5)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=PLAYER,
        model_point=900,
        behavior_id=100920,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    ForceAnimation(character, 20011, unknown2=1.0)
    AddSpecialEffect(character, 8090)
    Wait(5.0)
    CancelSpecialEffect(character, 8090)


@RestartOnRest(1037532450)
def Event_1037532450(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 1037532450"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
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
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_3)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfHasAIStatus(OR_2, 1037530351, ai_status=AIStatusType.Search)
    IfHasAIStatus(OR_2, 1037530351, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_2, 1037530352, ai_status=AIStatusType.Search)
    IfHasAIStatus(OR_2, 1037530352, ai_status=AIStatusType.Battle)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(1037533700)
def Event_1037533700(_, character: uint):
    """Event 1037533700"""
    EndIfPlayerNotInOwnWorld()
    DisableCharacter(character)
    DisableBackread(character)
    EndIfFlagEnabled(400441)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    DisableHealthBar(character)
    IfFlagEnabled(AND_1, 14009267)
    AwaitConditionTrue(AND_1)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableImmortality(character)
    End()
