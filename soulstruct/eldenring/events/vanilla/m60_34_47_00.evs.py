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
    RegisterGrace(grace_flag=1034470000, obj=1034471951, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76214, 76211, 1034471981, 77220, 1, 78220, 78221, 78222, 78223, 78224, 78225, 78226, 78227, 78228, 78229),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005605,
        args=(1034471610, 10, 1, 0, 0, 10012690, 0, 1034472610, 1034472611, 1034472612, 1034470610, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    Event_1034472611(
        0,
        flag=1034470611,
        destination=1034471611,
        left_flag=1034472613,
        cancel_flag__right_flag=1034472614
    )
    Event_1034472612(0, flag=1034470611, obj=1034471612)
    Event_1034472260(0, 1034470250, 1034471250, 1034470250, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    Event_1034472260(1, 1034470251, 1034471251, 1034470251, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    Event_1034472261(
        0,
        1034470250,
        1034471250,
        1034470250,
        1034475260,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1034471300,
        1034472250,
    )
    Event_1034472261(
        1,
        1034470251,
        1034471251,
        1034470251,
        1034475263,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1034471310,
        1034472251,
    )
    Event_1034472262(0, 1034470250, 0.0, 1034470250, 0.0, 1034470260, 30010, 20010, 20.0, 0.0, 0.0, 1034472250)
    Event_1034472262(1, 1034470250, 0.0, 1034470250, 0.0, 1034470261, 30010, 20010, 20.0, 0.0, 0.0, 1034472250)
    Event_1034472262(3, 1034470250, 0.0, 1034470250, 0.0, 1034470262, 30010, 20010, 20.0, 0.0, 0.0, 1034472250)
    Event_1034472262(4, 1034470251, 0.0, 1034470251, 0.0, 1034470263, 30010, 20010, 20.0, 0.0, 0.0, 1034472251)
    Event_1034472262(5, 1034470251, 0.0, 1034470251, 0.0, 1034470264, 30010, 20010, 20.0, 0.0, 0.0, 1034472251)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(
        0,
        90005211,
        args=(1034470340, 30005, 20005, 1034472340, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(1034470200, 1034472200, 5.0, 0.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1034470201, 1034472200, 5.0, 2.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1034470202, 1034472200, 5.0, 1.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1034470203, 1034472200, 5.0, 0.5, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1034470204, 1034472200, 5.0, 1.5, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1034470205, 1034472200, 5.0, 0.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1034470206, 1034472200, 5.0, 2.0, 1705), arg_types="IIffi")


@RestartOnRest(1034472260)
def Event_1034472260(
    _,
    flag: uint,
    destination: uint,
    character: uint,
    seconds: float,
    seconds_1: float,
    seconds_2: float,
    seconds_3: float,
    seconds_4: float,
    seconds_5: float,
    seconds_6: float,
):
    """Event 1034472260"""
    EndIfFlagEnabled(flag)
    IfAttackedWithDamageType(AND_1, attacked_entity=character, attacker=20000)
    EndIfConditionTrue(input_condition=AND_1)
    ForceAnimation(destination, 0, unknown2=1.0)
    Move(character, destination=destination, destination_type=CoordEntityType.Object, model_point=220, short_move=True)
    Wait(5.400000095367432)
    Restart()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_2)
    Wait(seconds_3)
    Wait(seconds_4)
    Wait(seconds_5)
    Wait(seconds_6)


@RestartOnRest(1034472261)
def Event_1034472261(
    _,
    flag: uint,
    obj: uint,
    character: uint,
    character_1: uint,
    seconds: float,
    seconds_1: float,
    seconds_2: float,
    seconds_3: float,
    seconds_4: float,
    item_lot_param_id: int,
    flag_1: uint,
):
    """Event 1034472261"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    DisableObject(obj)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObject(obj)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=200, model_point=803160)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=20000)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    ForceAnimation(obj, 1, unknown2=1.0)
    DeleteObjectVFX(obj)
    Wait(1.0)
    DisableObject(obj)
    SkipLinesIfPlayerNotInOwnWorld(2)
    Wait(0.30000001192092896)
    AwardItemLot(item_lot_param_id, host_only=True)
    End()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_2)
    Wait(seconds_3)
    Wait(seconds_4)


@RestartOnRest(1034472262)
def Event_1034472262(
    _,
    character: uint,
    seconds: float,
    attacked_entity: uint,
    seconds_1: float,
    character_1: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds_2: float,
    seconds_3: float,
    flag: uint,
):
    """Event 1034472262"""
    EndIfFlagEnabled(character)
    GotoIfUnknown_1004_05(Label.L0, character=character_1, unk_8_12=True)
    ForceAnimation(character_1, animation_id, unknown2=1.0)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacked_entity, attacker=20000)
    IfAttackedWithDamageType(OR_2, attacked_entity=character_1, attacker=20000)
    IfUnknownCharacterCondition_34(OR_2, character=character_1, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character_1, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character_1, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character_1, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character_1, unk_8_12=260, unk_12_16=1)
    IfEntityWithinDistance(OR_2, entity=character_1, other_entity=20000, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_2)
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
    IfConditionTrue(OR_3, input_condition=AND_4)
    IfConditionTrue(OR_3, input_condition=AND_5)
    IfConditionTrue(OR_3, input_condition=AND_6)
    IfConditionTrue(OR_3, input_condition=AND_7)
    IfConditionTrue(OR_3, input_condition=AND_8)
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_3)
    EnableNetworkFlag(flag)
    Unknown_2004_83(character=character_1, unk_4_8=1)
    Wait(seconds_2)
    ForceAnimation(character_1, animation_id_1, unknown2=1.0)
    End()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_3)


@RestartOnRest(1034472611)
def Event_1034472611(_, flag: uint, destination: uint, left_flag: uint, cancel_flag__right_flag: uint):
    """Event 1034472611"""
    IfFlagEnabled(OR_1, flag)
    IfPlayerNotInOwnWorld(OR_1)
    EndIfConditionTrue(input_condition=OR_1)
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    IfActionButtonParamActivated(MAIN, action_button_id=9523, entity=destination)
    DisplayDialogAndSetFlags(
        message=108186,
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
    IfPlayerHasGood(AND_2, 8186)
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 50050, unknown2=1.0)
    Wait(1.5)
    DisplayDialog(text=308186, anchor_entity=destination)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 60810, unknown2=1.0)
    Wait(2.5)
    EnableNetworkFlag(flag)
    EnableNetworkFlag(1034470610)
    DisplayDialog(text=208186, anchor_entity=destination)
    RemoveGoodFromPlayer(item=8186, quantity=1)


@RestartOnRest(1034472612)
def Event_1034472612(_, flag: uint, obj: uint):
    """Event 1034472612"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(obj)
    IfFlagEnabled(MAIN, flag)
    EnableObject(obj)
