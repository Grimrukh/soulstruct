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
    RegisterGrace(grace_flag=1034480000, obj=1034481950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76214, 76212, 1034481980, 77220, 2, 78220, 78221, 78222, 78223, 78224, 78225, 78226, 78227, 78228, 78229),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005460, args=(1034480200,))
    RunCommonEvent(0, 90005461, args=(1034480200,))
    RunCommonEvent(0, 90005462, args=(1034480200,))
    RunCommonEvent(0, 90005460, args=(1034480201,))
    RunCommonEvent(0, 90005461, args=(1034480201,))
    RunCommonEvent(0, 90005462, args=(1034480201,))
    RunCommonEvent(0, 90005525, args=(1034480610, 1034481610), arg_types="II")
    RunCommonEvent(0, 90005525, args=(1034480611, 1034481611), arg_types="II")
    Event_1034482600(0, obj=1034481620, entity=1034481621, flag=82022)
    Event_1034482800()
    Event_1034482810()
    Event_1034482849()
    Event_1034482610(0, obj=1034481640, flag=1034482640, owner_entity=1034480640)
    Event_1034482610(1, obj=1034481641, flag=1034482641, owner_entity=1034480640)
    Event_1034482610(2, obj=1034481642, flag=1034482642, owner_entity=1034480640)
    Event_1034482610(3, obj=1034481643, flag=1034482643, owner_entity=1034480640)
    Event_1034482610(4, obj=1034481644, flag=1034482644, owner_entity=1034480640)
    Event_1034482610(5, obj=1034481645, flag=1034482645, owner_entity=1034480640)
    Event_1034482610(6, obj=1034481646, flag=1034482646, owner_entity=1034480640)
    Event_1034482610(7, obj=1034481647, flag=1034482647, owner_entity=1034480640)
    Event_1034482610(8, obj=1034481648, flag=1034482648, owner_entity=1034480640)
    Event_1034482610(9, obj=1034481649, flag=1034482649, owner_entity=1034480640)
    Event_1034482260(0, 1034480250, 1034481250, 1034480250, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    Event_1034482260(1, 1034480251, 1034481251, 1034480251, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    Event_1034482261(
        0,
        1034480250,
        1034481250,
        1034480250,
        1034485260,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1034481300,
        1034482250,
    )
    Event_1034482261(
        1,
        1034480251,
        1034481251,
        1034480251,
        1034485263,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1034481310,
        1034482251,
    )
    Event_1034482262(0, 1034480250, 0.0, 1034480250, 0.0, 1034480260, 30010, 20010, 20.0, 0.0, 0.0, 1034482250)
    Event_1034482262(1, 1034480250, 0.0, 1034480250, 0.0, 1034480261, 30010, 20010, 20.0, 0.0, 0.0, 1034482250)
    Event_1034482262(3, 1034480250, 0.0, 1034480250, 0.0, 1034480262, 30010, 20010, 20.0, 0.0, 0.0, 1034482250)
    Event_1034482262(4, 1034480251, 0.0, 1034480251, 0.0, 1034480263, 30010, 20010, 20.0, 0.0, 0.0, 1034482251)
    Event_1034482262(5, 1034480251, 0.0, 1034480251, 0.0, 1034480264, 30010, 20010, 20.0, 0.0, 0.0, 1034482251)
    RunCommonEvent(0, 90005706, args=(1034480700, 930023, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1034480700)
    RunCommonEvent(0, 90005251, args=(1034480210, 2.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(1034480210, 1034482210, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1034480212, 1034482210, 15.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1034480213, 1034482210, 15.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1034480214, 1034482210, 15.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1034480215, 1034482210, 15.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1034480211, 1034482211, 15.0, 0.0, 0), arg_types="IIffi")


@RestartOnRest(1034482260)
def Event_1034482260(
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
    """Event 1034482260"""
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


@RestartOnRest(1034482261)
def Event_1034482261(
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
    """Event 1034482261"""
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


@RestartOnRest(1034482262)
def Event_1034482262(
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
    """Event 1034482262"""
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


@RestartOnRest(1034482600)
def Event_1034482600(_, obj: uint, entity: uint, flag: uint):
    """Event 1034482600"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    CreateObjectVFX(obj, vfx_id=200, model_point=803220)

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(MAIN, flag)
    ForceAnimation(entity, 1, unknown2=1.0)
    DeleteObjectVFX(obj)


@RestartOnRest(1034482610)
def Event_1034482610(_, obj: uint, flag: uint, owner_entity: uint):
    """Event 1034482610"""
    EndIfFlagEnabled(flag)
    EndIfObjectDestroyed(obj)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=obj, attacker=20000)
    IfEntityWithinDistance(OR_2, entity=obj, other_entity=20000, radius=2.0)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DestroyObject(obj, request_slot=0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    End()


@RestartOnRest(1034482800)
def Event_1034482800():
    """Event 1034482800"""
    EndIfFlagEnabled(1034480800)
    IfHealthValueLessThanOrEqual(MAIN, 1034480800, value=0)
    Wait(4.0)
    PlaySoundEffect(1034480800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 1034480800)
    KillBossAndDisplayBanner(character=1034480800, banner_type=BannerType.DutyFulfilled)
    EnableObjectActivation(1034481540, obj_act_id=-1)
    EnableFlag(1034480800)
    End()


@RestartOnRest(1034482810)
def Event_1034482810():
    """Event 1034482810"""
    GotoIfFlagDisabled(Label.L0, flag=1034480800)
    DisableCharacter(1034480800)
    DisableAnimations(1034480800)
    Kill(1034480800)
    EnableObjectActivation(1034481540, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(1034480800, 30000, loop=True, unknown2=1.0)
    DisableAI(1034480800)
    IfFlagEnabled(AND_2, 1034482805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=1034482800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(1034480800)
    SetNetworkUpdateRate(1034480800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(1034480800, 20000, unknown2=1.0)
    EnableBossHealthBar(1034480800, name=904020540)
    DisableObjectActivation(1034481540, obj_act_id=-1)


@RestartOnRest(1034482849)
def Event_1034482849():
    """Event 1034482849"""
    RunCommonEvent(
        0,
        9005800,
        args=(1034480800, 1034481800, 1034482800, 1034482805, 1034485800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005801,
        args=(1034480800, 1034481800, 1034482800, 1034482805, 1034482806, 10000),
        arg_types="IIIIIi",
    )
    RunCommonEvent(0, 9005811, args=(1034480800, 1034481800, 3, 0), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(1034480800, 920900, 1034482805, 1034482806, 0, 1034482802, 0, 0),
        arg_types="IiIIIIii",
    )
    RunCommonEvent(0, 9005812, args=(1034480800, 1034481801, 3, 0, 0), arg_types="IIiIi")
