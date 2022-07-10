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
    RunCommonEvent(0, 90005600, args=(1050570000, 1050571950, 5.0, 1050570480), arg_types="IIfI")
    Event_1050572820(0, 1050570800, 30000, 20000, 1050572800, 0.0, 0, 0, 0, 0)
    RunCommonEvent(0, 90005870, args=(1050570800, 904980600, 24), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1050570800, 0, 1050570800, 0, 30530, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005870, args=(1050570850, 904811600, 18), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1050570850, 0, 1050570850, 0, 30555, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1050570850, 18, 0), arg_types="III")
    Event_1050572320(0, character=1050570320, destination=1051570320, special_effect=5030)
    Event_1050572330(0, character=1050570320, special_effect_id=5021)
    Event_1050572340(0, character=1050570320, region=1050572320, flag=1050572330)
    Event_1050572200(0, character=1050575200)
    Event_1050572250()
    Event_1050572250(slot=1)


@RestartOnRest(1050572200)
def Event_1050572200(_, character: uint):
    """Event 1050572200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@RestartOnRest(1050572250)
def Event_1050572250():
    """Event 1050572250"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=1050570250)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1050572250)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=1050570250,
        source_entity=1050572251,
        model_point=900,
        behavior_id=802105000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=1050570250,
        source_entity=1050572251,
        model_point=900,
        behavior_id=802105010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=1050570250,
        source_entity=1050572251,
        model_point=900,
        behavior_id=802105020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=1050570250,
        source_entity=1050572251,
        model_point=900,
        behavior_id=802105030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=1050570250,
        source_entity=1050572251,
        model_point=900,
        behavior_id=802105040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=1050570250,
        source_entity=1050572251,
        model_point=900,
        behavior_id=802105050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=1050570250,
        source_entity=1050572251,
        model_point=900,
        behavior_id=802105060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=1050570250,
        source_entity=1050572251,
        model_point=900,
        behavior_id=802105070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(1050572320)
def Event_1050572320(_, character: uint, destination: uint, special_effect: int):
    """Event 1050572320"""
    IfCharacterHasSpecialEffect(MAIN, character, special_effect)
    Move(
        character,
        destination=destination,
        destination_type=CoordEntityType.Object,
        model_point=90,
        copy_draw_parent=character,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(1050572330)
def Event_1050572330(_, character: uint, special_effect_id: int):
    """Event 1050572330"""
    AddSpecialEffect(character, special_effect_id)


@RestartOnRest(1050572340)
def Event_1050572340(_, character: uint, region: uint, flag: uint):
    """Event 1050572340"""
    IfCharacterAlive(AND_15, character)
    SkipLinesIfConditionTrue(1, AND_15)
    End()
    IfCharacterBackreadEnabled(AND_14, character)
    AwaitConditionTrue(AND_14)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfCharacterType(AND_1, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfAllPlayersOutsideRegion(AND_2, region=region)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    AddSpecialEffect(character, 15338)
    EnableNetworkFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterType(AND_5, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_5, PLAYER, 3710)
    IfConditionTrue(OR_5, input_condition=AND_5)
    IfCharacterHuman(OR_5, PLAYER)
    IfCharacterHollow(OR_5, PLAYER)
    IfCharacterWhitePhantom(OR_5, PLAYER)
    IfConditionTrue(AND_6, input_condition=OR_5)
    IfCharacterInsideRegion(AND_6, character=PLAYER, region=region)
    IfConditionTrue(OR_6, input_condition=AND_6)
    IfFlagDisabled(OR_6, flag)
    IfConditionTrue(MAIN, input_condition=OR_6)
    DisableNetworkFlag(flag)
    AddSpecialEffect(character, 15339)
    Wait(3.0)
    Restart()


@RestartOnRest(1050572820)
def Event_1050572820(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 1050572820"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    DisableAI(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
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
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    EnableAI(character)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()
