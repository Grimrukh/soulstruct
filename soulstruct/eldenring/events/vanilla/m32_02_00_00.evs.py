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
    RegisterGrace(grace_flag=32020000, obj=32021950, unknown=5.0)
    Event_32022800()
    Event_32022810()
    Event_32022811()
    Event_32022849()
    Event_32022200(0, 32020205, 30002, 20002, 0.0, 0, 0, 0, 0, 32021615, 32021616, 0, 0)
    Event_32022250(0, 32020206, 30000, 20000, 0.0, 0, 0, 0, 0, 32021206, 0, 0, 0, 32020206)
    Event_32022270(0, 32020206, 30006, 20006, 32020206, 5.0, 0.0, 0, 1, 0, 0)
    Event_32022200(2, 32020207, 30002, 20002, 0.0, 0, 0, 0, 0, 32021618, 32021619, 0, 0)
    Event_32022200(5, 32020214, 30001, 20001, 0.0, 0, 0, 0, 0, 32021636, 0, 0, 0)
    Event_32022200(6, 32020215, 30000, 20000, 0.0, 0, 0, 0, 0, 32021625, 32021626, 0, 0)
    Event_32022200(7, 32020216, 30002, 20002, 0.0, 0, 0, 0, 0, 32021633, 32021634, 32021635, 0)
    Event_32022250(1, 32020221, 30005, 20005, 0.0, 0, 0, 0, 0, 32021221, 0, 0, 0, 32020221)
    Event_32022270(1, 32020221, 30006, 20006, 32020221, 5.0, 0.0, 0, 1, 0, 0)
    Event_32022250(2, 32020222, 30000, 20000, 0.0, 0, 0, 0, 0, 32021222, 0, 0, 0, 32020222)
    Event_32022270(2, 32020222, 30006, 20006, 32020222, 5.0, 0.0, 0, 1, 0, 0)
    Event_32022250(3, 32020230, 30001, 20001, 0.0, 0, 0, 0, 0, 32021230, 0, 0, 0, 32020230)
    Event_32022270(3, 32020230, 30007, 20007, 32020230, 10.0, 0.0, 0, 1, 0, 0)
    Event_32022250(4, 32020231, 30000, 20000, 0.0, 0, 0, 0, 0, 32021231, 0, 0, 0, 32020231)
    Event_32022270(4, 32020231, 30006, 20006, 32020231, 10.0, 0.0, 0, 1, 0, 0)
    Event_32022250(5, 32020232, 30001, 20001, 0.0, 0, 0, 0, 0, 32021232, 0, 0, 0, 32020232)
    Event_32022270(5, 32020232, 30007, 20007, 32020232, 10.0, 0.0, 0, 1, 0, 0)
    Event_32022200(20, 32020233, 30002, 20002, 0.0, 0, 0, 0, 0, 32021669, 32021670, 0, 0)
    Event_32022200(21, 32020234, 30005, 20005, 0.0, 0, 0, 0, 0, 32021671, 0, 0, 0)
    Event_32022510()
    RunCommonEvent(0, 90005502, args=(32020514, 32021516, 32022517), arg_types="III")
    RunCommonEvent(
        0,
        90005501,
        args=(32020510, 32020511, 0, 32021510, 32021511, 32021512, 32020512),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(32020515, 32020516, 2, 32021515, 32021516, 32021517, 32020517),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(32020520, 32020521, 0, 32021520, 32021521, 32021522, 32020522),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(32020525, 32020526, 0, 32021525, 32021526, 32021527, 32020527),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005646,
        args=(32020800, 32022840, 32022841, 32021840, 32022840, 32, 2, 0, 0),
        arg_types="IIIIIBBbb",
    )


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005250, args=(32020201, 32022200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(32020202, 26.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(32020208, 32022208, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32020210, 32022210, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32020211, 32022210, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32020212, 32022213, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32020212, 32022212, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32020213, 32022210, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32020213, 32022213, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32020217, 32022217, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32020220, 32022220, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32020400, 32022230, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32020235, 32022230, 5.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005260, args=(32020236, 32022230, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(32020309, 18.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(32020310, 30010, 20010, 6.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(32020311, 30010, 20010, 6.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005250, args=(32020305, 32022305, 2.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(32020306, 30011, 20011, 32022306, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(32020307, 30011, 20011, 32022306, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(32020308, 30010, 20010, 32022306, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_32020519()


@NeverRestart(32022510)
def Event_32022510():
    """Event 32022510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            32020510,
            32020511,
            0,
            32021510,
            32021511,
            32023511,
            32021512,
            32023512,
            32022511,
            32022512,
            32020512,
            32020513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            32020515,
            32020516,
            2,
            32021515,
            32021516,
            32023516,
            32021517,
            32023517,
            32022516,
            32022517,
            32020517,
            32020518,
            32020514,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            32020520,
            32020521,
            0,
            32021520,
            32021521,
            32023521,
            32021522,
            32023522,
            32022521,
            32022522,
            32020522,
            32020523,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            32020525,
            32020526,
            0,
            32021525,
            32021526,
            32023526,
            32021527,
            32023527,
            32022526,
            32022527,
            32020527,
            32020528,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(32020519)
def Event_32020519():
    """Event 32020519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(32020510)
    EnableFlag(32020520)
    EnableFlag(32020525)
    DisableThisSlotFlag()


@RestartOnRest(32022200)
def Event_32022200(
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
    """Event 32022200"""
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


@RestartOnRest(32022250)
def Event_32022250(
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
    """Event 32022250"""
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


@RestartOnRest(32022270)
def Event_32022270(
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
    """Event 32022270"""
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


@RestartOnRest(32022800)
def Event_32022800():
    """Event 32022800"""
    EndIfFlagEnabled(32020800)
    IfHealthValueLessThanOrEqual(MAIN, 32020800, value=0)
    Wait(4.0)
    PlaySoundEffect(32028000, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 32020800)
    KillBossAndDisplayBanner(character=32020800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(32020800)
    EnableFlag(9262)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61262)


@RestartOnRest(32022810)
def Event_32022810():
    """Event 32022810"""
    GotoIfFlagDisabled(Label.L0, flag=32020800)
    DisableCharacter(32020800)
    DisableAnimations(32020800)
    Kill(32020800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(32020800)
    AddSpecialEffect(32020800, 8090)
    EnableInvincibility(32020800)
    SetLockOnPoint(character=32020800, lock_on_model_point=220, state=False)
    ForceAnimation(32020800, 30001, loop=True, unknown2=1.0)
    IfFlagEnabled(AND_2, 32022805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=32022800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ForceAnimation(32020800, 20001, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(32020800)
    SetNetworkUpdateRate(32020800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(32020800, name=903350320)
    DisableInvincibility(32020800)
    SetLockOnPoint(character=32020800, lock_on_model_point=220, state=True)


@RestartOnRest(32022811)
def Event_32022811():
    """Event 32022811"""
    EndIfFlagEnabled(32020800)
    IfHealthRatioLessThanOrEqual(AND_1, 32020800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(32022802)


@RestartOnRest(32022849)
def Event_32022849():
    """Event 32022849"""
    RunCommonEvent(
        0,
        9005800,
        args=(32020800, 32021800, 32022800, 32022805, 32025800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(32020800, 32021800, 32022800, 32022805, 32022806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(32020800, 32021800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(32020800, 931000, 32022805, 32022806, 0, 32022802, 0, 0), arg_types="IiIIIIii")
