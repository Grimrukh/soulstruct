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
    RegisterGrace(grace_flag=32040000, obj=32041950, unknown=5.0)
    Event_32042800()
    Event_32042810()
    Event_32042811()
    Event_32042849()
    Event_32042200(0, 32040206, 30004, 20004, 16576, 0.0, 0, 0, 0, 0, 32041682, 0, 0, 0)
    Event_32042250(0, 32040207, 30000, 20000, 16572, 0.0, 0, 0, 0, 0, 32041207, 0, 0, 0, 32040207)
    Event_32042270(0, 32040207, 30005, 20005, 32040207, 3.0, 0.0, 0, 1, 0, 0)
    Event_32042200(2, 32040210, 30004, 20004, 16576, 0.0, 0, 0, 0, 0, 32041681, 0, 0, 0)
    Event_32042200(3, 32040211, 30004, 20004, 16576, 0.0, 0, 0, 0, 0, 32041680, 0, 0, 0)
    Event_32042510()
    RunCommonEvent(
        0,
        90005501,
        args=(32040510, 32040511, 0, 32041510, 32041511, 32041512, 32040512),
        arg_types="IIIIIII",
    )
    Event_32042580()
    RunCommonEvent(
        0,
        90005646,
        args=(32040800, 32042840, 32042841, 32041840, 32042840, 32, 4, 0, 0),
        arg_types="IIIIIBBbb",
    )
    Event_32049570(
        0,
        flag=32040570,
        destination=32041570,
        left_flag=32042570,
        cancel_flag__right_flag=32042571,
        flag_1=32042572
    )
    Event_32042569(0, flag=32040570, obj=32041570, obj_1=32041571, obj_2=32041572, obj_3=32041573)
    RunCommonEvent(0, 900005610, args=(32041690, 100, 800, 0), arg_types="IiiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_32040519()
    RunCommonEvent(0, 90005250, args=(32040200, 32042200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32040217, 32042217, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005201, args=(32040221, 30005, 20005, 3.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(32040250, 15.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(32040302, 32042213, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32040303, 32042213, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32040306, 32042305, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32040350, 32042305, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32040351, 32042351, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32040400, 32042200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32040410, 32042410, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32040411, 32042410, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32040412, 32042217, 0.0, -1), arg_types="IIfi")


@NeverRestart(32042510)
def Event_32042510():
    """Event 32042510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            32040510,
            32040511,
            0,
            32041510,
            32041511,
            32043511,
            32041512,
            32043512,
            32042511,
            32042512,
            32040512,
            32040513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(32040519)
def Event_32040519():
    """Event 32040519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(32040510)
    DisableThisSlotFlag()


@RestartOnRest(32049570)
def Event_32049570(_, flag: uint, destination: uint, left_flag: uint, cancel_flag__right_flag: uint, flag_1: uint):
    """Event 32049570"""
    IfFlagEnabled(OR_1, flag)
    IfPlayerNotInOwnWorld(OR_1)
    EndIfConditionTrue(input_condition=OR_1)
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    IfActionButtonParamActivated(MAIN, action_button_id=9220, entity=destination)
    DisplayDialogAndSetFlags(
        message=108000,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=destination,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    StoreItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=8000, flag=flag_1, bit_count=2)
    IfEventValueGreaterThanOrEqual(AND_2, flag=flag_1, bit_count=6, value=2)
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 50050, unknown2=1.0)
    Wait(1.5)
    DisplayDialog(text=308000, anchor_entity=destination)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 60810, unknown2=1.0)
    Wait(1.3300000429153442)
    ForceAnimation(PLAYER, 60811, unknown2=1.0)
    Wait(1.5)
    DisplayDialog(text=208000, anchor_entity=destination)
    RemoveGoodFromPlayer(item=8000, quantity=2)
    EnableNetworkFlag(flag)


@RestartOnRest(32042569)
def Event_32042569(_, flag: uint, obj: uint, obj_1: uint, obj_2: uint, obj_3: uint):
    """Event 32042569"""
    EndIfThisEventSlotFlagEnabled()
    SkipLinesIfFlagDisabled(6, flag)
    DeleteObjectVFX(obj)
    DeleteObjectVFX(obj_3)
    EnableObject(obj_1)
    EnableObject(obj_2)
    DisableObject(obj_3)
    End()
    DeleteObjectVFX(obj)
    DeleteObjectVFX(obj_3)
    DisableObject(obj_1)
    DisableObject(obj_2)
    CreateObjectVFX(obj, vfx_id=200, model_point=806040)
    CreateObjectVFX(obj, vfx_id=201, model_point=806040)
    CreateObjectVFX(obj_3, vfx_id=101, model_point=806042)
    IfFlagEnabled(MAIN, flag)
    EnableObject(obj_1)
    Wait(1.3300000429153442)
    EnableObject(obj_2)
    Wait(0.5)
    DeleteObjectVFX(obj)
    DeleteObjectVFX(obj_3, erase_root=False)
    DisableObject(obj_3)


@RestartOnRest(32042580)
def Event_32042580():
    """Event 32042580"""
    RegisterLadder(start_climbing_flag=32040530, stop_climbing_flag=32040531, obj=32041530)
    RegisterLadder(start_climbing_flag=32040532, stop_climbing_flag=32040533, obj=32041532)


@RestartOnRest(32042200)
def Event_32042200(
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
    """Event 32042200"""
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


@RestartOnRest(32042250)
def Event_32042250(
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
    """Event 32042250"""
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


@RestartOnRest(32042270)
def Event_32042270(
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
    """Event 32042270"""
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


@RestartOnRest(32042800)
def Event_32042800():
    """Event 32042800"""
    EndIfFlagEnabled(32040800)
    IfHealthValueLessThanOrEqual(MAIN, 32040800, value=0)
    Wait(4.0)
    PlaySoundEffect(32048000, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 32040800)
    KillBossAndDisplayBanner(character=32040800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(32040800)
    EnableFlag(9263)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61263)


@RestartOnRest(32042810)
def Event_32042810():
    """Event 32042810"""
    GotoIfFlagDisabled(Label.L0, flag=32040800)
    DisableCharacter(32040800)
    DisableAnimations(32040800)
    Kill(32040800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(32040800)
    ForceAnimation(32040800, 30000, loop=True, unknown2=1.0)
    IfFlagEnabled(AND_2, 32042805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=32042800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ForceAnimation(32040800, 20000, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(32040800)
    SetNetworkUpdateRate(32040800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(32040800, name=904600321)


@RestartOnRest(32042811)
def Event_32042811():
    """Event 32042811"""
    EndIfFlagEnabled(32040800)
    IfHealthLessThanOrEqual(AND_1, 32040800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(32042802)


@RestartOnRest(32042849)
def Event_32042849():
    """Event 32042849"""
    RunCommonEvent(
        0,
        9005800,
        args=(32040800, 32041800, 32042800, 32042805, 32045800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(32040800, 32041800, 32042800, 32042805, 32042806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(32040800, 32041800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(32040800, 931000, 32042805, 32042806, 0, 32042802, 0, 0), arg_types="IiIIIIii")
