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
    Event_1054562200(0, character=1054565200)
    Event_1054562500()


@RestartOnRest(1054562200)
def Event_1054562200(_, character: uint):
    """Event 1054562200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@RestartOnRest(1054562500)
def Event_1054562500():
    """Event 1054562500"""
    EndIfFlagEnabled(1254560800)
    SetCharacterTalkRange(character=1054560100, distance=300.0)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005870, args=(1054560800, 904503600, 25), arg_types="IiI")
    RunCommonEvent(0, 90005861, args=(1254560800, 0, 1054560800, 1, 30510, 30066, 0.0), arg_types="IIIIiif")
    Event_1054562815()
    Event_1054562820(
        0,
        1054560800,
        30003,
        20003,
        1054562830,
        0.0,
        0.0,
        0,
        0,
        0,
        0,
        1054562831,
        1054562832,
        1054562833,
        1054562834,
        1054562835,
    )


@RestartOnRest(1054562815)
def Event_1054562815():
    """Event 1054562815"""
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=1054562811)
    AwaitConditionTrue(OR_1)
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=1254560800)
    Unknown_1004_04(line_count=1, character=1054560800, unk_8_12=1)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=1054562810)
    GotoIfConditionTrue(Label.L2, input_condition=OR_2)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=1054562812)
    GotoIfConditionFalse(Label.L3, input_condition=OR_3)
    Wait(1.0)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    CancelSpecialEffect(PLAYER, 4213)
    Unknown_2003_68(unknown1=10, unknown2=30.0, unknown3=0)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Unknown_2003_68(unknown1=16, unknown2=-1.0, unknown3=0)
    Wait(5.0)
    AddSpecialEffect(PLAYER, 4213)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    Unknown_2003_68(unknown1=10, unknown2=30.0, unknown3=0)
    Wait(3.0)
    CancelSpecialEffect(PLAYER, 4213)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    CancelSpecialEffect(PLAYER, 4213)
    Unknown_2003_68(unknown1=-1, unknown2=-1.0, unknown3=0)
    End()


@RestartOnRest(1054562820)
def Event_1054562820(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    region_1: uint,
    region_2: uint,
    region_3: uint,
    region_4: uint,
    region_5: uint,
):
    """Event 1054562820"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
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
    SkipLinesIfUnsignedEqual(1, left=0, right=region)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region_1)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region_2)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region_3)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region_4)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region_5)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_3)
    IfOutsideMap(AND_1, game_map=SPIRITCALLER_CAVE)
    IfCharacterBackreadEnabled(AND_1, character)
    IfUnknownCondition_31(AND_1, hours=16, unknown1=3.0, unknown2=0)
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
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    Unknown_2004_83(character=character, unk_4_8=1)
    EnableNetworkFlag(1054562820)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    IfCharacterInsideRegion(OR_5, character=PLAYER, region=region)
    GotoIfConditionTrue(Label.L5, input_condition=OR_5)
    IfCharacterInsideRegion(OR_6, character=PLAYER, region=region_1)
    GotoIfConditionTrue(Label.L6, input_condition=OR_6)
    IfCharacterInsideRegion(OR_7, character=PLAYER, region=region_2)
    GotoIfConditionTrue(Label.L7, input_condition=OR_7)
    IfCharacterInsideRegion(OR_8, character=PLAYER, region=region_3)
    GotoIfConditionTrue(Label.L8, input_condition=OR_8)
    IfCharacterInsideRegion(OR_8, character=PLAYER, region=region_4)
    GotoIfConditionTrue(Label.L9, input_condition=OR_8)
    IfCharacterInsideRegion(OR_8, character=PLAYER, region=region_5)
    GotoIfConditionTrue(Label.L10, input_condition=OR_8)
    Goto(Label.L14)

    # --- Label 5 --- #
    DefineLabel(5)
    Move(character, destination=1054562820, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L14)

    # --- Label 6 --- #
    DefineLabel(6)
    Move(character, destination=1054562821, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L14)

    # --- Label 7 --- #
    DefineLabel(7)
    Move(character, destination=1054562822, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L14)

    # --- Label 8 --- #
    DefineLabel(8)
    Move(character, destination=1054562823, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L14)

    # --- Label 9 --- #
    DefineLabel(9)
    Move(character, destination=1054562824, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L14)

    # --- Label 10 --- #
    DefineLabel(10)
    Move(character, destination=1054562825, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L14)

    # --- Label 14 --- #
    DefineLabel(14)
    AddSpecialEffect(character, 10206)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()
