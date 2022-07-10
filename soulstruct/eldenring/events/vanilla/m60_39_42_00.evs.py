"""
linked:
0
72
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1039420000, obj=1039421950, unknown=5.0)
    Event_1039422202(0, character=1039420202)
    Event_1039422202(1, character=1039420203)
    Event_1039422202(2, character=1039420204)
    Event_1039422210(0, character=1039420210, region=1039422210, flag=1039422210)
    Event_1039422210(1, character=1039420211, region=1039422210, flag=1039422211)
    Event_1039422210(2, character=1039420212, region=1039422210, flag=1039422212)
    Event_1039422210(3, character=1039420213, region=1039422210, flag=1039422213)
    Event_1039422210(4, character=1039420214, region=1039422210, flag=1039422214)
    Event_1039422210(5, character=1039420215, region=1039422210, flag=1039422215)
    Event_1039422210(6, character=1039420216, region=1039422210, flag=1039422216)
    Event_1039422210(7, character=1039420217, region=1039422210, flag=1039422217)
    Event_1039422210(8, character=1039420218, region=1039422210, flag=1039422218)
    Event_1039422340(0, character=1039420340, region=1039422340, flag=1039422340)
    Event_1039422200(0, attacker__character=1039425200, region=1039422200)
    Event_1039422600(0, obj=1039421600, entity=1039421601, flag=82020)
    RunCommonEvent(
        0,
        90005605,
        args=(1039421610, 60, 35, 45, 0, 1035452630, 0, 1035452610, 1039422611, 1039422612, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    RunCommonEvent(0, 90005630, args=(61394200, 1039421500, 115), arg_types="IIi")
    RunCommonEvent(0, 90005683, args=(62203, 1039421684, 209, 78294, 78294), arg_types="IIiII")
    RunCommonEvent(0, 90005631, args=(1039421640, 61020), arg_types="Ii")
    RunCommonEvent(0, 90005706, args=(1039420700, 930025, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1039420700)


@RestartOnRest(1039422200)
def Event_1039422200(_, attacker__character: uint, region: uint):
    """Event 1039422200"""
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5657)
    AddSpecialEffect(attacker__character, 4802)
    EndIfFlagEnabled(1039422200)
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5657)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacker__character, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacker__character, attacker=35000)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000, attacker=attacker__character)
    IfEntityWithinDistance(OR_2, entity=PLAYER, other_entity=attacker__character, radius=10.0)
    IfEntityWithinDistance(OR_2, entity=35000, other_entity=attacker__character, radius=10.0)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfCharacterInsideRegion(OR_2, character=35000, region=region)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1039422200)
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5657)


@RestartOnRest(1039422202)
def Event_1039422202(_, character: uint):
    """Event 1039422202"""
    Kill(character)
    End()


@RestartOnRest(1039422210)
def Event_1039422210(_, character: uint, region: uint, flag: uint):
    """Event 1039422210"""
    IfCharacterDead(AND_10, character)
    EndIfConditionTrue(input_condition=AND_10)
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    DisableCharacter(character)
    DisableAnimations(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
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
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_4)
    IfConditionTrue(OR_3, input_condition=AND_5)
    IfConditionTrue(OR_3, input_condition=AND_6)
    IfConditionTrue(OR_3, input_condition=AND_7)
    IfConditionTrue(OR_3, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_3)
    EnableNetworkFlag(flag)
    Unknown_2004_83(character=character, unk_4_8=1)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
    ForceAnimation(character, 30004, unknown2=1.0)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 20004, unknown2=1.0)
    End()


@RestartOnRest(1039422340)
def Event_1039422340(_, character: uint, region: uint, flag: uint):
    """Event 1039422340"""
    IfCharacterDead(AND_10, character)
    EndIfConditionTrue(input_condition=AND_10)
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    DisableCharacter(character)
    DisableAnimations(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
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
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_4)
    IfConditionTrue(OR_3, input_condition=AND_5)
    IfConditionTrue(OR_3, input_condition=AND_6)
    IfConditionTrue(OR_3, input_condition=AND_7)
    IfConditionTrue(OR_3, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_3)
    EnableNetworkFlag(flag)
    Unknown_2004_83(character=character, unk_4_8=1)
    ForceAnimation(character, 30004, unknown2=1.0)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 20004, unknown2=1.0)
    End()


@RestartOnRest(1039422600)
def Event_1039422600(_, obj: uint, entity: uint, flag: uint):
    """Event 1039422600"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    CreateObjectVFX(obj, vfx_id=200, model_point=803220)

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(MAIN, flag)
    ForceAnimation(entity, 1, unknown2=1.0)
    DeleteObjectVFX(obj)


@RestartOnRest(1039422610)
def Event_1039422610(
    _,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
):
    """Event 1039422610"""
    EndIfTryingToCreateSession()
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    IfLeavingSession(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9140, entity=anchor_entity)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialogAndSetFlags(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=anchor_entity,
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
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)
