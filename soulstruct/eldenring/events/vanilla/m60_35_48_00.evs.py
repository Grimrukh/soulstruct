"""
linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1035482210(0, character=1035480220)
    Event_1035482210(1, character=1035480230)
    Event_1035482270()
    Event_1035482270(slot=1)
    Event_1035482280()
    Event_1035482280(slot=1)
    Event_1035482260(0, 1035480250, 1035481250, 1035480250, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    Event_1035482261(
        0,
        1035480250,
        1035481250,
        1035480250,
        1035485260,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1035480100,
        1035482250,
    )
    Event_1035482262(0, 1035480250, 0.0, 1035480250, 0.0, 1035480260, 30010, 20010, 20.0, 0.0, 0.0, 1035482250)
    Event_1035482262(1, 1035480250, 0.0, 1035480250, 0.0, 1035480261, 30010, 20010, 20.0, 0.0, 0.0, 1035482250)
    Event_1035482262(3, 1035480250, 0.0, 1035480250, 0.0, 1035480262, 30010, 20010, 20.0, 0.0, 0.0, 1035482250)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005201, args=(1035480200, 30001, 20001, 15.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1035480200, 15.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1035480210, 1.0, 0.0, -1), arg_types="Iffi")


@RestartOnRest(1035482210)
def Event_1035482210(_, character: uint):
    """Event 1035482210"""
    Kill(character)


@RestartOnRest(1035482260)
def Event_1035482260(
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
    """Event 1035482260"""
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


@RestartOnRest(1035482261)
def Event_1035482261(
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
    """Event 1035482261"""
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


@RestartOnRest(1035482262)
def Event_1035482262(
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
    """Event 1035482262"""
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


@RestartOnRest(1035482270)
def Event_1035482270():
    """Event 1035482270"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=1035480270)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1035482270)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=1035480270,
        source_entity=1035482271,
        model_point=900,
        behavior_id=802102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=1035480270,
        source_entity=1035482271,
        model_point=900,
        behavior_id=802102010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=1035480270,
        source_entity=1035482271,
        model_point=900,
        behavior_id=802102020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=1035480270,
        source_entity=1035482271,
        model_point=900,
        behavior_id=802102030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=1035480270,
        source_entity=1035482271,
        model_point=900,
        behavior_id=802102040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=1035480270,
        source_entity=1035482271,
        model_point=900,
        behavior_id=802102050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=1035480270,
        source_entity=1035482271,
        model_point=900,
        behavior_id=802102060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=1035480270,
        source_entity=1035482271,
        model_point=900,
        behavior_id=802102070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(1035482280)
def Event_1035482280():
    """Event 1035482280"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=1035480280)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1035482280)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=1035480280,
        source_entity=1035482281,
        model_point=900,
        behavior_id=802102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=1035480280,
        source_entity=1035482281,
        model_point=900,
        behavior_id=802102010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=1035480280,
        source_entity=1035482281,
        model_point=900,
        behavior_id=802102020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=1035480280,
        source_entity=1035482281,
        model_point=900,
        behavior_id=802102030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=1035480280,
        source_entity=1035482281,
        model_point=900,
        behavior_id=802102040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=1035480280,
        source_entity=1035482281,
        model_point=900,
        behavior_id=802102050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=1035480280,
        source_entity=1035482281,
        model_point=900,
        behavior_id=802102060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=1035480280,
        source_entity=1035482281,
        model_point=900,
        behavior_id=802102070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    Restart()
