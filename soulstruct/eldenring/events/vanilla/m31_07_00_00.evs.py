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
    RegisterGrace(grace_flag=31070000, obj=31071950, unknown=5.0)
    Event_31072800()
    Event_31072801()
    Event_31072802()
    Event_31042810()
    Event_31042849()
    Event_31072811()
    RunCommonEvent(0, 900005610, args=(31071200, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005261, args=(31070400, 31072400, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31070290, 31072290, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31070291, 31072290, 3.0, 0.20000000298023224, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(31070295, 31072295, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(31070296, 31072295, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(31070297, 31072297, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(31070298, 31072297, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(31070299, 31072297, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(31070300, 6.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(31070280, 31072290, 3.0, 0.5, 0), arg_types="IIffi")
    Event_31072280(0, character=31070290)
    Event_31072280(1, character=31070291)
    Event_31072280(2, character=31070280)
    RunCommonEvent(0, 90005211, args=(31070250, 30000, 20000, 31072250, 0.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31070251, 30000, 20000, 31072251, 0.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31070252, 30000, 20000, 31072252, 0.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31070254, 30000, 20000, 31072254, 0.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31070255, 30000, 20000, 31072254, 0.0, 0.5, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31070257, 30000, 20000, 31072257, 0.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31070258, 30000, 20000, 31072258, 0.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(31070200, 31072200, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(31070201, 30002, 20002, 31072201, 0.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(31070210, 31072210, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(31070213, 31072400, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31070214, 31072400, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31070215, 31072400, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31070216, 31072400, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31070217, 31072400, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31070218, 31072400, 1.0, 0.0, 0), arg_types="IIffi")
    Event_31072213(0, character=31070213, region=31072213)
    Event_31072213(1, character=31070214, region=31072213)
    Event_31072213(2, character=31070215, region=31072213)
    Event_31072213(3, character=31070216, region=31072213)
    Event_31072213(4, character=31070217, region=31072213)
    RunCommonEvent(0, 90005261, args=(31070225, 31072225, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31070226, 31072225, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31070227, 31072225, 1.0, 0.0, 0), arg_types="IIffi")
    Event_310722205(0, character=31070225)
    Event_310722205(1, character=31070226)
    Event_310722205(2, character=31070227)
    Event_31072225(0, character=31070225)
    Event_31072225(1, character=31070226)
    Event_31072225(2, character=31070227)
    RunCommonEvent(0, 90005261, args=(31070230, 31072230, 5.0, 0.0, 0), arg_types="IIffi")
    Event_31072230(1, 31070231, 30001, 20001, 1.0, 0.4000000059604645, 0, 0, 0, 0)
    Event_31072230(2, 31070232, 30001, 20001, 1.0, 0.6000000238418579, 0, 0, 0, 0)
    Event_31072230(3, 31070233, 30001, 20001, 1.0, 0.800000011920929, 0, 0, 0, 0)
    Event_31072230(4, 31070234, 30001, 20001, 1.0, 0.5, 0, 0, 0, 0)
    RunCommonEvent(0, 90005211, args=(31070350, 30001, 20001, 31072350, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31070320, 30000, 30001, 0, 6.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31070321, 30000, 30001, 0, 6.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(31070322, 30000, 30001, 0, 4.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005646,
        args=(31070800, 31072840, 31072841, 31071840, 31072840, 31, 7, 0, 0),
        arg_types="IIIIIBBbb",
    )


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(31070302, 31072302, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31070303, 31072302, 1.0, 0.0, 0), arg_types="IIffi")
    Event_310722300(0, 31070302, 10.0)
    Event_310722300(1, 31070303, 11.0)


@RestartOnRest(31072213)
def Event_31072213(_, character: uint, region: uint):
    """Event 31072213"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=character, other_entity=PLAYER, radius=2.0)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=region)
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
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfHasAIStatus(OR_2, character, ai_status=AIStatusType.Battle)
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
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31072220)
def Event_31072220(_, character: uint):
    """Event 31072220"""
    IfCharacterDead(AND_15, character)
    EndIfConditionTrue(input_condition=AND_15)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 8081)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=31072225)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    Restart()


@RestartOnRest(310722205)
def Event_310722205(_, character: uint):
    """Event 310722205"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfCharacterType(AND_10, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_10, PLAYER, 3710)
    IfConditionTrue(OR_2, input_condition=AND_9)
    IfCharacterHuman(OR_2, PLAYER)
    IfCharacterHollow(OR_2, PLAYER)
    IfCharacterWhitePhantom(OR_2, PLAYER)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfCharacterHasSpecialEffect(AND_2, character, 8081)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31072225)
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
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=AND_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)


@RestartOnRest(31072225)
def Event_31072225(_, character: uint):
    """Event 31072225"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8092)


@RestartOnRest(31072230)
def Event_31072230(
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
    """Event 31072230"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=31070230, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=31070231, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=31070232, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=31070233, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=31070234, attacker=0)
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
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(OR_5, input_condition=OR_2)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_5)
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


@RestartOnRest(31072280)
def Event_31072280(_, character: uint):
    """Event 31072280"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=character, other_entity=PLAYER, radius=2.0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfHasAIStatus(OR_2, character, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(310722300)
def Event_310722300(_, character: uint, seconds: float):
    """Event 310722300"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31072302)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_5)
    Wait(seconds)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31072800)
def Event_31072800():
    """Event 31072800"""
    EndIfFlagEnabled(31070800)
    IfCharacterDead(AND_1, 31070800)
    IfCharacterDead(AND_1, 31070801)
    IfConditionTrue(MAIN, input_condition=AND_1)
    KillBossAndDisplayBanner(character=31070800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31070800)
    EnableFlag(9239)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61239)


@RestartOnRest(31072801)
def Event_31072801():
    """Event 31072801"""
    EndIfFlagEnabled(31070800)
    IfHealthValueLessThanOrEqual(MAIN, 31070800, value=0)
    Wait(4.0)
    PlaySoundEffect(31070800, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31072802)
def Event_31072802():
    """Event 31072802"""
    EndIfFlagEnabled(31070800)
    IfHealthValueLessThanOrEqual(MAIN, 31070801, value=0)
    Wait(4.0)
    PlaySoundEffect(31070801, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31042810)
def Event_31042810():
    """Event 31042810"""
    GotoIfFlagDisabled(Label.L0, flag=31070800)
    DisableCharacter(31070800)
    DisableCharacter(31070801)
    DisableAnimations(31070800)
    DisableAnimations(31070801)
    Kill(31070800)
    Kill(31070801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(31070801, 30009, loop=True, unknown2=1.0)
    DisableAI(31070800)
    DisableAI(31070801)
    AddSpecialEffect(31070800, 8092)
    AddSpecialEffect(31070801, 8092)
    IfFlagEnabled(AND_2, 31072805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31072800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableNetworkFlag(31070801)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBossHealthBar(31070800, name=903810310)
    EnableBossHealthBar(31070801, name=903810311, bar_slot=1)
    EnableAI(31070800)
    EnableAI(31070801)
    SetNetworkUpdateRate(31070800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(31070801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(2.0)
    ForceAnimation(31070801, 20029, unknown2=1.0)


@RestartOnRest(31072811)
def Event_31072811():
    """Event 31072811"""
    EndIfFlagEnabled(31070800)
    IfCharacterDead(OR_15, 31070800)
    IfCharacterDead(OR_15, 31070801)
    IfConditionTrue(MAIN, input_condition=OR_15)
    EnableFlag(31072842)


@RestartOnRest(31042849)
def Event_31042849():
    """Event 31042849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31070800, 31071800, 31072800, 31072805, 31075800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31070800, 31071800, 31072800, 31072805, 31072806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31070800, 31071800, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(31070800, 931000, 31072805, 31072806, 0, 31072842, 0, 0), arg_types="IiIIIIii")
