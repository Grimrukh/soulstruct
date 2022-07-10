"""
linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1038430000, obj=1038431950, unknown=5.0)
    Event_1038432260(0, 1038430250, 1038431250, 1038430250, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    Event_1038432261(
        0,
        1038430250,
        1038431250,
        1038430250,
        1038435260,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1038430100,
        1038432250,
    )
    Event_1038432262(0, 1038430250, 0.0, 1038430250, 0.0, 1038430260, 30010, 20010, 20.0, 0.0, 0.0, 1038432250)
    Event_1038432262(1, 1038430250, 0.0, 1038430250, 0.0, 1038430261, 30010, 20010, 20.0, 0.0, 0.0, 1038432250)
    Event_1038432262(3, 1038430250, 0.0, 1038430250, 0.0, 1038430262, 30010, 20010, 20.0, 0.0, 0.0, 1038432250)
    RunCommonEvent(0, 90005704, args=(1038430700, 3381, 3380, 1038439201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1038430700, 3381, 3382, 1038439201, 3381, 3380, 3384, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1038430700, 3383, 3380, 3384), arg_types="IIII")
    Event_1038430700(0, character=1038430700)
    Event_1038430701(0, 1038430700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1038430700)
    RunCommonEvent(0, 90005201, args=(1038430210, 30001, 20001, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    Event_1038430702()


@RestartOnRest(1038432260)
def Event_1038432260(
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
    """Event 1038432260"""
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


@RestartOnRest(1038432261)
def Event_1038432261(
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
    """Event 1038432261"""
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


@RestartOnRest(1038432262)
def Event_1038432262(
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
    """Event 1038432262"""
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


@RestartOnRest(1038430700)
def Event_1038430700(_, character: uint):
    """Event 1038430700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3380)
    DisableFlag(1038439202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L9, flag=3389)
    GotoIfFlagEnabled(Label.L10, flag=3390)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagRangeAnyEnabled(MAIN, flag_range=(3389, 3390))
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=3380)
    GotoIfFlagEnabled(Label.L1, flag=3381)
    GotoIfFlagEnabled(Label.L3, flag=3383)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    SetTeamType(character, TeamType.HostileNPC)
    AddSpecialEffect(character, 9628)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagRangeAllDisabled(MAIN, flag_range=(3389, 3390))
    Restart()


@RestartOnRest(1038430701)
def Event_1038430701(_, character: uint):
    """Event 1038430701"""
    EndIfPlayerNotInOwnWorld()
    WaitFrames(frames=1)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=PLAYER)
    IfHealthLessThanOrEqual(OR_1, character, value=0.0)
    IfFlagRangeAnyEnabled(AND_1, flag_range=(1041389320, 1041389322))
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1041389334)


@RestartOnRest(1038430702)
def Event_1038430702():
    """Event 1038430702"""
    EndIfPlayerNotInOwnWorld()
    IfFlagRangeAnyEnabled(AND_1, flag_range=(1041389320, 1041389322))
    IfFlagDisabled(AND_1, 1041382729)
    IfFlagDisabled(AND_1, 1038412709)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(3398)
    EnableFlag(1038432709)
