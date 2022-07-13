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
    RegisterGrace(grace_flag=32050000, obj=32051950, unknown=5.0)
    Event_32052800()
    Event_32052810()
    Event_32052811()
    Event_32052849()
    RunCommonEvent(
        0,
        90005501,
        args=(32050510, 32050511, 0, 32051510, 32051511, 32051512, 32050512),
        arg_types="IIIIIII",
    )
    Event_32052510()
    RunCommonEvent(
        0,
        90005646,
        args=(32050800, 32052840, 32052841, 32051840, 32052840, 32, 5, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 900005610, args=(32051680, 100, 800, 0), arg_types="IiiI")
    Event_32052200(0, 32050208, 30002, 20002, 0.0, 0, 0, 0, 0, 32051605, 32051606, 32051607, 0)
    Event_32052200(1, 32050209, 30000, 20000, 0.0, 0, 0, 0, 0, 32051608, 0, 0, 0)
    Event_32052200(2, 32050210, 30001, 20001, 0.0, 0, 0, 0, 0, 32051609, 0, 0, 0)
    Event_32052250(0, 32050211, 30005, 20005, 0.0, 0, 0, 0, 0, 32051211, 0, 0, 0, 32050211)
    Event_32052270(0, 32050211, 30007, 20007, 32050211, 5.0, 0.0, 0, 1, 0, 0)
    Event_32052400()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_32050519()
    Event_32052820()
    RunCommonEvent(0, 90005250, args=(32050200, 32052200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(32050201, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(32050205, 32052205, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32050212, 32052212, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32050250, 32052200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(32050255, 32052206, 2.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(32050257, 32052206, 2.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(32050256, 32052205, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32050258, 32052212, 1.0, 3033), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32050259, 32052212, 1.0, 3033), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32050300, 32052300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32050301, 32052300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32050302, 32052300, 0.0, 3011), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32050305, 32052305, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005260, args=(32050306, 32052306, 10.0, 0.0, 3011), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(32050307, 32052306, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32050308, 32052306, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005271, args=(32050310, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(32050311, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(32050312, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(32050313, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(32050314, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(32050315, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(32050316, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(32050317, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(32050318, 0.0, -1), arg_types="Ifi")


@NeverRestart(32052510)
def Event_32052510():
    """Event 32052510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            32050510,
            32050511,
            0,
            32051510,
            32051511,
            32053511,
            32051512,
            32053512,
            32052511,
            32052512,
            32050512,
            32050513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(32050519)
def Event_32050519():
    """Event 32050519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(32050510)
    DisableThisSlotFlag()


@RestartOnRest(32052200)
def Event_32052200(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    obj: uint,
    obj_1: uint,
    obj_2: uint,
    obj_3: uint,
):
    """Event 32052200"""
    EndIfThisEventSlotFlagEnabled()
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
    IfObjectDestroyed(OR_10, obj)
    IfObjectDestroyed(OR_10, obj_1)
    IfObjectDestroyed(OR_10, obj_2)
    IfObjectDestroyed(OR_10, obj_3)
    IfConditionTrue(AND_1, input_condition=OR_10)
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
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
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


@RestartOnRest(32052250)
def Event_32052250(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    obj: uint,
    obj_1: uint,
    obj_2: uint,
    obj_3: uint,
    flag: uint,
):
    """Event 32052250"""
    EndIfFlagEnabled(flag)
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
    IfObjectDestroyed(OR_10, obj)
    IfObjectDestroyed(OR_10, obj_1)
    IfObjectDestroyed(OR_10, obj_2)
    IfObjectDestroyed(OR_10, obj_3)
    IfConditionTrue(AND_1, input_condition=OR_10)
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
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableFlag(flag)
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


@RestartOnRest(32052270)
def Event_32052270(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    flag: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 32052270"""
    EndIfThisEventSlotFlagEnabled()
    EndIfFlagDisabled(flag)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
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
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
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


@RestartOnRest(32052400)
def Event_32052400():
    """Event 32052400"""
    GotoIfCharacterHasSpecialEffect(Label.L0, character=31180400, special_effect=16747)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=32052401)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(31180400, 16747)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(3.0)
    Restart()


@RestartOnRest(32052800)
def Event_32052800():
    """Event 32052800"""
    EndIfFlagEnabled(32050800)
    IfHealthValueLessThanOrEqual(AND_1, 32050800, value=0)
    IfHealthValueLessThanOrEqual(AND_1, 32050801, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(4.0)
    PlaySoundEffect(32050800, 888880000, sound_type=SoundType.s_SFX)
    IfHealthValueEqual(AND_2, 32050800, value=0)
    IfHealthValueEqual(AND_2, 32050801, value=0)
    IfConditionTrue(MAIN, input_condition=AND_2)
    KillBossAndDisplayBanner(character=32050800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(32050800)
    EnableFlag(9265)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61265)


@RestartOnRest(32052810)
def Event_32052810():
    """Event 32052810"""
    GotoIfFlagDisabled(Label.L0, flag=32050800)
    DisableCharacter(32050800)
    DisableCharacter(32050801)
    DisableAnimations(32050800)
    DisableAnimations(32050801)
    Kill(32050800)
    Kill(32050801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(32050800)
    DisableAI(32050801)
    GotoIfFlagEnabled(Label.L1, flag=32050801)
    ForceAnimation(32050800, 30000, loop=True, unknown2=1.0)
    ForceAnimation(32050801, 30000, loop=True, unknown2=1.0)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=32052801)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=32050800, attacker=PLAYER)
    IfAttackedWithDamageType(OR_1, attacked_entity=32050801, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(32050801)
    ForceAnimation(32050800, 20000, unknown2=1.0)
    ForceAnimation(32050801, 20000, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(32050800, 30000, loop=True, unknown2=1.0)
    ForceAnimation(32050801, 30000, loop=True, unknown2=1.0)
    IfFlagEnabled(AND_2, 32052805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=32052800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ForceAnimation(32050800, 20000, unknown2=1.0)
    ForceAnimation(32050801, 20000, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(32050800)
    EnableAI(32050801)
    SetNetworkUpdateRate(32050800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(32050801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(32050800, name=903350321)
    EnableBossHealthBar(32050801, name=903350322, bar_slot=1)


@RestartOnRest(32052811)
def Event_32052811():
    """Event 32052811"""
    EndIfFlagEnabled(32050800)
    IfHealthRatioLessThanOrEqual(AND_1, 32050800, value=0.6000000238418579)
    IfHealthRatioLessThanOrEqual(AND_1, 32050800, value=0.6000000238418579)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfCharacterDead(OR_1, 32050800)
    IfCharacterDead(OR_1, 32050801)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(32052802)


@RestartOnRest(32052820)
def Event_32052820():
    """Event 32052820"""
    EndIfFlagEnabled(32050800)
    EndIfFlagEnabled(32050801)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(32058590)
    DisableFlag(32058590)


@RestartOnRest(32052849)
def Event_32052849():
    """Event 32052849"""
    RunCommonEvent(
        0,
        9005800,
        args=(32050800, 32051800, 32052800, 32052805, 32055800, 10000, 32050801, 32052801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(32050800, 32051800, 32052800, 32052805, 32052806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(32050800, 32051800, 7, 32050801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(32050800, 931000, 32052805, 32052806, 0, 32052802, 0, 0), arg_types="IiIIIIii")
