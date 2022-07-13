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
    RegisterGrace(grace_flag=32010000, obj=32011950, unknown=5.0)
    Event_32012800()
    Event_32012810()
    Event_32012811()
    Event_32012849()
    Event_32012510()
    RunCommonEvent(
        0,
        90005501,
        args=(32010510, 32010511, 0, 32011510, 32011511, 32011512, 32010512),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(32010515, 32010516, 0, 32011515, 32011516, 32011517, 32010517),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(32010520, 32010521, 0, 32011520, 32011521, 32011522, 32010522),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005646,
        args=(32010800, 32012840, 32012841, 32011840, 32012840, 32, 1, 0, 0),
        arg_types="IIIIIBBbb",
    )
    Event_32012250(0, 32010201, 30004, 20004, 16576, 0.0, 0, 0, 0, 0, 32011201, 0, 0, 0, 32010201)
    Event_32012270(0, 32010201, 30005, 20005, 32010201, 3.0, 0.0, 0, 1, 0, 0)
    Event_32012250(1, 32010202, 30004, 20004, 16576, 0.0, 0, 0, 0, 0, 32011202, 0, 0, 0, 32010202)
    Event_32012270(1, 32010202, 30005, 20005, 32010202, 3.0, 0.0, 0, 1, 0, 0)
    Event_32012250(2, 32010203, 30004, 20004, 16576, 0.0, 0, 0, 0, 0, 32011203, 0, 0, 0, 32010203)
    Event_32012270(2, 32010203, 30006, 20006, 32010203, 3.0, 0.0, 0, 1, 0, 0)
    RunCommonEvent(0, 90005211, args=(32010205, 30006, 20006, 32012205, 5.0, 0.0, 0, 1, 0, 0), arg_types="IiiIffIIII")
    Event_32012250(3, 32010211, 30002, 20002, 16574, 0.0, 0, 0, 0, 0, 32011211, 0, 0, 0, 32010211)
    Event_32012270(3, 32010211, 30005, 20005, 32010211, 3.0, 0.0, 0, 1, 0, 0)
    Event_32012250(4, 32010215, 30000, 20000, 16572, 0.0, 0, 0, 0, 0, 32011215, 0, 0, 0, 32010215)
    Event_32012270(4, 32010215, 30006, 20006, 32010215, 3.0, 0.0, 0, 1, 0, 0)
    Event_32012250(5, 32010218, 30004, 20004, 16576, 0.0, 0, 0, 0, 0, 32011218, 0, 0, 0, 32010218)
    Event_32012270(5, 32010218, 30005, 20005, 32010218, 3.0, 0.0, 0, 1, 0, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_32010519()
    Event_32012820()
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(32010519)
    EnableFlag(32010510)
    EnableFlag(32010515)
    EnableFlag(32010520)
    RunCommonEvent(0, 90005211, args=(32010205, 30006, 20006, 32012205, 5.0, 0.0, 0, 1, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(32010212, 32012300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32010212, 32012301, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32010217, 32012220, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32010219, 32012219, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32010220, 32012220, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32010300, 32012300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32010300, 32012301, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32010301, 32012301, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32010350, 32012350, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32010351, 32012350, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32010352, 32012350, 0.0, -1), arg_types="IIfi")


@NeverRestart(32012510)
def Event_32012510():
    """Event 32012510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            32010510,
            32010511,
            0,
            32011510,
            32011511,
            32013511,
            32011512,
            32013512,
            32012511,
            32012512,
            32010512,
            32010513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            32010515,
            32010516,
            0,
            32011515,
            32011516,
            32013516,
            32011517,
            32013517,
            32012516,
            32012517,
            32010517,
            32010518,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            32010520,
            32010521,
            0,
            32011520,
            32011521,
            32013521,
            32011522,
            32013522,
            32012521,
            32012522,
            32010522,
            32010523,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(32010519)
def Event_32010519():
    """Event 32010519"""
    EndIfThisEventSlotFlagEnabled()
    DisableThisSlotFlag()


@RestartOnRest(32012200)
def Event_32012200(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    special_effect_id: int,
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
    """Event 32012200"""
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
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect_id)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(32012250)
def Event_32012250(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    special_effect_id: int,
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
    """Event 32012250"""
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
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect_id)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(32012270)
def Event_32012270(
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
    """Event 32012270"""
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


@RestartOnRest(32012650)
def Event_32012650(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 32012650"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(700690)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, 700690)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9126, flag=flag, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=109, flag=flag, bit_count=1)
    EnableFlag(700690)


@RestartOnRest(32012651)
def Event_32012651(_, tutorial_param_id: int, flag: uint, flag_1: uint, tutorial_param_id_1: int):
    """Event 32012651"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag)
    IfLeavingSession(AND_1)
    IfInsideMap(AND_1, game_map=LIMGRAVE_TUNNELS)
    IfPlayerDoesNotHaveGood(AND_1, 9116, including_storage=True)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    EnableFlag(flag_1)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9116, flag=flag, bit_count=1)


@RestartOnRest(32012800)
def Event_32012800():
    """Event 32012800"""
    EndIfFlagEnabled(32010800)
    IfHealthValueLessThanOrEqual(MAIN, 32010800, value=0)
    Wait(4.0)
    PlaySoundEffect(32018000, 888880000, sound_type=SoundType.s_SFX)
    IfHealthValueEqual(MAIN, 32010800, value=0)
    KillBossAndDisplayBanner(character=32010800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(32010800)
    EnableFlag(9261)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61261)


@RestartOnRest(32012810)
def Event_32012810():
    """Event 32012810"""
    GotoIfFlagDisabled(Label.L0, flag=32010800)
    DisableCharacter(32010800)
    DisableAnimations(32010800)
    Kill(32010800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(32010800)
    GotoIfFlagEnabled(Label.L1, flag=32010801)
    ForceAnimation(32010800, 30000, loop=True, unknown2=1.0)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=32012801)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=32010800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(32010801)
    ForceAnimation(32010800, 20000, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 32012805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=32012800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(32010800)
    SetNetworkUpdateRate(32010800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(32010800, name=904600320)


@RestartOnRest(32012811)
def Event_32012811():
    """Event 32012811"""
    EndIfFlagEnabled(32010800)
    IfHealthRatioLessThanOrEqual(AND_1, 32010800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(32012802)


@RestartOnRest(32012820)
def Event_32012820():
    """Event 32012820"""
    EndIfFlagEnabled(32010800)
    EndIfFlagEnabled(32010801)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(32018590)
    DisableFlag(32018590)


@RestartOnRest(32012849)
def Event_32012849():
    """Event 32012849"""
    RunCommonEvent(
        0,
        9005800,
        args=(32010800, 32011800, 32012800, 32012805, 32015800, 10000, 32010801, 32012801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(32010800, 32011800, 32012800, 32012805, 32012806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(32010800, 32011800, 7, 32010801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(32010800, 931000, 32012805, 32012806, 0, 32012802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(32012920)
def Event_32012920():
    """Event 32012920"""
    DisableNetworkSync()
    IfObjectBackreadEnabled(MAIN, obj=32011515)
    EnableFlag(32010519)
    IfObjectBackreadDisabled(MAIN, obj=32011515)
    DisableFlag(32010519)
    Restart()
