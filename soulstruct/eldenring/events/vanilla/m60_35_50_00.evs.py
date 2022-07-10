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
    RegisterGrace(grace_flag=1035500002, obj=1035501953, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76214, 76214, 1035501983, 77220, 4, 78220, 78221, 78222, 78223, 78224, 78225, 78226, 78227, 78228, 78229),
        arg_types="IIIIIIIIIIIIIII",
    )
    RegisterGrace(grace_flag=1035500000, obj=1035501950, unknown=5.0)
    RegisterGrace(grace_flag=1035500001, obj=1035501951, unknown=5.0)
    RunCommonEvent(0, 900005610, args=(1035501650, 100, 800, 0), arg_types="IiiI")
    Event_1035502200(0, region=1035502700)
    RunCommonEvent(0, 9005810, args=(1035500800, 76232, 1035500952, 1035501952, 5.0), arg_types="IIIIf")
    RunCommonEvent(0, 90005300, args=(1035500322, 1035500322, 40220, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1035500320, 1035500320, 40250, 0.0, 0), arg_types="IIifi")
    Event_1035502580()
    RunCommonEvent(
        0,
        90005501,
        args=(1035500510, 1035500511, 4, 1035501510, 1035501511, 1035501512, 1035500512),
        arg_types="IIIIIII",
    )
    Event_1035502510()
    Event_1035502500()
    RunCommonEvent(0, 90005511, args=(1035500560, 1035501560, 1035503560, 99020, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(1035500560, 1035502560, 1035502561), arg_types="III")
    RunCommonEvent(0, 90005201, args=(1035500200, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500210, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500211, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1035500217, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(1035500218, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(
        0,
        90005210,
        args=(1035500219, 30000, 20000, 1035502200, 10.0, 5.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005201, args=(1035500220, 30000, 20000, 5.0, 1.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(
        0,
        90005210,
        args=(1035500222, 30003, 20003, 1035502222, 16.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005210,
        args=(1035500223, 30000, 20000, 1035502200, 10.0, 3.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005210,
        args=(1035500224, 30000, 20000, 1035502200, 10.0, 4.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005210,
        args=(1035500225, 30000, 20000, 1035502200, 7.0, 2.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005201, args=(1035500226, 30000, 20000, 5.0, 1.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(
        0,
        90005210,
        args=(1035500227, 30000, 20000, 1035502200, 10.0, 4.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005210,
        args=(1035500228, 30000, 20000, 1035502200, 6.0, 2.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005210,
        args=(1035500229, 30000, 20000, 1035502200, 10.0, 5.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005210,
        args=(1035500230, 30000, 20000, 1035502200, 10.0, 4.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005201, args=(1035500240, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500241, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500244, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500252, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500254, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500255, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500256, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500258, 30000, 20000, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500278, 30000, 20000, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500279, 30000, 20000, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500280, 30000, 20000, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500281, 30000, 20000, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500282, 30000, 20000, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500283, 30000, 20000, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1035500284, 30000, 20000, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(1035500290, 30000, 20000, 1035502299, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1035500291, 30000, 20000, 1035502291, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1035500292, 30000, 20000, 1035502292, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005251, args=(1035500303, 15.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(1035500310, 1035502311, 18.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(1035500313, 1035502313, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1035500314, 1035502314, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1035500342, 1035502342, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(1035500350, 30003, 20003, 1035502350, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005210,
        args=(1035500353, 30003, 20003, 1035502354, 20.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005210,
        args=(1035500354, 30003, 20003, 1035502354, 20.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005200, args=(1035500356, 30003, 20003, 1035502356, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1035500390, 1035502390, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1035500391, 1035502391, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1035500395, 5.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1035500400, 1035502400, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1035500401, 1035502400, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1035500402, 1035502402, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1035500409, 1035502409, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005260, args=(1035500410, 1035502410, 42.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(1035500411, 1035502411, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1035500412, 1035502412, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1035500413, 1035502412, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(1035500414, 30006, 20006, 1035502414, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005251, args=(1035500415, 17.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1035500416, 1035502416, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005260, args=(1035500423, 1035502410, 40.0, 0.0, -1), arg_types="IIffi")
    Event_1035502401()
    Event_1035502400(0, 1035500407, 1035502407, 0.0, -1)
    Event_1035502400(1, 1035500408, 1035502407, 0.0, -1)
    Event_1035502400(2, 1035500419, 1035502419, 0.0, -1)
    Event_1035502400(3, 1035500420, 1035502420, 0.0, -1)
    Event_1035502400(4, 1035500421, 1035502420, 0.0, -1)
    Event_1035502400(5, 1035500422, 1035502422, 0.0, -1)
    Event_1035502400(6, 1035500424, 1035502422, 5.0, -1)
    Event_1035502400(7, 1035500425, 1035502425, 0.0, -1)
    Event_1035502400(8, 1035500426, 1035502420, 0.0, -1)
    Event_1035502400(9, 1035500427, 1035502419, 0.0, -1)
    Event_1035502400(10, 1035500428, 1035502420, 0.0, -1)
    Event_1035502849()
    Event_1035500800()
    Event_1035502810()
    Event_1035502840()
    Event_1035502841()
    Event_1035502842()
    Event_1035502210(0, obj=1035501600, flag=1035502600, owner_entity=1035500399)
    Event_1035502210(1, obj=1035501601, flag=1035502601, owner_entity=1035500399)
    Event_1035502210(2, obj=1035501602, flag=1035502602, owner_entity=1035500399)
    Event_1035502210(3, obj=1035501603, flag=1035502603, owner_entity=1035500399)
    Event_1035502210(4, obj=1035501604, flag=1035502604, owner_entity=1035500399)
    Event_1035502210(5, obj=1035501605, flag=1035502605, owner_entity=1035500399)
    Event_1035502210(6, obj=1035501606, flag=1035502606, owner_entity=1035500399)
    Event_1035502210(7, obj=1035501608, flag=1035502608, owner_entity=1035500399)
    Event_1035500700(
        0,
        character=1035500700,
        character_1=1035500702,
        character_2=1035500704,
        character_3=1035500706,
        obj=1035501702
    )
    Event_1035500701(
        0,
        character=1035500701,
        character_1=1035500703,
        character_2=1035500705,
        character_3=1035500707,
        obj=1035501701
    )
    Event_1035500702()
    Event_1035500703(0, flag=1035502705, region=1035502720)
    Event_1035500703(1, flag=1035502706, region=1035502721)
    RunCommonEvent(0, 90005750, args=(1035501700, 4110, 101490, 400149, 400149, 1035509215, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005750, args=(1035501700, 4110, 101495, 400149, 400149, 1035509216, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005706, args=(1035500710, 90102, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1035500700)
    DisableBackread(1035500701)
    DisableBackread(1035500702)
    DisableBackread(1035500703)
    DisableBackread(1035500704)
    DisableBackread(1035500705)
    DisableBackread(1035500706)
    DisableBackread(1035500707)
    DisableBackread(1035500710)
    EnableObjectInvulnerability(1035501702)
    Event_1035502514()


@RestartOnRest(1035502200)
def Event_1035502200(_, region: uint):
    """Event 1035502200"""
    DisableNetworkSync()
    Wait(0.10000000149011612)
    IfCharacterInsideRegion(AND_1, character=20000, region=region)
    IfFailedToCreateSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(20000, 9621)
    Wait(0.10000000149011612)
    IfCharacterOutsideRegion(OR_2, character=20000, region=region)
    IfFailedToCreateSession(OR_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    CancelSpecialEffect(20000, 9621)
    Restart()


@RestartOnRest(1035502210)
def Event_1035502210(_, obj: uint, flag: uint, owner_entity: uint):
    """Event 1035502210"""
    EndIfFlagEnabled(flag)
    EndIfObjectDestroyed(obj)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=obj, attacker=20000)
    IfEntityWithinDistance(OR_2, entity=obj, other_entity=20000, radius=2.0)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DestroyObject(obj, request_slot=0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    End()


@RestartOnRest(1035502401)
def Event_1035502401():
    """Event 1035502401"""
    EnableNetworkSync()
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1035502499)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1035502499)


@RestartOnRest(1035502400)
def Event_1035502400(_, character: uint, region: uint, seconds: float, animation_id: int):
    """Event 1035502400"""
    EnableNetworkSync()
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfFlagEnabled(AND_3, 1035502499)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=AND_3)
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
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@NeverRestart(1035502510)
def Event_1035502510():
    """Event 1035502510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1035500510,
            1035500511,
            4,
            1035501510,
            1035501511,
            1035503511,
            1035501512,
            1035503512,
            1035502511,
            1035502512,
            1035500512,
            1035500513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(1035502514)
def Event_1035502514():
    """Event 1035502514"""
    EndIfFlagEnabled(1035500514)
    EnableFlag(1035500514)
    DisableFlag(1035500510)


@NeverRestart(1035502580)
def Event_1035502580():
    """Event 1035502580"""
    RegisterLadder(start_climbing_flag=1035500580, stop_climbing_flag=1035500581, obj=1035501580)
    RegisterLadder(start_climbing_flag=1035500582, stop_climbing_flag=1035500583, obj=1035501582)
    RegisterLadder(start_climbing_flag=1035500584, stop_climbing_flag=1035500585, obj=1035501584)
    RegisterLadder(start_climbing_flag=1035500586, stop_climbing_flag=1035500587, obj=1035501586)


@RestartOnRest(1035502500)
def Event_1035502500():
    """Event 1035502500"""
    DisableObject(1035501200)
    DisableObject(1035501201)
    DisableObject(1035506400)


@RestartOnRest(1035500800)
def Event_1035500800():
    """Event 1035500800"""
    EndIfFlagEnabled(1035500800)
    IfHealthValueLessThanOrEqual(MAIN, 1035500800, value=0)
    Wait(4.0)
    PlaySoundEffect(1035500800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 1035500800)
    KillBossAndDisplayBanner(character=1035500800, banner_type=BannerType.Unknown)
    EnableFlag(1035500800)
    EnableFlag(9181)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61181)


@RestartOnRest(1035502810)
def Event_1035502810():
    """Event 1035502810"""
    GotoIfFlagDisabled(Label.L0, flag=1035500800)
    DisableCharacter(1035500800)
    DisableAnimations(1035500800)
    Kill(1035500800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(1035500800)
    GotoIfFlagEnabled(Label.L1, flag=1035500801)
    DisableCharacter(1035500800)
    ForceAnimation(1035500800, 30000, loop=True, unknown2=1.0)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1035502801)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=1035500800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(1035500801)
    EnableCharacter(1035500800)
    ForceAnimation(1035500800, 20010, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=1035502800)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=1035502802)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfFlagEnabled(AND_2, 1035502805)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(1035500800)
    SetNetworkUpdateRate(1035500800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(1035500800, name=903253500)


@RestartOnRest(1035502840)
def Event_1035502840():
    """Event 1035502840"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1035500800)
    IfCharacterInsideRegion(AND_1, character=1035500800, region=1035502840)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1035502841)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1035502842)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1035502843)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1035502844)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1035502845)
    IfFlagDisabled(AND_1, 1035502821)
    IfFlagDisabled(AND_1, 1035502822)
    IfFlagDisabled(AND_1, 1035502823)
    IfFlagDisabled(AND_1, 1035502824)
    IfFlagDisabled(AND_1, 1035502825)
    IfFlagDisabled(AND_1, 1035502826)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=1035502841)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=1035502842)
    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=1035502843)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=1035502844)
    GotoIfCharacterInsideRegion(Label.L4, character=PLAYER, region=1035502845)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagDisabled(1, 1035502839)
    EnableNetworkFlag(1035502822)
    SkipLinesIfFlagEnabled(1, 1035502839)
    EnableNetworkFlag(1035502824)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagDisabled(1, 1035502839)
    EnableNetworkFlag(1035502821)
    SkipLinesIfFlagEnabled(1, 1035502839)
    EnableNetworkFlag(1035502823)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfFlagDisabled(1, 1035502839)
    EnableNetworkFlag(1035502825)
    SkipLinesIfFlagEnabled(1, 1035502839)
    EnableNetworkFlag(1035502826)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    Wait(1.0)
    Restart()


@RestartOnRest(1035502841)
def Event_1035502841():
    """Event 1035502841"""
    EndIfFlagEnabled(1035500800)
    IfFlagEnabled(OR_1, 1035502821)
    IfFlagEnabled(OR_1, 1035502822)
    IfFlagEnabled(OR_1, 1035502823)
    IfFlagEnabled(OR_1, 1035502824)
    IfFlagEnabled(OR_1, 1035502825)
    IfFlagEnabled(OR_1, 1035502826)
    IfConditionTrue(MAIN, input_condition=OR_1)
    AddSpecialEffect(1035500800, 13806)
    DisableAnimations(1035500800)
    Wait(1.0)
    GotoIfFlagEnabled(Label.L1, flag=1035502821)
    GotoIfFlagEnabled(Label.L2, flag=1035502822)
    GotoIfFlagEnabled(Label.L3, flag=1035502823)
    GotoIfFlagEnabled(Label.L4, flag=1035502824)
    GotoIfFlagEnabled(Label.L5, flag=1035502825)
    GotoIfFlagEnabled(Label.L6, flag=1035502826)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(1035500800, destination=1035502821, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    Move(1035500800, destination=1035502822, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 3 --- #
    DefineLabel(3)
    Move(1035500800, destination=1035502823, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    Move(1035500800, destination=1035502824, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 5 --- #
    DefineLabel(5)
    Move(1035500800, destination=1035502825, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 6 --- #
    DefineLabel(6)
    Move(1035500800, destination=1035502826, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    EnableAnimations(1035500800)
    CancelSpecialEffect(1035500800, 13806)
    ForceAnimation(1035500800, 20010, unknown2=1.0)
    Wait(1.0)
    SkipLinesIfPlayerNotInOwnWorld(6)
    DisableNetworkFlag(1035502821)
    DisableNetworkFlag(1035502822)
    DisableNetworkFlag(1035502823)
    DisableNetworkFlag(1035502824)
    DisableNetworkFlag(1035502825)
    DisableNetworkFlag(1035502826)
    Restart()


@RestartOnRest(1035502842)
def Event_1035502842():
    """Event 1035502842"""
    EndIfFlagEnabled(1035500800)
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(MAIN, 1035502810)
    EnableNetworkFlag(1035502839)
    Wait(3.0)
    DisableNetworkFlag(1035502839)
    Wait(5.0)
    EnableNetworkFlag(1035502839)
    Wait(4.0)
    DisableNetworkFlag(1035502839)
    Wait(1.0)
    EnableNetworkFlag(1035502839)
    Wait(6.0)
    DisableNetworkFlag(1035502839)
    Wait(7.0)
    Restart()


@RestartOnRest(1035502849)
def Event_1035502849():
    """Event 1035502849"""
    RunCommonEvent(
        0,
        9005800,
        args=(1035500800, 1035501800, 1035502800, 1035502805, 1035505800, 10000, 1035500801, 1035502801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005801,
        args=(1035500800, 1035501800, 1035502800, 1035502805, 1035502806, 10000),
        arg_types="IIIIIi",
    )
    RunCommonEvent(0, 9005811, args=(1035500800, 1035501800, 3, 1035500801), arg_types="IIiI")
    RunCommonEvent(0, 9005813, args=(1035500800, 1035501801, 3, 0, 3), arg_types="IIiIi")
    RunCommonEvent(
        0,
        9005822,
        args=(1035500800, 920200, 1035502805, 1035502806, 1035500801, 0, 0, 0),
        arg_types="IiIIIIii",
    )


@RestartOnRest(1035500700)
def Event_1035500700(_, character: uint, character_1: uint, character_2: uint, character_3: uint, obj: uint):
    """Event 1035500700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    DisableNetworkConnectedFlagRange(flag_range=(1035502700, 1035502702))
    SkipLinesIfFlagDisabled(2, 1035509205)
    EnableRandomFlagInRange(flag_range=(1035502700, 1035502702))
    SkipLines(1)
    EnableNetworkFlag(1035502701)
    SkipLinesIfFlagDisabled(2, 1035509202)
    DisableNetworkConnectedFlagRange(flag_range=(1035502700, 1035502702))
    EnableNetworkFlag(1035502700)
    SkipLinesIfFlagDisabled(2, 1035509203)
    DisableNetworkConnectedFlagRange(flag_range=(1035502700, 1035502702))
    EnableNetworkFlag(1035502701)
    SkipLinesIfFlagDisabled(2, 1035509204)
    DisableNetworkConnectedFlagRange(flag_range=(1035502700, 1035502702))
    EnableNetworkFlag(1035502702)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L5, flag=3565)
    GotoIfFlagEnabled(Label.L6, flag=3566)
    GotoIfFlagEnabled(Label.L7, flag=3567)
    GotoIfFlagEnabled(Label.L8, flag=3568)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DisableObjectInvulnerability(obj)
    IfFlagRangeAnyEnabled(MAIN, flag_range=(3565, 3568))
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)

    # --- Label 6 --- #
    DefineLabel(6)

    # --- Label 7 --- #
    DefineLabel(7)

    # --- Label 8 --- #
    DefineLabel(8)
    EnableCharacter(character)
    EnableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    EnableCharacter(character_2)
    EnableBackread(character_2)
    EnableCharacter(character_3)
    EnableBackread(character_3)
    ForceAnimation(character_1, 930010, unknown2=1.0)
    ForceAnimation(character_2, 930010, unknown2=1.0)
    ForceAnimation(character_3, 930010, unknown2=1.0)
    EnableObjectInvulnerability(obj)
    RestoreObject(obj)
    SkipLinesIfFlagDisabled(1, 1035502700)
    ForceAnimation(character, 930024, unknown2=1.0)
    SkipLinesIfFlagDisabled(1, 1035502701)
    ForceAnimation(character, 930026, unknown2=1.0)
    SkipLinesIfFlagDisabled(1, 1035502702)
    ForceAnimation(character, 930028, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagRangeAllDisabled(MAIN, flag_range=(3565, 3568))
    Restart()


@RestartOnRest(1035500701)
def Event_1035500701(_, character: uint, character_1: uint, character_2: uint, character_3: uint, obj: uint):
    """Event 1035500701"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L9, flag=3569)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableObject(obj)
    IfFlagEnabled(MAIN, 3569)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    EnableCharacter(character)
    EnableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    EnableCharacter(character_2)
    EnableBackread(character_2)
    EnableCharacter(character_3)
    EnableBackread(character_3)
    EnableObject(obj)
    ForceAnimation(character_1, 930009, unknown2=1.0)
    ForceAnimation(character_2, 930009, unknown2=1.0)
    ForceAnimation(character_3, 930009, unknown2=1.0)
    ForceAnimation(character, 30019, unknown2=1.0)
    SetCharacterTalkRange(character=character, distance=100.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3569)
    Restart()


@RestartOnRest(1035500702)
def Event_1035500702():
    """Event 1035500702"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(1035509208)
    IfEventValueGreaterThanOrEqual(AND_1, flag=67470, bit_count=8, value=1)
    IfEventValueGreaterThanOrEqual(AND_1, flag=66450, bit_count=8, value=1)
    IfEventValueGreaterThanOrEqual(AND_1, flag=130290, bit_count=8, value=3)
    IfEventValueGreaterThanOrEqual(AND_1, flag=130300, bit_count=8, value=2)
    IfEventValueGreaterThanOrEqual(AND_1, flag=130340, bit_count=8, value=1)
    IfEventValueGreaterThanOrEqual(AND_1, flag=130350, bit_count=8, value=1)
    IfEventValueGreaterThanOrEqual(AND_1, flag=130360, bit_count=8, value=1)
    IfEventValueGreaterThanOrEqual(AND_1, flag=130370, bit_count=8, value=2)
    IfEventValueGreaterThanOrEqual(AND_1, flag=130380, bit_count=8, value=1)
    IfEventValueGreaterThanOrEqual(AND_1, flag=130390, bit_count=8, value=1)
    IfEventValueGreaterThanOrEqual(AND_1, flag=69900, bit_count=8, value=1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1035509208)
    End()


@RestartOnRest(1035500703)
def Event_1035500703(_, flag: uint, region: uint):
    """Event 1035500703"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 3569)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
