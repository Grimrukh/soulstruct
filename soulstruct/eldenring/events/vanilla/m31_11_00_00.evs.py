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
    RegisterGrace(grace_flag=31110000, obj=31111950, unknown=5.0)
    Event_31112800()
    Event_31112801()
    Event_31112802()
    Event_31112810()
    Event_31112811()
    Event_31112849()
    Event_31112803()
    RunCommonEvent(
        0,
        90005646,
        args=(31110800, 31112840, 31112841, 31111840, 31112840, 31, 11, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 91005600, args=(31112800, 31111695, 5), arg_types="IIi")
    RunCommonEvent(0, 900005610, args=(31111200, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005525, args=(31110600, 31111600), arg_types="II")
    RunCommonEvent(0, 90005525, args=(31110601, 31111601), arg_types="II")
    RunCommonEvent(0, 90005525, args=(31110602, 31111602), arg_types="II")
    RunCommonEvent(0, 90005525, args=(31110603, 31111603), arg_types="II")
    Event_31112400()
    Event_31113700(0, 31110700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005211, args=(31110200, 30006, 20006, 31112200, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31110201, 30003, 20003, 31112201, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31110202, 30001, 20001, 31112202, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(31110208, 31112208, 2.0, 0.0, 1707), arg_types="IIffi")
    Event_31112208()
    Event_31112250(0, 31110209, 31112209, 5.0, 0.0, 3031)
    RunCommonEvent(0, 90005211, args=(31110210, 30002, 20002, 31112210, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31110213, 30007, 20007, 31112213, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(31110215, 31112215, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31110216, 30002, 20002, 31112216, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31110217, 30002, 20002, 31112217, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31110223, 30004, 20004, 31112223, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(31110280, 31112280, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31110285, 31112285, 2.0, 3.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31110287, 31112285, 2.0, 3.5, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31110240, 31112240, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31112250(1, 31110241, 31112241, 3.0, 0.0, 3011)
    RunCommonEvent(0, 90005261, args=(31110242, 31112240, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005201, args=(31110248, 30001, 20001, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(31110249, 30001, 20001, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(31110250, 30001, 20001, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    Event_31112250(2, 31110251, 31112251, 2.0, 0.0, 3011)
    RunCommonEvent(0, 90005211, args=(31110256, 30000, 20000, 31112256, 1.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(31110257, 30000, 20000, 31112256, 1.0, 0.800000011920929, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(31110258, 31112300, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31112240(0, character=31110258)
    RunCommonEvent(0, 90005261, args=(31110262, 31112262, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31110263, 31112262, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31112245(0, character=31110262)
    Event_31112245(1, character=31110263)
    RunCommonEvent(0, 90005261, args=(31110300, 31112300, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31110310, 30006, 20006, 31112213, 2.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")


@RestartOnRest(31112208)
def Event_31112208():
    """Event 31112208"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(31110208, 8081)
    AddSpecialEffect(31110208, 8082)
    AddSpecialEffect(31110208, 5000)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=31110208, other_entity=PLAYER, radius=4.0)
    IfCharacterHasSpecialEffect(AND_4, 31110208, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 31110208, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 31110208, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 31110208, 90160)
    IfCharacterHasSpecialEffect(AND_5, 31110208, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 31110208, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 31110208, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 31110208, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 31110208, 90162)
    IfCharacterHasSpecialEffect(AND_6, 31110208, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 31110208, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 31110208, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 31110208, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 31110208, 90161)
    IfCharacterHasSpecialEffect(AND_7, 31110208, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 31110208, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 31110208, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 31110208, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 31110208, 90162)
    IfCharacterHasSpecialEffect(AND_8, 31110208, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 31110208, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 31110208, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 31110208, 90160)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfHasAIStatus(OR_2, 31110208, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(OR_2, attacked_entity=31110208, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=31110208, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31110208, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31110208, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31110208, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31110208, unk_8_12=260, unk_12_16=1)
    IfCharacterInsideRegion(OR_2, character=31110208, region=31112207)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(31110208, 8081)
    CancelSpecialEffect(31110208, 8082)
    CancelSpecialEffect(31110208, 5000)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31112240)
def Event_31112240(_, character: uint):
    """Event 31112240"""
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
    IfEntityWithinDistance(AND_1, entity=character, other_entity=PLAYER, radius=6.0)
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


@RestartOnRest(31112245)
def Event_31112245(_, character: uint):
    """Event 31112245"""
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
    IfCharacterInsideRegion(AND_1, character=character, region=31112263)
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


@RestartOnRest(31112250)
def Event_31112250(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 31112250"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=character, radius=radius)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_2)
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


@RestartOnRest(31112310)
def Event_31112310(_, character: uint):
    """Event 31112310"""
    AddSpecialEffect(character, 8087)


@RestartOnRest(31112301)
def Event_31112301():
    """Event 31112301"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(31110301, 8081)
    AddSpecialEffect(31110301, 8082)
    AddSpecialEffect(31110301, 5000)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=31110301, other_entity=PLAYER, radius=4.0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfHasAIStatus(OR_2, 31110301, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(OR_2, attacked_entity=31110301, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(31110301, 8081)
    CancelSpecialEffect(31110301, 8082)
    CancelSpecialEffect(31110301, 5000)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@NeverRestart(31112400)
def Event_31112400():
    """Event 31112400"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=31118700)
    DisableObject(31111700)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9533, entity=31111700)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfFlagEnabled(OR_1, 31118700)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L9, flag=31118700)
    IfPlayerHasGood(AND_2, 8169)
    GotoIfConditionTrue(Label.L3, input_condition=AND_2)
    DisplayDialog(text=30080, anchor_entity=31111700)
    Wait(1.399999976158142)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    ForceAnimation(PLAYER, 60010, unknown2=1.0)
    Wait(2.799999952316284)
    DisplayDialog(text=208169, anchor_entity=31111700)

    # --- Label 9 --- #
    DefineLabel(9)
    ForceAnimation(31111700, 1, unknown2=1.0)
    EnableNetworkFlag(31118700)


@RestartOnRest(31112800)
def Event_31112800():
    """Event 31112800"""
    EndIfFlagEnabled(31110800)
    IfCharacterDead(AND_1, 31110800)
    IfCharacterDead(AND_1, 31110801)
    IfCharacterDead(AND_1, 31110802)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(3.0)
    KillBossAndDisplayBanner(character=31110800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31110800)
    EnableFlag(9246)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61246)


@RestartOnRest(31112801)
def Event_31112801():
    """Event 31112801"""
    EndIfFlagEnabled(31110800)
    IfHealthValueLessThanOrEqual(MAIN, 31110800, value=0)
    Wait(4.0)
    PlaySoundEffect(31110800, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31112802)
def Event_31112802():
    """Event 31112802"""
    EndIfFlagEnabled(31110800)
    IfHealthValueLessThanOrEqual(MAIN, 31110801, value=0)
    Wait(4.0)
    PlaySoundEffect(31110801, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31112803)
def Event_31112803():
    """Event 31112803"""
    EndIfFlagEnabled(31110800)
    IfHealthValueLessThanOrEqual(MAIN, 31110802, value=0)
    Wait(4.0)
    PlaySoundEffect(31110802, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31112810)
def Event_31112810():
    """Event 31112810"""
    GotoIfFlagDisabled(Label.L0, flag=31110800)
    DisableCharacter(31110800)
    DisableCharacter(31110801)
    DisableCharacter(31110802)
    DisableAnimations(31110800)
    DisableAnimations(31110801)
    DisableAnimations(31110802)
    Kill(31110800)
    Kill(31110801)
    Kill(31110802)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31110800)
    DisableAI(31110801)
    DisableAI(31110802)
    ForceAnimation(31110800, 30001, unknown2=1.0)
    ForceAnimation(31110801, 30001, unknown2=1.0)
    ForceAnimation(31110802, 30000, unknown2=1.0)
    IfFlagEnabled(AND_2, 31112805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31112800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(31110800)
    EnableAI(31110801)
    EnableAI(31110802)
    SetNetworkUpdateRate(31110800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(31110801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(31110802, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31110800, name=903350313)
    EnableBossHealthBar(31110801, name=903350312, bar_slot=1)
    EnableBossHealthBar(31110802, name=903350314, bar_slot=2)
    ForceAnimation(31110800, 20001, unknown2=1.0)
    ForceAnimation(31110801, 20001, unknown2=1.0)
    ForceAnimation(31110802, 20000, unknown2=1.0)


@RestartOnRest(31112811)
def Event_31112811():
    """Event 31112811"""
    EndIfFlagEnabled(31110800)
    IfCharacterDead(OR_15, 31110800)
    IfCharacterDead(OR_15, 31110801)
    IfCharacterDead(OR_15, 31110802)
    IfConditionTrue(MAIN, input_condition=OR_15)
    EnableFlag(31112842)


@RestartOnRest(31112849)
def Event_31112849():
    """Event 31112849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31110800, 31111800, 31112800, 31112805, 31115800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31110800, 31111800, 31112800, 31112805, 31112806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31110800, 31111800, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(31110800, 931000, 31112805, 31112806, 0, 31112842, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(31113700)
def Event_31113700(_, character: uint):
    """Event 31113700"""
    EndIfPlayerNotInOwnWorld()
    DisableCharacter(character)
    DisableBackread(character)
    EndIfFlagEnabled(400431)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    DisableHealthBar(character)
    IfFlagEnabled(OR_1, 1044369228)
    IfFlagEnabled(OR_1, 14009263)
    IfFlagEnabled(AND_1, 14009267)
    IfConditionTrue(AND_1, input_condition=OR_1)
    AwaitConditionTrue(AND_1)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableImmortality(character)
    End()
