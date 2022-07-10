"""
linked:


strings:

"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@RestartOnRest(90005200)
def Event_90005200(
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
    """Event 90005200"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
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
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(90005201)
def Event_90005201(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 90005201"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
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
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
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


@RestartOnRest(90005210)
def Event_90005210(
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
):
    """Event 90005210"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
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
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=region)
    IfEntityWithinDistance(AND_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=AND_3)
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
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(90005211)
def Event_90005211(
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
):
    """Event 90005211"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
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
    SkipLinesIfUnsignedEqual(1, left=0, right=region)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_3)
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
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(90005213)
def Event_90005213(
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
    character_1: uint,
    seconds_1: float,
):
    """Event 90005213"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
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
    SkipLinesIfUnsignedEqual(1, left=0, right=region)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfUnknownCharacterCondition_35(AND_11, character=character_1, unk_8_12=1)
    IfConditionTrue(OR_3, input_condition=AND_11)
    IfConditionTrue(AND_1, input_condition=OR_3)
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
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_11)
    Wait(seconds)
    SkipLines(1)
    Wait(seconds_1)
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


@RestartOnRest(90005220)
def Event_90005220(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
):
    """Event 90005220"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterHasSpecialEffect(OR_11, character, 5080)
    IfCharacterHasSpecialEffect(OR_11, character, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Battle)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown5)
    SkipLinesIfUnsignedEqual(1, left=left_2, right=0)
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
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(90005221)
def Event_90005221(_, character: uint, animation_id: int, animation_id_1: int, seconds: float, left: uint):
    """Event 90005221"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
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
    Unknown_2004_83(character=character, unk_4_8=1)
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


@RestartOnRest(90005250)
def Event_90005250(_, character: uint, region: uint, seconds: float, animation_id: int):
    """Event 90005250"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(90005251)
def Event_90005251(_, character: uint, radius: float, seconds: float, animation_id: int):
    """Event 90005251"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(90005260)
def Event_90005260(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 90005260"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=region)
    IfEntityWithinDistance(AND_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=AND_3)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(90005261)
def Event_90005261(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 90005261"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
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
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_3)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(90005271)
def Event_90005271(_, character: uint, seconds: float, animation_id: int):
    """Event 90005271"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
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
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(90005300)
def Event_90005300(_, flag: uint, character: uint, item_lot_param_id: int, seconds: float, left: int):
    """Event 90005300"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    SkipLinesIfValueEqual(3, left=left, right=0)
    DisableCharacter(character)
    DropMandatoryTreasure(character)
    End()
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterDrawGroupEnabled(MAIN, character=character)
    Wait(seconds)
    EnableFlag(flag)
    EndIfPlayerNotInOwnWorld()
    EndIfValueEqual(left=left, right=1)
    EndIfValueEqual(left=item_lot_param_id, right=0)
    AwardItemLot(item_lot_param_id, host_only=True)
    End()


@RestartOnRest(90005360)
def Event_90005360(_, flag: uint, character: uint, item_lot_param_id: int):
    """Event 90005360"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(MAIN, flag)
    DisplayBanner(BannerType.HollowArenaDraw)
    EndIfPlayerNotInOwnWorld()
    AwardItemLot(item_lot_param_id, host_only=True)


@RestartOnRest(90005390)
def Event_90005390(
    _,
    flag: uint,
    flag_1: uint,
    anchor_entity: uint,
    character: uint,
    left: int,
    item_lot_param_id: int,
):
    """Event 90005390"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag_1)
    IfCharacterDead(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(1.0)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)
    CreateTemporaryVFX(
        vfx_id=601111,
        anchor_entity=anchor_entity,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(
        vfx_id=601110,
        anchor_entity=anchor_entity,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 3 --- #
    DefineLabel(3)
    Wait(3.0)
    DisableCharacter(character)
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfValueEqual(1, left=item_lot_param_id, right=0)
    AwardItemLot(item_lot_param_id, host_only=True)
    EnableNetworkFlag(flag)


@RestartOnRest(90005391)
def Event_90005391(_, flag: uint, flag_1: uint, character: uint, character_1: uint, left: int):
    """Event 90005391"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableGravity(character_1)
    DisableAI(character_1)
    Unknown_2004_73(entity=character_1, unk_4_8=1)
    IfCharacterDead(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetBackreadStateAlternate(character, True)
    SetBackreadStateAlternate(character_1, True)
    Wait(0.5)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=character,
    )
    Wait(0.5)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)
    CreateTemporaryVFX(vfx_id=601101, anchor_entity=character, model_point=900, anchor_type=CoordEntityType.Character)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(vfx_id=601100, anchor_entity=character, model_point=900, anchor_type=CoordEntityType.Character)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character_1)
    EnableGravity(character_1)
    EnableAnimations(character_1)
    EnableAI(character_1)
    DisableCharacter(character)
    SetBackreadStateAlternate(character, False)
    SetBackreadStateAlternate(character_1, False)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(flag_1)


@RestartOnRest(90005400)
def Event_90005400(_, character: uint, special_effect_id: int, seconds: float, seconds_1: float, left: uint):
    """Event 90005400"""
    EndIfThisEventSlotFlagEnabled()
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    SkipLinesIfValueEqual(2, left=special_effect_id, right=0)
    AddSpecialEffect(character, special_effect_id)
    SkipLines(1)
    AddSpecialEffect(character, 4421)
    ForceAnimation(character, 14100, loop=True, unknown2=1.0)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfCharacterHasSpecialEffect(OR_2, character, 5112)
    IfConditionTrue(MAIN, input_condition=OR_2)
    WaitFrames(frames=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5111)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=character, special_effect=5112)
    Wait(seconds_1)
    SkipLines(1)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, 14102, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(90005401)
def Event_90005401(_, flag: uint, character: uint):
    """Event 90005401"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    AddSpecialEffect(character, 4430)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterHasSpecialEffect(AND_1, character, 4431)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)


@RestartOnRest(90005410)
def Event_90005410(_, flag: uint, character: uint, unk_8_12: uint):
    """Event 90005410"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterHasSpecialEffect(AND_1, character, 9500)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfFlagEnabled(OR_1, flag)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    Unknown_2004_71(unk_0_4=0, unk_4_8=0, unk_8_12=unk_8_12)
    IfPlayerInOwnWorld(AND_3)
    IfCharacterHasSpecialEffect(AND_3, 20000, 202)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfFlagDisabled(OR_3, flag)
    IfConditionTrue(MAIN, input_condition=OR_3)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableNetworkFlag(flag)
    Restart()


@RestartOnRest(90005411)
def Event_90005411(_, obj: uint, character: uint, left: uint):
    """Event 90005411"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfUnsignedNotEqual(1, left=left, right=0)
    WaitFrames(frames=1)
    CreateObjectVFX(obj, vfx_id=200, model_point=620)
    IfCharacterHasSpecialEffect(MAIN, character, 9502)
    DeleteObjectVFX(obj)
    IfCharacterHasSpecialEffect(MAIN, character, 9503)
    Restart()


@RestartOnRest(90005420)
def Event_90005420(
    _,
    character__obj_2: uint,
    obj__obj_1__obj_2: uint,
    obj_1: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    seconds: float,
):
    """Event 90005420"""
    DisableAnimations(character__obj_2)
    Unknown_2005_17(obj_1=obj__obj_1__obj_2, obj_2=character__obj_2)
    Unknown_2005_18(obj_1=obj_1, obj_2=obj__obj_1__obj_2, unk_8_12=151)
    SetNetworkUpdateRate(character__obj_2, is_fixed=True, update_rate=CharacterUpdateRate.Unknown102)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Unknown105)
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(character_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Unknown_2004_60(character=character_1, obj=obj__obj_1__obj_2)
    Unknown_2004_60(character=character_2, obj=obj__obj_1__obj_2)
    End()
    Wait(seconds)


@RestartOnRest(90005421)
def Event_90005421(_, character: uint, obj: uint, flag: uint):
    """Event 90005421"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    DisableObjectActivation(obj, obj_act_id=-1)
    IfCharacterHasSpecialEffect(AND_1, character, 11500)
    IfFlagDisabled(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableObjectActivation(obj, obj_act_id=-1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 11500)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Restart()


@RestartOnRest(90005422)
def Event_90005422(_, flag: uint, obj: uint, obj_act_id: uint):
    """Event 90005422"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableTreasure(obj=obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableTreasure(obj=obj)
    IfPlayerInOwnWorld(AND_1)
    IfObjectActivated(AND_1, obj_act_id=obj_act_id)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfObjectDestroyed(OR_1, obj)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Wait(3.200000047683716)
    EnableTreasure(obj=obj)


@RestartOnRest(90005423)
def Event_90005423(_, character: uint):
    """Event 90005423"""
    IfCharacterHasSpecialEffect(AND_1, character, 5551)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Unknown_2004_60(character=character, obj=0)
    ChangeCharacterCloth(character, bit_count=20, state_id=2)


@RestartOnRest(90005424)
def Event_90005424(_, obj: uint, character: uint, character_1: uint, character_2: uint, obj_1: uint):
    """Event 90005424"""
    IfObjectDestroyed(MAIN, obj)
    ChangeCharacterCloth(character, bit_count=20, state_id=2)
    ChangeCharacterCloth(character_1, bit_count=20, state_id=2)
    AddSpecialEffect(character, 5551)
    AddSpecialEffect(character_1, 5551)
    Kill(character_2, award_souls=True)
    DisableObject(obj_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    EnableTreasure(obj=obj)


@NeverRestart(90005440)
def Event_90005440(_, character: uint, character_1: uint):
    """Event 90005440"""
    AddSpecialEffect(character_1, 14500)
    DisableHealthBar(character_1)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 3245)
    IfEntityWithinDistance(AND_1, entity=character_1, other_entity=PLAYER, radius=6.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(character)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character_1, 14501)
    AddSpecialEffect(character_1, 14502)
    EnableHealthBar(character_1)
    SetLockOnPoint(character=character_1, lock_on_model_point=220, state=True)
    IfCharacterDoesNotHaveSpecialEffect(OR_2, PLAYER, 3245)
    IfEntityBeyondDistance(OR_2, entity=character_1, other_entity=PLAYER, radius=6.0)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character_1, 14503)
    IfPlayerInOwnWorld(AND_2)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Restart()
    AICommand(0, command_id=0, command_slot=0)
    EzstateAIRequest(0, command_id=0, command_slot=0)


@RestartOnRest(90005450)
def Event_90005450(_, character__unk_0_4: uint, obj: uint, obj_1: uint, obj_2: uint):
    """Event 90005450"""
    SetBackreadStateAlternate(character__unk_0_4, True)
    EnableImmortality(character__unk_0_4)
    Unknown_2004_63(unk_0_4=character__unk_0_4, unk_4_8=2000.0)
    Unknown_2004_69(unk_0_4=character__unk_0_4, unk_4_8=0)
    Unknown_2004_70(unk_0_4=character__unk_0_4, unk_4_8=1)
    DisableHealthBar(character__unk_0_4)
    AttachObjectToCharacter(character=character__unk_0_4, model_point=100, obj=obj)
    AttachObjectToCharacter(character=character__unk_0_4, model_point=80, obj=obj_1)
    AttachObjectToCharacter(character=character__unk_0_4, model_point=165, obj=obj_2)


@RestartOnRest(90005451)
def Event_90005451(_, character: uint, obj: uint):
    """Event 90005451"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfUnknownObjectCondition_6(
        AND_1,
        unk_4_5=1,
        obj=obj,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=0.44999998807907104,
    )
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 12450)


@RestartOnRest(90005452)
def Event_90005452(_, character: uint, flag: uint):
    """Event 90005452"""
    EndIfFlagEnabled(flag)
    IfCharacterHasSpecialEffect(AND_1, character, 12455)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)


@RestartOnRest(90005453)
def Event_90005453(_, character__obj: uint, obj: uint, model_point: int, seconds: float):
    """Event 90005453"""
    EndIfObjectDestroyed(obj)
    AttachObjectToCharacter(character=character__obj, model_point=model_point, obj=obj)
    IfCharacterWhitePhantom(OR_10, PLAYER)
    IfCharacterHollow(OR_10, PLAYER)
    IfCharacterType(OR_10, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterType(OR_10, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_10, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_10, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_10, PLAYER, character_type=CharacterType.Unknown18)
    GotoIfConditionFalse(Label.L10, input_condition=OR_10)
    EnableObjectInvulnerability(obj)

    # --- Label 10 --- #
    DefineLabel(10)
    IfObjectDestroyed(OR_1, character__obj)
    IfCharacterHasSpecialEffect(OR_1, character__obj, 12460)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfObjectDestroyed(obj)
    EnableObjectInvulnerability(obj)
    Wait(seconds)
    DestroyObject(obj, request_slot=0)


@RestartOnRest(90005454)
def Event_90005454(_, character: uint, flag: uint, flag_1: uint):
    """Event 90005454"""
    SkipLinesIfFlagDisabled(1, flag_1)
    ForceAnimation(character, 30001, loop=True, unknown2=1.0)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AddSpecialEffect(character, 5005)
    ReplanAI(character)
    DisableGravity(character)
    WaitFrames(frames=1)
    SkipLinesIfFlagDisabled(2, flag_1)
    ForceAnimation(character, 30001, loop=True, unknown2=1.0)
    SkipLines(1)
    ForceAnimation(character, 0, loop=True, unknown2=1.0)
    IfPlayerInOwnWorld(AND_1)
    IfEntityWithinDistance(AND_1, entity=character, other_entity=PLAYER, radius=200.0)
    IfFlagEnabled(OR_1, flag)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 5006)
    ReplanAI(character)
    EnableGravity(character)
    IfPlayerInOwnWorld(AND_2)
    IfEntityBeyondDistance(AND_2, entity=character, other_entity=PLAYER, radius=220.0)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagDisabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    DisableNetworkFlag(flag)
    Restart()


@RestartOnRest(90005456)
def Event_90005456(_, character: uint, obj: uint, obj_1: uint, flag: uint):
    """Event 90005456"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    IfCharacterHasSpecialEffect(AND_1, character, 12455)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableObjectActivation(obj, obj_act_id=-1)
    EnableObjectActivation(obj_1, obj_act_id=-1)


@RestartOnRest(90005457)
def Event_90005457(_, character: uint, obj: uint, obj_1: uint, obj_2: uint):
    """Event 90005457"""
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=12455)
    DisableObject(obj)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    EndOfAnimation(obj=obj_1, animation_id=1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AttachObjectToCharacter(character=character, model_point=100, obj=obj)
    EndOfAnimation(obj=obj_1, animation_id=1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    IfCharacterHasSpecialEffect(AND_1, character, 12455)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableObject(obj)
    EnableObjectActivation(obj_2, obj_act_id=-1)


@RestartOnRest(90005458)
def Event_90005458(_, character: uint, obj: uint):
    """Event 90005458"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AttachObjectToCharacter(character=character, model_point=166, obj=obj)
    DisableObject(obj)
    IfCharacterHasSpecialEffect(AND_1, character, 12465)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObject(obj)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(90005459)
def Event_90005459(_, copy_draw_parent: uint, flag: uint, character: uint):
    """Event 90005459"""
    DisableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character)
    Move(
        character,
        destination=copy_draw_parent,
        destination_type=CoordEntityType.Character,
        model_point=270,
        copy_draw_parent=copy_draw_parent,
    )


@RestartOnRest(90005460)
def Event_90005460(_, character: uint):
    """Event 90005460"""
    IfCharacterBackreadEnabled(MAIN, character)
    CreateNPCPart(character, npc_part_id=60, part_index=NPCPartType.Part6, part_health=999999999)
    SetNPCPartEffects(
        character,
        npc_part_id=60,
        material_sfx_id=124,
        material_vfx_id=124,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )


@RestartOnRest(90005461)
def Event_90005461(_, character: uint):
    """Event 90005461"""
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 11753)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateNPCPart(character, npc_part_id=10, part_index=NPCPartType.Part1, part_health=11)
    CreateNPCPart(character, npc_part_id=20, part_index=NPCPartType.Part2, part_health=11)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfCharacterPartHealthLessThanOrEqual(AND_3, character, npc_part_id=10, value=10)
    IfCharacterPartHealthLessThanOrEqual(AND_3, character, npc_part_id=20, value=1)
    IfCharacterPartHealthLessThanOrEqual(AND_4, character, npc_part_id=10, value=9)
    IfCharacterPartHealthLessThanOrEqual(AND_4, character, npc_part_id=20, value=2)
    IfCharacterPartHealthLessThanOrEqual(AND_5, character, npc_part_id=10, value=8)
    IfCharacterPartHealthLessThanOrEqual(AND_5, character, npc_part_id=20, value=3)
    IfCharacterPartHealthLessThanOrEqual(AND_6, character, npc_part_id=10, value=7)
    IfCharacterPartHealthLessThanOrEqual(AND_6, character, npc_part_id=20, value=4)
    IfCharacterPartHealthLessThanOrEqual(AND_7, character, npc_part_id=10, value=6)
    IfCharacterPartHealthLessThanOrEqual(AND_7, character, npc_part_id=20, value=5)
    IfCharacterPartHealthLessThanOrEqual(AND_8, character, npc_part_id=10, value=5)
    IfCharacterPartHealthLessThanOrEqual(AND_8, character, npc_part_id=20, value=6)
    IfCharacterPartHealthLessThanOrEqual(AND_9, character, npc_part_id=10, value=4)
    IfCharacterPartHealthLessThanOrEqual(AND_9, character, npc_part_id=20, value=7)
    IfCharacterPartHealthLessThanOrEqual(AND_10, character, npc_part_id=10, value=3)
    IfCharacterPartHealthLessThanOrEqual(AND_10, character, npc_part_id=20, value=8)
    IfCharacterPartHealthLessThanOrEqual(AND_11, character, npc_part_id=10, value=2)
    IfCharacterPartHealthLessThanOrEqual(AND_11, character, npc_part_id=20, value=9)
    IfCharacterPartHealthLessThanOrEqual(AND_12, character, npc_part_id=10, value=1)
    IfCharacterPartHealthLessThanOrEqual(AND_12, character, npc_part_id=20, value=10)
    IfCharacterPartHealthLessThanOrEqual(OR_15, character, npc_part_id=10, value=0)
    IfCharacterPartHealthLessThanOrEqual(OR_15, character, npc_part_id=20, value=0)
    IfConditionTrue(OR_15, input_condition=AND_3)
    IfConditionTrue(OR_15, input_condition=AND_4)
    IfConditionTrue(OR_15, input_condition=AND_5)
    IfConditionTrue(OR_15, input_condition=AND_6)
    IfConditionTrue(OR_15, input_condition=AND_7)
    IfConditionTrue(OR_15, input_condition=AND_8)
    IfConditionTrue(OR_15, input_condition=AND_9)
    IfConditionTrue(OR_15, input_condition=AND_10)
    IfConditionTrue(OR_15, input_condition=AND_11)
    IfConditionTrue(OR_15, input_condition=AND_12)
    IfCharacterHasSpecialEffect(OR_15, character, 11753)
    IfConditionTrue(MAIN, input_condition=OR_15)
    SetNPCPartHealth(character, npc_part_id=10, desired_health=0, overwrite_max=False)
    SetNPCPartHealth(character, npc_part_id=20, desired_health=0, overwrite_max=False)
    SkipLinesIfCharacterHasSpecialEffect(line_count=1, character=character, special_effect=11753)
    ForceAnimation(character, 20001, unknown2=1.0)
    Wait(2.0)
    Restart()


@RestartOnRest(90005462)
def Event_90005462(_, character: uint):
    """Event 90005462"""
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 11752)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=11)
    CreateNPCPart(character, npc_part_id=50, part_index=NPCPartType.Part5, part_health=11)
    IfCharacterPartHealthLessThanOrEqual(AND_3, character, npc_part_id=30, value=10)
    IfCharacterPartHealthLessThanOrEqual(AND_3, character, npc_part_id=50, value=1)
    IfCharacterPartHealthLessThanOrEqual(AND_4, character, npc_part_id=30, value=9)
    IfCharacterPartHealthLessThanOrEqual(AND_4, character, npc_part_id=50, value=2)
    IfCharacterPartHealthLessThanOrEqual(AND_5, character, npc_part_id=30, value=8)
    IfCharacterPartHealthLessThanOrEqual(AND_5, character, npc_part_id=50, value=3)
    IfCharacterPartHealthLessThanOrEqual(AND_6, character, npc_part_id=30, value=7)
    IfCharacterPartHealthLessThanOrEqual(AND_6, character, npc_part_id=50, value=4)
    IfCharacterPartHealthLessThanOrEqual(AND_7, character, npc_part_id=30, value=6)
    IfCharacterPartHealthLessThanOrEqual(AND_7, character, npc_part_id=50, value=5)
    IfCharacterPartHealthLessThanOrEqual(AND_8, character, npc_part_id=30, value=5)
    IfCharacterPartHealthLessThanOrEqual(AND_8, character, npc_part_id=50, value=6)
    IfCharacterPartHealthLessThanOrEqual(AND_9, character, npc_part_id=30, value=4)
    IfCharacterPartHealthLessThanOrEqual(AND_9, character, npc_part_id=50, value=7)
    IfCharacterPartHealthLessThanOrEqual(AND_10, character, npc_part_id=30, value=3)
    IfCharacterPartHealthLessThanOrEqual(AND_10, character, npc_part_id=50, value=8)
    IfCharacterPartHealthLessThanOrEqual(AND_11, character, npc_part_id=30, value=2)
    IfCharacterPartHealthLessThanOrEqual(AND_11, character, npc_part_id=50, value=9)
    IfCharacterPartHealthLessThanOrEqual(AND_12, character, npc_part_id=30, value=1)
    IfCharacterPartHealthLessThanOrEqual(AND_12, character, npc_part_id=50, value=10)
    IfCharacterPartHealthLessThanOrEqual(OR_15, character, npc_part_id=30, value=0)
    IfCharacterPartHealthLessThanOrEqual(OR_15, character, npc_part_id=50, value=0)
    IfConditionTrue(OR_15, input_condition=AND_3)
    IfConditionTrue(OR_15, input_condition=AND_4)
    IfConditionTrue(OR_15, input_condition=AND_5)
    IfConditionTrue(OR_15, input_condition=AND_6)
    IfConditionTrue(OR_15, input_condition=AND_7)
    IfConditionTrue(OR_15, input_condition=AND_8)
    IfConditionTrue(OR_15, input_condition=AND_9)
    IfConditionTrue(OR_15, input_condition=AND_10)
    IfConditionTrue(OR_15, input_condition=AND_11)
    IfConditionTrue(OR_15, input_condition=AND_12)
    IfConditionTrue(MAIN, input_condition=OR_15)
    SetNPCPartHealth(character, npc_part_id=30, desired_health=0, overwrite_max=False)
    SetNPCPartHealth(character, npc_part_id=50, desired_health=0, overwrite_max=False)
    ForceAnimation(character, 20000, unknown2=1.0)
    Wait(2.0)
    Restart()


@RestartOnRest(90005463)
def Event_90005463(_, character: uint, character_1: uint):
    """Event 90005463"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfEventValueGreaterThanOrEqual(OR_10, flag=character, bit_count=3, value=5)
    IfAttackedWithDamageType(AND_1, attacked_entity=character_1, attacker=0)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 11757)
    IfConditionTrue(OR_10, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_10)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character_1, 11757)


@RestartOnRest(90005464)
def Event_90005464(_, flag: uint, character: uint, character_1: uint, value: uint):
    """Event 90005464"""
    IfEventValueGreaterThan(AND_15, flag=flag, bit_count=3, value=value)
    EndIfConditionTrue(input_condition=AND_15)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableAI(character_1)
    IfCharacterHasSpecialEffect(AND_1, character, 11771)
    IfEventValueEqual(AND_1, flag=flag, bit_count=3, value=value)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFrames(frames=1)
    IncrementEventValue(flag, bit_count=3, max_value=5)
    EnableCharacter(character_1)
    ForceAnimation(character_1, 20000, unknown2=1.0)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=70,
        copy_draw_parent=character,
    )
    Wait(3.0)
    EnableAnimations(character_1)
    EnableAI(character_1)


@RestartOnRest(90005470)
def Event_90005470(_, character: uint):
    """Event 90005470"""
    IfCharacterBackreadEnabled(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=12160)
    CreateNPCPart(character, npc_part_id=20, part_index=NPCPartType.Part2, part_health=80, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=20,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=12161)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=80, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=30,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=12162)
    CreateNPCPart(character, npc_part_id=40, part_index=NPCPartType.Part4, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=40,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=12163)
    CreateNPCPart(character, npc_part_id=50, part_index=NPCPartType.Part5, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=50,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=6, character=character, special_effect=12160)
    IfCharacterPartHealthLessThanOrEqual(AND_2, character, npc_part_id=20, value=0)
    IfCharacterHasSpecialEffect(AND_2, character, 12156)
    IfCharacterHasSpecialEffect(AND_2, character, 12168)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 12170)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 12171)
    IfConditionTrue(OR_2, input_condition=AND_2)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=6, character=character, special_effect=12161)
    IfCharacterPartHealthLessThanOrEqual(AND_3, character, npc_part_id=30, value=0)
    IfCharacterHasSpecialEffect(AND_3, character, 12156)
    IfCharacterHasSpecialEffect(AND_3, character, 12169)
    IfCharacterDoesNotHaveSpecialEffect(AND_3, character, 12170)
    IfCharacterDoesNotHaveSpecialEffect(AND_3, character, 12171)
    IfConditionTrue(OR_3, input_condition=AND_3)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character, special_effect=12162)
    IfCharacterPartHealthLessThanOrEqual(AND_4, character, npc_part_id=40, value=0)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 12170)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 12171)
    IfConditionTrue(OR_4, input_condition=AND_4)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character, special_effect=12163)
    IfCharacterPartHealthLessThanOrEqual(AND_5, character, npc_part_id=50, value=0)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 12170)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 12171)
    IfConditionTrue(OR_5, input_condition=AND_5)
    IfConditionTrue(OR_9, input_condition=OR_2)
    IfConditionTrue(OR_9, input_condition=OR_3)
    IfConditionTrue(OR_9, input_condition=OR_4)
    IfConditionTrue(OR_9, input_condition=OR_5)
    IfConditionTrue(MAIN, input_condition=OR_9)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=OR_5)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=OR_4)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=OR_2)
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    ForceAnimation(character, 20011, wait_for_completion=True, unknown2=1.0)
    CreateNPCPart(character, npc_part_id=20, part_index=NPCPartType.Part2, part_health=80, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=20,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)

    # --- Label 3 --- #
    DefineLabel(3)
    ForceAnimation(character, 20008, wait_for_completion=True, unknown2=1.0)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=80, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=20,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=character, special_effect=12156)
    ForceAnimation(character, 20006, wait_for_completion=True, unknown2=1.0)
    SkipLines(1)
    ForceAnimation(character, 20010, wait_for_completion=True, unknown2=1.0)
    CreateNPCPart(character, npc_part_id=40, part_index=NPCPartType.Part4, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=40,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)

    # --- Label 5 --- #
    DefineLabel(5)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=character, special_effect=12156)
    ForceAnimation(character, 20007, wait_for_completion=True, unknown2=1.0)
    SkipLines(1)
    ForceAnimation(character, 2009, wait_for_completion=True, unknown2=1.0)
    CreateNPCPart(character, npc_part_id=50, part_index=NPCPartType.Part5, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=50,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=12160)
    SetNPCPartHealth(character, npc_part_id=20, desired_health=9999999, overwrite_max=False)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=12161)
    SetNPCPartHealth(character, npc_part_id=30, desired_health=9999999, overwrite_max=False)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=12162)
    SetNPCPartHealth(character, npc_part_id=40, desired_health=9999999, overwrite_max=False)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=12163)
    SetNPCPartHealth(character, npc_part_id=50, desired_health=9999999, overwrite_max=False)
    Wait(1.0)
    Restart()


@RestartOnRest(90005471)
def Event_90005471(_, character: uint):
    """Event 90005471"""
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterHasSpecialEffect(AND_1, character, 12160)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 12170)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetNPCPartHealth(character, npc_part_id=20, desired_health=9999999, overwrite_max=False)
    Goto(Label.L0)
    CreateNPCPart(character, npc_part_id=20, part_index=NPCPartType.Part2, part_health=80, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=20,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterPartHealthLessThanOrEqual(AND_2, character, npc_part_id=20, value=0)
    IfCharacterHasSpecialEffect(AND_2, character, 12156)
    IfCharacterHasSpecialEffect(AND_2, character, 12168)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 12171)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfCharacterHasSpecialEffect(OR_2, character, 12170)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SkipLinesIfCharacterHasSpecialEffect(line_count=1, character=character, special_effect=12170)
    ForceAnimation(character, 20011, wait_for_completion=True, unknown2=1.0)
    CreateNPCPart(character, npc_part_id=20, part_index=NPCPartType.Part2, part_health=80, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=20,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(90005472)
def Event_90005472(_, character: uint):
    """Event 90005472"""
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterHasSpecialEffect(AND_1, character, 12161)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 12170)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetNPCPartHealth(character, npc_part_id=30, desired_health=9999999, overwrite_max=False)
    Goto(Label.L0)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=80, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=30,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterPartHealthLessThanOrEqual(AND_2, character, npc_part_id=30, value=0)
    IfCharacterHasSpecialEffect(AND_2, character, 12156)
    IfCharacterHasSpecialEffect(AND_2, character, 12169)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 12171)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfCharacterHasSpecialEffect(OR_2, character, 12170)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SkipLinesIfCharacterHasSpecialEffect(line_count=1, character=character, special_effect=12170)
    ForceAnimation(character, 20008, wait_for_completion=True, unknown2=1.0)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=80, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=30,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(90004473)
def Event_90004473(_, character: uint):
    """Event 90004473"""
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterHasSpecialEffect(AND_1, character, 12162)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 12170)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetNPCPartHealth(character, npc_part_id=40, desired_health=9999999, overwrite_max=False)
    Goto(Label.L0)
    CreateNPCPart(character, npc_part_id=40, part_index=NPCPartType.Part4, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=40,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterPartHealthLessThanOrEqual(AND_2, character, npc_part_id=40, value=0)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 12171)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfCharacterHasSpecialEffect(OR_2, character, 12170)
    IfConditionTrue(MAIN, input_condition=OR_2)
    GotoIfCharacterHasSpecialEffect(Label.L9, character=character, special_effect=12170)
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=12156)
    ForceAnimation(character, 20006, wait_for_completion=True, unknown2=1.0)
    CreateNPCPart(character, npc_part_id=40, part_index=NPCPartType.Part4, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=40,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 20010, wait_for_completion=True, unknown2=1.0)
    CreateNPCPart(character, npc_part_id=40, part_index=NPCPartType.Part4, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=40,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    Wait(1.0)
    Restart()


@RestartOnRest(90005474)
def Event_90005474(_, character: uint):
    """Event 90005474"""
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterHasSpecialEffect(AND_1, character, 12163)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 12170)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetNPCPartHealth(character, npc_part_id=50, desired_health=9999999, overwrite_max=False)
    Goto(Label.L0)
    CreateNPCPart(character, npc_part_id=50, part_index=NPCPartType.Part5, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=50,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterPartHealthLessThanOrEqual(AND_2, character, npc_part_id=50, value=0)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 12171)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfCharacterHasSpecialEffect(OR_2, character, 12170)
    IfConditionTrue(MAIN, input_condition=OR_2)
    GotoIfCharacterHasSpecialEffect(Label.L9, character=character, special_effect=12170)
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=12156)
    ForceAnimation(character, 20007, wait_for_completion=True, unknown2=1.0)
    CreateNPCPart(character, npc_part_id=50, part_index=NPCPartType.Part5, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=50,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 20009, wait_for_completion=True, unknown2=1.0)
    CreateNPCPart(character, npc_part_id=50, part_index=NPCPartType.Part5, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=50,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    Wait(1.0)
    Restart()


@NeverRestart(90005476)
def Event_90005476(_, character: uint, character_1: uint):
    """Event 90005476"""
    IfCharacterAlive(AND_9, character)
    GotoIfConditionTrue(Label.L0, input_condition=AND_9)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterHasSpecialEffect(AND_1, character, 11805)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=230,
        copy_draw_parent=character_1,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(90005480)
def Event_90005480(_, character: uint):
    """Event 90005480"""
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 16472)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 16473)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 16474)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 16475)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    IfCharacterPartHealthComparison(OR_3, character, npc_part_id=30, value=0, comparison_type=ComparisonType.Equal)
    SkipLinesIfConditionFalse(3, OR_3)
    AddSpecialEffect(character, 16498)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=61)
    SetDisplayMask(character, bit_index=10, switch_type=OnOffChange.Off)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    IfCharacterPartHealthComparison(OR_4, character, npc_part_id=40, value=0, comparison_type=ComparisonType.Equal)
    SkipLinesIfConditionFalse(3, OR_4)
    AddSpecialEffect(character, 16498)
    CreateNPCPart(character, npc_part_id=40, part_index=NPCPartType.Part4, part_health=61)
    SetDisplayMask(character, bit_index=11, switch_type=OnOffChange.Off)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    IfCharacterPartHealthComparison(OR_5, character, npc_part_id=50, value=0, comparison_type=ComparisonType.Equal)
    SkipLinesIfConditionFalse(3, OR_5)
    AddSpecialEffect(character, 16498)
    CreateNPCPart(character, npc_part_id=50, part_index=NPCPartType.Part5, part_health=61)
    SetDisplayMask(character, bit_index=12, switch_type=OnOffChange.Off)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    IfCharacterPartHealthComparison(OR_6, character, npc_part_id=60, value=0, comparison_type=ComparisonType.Equal)
    SkipLinesIfConditionFalse(3, OR_6)
    AddSpecialEffect(character, 16498)
    CreateNPCPart(character, npc_part_id=60, part_index=NPCPartType.Part6, part_health=61)
    SetDisplayMask(character, bit_index=13, switch_type=OnOffChange.Off)

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterPartHealthLessThanOrEqual(AND_3, character, npc_part_id=30, value=0)
    IfCharacterPartHealthLessThanOrEqual(AND_4, character, npc_part_id=40, value=0)
    IfCharacterPartHealthLessThanOrEqual(AND_5, character, npc_part_id=50, value=0)
    IfCharacterPartHealthLessThanOrEqual(AND_6, character, npc_part_id=60, value=0)
    IfConditionTrue(OR_1, input_condition=AND_3)
    IfConditionTrue(OR_1, input_condition=AND_4)
    IfConditionTrue(OR_1, input_condition=AND_5)
    IfConditionTrue(OR_1, input_condition=AND_6)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_3)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=AND_4)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=AND_5)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=AND_6)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(character, 16497)
    AddSpecialEffect(character, 16484)
    AddSpecialEffect(character, 16472)
    SetDisplayMask(character, bit_index=10, switch_type=OnOffChange.On)
    WaitFrames(frames=2)
    SkipLinesIfCharacterHasSpecialEffect(line_count=1, character=character, special_effect=16485)
    ForceAnimation(character, 20000, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    AddSpecialEffect(character, 16497)
    AddSpecialEffect(character, 16484)
    AddSpecialEffect(character, 16473)
    SetDisplayMask(character, bit_index=11, switch_type=OnOffChange.On)
    WaitFrames(frames=2)
    SkipLinesIfCharacterHasSpecialEffect(line_count=1, character=character, special_effect=16485)
    ForceAnimation(character, 20001, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L9)

    # --- Label 5 --- #
    DefineLabel(5)
    AddSpecialEffect(character, 16497)
    AddSpecialEffect(character, 16484)
    AddSpecialEffect(character, 16474)
    SetDisplayMask(character, bit_index=12, switch_type=OnOffChange.On)
    WaitFrames(frames=2)
    SkipLinesIfCharacterHasSpecialEffect(line_count=1, character=character, special_effect=16485)
    ForceAnimation(character, 20002, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L9)

    # --- Label 6 --- #
    DefineLabel(6)
    AddSpecialEffect(character, 16497)
    AddSpecialEffect(character, 16484)
    AddSpecialEffect(character, 16475)
    SetDisplayMask(character, bit_index=13, switch_type=OnOffChange.On)
    WaitFrames(frames=2)
    SkipLinesIfCharacterHasSpecialEffect(line_count=1, character=character, special_effect=16485)
    ForceAnimation(character, 20003, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    Wait(1.0)
    Restart()


@RestartOnRest(90005481)
def Event_90005481(_, character: uint):
    """Event 90005481"""
    CreateNPCPart(character, npc_part_id=10, part_index=NPCPartType.Part1, part_health=9999)
    SetNPCPartEffects(
        character,
        npc_part_id=0,
        material_sfx_id=110,
        material_vfx_id=110,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    IfCharacterHasSpecialEffect(AND_1, character, 16499)
    IfUnknownCharacterCondition_30(AND_1, character=character, npc_part_id=10, unk_12_16=0, unk_16_20=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(character, 20007, unknown2=1.0)
    Wait(1.0)
    Restart()


@RestartOnRest(90005485)
def Event_90005485(_, character__unk_0_4: uint):
    """Event 90005485"""
    DisableNetworkSync()
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    SetBackreadStateAlternate(character__unk_0_4, True)
    Unknown_2004_63(unk_0_4=character__unk_0_4, unk_4_8=2000.0)
    Unknown_2004_69(unk_0_4=character__unk_0_4, unk_4_8=0)
    Unknown_2004_70(unk_0_4=character__unk_0_4, unk_4_8=1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableGravity(character__unk_0_4)
    IfEntityWithinDistance(OR_1, entity=character__unk_0_4, other_entity=PLAYER, radius=200.0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableGravity(character__unk_0_4)
    IfEntityWithinDistance(AND_2, entity=character__unk_0_4, other_entity=PLAYER, radius=220.0)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()


@RestartOnRest(90005490)
def Event_90005490(
    _,
    character__unk_0_4: uint,
    character: uint,
    obj: uint,
    obj_1: uint,
    obj_act_id: uint,
    region: uint,
    left: uint,
):
    """Event 90005490"""
    DisableGravity(character__unk_0_4)
    SetNetworkUpdateRate(character__unk_0_4, is_fixed=True, update_rate=CharacterUpdateRate.Unknown105)
    Unknown_2004_69(unk_0_4=character__unk_0_4, unk_4_8=0)
    Unknown_2004_63(unk_0_4=character__unk_0_4, unk_4_8=2000.0)
    Move(
        character__unk_0_4,
        destination=obj,
        destination_type=CoordEntityType.Object,
        model_point=100,
        short_move=True,
    )
    EndOfAnimation(obj=obj, animation_id=0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    SetNetworkUpdateAuthority(character__unk_0_4, authority_level=UpdateAuthority.Unknown8192)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_15, input_condition=AND_15)
    IfCharacterHuman(OR_15, PLAYER)
    IfCharacterHollow(OR_15, PLAYER)
    IfCharacterWhitePhantom(OR_15, PLAYER)
    IfCharacterType(OR_15, PLAYER, character_type=CharacterType.Unknown17)
    IfConditionTrue(AND_1, input_condition=OR_15)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfHasAIStatus(AND_1, character__unk_0_4, ai_status=AIStatusType.Battle)
    IfCharacterDead(AND_10, character)
    IfConditionFalse(AND_1, input_condition=AND_10)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfObjectActivated(OR_1, obj_act_id=obj_act_id)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SetNetworkUpdateRate(character__unk_0_4, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(character__unk_0_4, 16601)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    AICommand(character__unk_0_4, command_id=20, command_slot=0)
    SkipLines(1)
    AICommand(character__unk_0_4, command_id=10, command_slot=0)
    ReplanAI(character__unk_0_4)
    ForceAnimation(obj, 0, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    EnableObjectActivation(obj_1, obj_act_id=-1)
    AICommand(character__unk_0_4, command_id=-1, command_slot=0)
    ReplanAI(character__unk_0_4)
    SetNetworkUpdateRate(character__unk_0_4, is_fixed=True, update_rate=CharacterUpdateRate.Unknown105)
    Restart()


@RestartOnRest(90005491)
def Event_90005491(_, character: uint, obj: uint, region: uint):
    """Event 90005491"""
    IfCharacterAlive(AND_1, character, target_comparison_type=ComparisonType.GreaterThanOrEqual)
    IfEntityWithinDistance(AND_1, entity=character, other_entity=obj, radius=2.0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ActivateObject(obj, obj_act_id=-1, relative_index=-1)
    Wait(0.5)
    Restart()


@NeverRestart(90005500)
def Event_90005500(
    _,
    flag: uint,
    flag_1: uint,
    left: uint,
    obj: uint,
    obj_1: uint,
    obj_act_id: uint,
    obj_2: uint,
    obj_act_id_1: uint,
    region: uint,
    region_1: uint,
    flag_2: uint,
    flag_3: uint,
    left_1: uint,
):
    """Event 90005500"""
    IfFlagEnabled(AND_13, flag)
    IfFlagEnabled(AND_13, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_13)
    IfFlagDisabled(AND_14, flag)
    IfFlagDisabled(AND_14, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_14)
    IfConditionTrue(AND_15, input_condition=OR_15)
    IfFlagEnabled(AND_15, flag_2)
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableObjectActivation(obj_2, obj_act_id=-1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    IfObjectActivated(OR_1, obj_act_id=obj_act_id_1)
    IfFlagDisabled(OR_2, flag)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=region)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfFlagEnabled(AND_3, left_1)
    IfConditionTrue(OR_4, input_condition=OR_1)
    IfConditionTrue(OR_4, input_condition=OR_2)
    IfConditionTrue(OR_4, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_4)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_2)
    DisableNetworkFlag(flag)
    DisableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=flag_3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 1000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 2000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 3000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 4000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 5000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 6000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 7000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 8000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 9000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 10000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 1000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 2000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 3000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 4000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 5000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 6000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 7000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 8000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 9000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 10000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 11 --- #
    DefineLabel(11)
    ForceAnimation(obj_2, 3, skip_transition=True, unknown2=1.0)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_3)

    # --- Label 2 --- #
    DefineLabel(2)
    IfAllPlayersOutsideRegion(OR_10, region=region_1)
    IfFlagEnabled(OR_10, flag)
    IfObjectBackreadEnabled(AND_1, obj=obj)
    IfConditionTrue(AND_1, input_condition=OR_10)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfUnknown_204(Label.L3, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 1000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 2000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 3000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 4000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 5000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 6000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 7000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 8000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 9000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 10000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 1000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 2000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 3000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 4000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 5000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 6000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 7000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 8000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 9000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 10000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 12 --- #
    DefineLabel(12)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    IfObjectActivated(OR_5, obj_act_id=obj_act_id)
    IfFlagEnabled(OR_6, flag)
    IfCharacterInsideRegion(AND_7, character=PLAYER, region=region_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, PLAYER, 4800)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfFlagEnabled(AND_7, left_1)
    IfConditionTrue(OR_8, input_condition=OR_5)
    IfConditionTrue(OR_8, input_condition=OR_6)
    IfConditionTrue(OR_8, input_condition=AND_7)
    IfConditionTrue(MAIN, input_condition=OR_8)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_2)
    EnableNetworkFlag(flag)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=OR_5)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 1000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 2000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 3000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 4000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 5000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 6000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 7000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 8000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 9000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 10000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 1000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 2000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 3000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 4000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 5000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 6000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 7000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 8000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 9000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 10000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 14 --- #
    DefineLabel(14)
    ForceAnimation(obj_1, 3, skip_transition=True, unknown2=1.0)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_3)

    # --- Label 5 --- #
    DefineLabel(5)
    IfAllPlayersOutsideRegion(OR_11, region=region)
    IfFlagDisabled(OR_11, flag)
    IfObjectBackreadEnabled(AND_2, obj=obj)
    IfConditionTrue(AND_2, input_condition=OR_11)
    IfConditionTrue(MAIN, input_condition=AND_2)
    GotoIfUnknown_204(Label.L6, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 1000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 2000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 3000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 4000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 5000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 6000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 7000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 8000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 9000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 10000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)

    # --- Label 6 --- #
    DefineLabel(6)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 1000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 2000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 3000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 4000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 5000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 6000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 7000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 8000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 9000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 10000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 15 --- #
    DefineLabel(15)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    IfFlagDisabled(MAIN, flag_2)
    Restart()


@RestartOnRest(90005501)
def Event_90005501(_, flag: uint, flag_1: uint, left: uint, obj: uint, obj_1: uint, obj_2: uint, flag_2: uint):
    """Event 90005501"""
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableFlag(flag_2)
    IfObjectBackreadEnabled(MAIN, obj=obj)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 20, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(obj, 1000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(obj, 2000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(obj, 3000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(obj, 4000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(obj, 5000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(obj, 6000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(obj, 7000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(obj, 8000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(obj, 9000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(obj, 10000020, unknown2=1.0)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableFlag(flag_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 10, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 1000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 2000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 3000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 4000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 5000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 6000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 7000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 8000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 9000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 10000010, skip_transition=True, unknown2=1.0)

    # --- Label 15 --- #
    DefineLabel(15)
    DisableFlag(flag_1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    End()


@RestartOnRest(90005502)
def Event_90005502(_, flag: uint, obj: uint, region: uint):
    """Event 90005502"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    WaitFrames(frames=2)
    DisableObjectActivation(obj, obj_act_id=-1)
    IfCharacterHuman(OR_15, PLAYER)
    IfCharacterHollow(OR_15, PLAYER)
    IfCharacterInsideRegion(AND_13, character=PLAYER, region=region)
    IfConditionTrue(AND_13, input_condition=OR_15)
    IfConditionTrue(OR_1, input_condition=AND_13)
    IfActionButtonParamActivated(OR_2, action_button_id=8301, entity=obj)
    IfConditionTrue(OR_3, input_condition=OR_1)
    IfConditionTrue(OR_3, input_condition=OR_2)
    IfFlagEnabled(OR_3, flag)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_1)
    EndIfFlagEnabled(flag)
    DisplayDialog(text=4000, anchor_entity=0, number_buttons=NumberButtons.OneButton)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(flag)
    Restart()


@NeverRestart(90005503)
def Event_90005503(
    _,
    flag: uint,
    flag_1: uint,
    left: uint,
    obj: uint,
    obj__region: uint,
    region: uint,
    region_1: uint,
    region_2: uint,
    flag_2: uint,
    flag_3: uint,
    left_1: uint,
):
    """Event 90005503"""
    IfFlagEnabled(AND_13, flag)
    IfFlagEnabled(AND_13, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_13)
    IfFlagDisabled(AND_14, flag)
    IfFlagDisabled(AND_14, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_14)
    IfConditionTrue(AND_15, input_condition=OR_15)
    IfFlagEnabled(AND_15, flag_2)
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    IfFlagDisabled(OR_1, flag)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=obj__region)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 4800)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfFlagEnabled(AND_2, left_1)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=region_2)
    IfCharacterDoesNotHaveSpecialEffect(AND_3, PLAYER, 4800)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfFlagEnabled(AND_3, left_1)
    IfConditionTrue(OR_4, input_condition=OR_1)
    IfConditionTrue(OR_4, input_condition=AND_2)
    IfConditionTrue(OR_4, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_4)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_2)
    DisableNetworkFlag(flag)
    DisableFlag(flag_1)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 1000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 2000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 3000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 4000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    IfAllPlayersOutsideRegion(AND_10, region=region_1)
    IfAllPlayersOutsideRegion(AND_10, region=region)
    IfConditionTrue(OR_10, input_condition=AND_10)
    IfFlagEnabled(OR_10, flag)
    IfObjectBackreadEnabled(AND_1, obj=obj)
    IfConditionTrue(AND_1, input_condition=OR_10)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfUnknown_204(Label.L3, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 1000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 2000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 3000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 4000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 1000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 2000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 3000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 4000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 12 --- #
    DefineLabel(12)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(OR_5, flag)
    IfCharacterInsideRegion(AND_6, character=PLAYER, region=region_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, PLAYER, 4800)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfFlagEnabled(AND_6, left_1)
    IfCharacterInsideRegion(AND_7, character=PLAYER, region=region)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, PLAYER, 4800)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfFlagEnabled(AND_7, left_1)
    IfConditionTrue(OR_8, input_condition=OR_5)
    IfConditionTrue(OR_8, input_condition=AND_6)
    IfConditionTrue(OR_8, input_condition=AND_7)
    IfConditionTrue(MAIN, input_condition=OR_8)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableObjectActivation(obj__region, obj_act_id=-1)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_2)
    EnableNetworkFlag(flag)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=OR_5)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 1000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 2000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 3000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 4000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 1000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 2000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 3000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 4000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 14 --- #
    DefineLabel(14)
    ForceAnimation(obj__region, 3, skip_transition=True, unknown2=1.0)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_3)

    # --- Label 5 --- #
    DefineLabel(5)
    IfAllPlayersOutsideRegion(AND_11, region=region_1)
    IfAllPlayersOutsideRegion(AND_11, region=region)
    IfConditionTrue(OR_11, input_condition=AND_11)
    IfFlagDisabled(OR_11, flag)
    IfObjectBackreadEnabled(AND_2, obj=obj)
    IfConditionTrue(AND_2, input_condition=OR_11)
    IfConditionTrue(MAIN, input_condition=AND_2)
    GotoIfUnknown_204(Label.L6, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 1000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 2000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 3000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 4000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)

    # --- Label 6 --- #
    DefineLabel(6)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 1000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 2000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 3000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 4000120, skip_transition=True, unknown2=1.0)

    # --- Label 15 --- #
    DefineLabel(15)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    IfFlagDisabled(MAIN, flag_2)
    Restart()


@NeverRestart(90005504)
def Event_90005504(_, flag: uint, flag_1: uint, left: uint, entity: uint, flag_2: uint):
    """Event 90005504"""
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableFlag(flag_2)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(entity, 20, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(entity, 1000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(entity, 2000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(entity, 3000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(entity, 4000020, unknown2=1.0)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableFlag(flag_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(entity, 10, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(entity, 1000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(entity, 2000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(entity, 3000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(entity, 4000010, skip_transition=True, unknown2=1.0)

    # --- Label 15 --- #
    DefineLabel(15)
    DisableFlag(flag_1)
    End()


@NeverRestart(90005505)
def Event_90005505(
    _,
    flag: uint,
    flag_1: uint,
    left: uint,
    obj: uint,
    obj_1: uint,
    obj_act_id: uint,
    obj_2: uint,
    obj_act_id_1: uint,
    flag_2: uint,
    flag_3: uint,
    left_1: uint,
):
    """Event 90005505"""
    IfFlagEnabled(AND_13, flag)
    IfFlagEnabled(AND_13, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_13)
    IfFlagDisabled(AND_14, flag)
    IfFlagDisabled(AND_14, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_14)
    IfConditionTrue(AND_15, input_condition=OR_15)
    IfFlagEnabled(AND_15, flag_2)
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    SkipLinesIfPlayerNotInOwnWorld(2)
    EnableObjectActivation(obj_2, obj_act_id=-1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    IfObjectActivated(OR_1, obj_act_id=obj_act_id_1)
    IfFlagDisabled(OR_2, flag)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfFlagEnabled(AND_3, left_1)
    IfActionButtonParamActivated(AND_3, action_button_id=8320, entity=obj)
    IfConditionTrue(OR_4, input_condition=OR_1)
    IfConditionTrue(OR_4, input_condition=OR_2)
    IfConditionTrue(OR_4, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_4)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    SkipLinesIfPlayerNotInOwnWorld(2)
    EnableNetworkFlag(flag_2)
    DisableNetworkFlag(flag)
    DisableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_3)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L2, flag=flag_3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L3)
    ForceAnimation(obj, 1000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L3)
    ForceAnimation(obj, 2000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(PLAYER, destination=obj, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 60200, unknown2=1.0)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L3)
    ForceAnimation(obj, 1000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L3)
    ForceAnimation(obj, 2000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 1000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 2000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 11 --- #
    DefineLabel(11)
    ForceAnimation(obj_2, 3, skip_transition=True, unknown2=1.0)
    DisableNetworkFlag(flag_3)

    # --- Label 3 --- #
    DefineLabel(3)
    IfObjectBackreadEnabled(AND_1, obj=obj)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfPlayerNotInOwnWorld(Label.L4)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 1000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 2000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 1000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 2000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 12 --- #
    DefineLabel(12)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerNotInOwnWorld(2)
    EnableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    IfObjectActivated(OR_5, obj_act_id=obj_act_id)
    IfFlagEnabled(OR_6, flag)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfFlagEnabled(AND_7, left_1)
    IfActionButtonParamActivated(AND_7, action_button_id=8320, entity=obj)
    IfConditionTrue(OR_8, input_condition=OR_5)
    IfConditionTrue(OR_8, input_condition=OR_6)
    IfConditionTrue(OR_8, input_condition=AND_7)
    IfConditionTrue(MAIN, input_condition=OR_8)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    SkipLinesIfPlayerNotInOwnWorld(2)
    EnableNetworkFlag(flag_2)
    EnableNetworkFlag(flag)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=AND_7)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=OR_5)
    GotoIfFlagEnabled(Label.L6, flag=flag_3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L7)
    ForceAnimation(obj, 1000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L7)
    ForceAnimation(obj, 2000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L7)

    # --- Label 5 --- #
    DefineLabel(5)
    Move(PLAYER, destination=obj, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 60200, unknown2=1.0)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L7)
    ForceAnimation(obj, 1000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L7)
    ForceAnimation(obj, 2000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L7)

    # --- Label 6 --- #
    DefineLabel(6)
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 1000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 2000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 14 --- #
    DefineLabel(14)
    ForceAnimation(obj_1, 3, skip_transition=True, unknown2=1.0)
    DisableNetworkFlag(flag_3)

    # --- Label 7 --- #
    DefineLabel(7)
    IfObjectBackreadEnabled(AND_2, obj=obj)
    IfConditionTrue(MAIN, input_condition=AND_2)
    GotoIfPlayerNotInOwnWorld(Label.L8)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 1000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 2000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)

    # --- Label 8 --- #
    DefineLabel(8)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 1000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 2000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 15 --- #
    DefineLabel(15)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    IfFlagDisabled(MAIN, flag_2)
    Restart()


@NeverRestart(90005507)
def Event_90005507(
    _,
    flag: uint,
    flag_1: uint,
    left: uint,
    obj: uint,
    entity: uint,
    region: uint,
    entity_1: uint,
    region_1: uint,
    region_2: uint,
    region_3: uint,
    flag_2: uint,
    flag_3: uint,
    left_1: uint,
):
    """Event 90005507"""
    IfFlagEnabled(AND_13, flag)
    IfFlagEnabled(AND_13, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_13)
    IfFlagDisabled(AND_14, flag)
    IfFlagDisabled(AND_14, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_14)
    IfConditionTrue(AND_15, input_condition=OR_15)
    IfFlagEnabled(AND_15, flag_2)
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=region_1)
    IfFlagDisabled(OR_2, flag)
    IfCharacterInsideRegion(AND_3, character=PLAYER, region=region_2)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfFlagEnabled(AND_3, left_1)
    IfConditionTrue(OR_4, input_condition=OR_1)
    IfConditionTrue(OR_4, input_condition=OR_2)
    IfConditionTrue(OR_4, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_4)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_2)
    DisableNetworkFlag(flag)
    DisableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=flag_3)
    ForceAnimation(entity_1, 1, skip_transition=True, unknown2=1.0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 1000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 2000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 3000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 4000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 5000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 6000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 7000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 8000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 9000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)
    ForceAnimation(obj, 10000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_3)
    ForceAnimation(entity_1, 1, skip_transition=True, unknown2=1.0)
    Wait(0.5)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 21, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 1000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 2000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 3000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 4000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 5000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 6000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 7000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 8000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 9000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L11)
    ForceAnimation(obj, 10000021, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 11 --- #
    DefineLabel(11)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_3)

    # --- Label 2 --- #
    DefineLabel(2)
    IfAllPlayersOutsideRegion(OR_10, region=region_3)
    IfFlagEnabled(OR_10, flag)
    IfObjectBackreadEnabled(AND_1, obj=obj)
    IfConditionTrue(AND_1, input_condition=OR_10)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(entity, 3, skip_transition=True, unknown2=1.0)
    GotoIfUnknown_204(Label.L3, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 1000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 2000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 3000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 4000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 5000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 6000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 7000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 8000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 9000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 10000110, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 1000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 2000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 3000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 4000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 5000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 6000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 7000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 8000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 9000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L12)
    ForceAnimation(obj, 10000110, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 12 --- #
    DefineLabel(12)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(OR_5, character=PLAYER, region=region)
    IfFlagEnabled(OR_6, flag)
    IfCharacterInsideRegion(AND_7, character=PLAYER, region=region_3)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, PLAYER, 4800)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfFlagEnabled(AND_7, left_1)
    IfConditionTrue(OR_8, input_condition=OR_5)
    IfConditionTrue(OR_8, input_condition=OR_6)
    IfConditionTrue(OR_8, input_condition=AND_7)
    IfConditionTrue(MAIN, input_condition=OR_8)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_2)
    EnableNetworkFlag(flag)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=OR_5)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)
    ForceAnimation(entity, 1, skip_transition=True, unknown2=1.0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 1000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 2000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 3000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 4000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 5000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 6000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 7000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 8000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 9000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)
    ForceAnimation(obj, 10000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_3)
    ForceAnimation(entity, 1, skip_transition=True, unknown2=1.0)
    Wait(0.5)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 12, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 1000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 2000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 3000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 4000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 5000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 6000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 7000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 8000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 9000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L14)
    ForceAnimation(obj, 10000012, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 14 --- #
    DefineLabel(14)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_3)

    # --- Label 5 --- #
    DefineLabel(5)
    IfAllPlayersOutsideRegion(OR_11, region=region_2)
    IfFlagDisabled(OR_11, flag)
    IfObjectBackreadEnabled(AND_2, obj=obj)
    IfConditionTrue(AND_2, input_condition=OR_11)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ForceAnimation(entity_1, 3, skip_transition=True, unknown2=1.0)
    GotoIfUnknown_204(Label.L6, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 1000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 2000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 3000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 4000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 5000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 6000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 7000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 8000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 9000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 10000120, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)

    # --- Label 6 --- #
    DefineLabel(6)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(obj, 120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 1000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 2000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 3000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 4000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 5000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 6000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 7000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 8000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 9000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(obj, 10000120, wait_for_completion=True, skip_transition=True, unknown2=1.0)

    # --- Label 15 --- #
    DefineLabel(15)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    IfFlagDisabled(MAIN, flag_2)
    Restart()


@RestartOnRest(90005508)
def Event_90005508(_, flag: uint, flag_1: uint, left: uint, entity: uint, obj: uint, obj_1: uint, flag_2: uint):
    """Event 90005508"""
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableFlag(flag_2)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(entity, 20, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(entity, 1000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(entity, 2000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(entity, 3000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(entity, 4000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(entity, 5000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(entity, 6000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(entity, 7000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(entity, 8000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(entity, 9000020, unknown2=1.0)
    Goto(Label.L10)
    ForceAnimation(entity, 10000020, unknown2=1.0)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableFlag(flag_1)
    EndOfAnimation(obj=obj, animation_id=1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(entity, 10, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(entity, 1000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(entity, 2000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(entity, 3000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(entity, 4000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(entity, 5000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(entity, 6000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(entity, 7000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(entity, 8000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(entity, 9000010, skip_transition=True, unknown2=1.0)
    Goto(Label.L15)
    ForceAnimation(entity, 10000010, skip_transition=True, unknown2=1.0)

    # --- Label 15 --- #
    DefineLabel(15)
    DisableFlag(flag_1)
    EndOfAnimation(obj=obj_1, animation_id=1)
    End()


@NeverRestart(90005510)
def Event_90005510(_, flag: uint, obj: uint, obj_act_id: uint, obj_act_id_1: int, text: int, left: uint):
    """Event 90005510"""
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfPlayerInOwnWorld(AND_1)
    IfObjectActivated(AND_1, obj_act_id=obj_act_id)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFramesAfterCutscene(frames=1)
    DisplayDialog(text=text, anchor_entity=obj)
    EnableFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(1, left=left, right=1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    End()


@NeverRestart(90005511)
def Event_90005511(_, flag: uint, obj: uint, obj_act_id: uint, obj_act_id_1: int, left: uint):
    """Event 90005511"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfObjectActivated(MAIN, obj_act_id=obj_act_id)
    EnableFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    EndIfUnsignedEqual(left=left, right=1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1, relative_index=3)
    End()


@NeverRestart(90005512)
def Event_90005512(_, flag: uint, region: uint, region_1: uint):
    """Event 90005512"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(OR_1, flag)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    RestartIfFlagEnabled(flag)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@RestartOnRest(90005513)
def Event_90005513(
    _,
    flag: uint,
    obj: uint,
    obj_1: uint,
    obj_act_id: uint,
    obj_act_id_1: int,
    animation_id: int,
    animation_id_1: int,
):
    """Event 90005513"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableObjectActivation(obj_1, obj_act_id=obj_act_id_1)
    EndOfAnimation(obj=obj, animation_id=animation_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagDisabled(AND_1, flag)
    IfObjectActivated(AND_1, obj_act_id=obj_act_id)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)
    DisableObjectActivation(obj_1, obj_act_id=obj_act_id_1)
    ForceAnimation(obj, animation_id, unknown2=1.0)


@NeverRestart(90005515)
def Event_90005515(_, flag: uint, anchor_entity: uint):
    """Event 90005515"""
    DisableNetworkSync()
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=7101, entity=anchor_entity)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfFlagEnabled(OR_1, flag)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(flag)
    DisplayDialog(text=4010, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(90005520)
def Event_90005520(_, flag: uint, obj: uint, start_climbing_flag: uint, stop_climbing_flag: uint):
    """Event 90005520"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(obj=obj, animation_id=2)
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, obj=obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9200, entity=obj)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)
    SkipLinesIfPlayerNotInOwnWorld(1)
    RotateToFaceEntity(PLAYER, obj, animation=60210)
    ForceAnimation(obj, 1, wait_for_completion=True, unknown2=1.0)
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, obj=obj)


@RestartOnRest(90005525)
def Event_90005525(_, flag: uint, obj: uint):
    """Event 90005525"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfPlayerInOwnWorld(AND_1)
    IfAttackedWithDamageType(AND_1, attacked_entity=obj, attacker=20000)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)
    ForceAnimation(obj, 1, wait_for_completion=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(obj)


@RestartOnRest(900055278)
def Event_900055278(
    _,
    flag: uint,
    obj: uint,
    model_point: int,
    action_button_id: int,
    text: int,
    left: int,
    left_1: int,
    left_2: int,
):
    """Event 900055278"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=101, model_point=model_point)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=action_button_id, entity=obj)
    IfFlagEnabled(AND_2, flag)
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_2)
    DisplayDialog(text=text, anchor_entity=flag, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableNetworkFlag(flag)
    DeleteObjectVFX(obj)
    DisableObject(obj)
    End()
    EndIfValueEqual(left=left, right=0)
    EndIfValueEqual(left=left_1, right=0)
    EndIfValueEqual(left=left_2, right=0)


@RestartOnRest(90005540)
def Event_90005540(
    _,
    flag: uint,
    obj: uint,
    obj_1: uint,
    obj_act_id: uint,
    obj_act_id_1: int,
    animation_id: int,
    animation_id_1: int,
):
    """Event 90005540"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableObjectActivation(obj_1, obj_act_id=obj_act_id_1)
    EndOfAnimation(obj=obj, animation_id=animation_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagDisabled(AND_1, flag)
    IfObjectActivated(AND_1, obj_act_id=obj_act_id)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)
    DisableObjectActivation(obj_1, obj_act_id=obj_act_id_1)
    ForceAnimation(obj, animation_id, unknown2=1.0)


@RestartOnRest(90005550)
def Event_90005550(_, flag: uint, obj: uint, obj_act_id: uint):
    """Event 90005550"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(obj=obj, animation_id=1)
    DisableObjectActivation(obj, obj_act_id=-1)
    EnableTreasure(obj=obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableTreasure(obj=obj)
    IfObjectActivated(MAIN, obj_act_id=obj_act_id)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)
    EnableFlag(flag)


@RestartOnRest(90005560)
def Event_90005560(_, flag: uint, obj: uint, left: int):
    """Event 90005560"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    PostDestruction(obj)
    EnableTreasure(obj=obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfValueNotEqual(2, left=left, right=0)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=200, model_point=803300)
    DisableTreasure(obj=obj)
    IfObjectDestroyed(AND_1, obj)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)
    EnableTreasure(obj=obj)
    SkipLinesIfValueNotEqual(1, left=left, right=0)
    DeleteObjectVFX(obj)


@NeverRestart(90005570)
def Event_90005570(_, flag: uint, unk_0_4: int, obj: uint, left: int, left_1: int, right: int):
    """Event 90005570"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    SkipLinesIfValueNotEqual(2, left=left_1, right=3)
    CreateObjectVFX(obj, vfx_id=90, model_point=6103)
    Goto(Label.L1)
    SkipLinesIfValueNotEqual(2, left=left_1, right=2)
    CreateObjectVFX(obj, vfx_id=90, model_point=6102)
    Goto(Label.L1)
    SkipLinesIfValueNotEqual(2, left=left_1, right=1)
    CreateObjectVFX(obj, vfx_id=90, model_point=6101)
    Goto(Label.L1)
    CreateObjectVFX(obj, vfx_id=90, model_point=6100)

    # --- Label 1 --- #
    DefineLabel(1)
    IfPlayerInOwnWorld(AND_2)
    IfFlagDisabled(AND_2, flag)
    SkipLinesIfValueNotEqual(2, left=left, right=2)
    IfActionButtonParamActivated(AND_2, action_button_id=4250, entity=obj)
    Goto(Label.L2)
    SkipLinesIfValueNotEqual(2, left=left, right=1)
    IfActionButtonParamActivated(AND_2, action_button_id=4300, entity=obj)
    Goto(Label.L2)
    IfActionButtonParamActivated(AND_2, action_button_id=4200, entity=obj)

    # --- Label 2 --- #
    DefineLabel(2)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    DeleteObjectVFX(obj)
    EndIfFlagEnabled(flag)
    WaitFramesAfterCutscene(frames=1)
    Unknown_2003_71(unk_0_4=unk_0_4)
    EnableFlag(flag)
    EndIfValueEqual(left=0, right=right)


@NeverRestart(900005571)
def Event_900005571(_, flag: uint, unk_0_4: int, flag_1: uint, right: int):
    """Event 900005571"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Unknown_2003_71(unk_0_4=unk_0_4)
    EnableFlag(flag)
    EndIfValueEqual(left=0, right=right)


@RestartOnRest(90005600)
def Event_90005600(_, grace_flag: uint, obj: uint, unknown: float, character: uint):
    """Event 90005600"""
    RegisterGrace(grace_flag=grace_flag, obj=obj, unknown=unknown)
    SkipLinesIfUnsignedEqual(1, left=0, right=character)
    DisableAnimations(character)
    GotoIfFlagEnabled(Label.L0, flag=grace_flag)
    IfPlayerInOwnWorld(AND_1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=obj, radius=5.0)
    IfFlagEnabled(AND_1, grace_flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfUnsignedEqual(left=0, right=character)
    DisableAnimations(character)
    AddSpecialEffect(character, 530)
    Wait(1.5)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)


@RestartOnRest(90005605)
def Event_90005605(
    _,
    obj: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    unknown1: int,
    flag: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
    left: uint,
    text: int,
    seconds: float,
    seconds_1: float,
):
    """Event 90005605"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    SkipLinesIfThisEventSlotFlagEnabled(3)
    DeleteObjectVFX(obj)
    DisableFlag(flag)
    WaitFrames(frames=1)
    IfTryingToCreateSession(OR_10)
    IfTryingToJoinSession(OR_10)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfFlagDisabled(OR_10, left)
    GotoIfConditionTrue(Label.L1, input_condition=OR_10)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    CreateObjectVFX(obj, vfx_id=200, model_point=806870)
    EnableFlag(flag)

    # --- Label 1 --- #
    DefineLabel(1)
    IfPlayerInOwnWorld(AND_1)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    SkipLinesIfUnsignedEqual(3, left=left, right=0)
    SkipLinesIfValueNotEqual(2, left=text, right=0)
    IfFlagEnabled(AND_1, left)
    IfFlagEnabled(AND_1, flag)
    IfActionButtonParamActivated(AND_1, action_button_id=9140, entity=obj)
    IfTryingToCreateSession(OR_4)
    IfTryingToJoinSession(OR_4)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfFlagDisabled(OR_4, left)
    IfConditionTrue(AND_4, input_condition=OR_4)
    IfFlagEnabled(AND_4, flag)
    IfTryingToCreateSession(OR_7)
    IfTryingToJoinSession(OR_7)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfFlagDisabled(OR_7, left)
    IfConditionFalse(AND_7, input_condition=OR_7)
    IfFlagDisabled(AND_7, flag)
    IfFlagState(AND_9, FlagSetting.Change, FlagType.Absolute, left)
    IfConditionTrue(OR_14, input_condition=AND_1)
    IfConditionTrue(OR_14, input_condition=AND_4)
    IfConditionTrue(OR_14, input_condition=AND_7)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfConditionTrue(OR_14, input_condition=AND_9)
    IfConditionTrue(MAIN, input_condition=OR_14)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_1)
    GotoIfFinishedConditionFalse(Label.L2, input_condition=AND_4)
    DeleteObjectVFX(obj)
    DisableFlag(flag)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(0.032999999821186066)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    IfUnsignedEqual(OR_13, left=left, right=0)
    IfValueEqual(OR_13, left=text, right=0)
    GotoIfConditionTrue(Label.L4, input_condition=OR_13)
    GotoIfFlagEnabled(Label.L4, flag=left)
    DisplayDialog(text=text, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    DisplayDialogAndSetFlags(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=obj,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L6, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    IfTryingToCreateSession(OR_15)
    IfTryingToJoinSession(OR_15)
    RestartIfConditionTrue(input_condition=OR_15)
    RotateToFaceEntity(PLAYER, obj, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490, unknown2=1.0)
    Wait(3.0)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start, unknown1=unknown1)
    Restart()
    Wait(seconds)
    Wait(seconds_1)


@NeverRestart(900005610)
def Event_900005610(_, obj: uint, vfx_id: int, model_point: int, right: uint):
    """Event 900005610"""
    DisableNetworkSync()
    DeleteObjectVFX(obj)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_1, right)
    IfCharacterMounted(AND_1, character=PLAYER)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=model_point)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagDisabled(OR_2, right)
    IfCharacterNotMounted(OR_2, character=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()


@NeverRestart(90005616)
def Event_90005616(_, flag: uint, region: uint):
    """Event 90005616"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfPlayerInOwnWorld(AND_1)
    IfFlagDisabled(AND_1, flag)
    IfFlagEnabled(AND_1, 400239)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayBattlefieldMessage(20600)


@NeverRestart(90005620)
def Event_90005620(
    _,
    flag: uint,
    obj: uint,
    obj_1: uint,
    obj_2: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
    right: int,
):
    """Event 90005620"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=200, model_point=806040)
    SkipLinesIfUnsignedEqual(1, left=obj_2, right=0)
    CreateObjectVFX(obj, vfx_id=201, model_point=806040)
    DisableObject(obj_1)
    SkipLinesIfUnsignedEqual(1, left=obj_2, right=0)
    DisableObject(obj_2)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9220, entity=obj)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfFlagEnabled(OR_1, flag)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L9, flag=flag)
    DisplayDialogAndSetFlags(
        message=108000,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=obj,
        display_distance=1.75,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    Wait(0.5)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    StoreItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=8000, flag=9580, bit_count=8)
    GotoIfUnsignedNotEqual(Label.L2, left=obj_2, right=0)
    IfEventValueGreaterThanOrEqual(AND_2, flag=9580, bit_count=8, value=1)
    GotoIfConditionTrue(Label.L3, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    IfEventValueGreaterThanOrEqual(AND_3, flag=9580, bit_count=8, value=2)
    GotoIfConditionTrue(Label.L4, input_condition=AND_3)
    ForceAnimation(PLAYER, 50050, unknown2=1.0)
    Wait(1.399999976158142)
    IfEventValueGreaterThanOrEqual(AND_4, flag=9580, bit_count=8, value=1)
    GotoIfConditionTrue(Label.L5, input_condition=AND_4)
    DisplayDialog(text=308000, anchor_entity=obj)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    DisplayDialog(text=408000, anchor_entity=obj)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    Move(PLAYER, destination=obj, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 60810, unknown2=1.0)
    Wait(2.700000047683716)
    DisplayDialog(text=208000, anchor_entity=obj)
    EnableObject(obj_1)
    RemoveGoodFromPlayer(item=8000, quantity=1)
    EnableNetworkFlag(flag)
    Goto(Label.L8)

    # --- Label 4 --- #
    DefineLabel(4)
    Move(PLAYER, destination=obj, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 60810, unknown2=1.0)
    Wait(2.6700000762939453)
    EnableObject(obj_1)
    ForceAnimation(PLAYER, 60811, unknown2=1.0)
    Wait(1.5)
    DisplayDialog(text=208000, anchor_entity=obj)
    EnableObject(obj_2)
    RemoveGoodFromPlayer(item=8000, quantity=2)
    EnableNetworkFlag(flag)
    Goto(Label.L8)

    # --- Label 9 --- #
    DefineLabel(9)
    EnableObject(obj_1)
    EnableObject(obj_2)

    # --- Label 8 --- #
    DefineLabel(8)
    DeleteObjectVFX(obj)
    End()
    EndIfValueEqual(left=0, right=right)


@NeverRestart(90005621)
def Event_90005621(_, flag: uint, obj: uint):
    """Event 90005621"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=101, model_point=806042)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DeleteObjectVFX(obj)
    PlaySoundEffect(obj, 90011, sound_type=SoundType.s_SFX)
    Wait(0.5)
    DisableObject(obj)


@RestartOnRest(90005630)
def Event_90005630(_, unknown1: uint, unknown2: uint, unknown3: int):
    """Event 90005630"""
    DisableNetworkSync()
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9270, entity=unknown2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Unknown_2003_75(unknown1=unknown1, unknown2=unknown2, unknown3=unknown3)
    RotateToFaceEntity(PLAYER, unknown2, wait_for_completion=True)
    RotateToFaceEntity(PLAYER, unknown2, animation=60480)
    Wait(1.0)
    Restart()


@RestartOnRest(90005631)
def Event_90005631(_, anchor_entity: uint, text: int):
    """Event 90005631"""
    DisableNetworkSync()
    IfActionButtonParamActivated(AND_1, action_button_id=9330, entity=anchor_entity)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialog(text=text, anchor_entity=anchor_entity, button_type=ButtonType.Yes_or_No)
    Wait(2.0)
    Restart()


@RestartOnRest(90005632)
def Event_90005632(_, flag: uint, obj: uint, item_lot_param_id: int):
    """Event 90005632"""
    EndIfFlagEnabled(flag)
    EndIfPlayerNotInOwnWorld()
    DeleteObjectVFX(obj, erase_root=False)
    CreateObjectVFX(obj, vfx_id=200, model_point=806840)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9310, entity=obj)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DeleteObjectVFX(obj)
    PlaySoundEffect(obj, 806841, sound_type=SoundType.s_SFX)
    Wait(0.10000000149011612)
    AwardItemLot(item_lot_param_id, host_only=True)


@RestartOnRest(90005633)
def Event_90005633(
    _,
    character: uint,
    flag: uint,
    character_1: uint,
    animation_id: int,
    animation_id_1: int,
    obj: uint,
    obj_1: uint,
):
    """Event 90005633"""
    AddSpecialEffect(character, 10124)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableObject(obj)
    DisableObject(obj_1)
    DisableTreasure(obj=obj_1)
    EndIfFlagEnabled(character)
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfEntityWithinDistance(AND_1, entity=character_1, other_entity=PLAYER, radius=15.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character_1)
    CancelSpecialEffect(character, 10124)
    ForceAnimation(character_1, animation_id, unknown2=1.0)
    EnableObject(obj)
    EnableObject(obj_1)
    ForceAnimation(obj, 2, unknown2=1.0)
    IfPlayerInOwnWorld(AND_2)
    IfFlagEnabled(AND_2, flag)
    IfEntityWithinDistance(AND_2, entity=character_1, other_entity=PLAYER, radius=5.0)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ForceAnimation(character_1, animation_id_1, unknown2=1.0)
    ForceAnimation(obj, 1, unknown2=1.0)
    Wait(3.799999952316284)
    DisableCharacter(character_1)
    DisableObject(obj)
    EnableTreasure(obj=obj_1)


@RestartOnRest(90005636)
def Event_90005636(
    _,
    flag: uint,
    character: uint,
    entity: uint,
    special_effect_id: int,
    destination: uint,
    region: uint,
    flag_1: uint,
    patrol_information_id: uint,
    right: int,
):
    """Event 90005636"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)

    # --- Label 1 --- #
    DefineLabel(1)
    IfPlayerInOwnWorld(AND_2)
    IfFlagEnabled(AND_2, flag)
    IfConditionTrue(OR_5, input_condition=AND_2)
    IfFlagEnabled(AND_3, flag_1)
    IfCharacterInsideRegion(AND_3, character=character, region=region)
    IfConditionTrue(OR_5, input_condition=AND_3)
    IfPlayerInOwnWorld(AND_4)
    IfFlagDisabled(AND_4, flag)
    SkipLinesIfFlagDisabled(1, flag_1)
    IfEntityBeyondDistance(AND_4, entity=PLAYER, other_entity=character, radius=30.0)
    IfActionButtonParamActivated(AND_4, action_button_id=9300, entity=entity)
    IfConditionTrue(OR_5, input_condition=AND_4)
    IfConditionTrue(MAIN, input_condition=OR_5)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    CreateTemporaryVFX(vfx_id=643041, anchor_entity=character, model_point=905, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=643040, anchor_entity=character, model_point=960, anchor_type=CoordEntityType.Character)
    Wait(0.20000000298023224)
    DisableCharacter(character)
    DisableAI(character)
    GotoIfFinishedConditionFalse(Label.L2, input_condition=AND_3)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=PLAYER)
    Wait(0.10000000149011612)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFinishedConditionFalse(Label.L3, input_condition=AND_4)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(1, flag_1)
    EnableNetworkFlag(flag_1)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=PLAYER)
    SkipLinesIfUnsignedEqual(1, left=0, right=patrol_information_id)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    WaitFrames(frames=1)
    EnableCharacter(character)
    DisableAnimations(character)
    ForceAnimation(character, 20028, unknown2=1.0)
    Wait(0.5)
    EnableAI(character)
    AddSpecialEffect(character, special_effect_id)

    # --- Label 3 --- #
    DefineLabel(3)
    Restart()
    EndIfValueEqual(left=0, right=right)


@RestartOnRest(90005637)
def Event_90005637(_, flag: uint, character: uint, region: uint):
    """Event 90005637"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(OR_1, flag)
    IfCharacterInsideRegion(OR_1, character=character, region=region)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(flag)
    AddSpecialEffect(character, 4463)
    Wait(3.0)
    Restart()


@RestartOnRest(90005640)
def Event_90005640(_, flag: uint, obj: uint):
    """Event 90005640"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    IfObjectBackreadEnabled(MAIN, obj=obj)
    EndOfAnimation(obj=obj, animation_id=2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfObjectBackreadEnabled(AND_1, obj=obj)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=obj, radius=50.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    ForceAnimation(obj, 1, unknown2=1.0)


@RestartOnRest(90005645)
def Event_90005645(
    _,
    flag: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
    obj: uint,
    player_start: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
):
    """Event 90005645"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableObject(obj)
    IfPlayerInOwnWorld(AND_1)
    IfEntityBeyondDistance(AND_1, entity=PLAYER, other_entity=obj, radius=1.0)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObject(obj)
    IfTryingToJoinSession(OR_2)
    IfTryingToCreateSession(OR_2)
    IfConditionFalse(AND_2, input_condition=OR_2)
    IfActionButtonParamActivated(AND_2, action_button_id=9290, entity=obj)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisplayDialogAndSetFlags(
        message=4100,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=obj,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    EnableFlag(cancel_flag__right_flag)
    Wait(2.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@NeverRestart(90005646)
def Event_90005646(
    _,
    flag: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
    obj: uint,
    player_start: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
):
    """Event 90005646"""
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfThisEventSlotFlagEnabled(1)
    CreateObjectVFX(obj, vfx_id=190, model_point=1300)
    IfTryingToJoinSession(OR_2)
    IfTryingToCreateSession(OR_2)
    IfConditionFalse(AND_2, input_condition=OR_2)
    IfActionButtonParamActivated(AND_2, action_button_id=9290, entity=obj)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisplayDialogAndSetFlags(
        message=4100,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=obj,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    EnableFlag(cancel_flag__right_flag)
    Wait(2.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(PLAYER, 60460, unknown2=1.0)
    Wait(2.5)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@NeverRestart(90005650)
def Event_90005650(_, flag: uint, obj: uint, obj_1: uint, obj_act_id: uint, obj_act_id_1: int):
    """Event 90005650"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(obj=obj, animation_id=2)
    DisableObjectActivation(obj_1, obj_act_id=obj_act_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfObjectActivated(AND_1, obj_act_id=obj_act_id)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)
    SkipLinesIfPlayerNotInOwnWorld(2)
    DisplayDialog(text=4200, anchor_entity=obj_1, display_distance=5.0)
    SkipLines(1)
    DisplayBattlefieldMessage(4200)
    ForceAnimation(obj, 1, unknown2=1.0)
    End()


@NeverRestart(90005652)
def Event_90005652(_, flag: uint, obj: uint, flag_1: uint):
    """Event 90005652"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(obj=obj, animation_id=2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)
    DisplayDialog(text=4200, anchor_entity=0, display_distance=5.0)
    ForceAnimation(obj, 1, unknown2=1.0)
    End()


@NeverRestart(90005651)
def Event_90005651(_, flag: uint, anchor_entity: uint):
    """Event 90005651"""
    DisableNetworkSync()
    IfActionButtonParamActivated(OR_1, action_button_id=7200, entity=anchor_entity)
    IfFlagEnabled(OR_1, flag)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(flag)
    DisplayDialog(text=4001, anchor_entity=anchor_entity)
    WaitFrames(frames=1)
    Restart()


@NeverRestart(90005660)
def Event_90005660(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
):
    """Event 90005660"""
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Wait(0.5)
    SkipLinesIfValueEqual(4, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(4, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(4, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=102000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(3.0)
    IfAllPlayersOutsideRegion(MAIN, region=region)
    ForceAnimation(entity, 3, wait_for_completion=True, unknown2=1.0)
    Restart()


@NeverRestart(90005670)
def Event_90005670(_, flag: uint, flag_1: uint, flag_2: uint, entity: uint, region: uint, region_1: uint, right: uint):
    """Event 90005670"""
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    IfCharacterHuman(OR_9, PLAYER)
    IfCharacterType(OR_9, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_9, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_9)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfFlagEnabled(OR_1, flag_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag)
    ForceAnimation(entity, 12, wait_for_completion=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    IfAllPlayersOutsideRegion(AND_10, region=region_1)
    GotoIfConditionTrue(Label.L10, input_condition=AND_10)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    GotoIfFlagDisabled(Label.L10, flag=right)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag_1)
    EnableFlag(flag_2)
    ForceAnimation(entity, 20, wait_for_completion=True, unknown2=1.0)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    Wait(0.10000000149011612)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_1)
    ForceAnimation(entity, 21, wait_for_completion=True, unknown2=1.0)
    SkipLinesIfUnknown_203(line_count=3, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag)
    ForceAnimation(entity, 10, unknown2=1.0)
    SkipLines(1)
    ForceAnimation(entity, 10, wait_for_completion=True, unknown2=1.0)
    Restart()


@NeverRestart(90005673)
def Event_90005673(_, flag: uint, region: uint):
    """Event 90005673"""
    IfCharacterHuman(OR_9, PLAYER)
    IfCharacterWhitePhantom(OR_9, PLAYER)
    IfCharacterType(OR_9, PLAYER, character_type=CharacterType.Unknown17)
    IfConditionTrue(AND_1, input_condition=OR_9)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag)
    IfCharacterType(OR_10, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_10, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_10, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_10, PLAYER, character_type=CharacterType.Unknown18)
    IfConditionTrue(AND_10, input_condition=OR_10)
    IfCharacterInsideRegion(AND_10, character=PLAYER, region=region)
    IfConditionTrue(OR_2, input_condition=AND_10)
    IfAllPlayersOutsideRegion(OR_2, region=region)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_10)
    Wait(1.0)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag)
    Restart()


@NeverRestart(90005671)
def Event_90005671(
    _,
    flag: uint,
    obj__obj_flag: uint,
    obj_flag__region: uint,
    model_point: int,
    behavior_param_id: int,
):
    """Event 90005671"""
    DisableNetworkSync()
    IfFlagEnabled(AND_1, flag)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=obj_flag__region)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 4195)
    IfConditionTrue(MAIN, input_condition=AND_1)
    MoveObjectToCharacter(obj__obj_flag, character=PLAYER, model_point=93)
    WaitFrames(frames=1)
    CreateHazard(
        obj_flag=obj_flag__region,
        obj=obj__obj_flag,
        model_point=model_point,
        behavior_param_id=behavior_param_id,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    WaitFrames(frames=1)
    RemoveObjectFlag(obj_flag=obj__obj_flag)
    Wait(0.5)
    Restart()


@NeverRestart(90005672)
def Event_90005672(_, flag: uint, region: uint):
    """Event 90005672"""
    IfFlagEnabled(AND_1, flag)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(PLAYER, 4195)
    Wait(0.5)
    Restart()


@NeverRestart(90005675)
def Event_90005675(
    _,
    flag: uint,
    obj_flag: uint,
    obj: uint,
    region: uint,
    behaviour_id: int,
    seconds: float,
    right: int,
):
    """Event 90005675"""
    IfUnknown_3_32(AND_10, unk_1_2=1, unk_4_8=0)
    IfFlagEnabled(AND_10, flag)
    GotoIfConditionFalse(Label.L10, input_condition=AND_10)
    DisableNetworkFlag(flag)
    EnableThisSlotFlag()

    # --- Label 10 --- #
    DefineLabel(10)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=region)
    IfThisEventSlotFlagEnabled(OR_1)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag)
    SkipLinesIfThisEventSlotFlagEnabled(1)
    Wait(seconds)
    SkipLinesIfValueEqual(2, left=1, right=right)
    ForceAnimation(obj, 1, unknown2=1.0)
    SkipLines(1)
    ForceAnimation(obj, 2, unknown2=1.0)
    SkipLinesIfValueEqual(2, left=behaviour_id, right=0)
    CreateBigHazardousObject(
        obj_flag=obj_flag,
        obj=obj,
        model_point_start=30,
        model_point_end=31,
        behaviour_id=behaviour_id,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLines(1)
    CreateBigHazardousObject(
        obj_flag=obj_flag,
        obj=obj,
        model_point_start=30,
        model_point_end=31,
        behaviour_id=103000,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    Wait(1.0)
    RemoveObjectFlag(obj_flag=obj_flag)
    Wait(4.099999904632568)
    Wait(0.10000000149011612)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag)
    Restart()


@RestartOnRest(90005680)
def Event_90005680(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint, obj: uint):
    """Event 90005680"""
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableFlag(flag_3)
    IfObjectBackreadEnabled(MAIN, obj=obj)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    ForceAnimation(obj, 20, unknown2=1.0)
    EnableFlag(flag_1)
    EnableFlag(flag_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(obj, 10, unknown2=1.0)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    End()


@NeverRestart(90005681)
def Event_90005681(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint, attacked_entity: uint):
    """Event 90005681"""
    IfFlagEnabled(AND_13, flag)
    IfFlagEnabled(AND_13, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_13)
    IfFlagDisabled(AND_14, flag)
    IfFlagDisabled(AND_14, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_14)
    IfConditionTrue(AND_15, input_condition=OR_15)
    IfFlagEnabled(AND_15, flag_3)
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    IfFlagDisabled(OR_1, flag)
    IfFlagEnabled(AND_2, flag_1)
    IfAttackedWithDamageType(AND_2, attacked_entity=attacked_entity, attacker=20000)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(OR_4, input_condition=OR_1)
    IfConditionTrue(OR_4, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_4)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag)
    EnableNetworkFlag(flag_3)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    ForceAnimation(attacked_entity, 21, wait_for_completion=True, unknown2=1.0)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_3)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(OR_5, flag)
    IfFlagDisabled(AND_6, flag_1)
    IfAttackedWithDamageType(AND_6, attacked_entity=attacked_entity, attacker=20000)
    IfConditionTrue(OR_6, input_condition=AND_6)
    IfConditionTrue(OR_8, input_condition=OR_5)
    IfConditionTrue(OR_8, input_condition=OR_6)
    IfConditionTrue(MAIN, input_condition=OR_8)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag)
    EnableNetworkFlag(flag_3)
    EnableFlag(flag_1)
    ForceAnimation(attacked_entity, 12, wait_for_completion=True, unknown2=1.0)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_3)
    EnableFlag(flag_2)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    IfFlagDisabled(MAIN, flag_3)
    Restart()


@NeverRestart(90005682)
def Event_90005682(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    model_point: int,
    model_point_1: int,
    model_point_2: int,
    model_point_3: int,
):
    """Event 90005682"""
    IfFlagEnabled(AND_1, flag)
    SkipLinesIfUnsignedEqual(1, left=region, right=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=model_point_1, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=model_point_2, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 4 --- #
    DefineLabel(4)
    Wait(7.199999809265137)
    Restart()


@NeverRestart(90005683)
def Event_90005683(_, flag: uint, obj: uint, vfx_id: int, flag_1: uint, flag_2: uint):
    """Event 90005683"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DeleteObjectVFX(obj)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9260, entity=obj)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialog(text=4210, anchor_entity=obj)
    EnableFlag(flag_1)
    EnableFlag(flag_2)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfUnsignedEqual(Label.L10, left=1049551600, right=obj)
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=800530)
    Goto(Label.L1)

    # --- Label 10 --- #
    DefineLabel(10)
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=800531)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, flag)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Restart()
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=800530)


@NeverRestart(90005684)
def Event_90005684(_, anchor_entity: uint):
    """Event 90005684"""
    DisableNetworkSync()
    IfActionButtonParamActivated(AND_1, action_button_id=9260, entity=anchor_entity)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialog(text=4210, anchor_entity=anchor_entity)
    Wait(1.0)
    Restart()


@NeverRestart(90005685)
def Event_90005685(_, character: uint):
    """Event 90005685"""
    EnableImmortality(character)
    DisableInvincibility(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    DisableHealthBar(character)
    AddSpecialEffect(character, 5000)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@NeverRestart(90005686)
def Event_90005686(_, source_entity: uint, flag: uint):
    """Event 90005686"""
    IfFlagEnabled(MAIN, flag)
    ShootProjectile(
        owner_entity=source_entity,
        source_entity=source_entity,
        model_point=10,
        behavior_id=244600980,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=source_entity,
        source_entity=source_entity,
        model_point=15,
        behavior_id=244600980,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=source_entity,
        source_entity=source_entity,
        model_point=20,
        behavior_id=244600981,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=source_entity,
        source_entity=source_entity,
        model_point=25,
        behavior_id=244600981,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=source_entity,
        source_entity=source_entity,
        model_point=30,
        behavior_id=244600981,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(frames=1)
    Restart()


@NeverRestart(90005687)
def Event_90005687(_, character: uint, patrol_information_id: uint, region: uint):
    """Event 90005687"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    WaitFrames(frames=1)


@NeverRestart(90005688)
def Event_90005688(
    _,
    character: uint,
    region: uint,
    patrol_information_id: uint,
    region_1: uint,
    patrol_information_id_1: uint,
    region_2: uint,
    patrol_information_id_2: uint,
):
    """Event 90005688"""
    IfCharacterInsideRegion(MAIN, character=character, region=region)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=region_1)
    SkipLinesIfUnsignedEqual(1, left=0, right=region_2)
    GotoIfCharacterInsideRegion(Label.L2, character=PLAYER, region=region_2)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id_1)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    ChangePatrolBehavior(30090400, patrol_information_id=patrol_information_id_2)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfCharacterOutsideRegion(MAIN, character=character, region=region)
    Restart()


@RestartOnRest(90005690)
def Event_90005690(_, region: uint):
    """Event 90005690"""
    DisableNetworkSync()
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=region)
    AddSpecialEffect(PLAYER, 4080)
    IfCharacterOutsideRegion(MAIN, character=PLAYER, region=region)
    CancelSpecialEffect(PLAYER, 4080)
    Restart()


@RestartOnRest(90005691)
def Event_90005691(_, region: uint):
    """Event 90005691"""
    DisableNetworkSync()
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=region)
    AddSpecialEffect(PLAYER, 4085)
    IfCharacterOutsideRegion(MAIN, character=PLAYER, region=region)
    CancelSpecialEffect(PLAYER, 4085)
    Restart()


@RestartOnRest(90005694)
def Event_90005694(
    _,
    obj_flag: uint,
    obj: uint,
    model_point__model_point_start: int,
    model_point_end: int,
    behavior_param_id__behaviour_id: int,
    radius: float,
    life: float,
    repetition_time: float,
):
    """Event 90005694"""
    RemoveObjectFlag(obj_flag=obj_flag)
    SkipLinesIfValueNotEqual(2, left=0, right=model_point_end)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=model_point__model_point_start,
        behavior_param_id=behavior_param_id__behaviour_id,
        target_type=DamageTargetType.Character,
        radius=radius,
        life=life,
        repetition_time=repetition_time,
    )
    SkipLines(1)
    CreateBigHazardousObject(
        obj_flag=obj_flag,
        obj=obj,
        model_point_start=model_point__model_point_start,
        model_point_end=model_point_end,
        behaviour_id=behavior_param_id__behaviour_id,
        target_type=DamageTargetType.Character,
        radius=radius,
        life=life,
        repetition_time=repetition_time,
    )


@RestartOnRest(90005695)
def Event_90005695(
    _,
    obj__obj_flag: uint,
    obj: uint,
    model_point__model_point_start: int,
    model_point_end: int,
    behavior_param_id__behaviour_id: int,
    radius: float,
    life: float,
    repetition_time: float,
):
    """Event 90005695"""
    RemoveObjectFlag(obj_flag=obj__obj_flag)
    EndIfObjectDestroyed(obj)
    SkipLinesIfValueNotEqual(2, left=0, right=model_point_end)
    CreateHazard(
        obj_flag=obj__obj_flag,
        obj=obj,
        model_point=model_point__model_point_start,
        behavior_param_id=behavior_param_id__behaviour_id,
        target_type=DamageTargetType.Character,
        radius=radius,
        life=life,
        repetition_time=repetition_time,
    )
    SkipLines(1)
    CreateBigHazardousObject(
        obj_flag=obj__obj_flag,
        obj=obj,
        model_point_start=model_point__model_point_start,
        model_point_end=model_point_end,
        behaviour_id=behavior_param_id__behaviour_id,
        target_type=DamageTargetType.Character,
        radius=radius,
        life=life,
        repetition_time=repetition_time,
    )
    IfObjectDestroyed(MAIN, obj__obj_flag)
    RemoveObjectFlag(obj_flag=obj__obj_flag)


@RestartOnRest(90005700)
def Event_90005700(
    _,
    character: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    value: float,
    first_flag: uint,
    last_flag: uint,
    right: int,
):
    """Event 90005700"""
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(MAIN, 3000)
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_1)
    DisableFlag(flag_2)
    IfFlagDisabled(AND_1, flag)
    IfFlagDisabled(AND_1, flag_1)
    IfHealthGreaterThan(AND_1, character, value=0.0)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=PLAYER)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=40000)
    IfCharacterHasSpecialEffect(OR_1, character, 1650000)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfHealthLessThan(AND_2, character, value=value)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfCharacterHasSpecialEffect(OR_2, character, 9641)
    IfFlagEnabled(OR_2, flag_2)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_1)
    SetTeamType(character, TeamType.HostileNPC)
    AddSpecialEffect(character, 9628)
    AddSpecialEffect(character, 9635)
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=1, right=right)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    Goto(Label.L9)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)

    # --- Label 9 --- #
    DefineLabel(9)
    SaveRequest()


@RestartOnRest(90005701)
def Event_90005701(_, attacked_entity: uint, flag: uint, flag_1: uint, flag_2: uint, right: int):
    """Event 90005701"""
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(MAIN, 3000)
    WaitFrames(frames=1)
    IfFlagDisabled(AND_1, flag)
    IfFlagDisabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=9, right=right)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=8, right=right)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=7, right=right)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=6, right=right)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=5, right=right)
    GotoIfValueComparison(Label.L5, comparison_type=ComparisonType.Equal, left=4, right=right)
    GotoIfValueComparison(Label.L6, comparison_type=ComparisonType.Equal, left=3, right=right)
    GotoIfValueComparison(Label.L7, comparison_type=ComparisonType.Equal, left=2, right=right)
    GotoIfValueComparison(Label.L8, comparison_type=ComparisonType.Equal, left=1, right=right)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(MAIN, input_condition=OR_2)
    WaitFrames(frames=1)

    # --- Label 0 --- #
    DefineLabel(0)
    IfAttackedWithDamageType(OR_3, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_3, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(MAIN, input_condition=OR_3)
    WaitFrames(frames=1)

    # --- Label 1 --- #
    DefineLabel(1)
    IfAttackedWithDamageType(OR_4, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_4, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(MAIN, input_condition=OR_4)
    WaitFrames(frames=1)

    # --- Label 2 --- #
    DefineLabel(2)
    IfAttackedWithDamageType(OR_5, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_5, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(MAIN, input_condition=OR_5)
    WaitFrames(frames=1)

    # --- Label 3 --- #
    DefineLabel(3)
    IfAttackedWithDamageType(OR_6, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_6, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(MAIN, input_condition=OR_6)
    WaitFrames(frames=1)

    # --- Label 4 --- #
    DefineLabel(4)
    IfAttackedWithDamageType(OR_7, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_7, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(MAIN, input_condition=OR_7)
    WaitFrames(frames=1)

    # --- Label 5 --- #
    DefineLabel(5)
    IfAttackedWithDamageType(OR_8, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_8, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(MAIN, input_condition=OR_8)
    WaitFrames(frames=1)

    # --- Label 6 --- #
    DefineLabel(6)
    IfAttackedWithDamageType(OR_9, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_9, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(MAIN, input_condition=OR_9)
    WaitFrames(frames=1)

    # --- Label 7 --- #
    DefineLabel(7)
    IfAttackedWithDamageType(OR_10, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_10, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(MAIN, input_condition=OR_10)
    WaitFrames(frames=1)

    # --- Label 8 --- #
    DefineLabel(8)
    IfAttackedWithDamageType(OR_11, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_11, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(MAIN, input_condition=OR_11)
    EnableFlag(flag_2)
    Restart()


@RestartOnRest(90005702)
def Event_90005702(_, character: uint, flag: uint, first_flag: uint, last_flag: uint):
    """Event 90005702"""
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(AND_1, flag)
    IfCharacterDead(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    SaveRequest()


@RestartOnRest(90005703)
def Event_90005703(
    _,
    character: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
    first_flag: uint,
    last_flag: uint,
    right: int,
):
    """Event 90005703"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(flag_2)
    GotoIfFlagEnabled(Label.L0, flag=first_flag)
    AddSpecialEffect(character, 9628)
    AddSpecialEffect(character, 9635)
    AddSpecialEffect(character, 9643)
    SkipLinesIfCharacterHasSpecialEffect(line_count=1, character=character, special_effect=445)
    AddSpecialEffect(character, 442)
    AddSpecialEffect(character, 9644)

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagDisabled(AND_1, flag_3)
    IfFlagEnabled(AND_1, first_flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, 9629)
    AddSpecialEffect(character, 9634)
    AddSpecialEffect(character, 9642)
    AddSpecialEffect(character, 9647)
    SkipLinesIfCharacterHasSpecialEffect(line_count=1, character=character, special_effect=445)
    AddSpecialEffect(character, 440)
    AddSpecialEffect(character, 9645)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=PLAYER)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=40000)
    IfCharacterHasSpecialEffect(OR_1, character, 1650000)
    IfHealthGreaterThanOrEqual(AND_4, character, value=1.0)
    SkipLinesIfConditionFalse(2, AND_4)
    IfHealthLessThan(AND_2, character, value=0.6499999761581421)
    Goto(Label.L10)
    IfHealthGreaterThanOrEqual(AND_5, character, value=0.8999999761581421)
    SkipLinesIfConditionFalse(2, AND_5)
    IfHealthLessThan(AND_2, character, value=0.550000011920929)
    Goto(Label.L10)
    IfHealthGreaterThanOrEqual(AND_6, character, value=0.800000011920929)
    SkipLinesIfConditionFalse(2, AND_6)
    IfHealthLessThan(AND_2, character, value=0.44999998807907104)
    Goto(Label.L10)
    IfHealthGreaterThanOrEqual(AND_7, character, value=0.699999988079071)
    SkipLinesIfConditionFalse(2, AND_7)
    IfHealthLessThan(AND_2, character, value=0.3499999940395355)
    Goto(Label.L10)
    IfHealthGreaterThanOrEqual(AND_8, character, value=0.699999988079071)
    SkipLinesIfConditionFalse(2, AND_8)
    IfHealthLessThan(AND_2, character, value=0.25)
    Goto(Label.L10)
    IfHealthLessThan(AND_2, character, value=0.15000000596046448)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfFlagEnabled(OR_5, flag)
    IfFlagEnabled(OR_5, flag_1)
    IfFlagEnabled(OR_2, flag_2)
    IfCharacterHasSpecialEffect(OR_2, character, 9641)
    IfConditionTrue(OR_2, input_condition=OR_5)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfHealthGreaterThan(AND_3, character, value=0.0)
    IfConditionTrue(AND_3, input_condition=OR_2)
    IfFlagEnabled(OR_3, flag_3)
    IfConditionTrue(OR_4, input_condition=OR_3)
    IfConditionTrue(OR_4, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_4)
    RestartIfFinishedConditionTrue(input_condition=OR_3)
    SetTeamType(character, TeamType.HostileNPC)
    AddSpecialEffect(character, 9628)
    AddSpecialEffect(character, 9635)
    AddSpecialEffect(character, 9643)
    SkipLinesIfCharacterHasSpecialEffect(line_count=1, character=character, special_effect=445)
    AddSpecialEffect(character, 442)
    AddSpecialEffect(character, 9644)
    GotoIfFinishedConditionTrue(Label.L9, input_condition=OR_5)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=1, right=right)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)

    # --- Label 9 --- #
    DefineLabel(9)
    SaveRequest()
    Restart()


@RestartOnRest(90005704)
def Event_90005704(_, attacked_entity: uint, flag: uint, flag_1: uint, flag_2: uint, right: int):
    """Event 90005704"""
    EndIfPlayerNotInOwnWorld()
    WaitFrames(frames=1)
    IfFlagDisabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=4, right=right)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=3, right=right)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=2, right=right)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=1, right=right)
    IfFlagEnabled(OR_1, flag)
    IfFlagDisabled(OR_1, flag_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(OR_2, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    RestartIfFinishedConditionTrue(input_condition=OR_1)
    WaitFrames(frames=1)

    # --- Label 4 --- #
    DefineLabel(4)
    IfFlagEnabled(OR_3, flag)
    IfFlagDisabled(OR_3, flag_1)
    IfAttackedWithDamageType(OR_4, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_4, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(OR_4, input_condition=OR_3)
    IfConditionTrue(MAIN, input_condition=OR_4)
    RestartIfFinishedConditionTrue(input_condition=OR_3)
    WaitFrames(frames=1)

    # --- Label 3 --- #
    DefineLabel(3)
    IfFlagEnabled(OR_5, flag)
    IfFlagDisabled(OR_5, flag_1)
    IfAttackedWithDamageType(OR_6, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_6, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(OR_6, input_condition=OR_5)
    IfConditionTrue(MAIN, input_condition=OR_6)
    RestartIfFinishedConditionTrue(input_condition=OR_5)
    WaitFrames(frames=1)

    # --- Label 2 --- #
    DefineLabel(2)
    IfFlagEnabled(OR_7, flag)
    IfFlagDisabled(OR_7, flag_1)
    IfAttackedWithDamageType(OR_8, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_8, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(OR_8, input_condition=OR_7)
    IfConditionTrue(MAIN, input_condition=OR_8)
    RestartIfFinishedConditionTrue(input_condition=OR_7)
    WaitFrames(frames=1)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(OR_9, flag)
    IfFlagDisabled(OR_9, flag_1)
    IfAttackedWithDamageType(OR_10, attacked_entity=attacked_entity, attacker=PLAYER)
    IfAttackedWithDamageType(OR_10, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(OR_10, input_condition=OR_9)
    IfConditionTrue(MAIN, input_condition=OR_10)
    RestartIfFinishedConditionTrue(input_condition=OR_9)
    EnableFlag(flag_2)
    Restart()


@RestartOnRest(90005705)
def Event_90005705(_, character: uint):
    """Event 90005705"""
    WaitFrames(frames=1)
    EnableCharacter(character)
    EnableBackread(character)
    EndIfPlayerNotInOwnWorld()
    EnableImmortality(character)
    IfAttackedWithDamageType(MAIN, attacked_entity=character, attacker=PLAYER)
    ForceAnimation(character, 20022, unknown2=1.0)
    Wait(10.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(90005706)
def Event_90005706(_, character: uint, animation_id: int, left: uint):
    """Event 90005706"""
    EnableBackread(character)
    EnableCharacter(character)
    DisableGravity(character)
    ForceAnimation(character, animation_id, unknown2=1.0)
    EndIfUnsignedEqual(left=left, right=0)
    IfCharacterHasSpecialEffect(AND_1, character, 9624)
    AwaitConditionTrue(AND_1)
    Move(character, destination=left, destination_type=CoordEntityType.Region, short_move=True)
    DisableGravity(character)
    End()


@RestartOnRest(90005707)
def Event_90005707(
    _,
    character: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
    first_flag: uint,
    last_flag: uint,
    right: int,
    animation_id: int,
    left: uint,
    flag_4: uint,
):
    """Event 90005707"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(flag_2)
    IfFlagDisabled(AND_1, flag_3)
    IfFlagEnabled(AND_1, first_flag)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 9642)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=PLAYER)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=40000)
    IfCharacterHasSpecialEffect(OR_1, character, 1650000)
    IfHealthGreaterThanOrEqual(AND_4, character, value=1.0)
    SkipLinesIfConditionFalse(2, AND_4)
    IfHealthLessThan(AND_2, character, value=0.6499999761581421)
    Goto(Label.L10)
    IfHealthGreaterThanOrEqual(AND_5, character, value=0.8999999761581421)
    SkipLinesIfConditionFalse(2, AND_5)
    IfHealthLessThan(AND_2, character, value=0.550000011920929)
    Goto(Label.L10)
    IfHealthGreaterThanOrEqual(AND_6, character, value=0.800000011920929)
    SkipLinesIfConditionFalse(2, AND_6)
    IfHealthLessThan(AND_2, character, value=0.44999998807907104)
    Goto(Label.L10)
    IfHealthGreaterThanOrEqual(AND_7, character, value=0.699999988079071)
    SkipLinesIfConditionFalse(2, AND_7)
    IfHealthLessThan(AND_2, character, value=0.3499999940395355)
    Goto(Label.L10)
    IfHealthGreaterThanOrEqual(AND_8, character, value=0.699999988079071)
    SkipLinesIfConditionFalse(2, AND_8)
    IfHealthLessThan(AND_2, character, value=0.25)
    Goto(Label.L10)
    IfHealthLessThan(AND_2, character, value=0.15000000596046448)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfFlagEnabled(OR_2, flag_2)
    IfCharacterHasSpecialEffect(OR_2, character, 9641)
    IfFlagEnabled(OR_2, flag)
    IfFlagEnabled(OR_2, flag_1)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfHealthGreaterThan(AND_3, character, value=0.0)
    IfConditionTrue(AND_3, input_condition=OR_2)
    IfFlagEnabled(OR_3, flag_3)
    IfConditionTrue(OR_4, input_condition=OR_3)
    IfConditionTrue(OR_4, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_4)
    RestartIfFinishedConditionTrue(input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L9, input_condition=OR_5)
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=1, right=right)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    Goto(Label.L9)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)

    # --- Label 9 --- #
    DefineLabel(9)
    SaveRequest()
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    WaitFramesAfterCutscene(frames=2)
    IfFlagDisabled(MAIN, left)
    ForceAnimation(character, animation_id, unknown2=1.0)
    EnableFlag(flag_4)
    Restart()


@RestartOnRest(90005708)
def Event_90005708(_, character: uint, flag: uint, left: uint):
    """Event 90005708"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterBackreadEnabled(AND_1, character)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFramesAfterCutscene(frames=1)
    RestartIfFlagDisabled(flag)
    SkipLinesIfUnsignedNotEqual(2, left=left, right=0)
    Unknown_2004_81(character=character)
    SkipLines(1)
    Move(character, destination=left, destination_type=CoordEntityType.Region, short_move=True)


@RestartOnRest(90005709)
def Event_90005709(_, attacked_entity: uint, model_point: int, vfx_id: int):
    """Event 90005709"""
    EndIfPlayerNotInOwnWorld()
    IfAttackedWithDamageType(MAIN, attacked_entity=attacked_entity, attacker=0)
    CreateTemporaryVFX(
        vfx_id=vfx_id,
        anchor_entity=attacked_entity,
        model_point=model_point,
        anchor_type=CoordEntityType.Character,
    )
    Restart()


@RestartOnRest(90005710)
def Event_90005710(_, flag: uint, obj: uint, vfx_id: int, model_point: int):
    """Event 90005710"""
    IfFlagDisabled(MAIN, flag)
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=model_point)
    IfFlagEnabled(MAIN, flag)
    Wait(2.0)
    DeleteObjectVFX(obj)
    Restart()


@RestartOnRest(90005711)
def Event_90005711(_, flag: uint, patrol_information_id: uint):
    """Event 90005711"""
    GotoIfPlayerInOwnWorld(Label.L0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkUpdateAuthority(20000, authority_level=UpdateAuthority.Unknown8192)
    IfFlagEnabled(MAIN, flag)
    ChangePatrolBehavior(35000, patrol_information_id=patrol_information_id)
    Restart()


@RestartOnRest(90005712)
def Event_90005712(_, character: uint, obj: uint, vfx_id: int, model_point: int):
    """Event 90005712"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=model_point)
    IfCharacterHasSpecialEffect(MAIN, character, 9502)
    DeleteObjectVFX(obj)
    IfCharacterHasSpecialEffect(MAIN, character, 9503)
    Restart()


@RestartOnRest(90005713)
def Event_90005713(_, flag: uint, character: uint, character_1: uint):
    """Event 90005713"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterHasSpecialEffect(AND_1, character, 9500)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfPlayerNotInOwnWorld(AND_2)
    IfFlagEnabled(AND_2, flag)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAI(character_1)
    IfPlayerInOwnWorld(AND_3)
    IfCharacterHasSpecialEffect(AND_3, 20000, 202)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfPlayerNotInOwnWorld(AND_4)
    IfFlagDisabled(AND_4, flag)
    IfConditionTrue(OR_3, input_condition=AND_4)
    IfConditionTrue(MAIN, input_condition=OR_3)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableNetworkFlag(flag)
    Restart()


@RestartOnRest(90005720)
def Event_90005720(_, character: uint, character_1: uint, special_effect: int, model_point: int):
    """Event 90005720"""
    EndIfCharacterHasSpecialEffect(character=character, special_effect=11020)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    IfCharacterHasSpecialEffect(AND_1, character, 10960)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    AddSpecialEffect(character_1, 8551)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        copy_draw_parent=character,
    )
    ForceAnimation(character_1, 20000, unknown2=1.0)
    End()


@RestartOnRest(90005721)
def Event_90005721(_, character: uint, character_1: uint):
    """Event 90005721"""
    IfCharacterDead(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitRandomSeconds(min_seconds=0.5, max_seconds=1.5)
    Kill(character_1, award_souls=True)
    End()


@RestartOnRest(90005722)
def Event_90005722(_, character: uint, character_1: uint):
    """Event 90005722"""
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=11020)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)

    # --- Label 0 --- #
    DefineLabel(0)
    IfHealthLessThan(OR_1, character, value=0.6499999761581421)
    IfHealthLessThan(
        OR_1,
        character_1,
        value=0.6499999761581421,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    IfConditionTrue(MAIN, input_condition=OR_1)
    AddSpecialEffect(character, 11012)
    AddSpecialEffect(character, 11020)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()


@RestartOnRest(90005723)
def Event_90005723(_, character: uint):
    """Event 90005723"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 11001)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 11020)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, 11000)
    IfCharacterHasSpecialEffect(OR_1, character, 11001)
    IfCharacterHasSpecialEffect(OR_1, character, 11020)
    IfConditionTrue(MAIN, input_condition=OR_1)
    CancelSpecialEffect(character, 11000)
    Restart()


@RestartOnRest(90005724)
def Event_90005724(
    _,
    flag: uint,
    character: uint,
    item_lot_param_id: int,
    seconds: float,
    left: int,
    character_1: uint,
):
    """Event 90005724"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    SkipLinesIfValueEqual(4, left=left, right=0)
    DisableCharacter(character)
    DisableAnimations(character)
    DropMandatoryTreasure(character)
    End()
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterDead(MAIN, character)
    Wait(seconds)
    EnableFlag(flag)
    EndIfPlayerNotInOwnWorld()
    EndIfValueEqual(left=left, right=1)
    AwardItemLot(item_lot_param_id, host_only=True)
    End()


@RestartOnRest(90005725)
def Event_90005725(
    _,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
    character: uint,
    character_1: uint,
    obj: uint,
):
    """Event 90005725"""
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    IfFlagEnabled(AND_10, flag)
    IfFlagEnabled(AND_10, flag_3)
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(flag_3)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableObject(obj)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L4, flag=flag_2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SkipLinesIfCharacterHasSpecialEffect(line_count=1, character=character, special_effect=11035)
    ForceAnimation(character, 930003, unknown2=1.0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=11035)
    ForceAnimation(character, 930002, unknown2=1.0)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetTeamType(character_1, TeamType.HostileNPC)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableObject(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(90005726)
def Event_90005726(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint, character: uint, obj: uint):
    """Event 90005726"""
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    IfFlagEnabled(AND_10, flag)
    IfFlagEnabled(AND_10, flag_3)
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(flag_3)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L4, flag=flag_2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930003, unknown2=1.0)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(90005727)
def Event_90005727(_, flag: uint, character: uint, character_1: uint, first_flag: uint, last_flag: uint):
    """Event 90005727"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(last_flag)
    AddSpecialEffect(character, 9629)
    AddSpecialEffect(character, 9634)
    AddSpecialEffect(character, 9642)
    AddSpecialEffect(character, 440)
    AddSpecialEffect(character, 9645)
    AddSpecialEffect(character_1, 9629)
    AddSpecialEffect(character_1, 9634)
    AddSpecialEffect(character_1, 9642)
    AddSpecialEffect(character_1, 440)
    AddSpecialEffect(character_1, 9645)
    IfFlagEnabled(OR_1, flag)
    IfConditionTrue(OR_15, input_condition=OR_1)
    IfAttackedWithDamageType(AND_1, attacked_entity=character, attacker=20000)
    IfHealthValueLessThan(AND_1, character, value=1)
    IfAttackedWithDamageType(AND_2, attacked_entity=character_1, attacker=20000)
    IfHealthValueLessThan(AND_2, character_1, value=1)
    IfConditionTrue(OR_15, input_condition=AND_1)
    IfConditionTrue(OR_15, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_15)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAI(character)
    AddSpecialEffect(character, 9628)
    AddSpecialEffect(character, 9635)
    AddSpecialEffect(character, 9643)
    AddSpecialEffect(character, 442)
    AddSpecialEffect(character, 9644)
    SetTeamType(character_1, TeamType.HostileNPC)
    EnableAI(character_1)
    AddSpecialEffect(character_1, 9628)
    AddSpecialEffect(character_1, 9635)
    AddSpecialEffect(character_1, 9643)
    AddSpecialEffect(character_1, 442)
    AddSpecialEffect(character_1, 9644)
    SkipLinesIfFlagEnabled(2, last_flag)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    End()


@RestartOnRest(90005728)
def Event_90005728(_, attacked_entity: uint, flag: uint, flag_1: uint):
    """Event 90005728"""
    EndIfPlayerNotInOwnWorld()
    IfAttackedWithDamageType(OR_1, attacked_entity=attacked_entity, attacker=20000)
    IfAttackedWithDamageType(OR_1, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagDisabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)
    End()


@RestartOnRest(90005729)
def Event_90005729(_, flag: uint, character: uint, distance: float, flag_1: uint):
    """Event 90005729"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    SetCharacterTalkRange(character=character, distance=distance)
    AwaitFlagEnabled(flag=flag_1)
    Wait(30.0)
    DisableNetworkFlag(flag_1)
    Restart()


@RestartOnRest(90005730)
def Event_90005730(_, flag: uint, seconds: float, flag_1: uint, flag_2: uint, flag_3: uint, flag_4: uint):
    """Event 90005730"""
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_2)
    IfFlagDisabled(AND_1, flag_3)
    IfFlagDisabled(AND_1, flag_4)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    IfFlagEnabled(OR_2, flag)
    IfFlagDisabled(OR_2, flag_2)
    IfFlagEnabled(OR_2, flag_3)
    IfFlagEnabled(OR_2, flag_4)
    IfFlagEnabled(OR_1, flag_1)
    IfConditionTrue(OR_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    RestartIfFinishedConditionTrue(input_condition=OR_2)
    EnableFlag(flag)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(OR_4, flag)
    IfFlagDisabled(OR_4, flag_2)
    IfFlagEnabled(OR_4, flag_3)
    IfFlagEnabled(OR_4, flag_4)
    IfFlagDisabled(OR_4, flag_1)
    IfTimeElapsed(OR_3, seconds=seconds)
    IfConditionTrue(OR_3, input_condition=OR_4)
    IfConditionTrue(MAIN, input_condition=OR_3)
    RestartIfFinishedConditionTrue(input_condition=OR_4)
    EnableFlag(flag)
    Restart()


@RestartOnRest(90005731)
def Event_90005731(_, flag: uint, other_entity: uint, radius: float, radius_1: float):
    """Event 90005731"""
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=other_entity, radius=radius)
    EnableFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    IfEntityBeyondDistance(AND_1, entity=PLAYER, other_entity=other_entity, radius=radius)
    IfEntityBeyondDistance(AND_1, entity=PLAYER, other_entity=other_entity, radius=radius_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(flag)
    Restart()


@RestartOnRest(90005732)
def Event_90005732(_, flag: uint, region: uint, region_1: uint):
    """Event 90005732"""
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=region)
    EnableFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=region)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=region_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(flag)
    Restart()


@RestartOnRest(90005733)
def Event_90005733(_, flag: uint):
    """Event 90005733"""
    EndIfPlayerNotInOwnWorld()
    DisableNetworkSync()
    DisableFlag(flag)
    IfFlagEnabled(AND_1, flag)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Unknown_2004_80(unk_0_4=0)
    Restart()


@RestartOnRest(90005740)
def Event_90005740(
    _,
    flag: uint,
    flag_1: uint,
    left: uint,
    character: uint,
    model_point: int,
    obj: uint,
    model_point_1: short,
    radius: float,
    animation: int,
    animation_id: int,
    special_effect: int,
    radius_1: float,
):
    """Event 90005740"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(MAIN, flag)
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    GotoIfUnsignedEqual(Label.L0, left=obj, right=0)
    MoveObjectToCharacter(obj, character=character, model_point=model_point_1)
    WaitFramesAfterCutscene(frames=1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=obj, radius=radius)
    GotoIfConditionTrue(Label.L9, input_condition=AND_1)
    IfEntityWithinDistance(AND_15, entity=PLAYER, other_entity=obj, radius=radius_1)
    IfEntityWithinDistance(AND_15, entity=PLAYER, other_entity=character, radius=radius_1)
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    RotateToFaceEntity(PLAYER, obj, wait_for_completion=True)
    RotateToFaceEntity(PLAYER, obj, animation=90006)
    Goto(Label.L8)

    # --- Label 0 --- #
    DefineLabel(0)
    RotateToFaceEntity(PLAYER, character, wait_for_completion=True)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
    GotoIfConditionTrue(Label.L9, input_condition=AND_1)
    RotateToFaceEntity(PLAYER, character, animation=90006)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    WaitFramesAfterCutscene(frames=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 9900)
    IfFlagDisabled(OR_2, flag)
    IfTimeElapsed(OR_2, seconds=2.0)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(OR_1, input_condition=OR_2)
    SkipLinesIfValueEqual(3, left=model_point, right=0)
    SkipLinesIfUnsignedEqual(2, left=obj, right=0)
    IfEntityWithinDistance(OR_1, entity=PLAYER, other_entity=obj, radius=radius)
    SkipLines(1)
    IfEntityWithinDistance(OR_1, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfFinishedConditionTrue(Label.L20, input_condition=AND_2)
    GotoIfFinishedConditionTrue(Label.L19, input_condition=OR_2)

    # --- Label 9 --- #
    DefineLabel(9)
    EnableFlag(flag_1)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    EnableFlag(left)
    SkipLinesIfValueEqual(1, left=model_point, right=0)
    Move(
        PLAYER,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        short_move=True,
    )
    SkipLinesIfValueEqual(2, left=special_effect, right=-1)
    RotateToFaceEntity(PLAYER, character, animation=animation)
    SkipLines(1)
    RotateToFaceEntity(PLAYER, character, animation=animation, wait_for_completion=True)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    WaitFramesAfterCutscene(frames=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_3, PLAYER, 9900)
    IfFlagDisabled(OR_3, flag)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L20, input_condition=AND_3)
    GotoIfValueComparison(Label.L18, comparison_type=ComparisonType.Equal, left=animation_id, right=-1)
    GotoIfValueComparison(Label.L10, comparison_type=ComparisonType.Equal, left=special_effect, right=-1)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, PLAYER, 9900)
    IfCharacterHasSpecialEffect(OR_4, PLAYER, special_effect)
    IfConditionTrue(OR_4, input_condition=AND_4)
    IfConditionTrue(MAIN, input_condition=OR_4)
    GotoIfFinishedConditionTrue(Label.L20, input_condition=AND_4)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableFlag(flag_1)
    ForceAnimation(PLAYER, animation_id, wait_for_completion=True, unknown2=1.0)
    Restart()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableFlag(flag_1)
    Restart()

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(flag)
    ForceAnimation(PLAYER, 0, unknown2=1.0)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(90005741)
def Event_90005741(
    _,
    flag: uint,
    flag_1: uint,
    left: uint,
    character: uint,
    animation__animation_id: int,
    left_1: uint,
    animation_id: int,
    special_effect: int,
    seconds: float,
):
    """Event 90005741"""
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfFlagEnabled(AND_1, left)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag_1)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    DisableFlag(left)
    GotoIfUnsignedEqual(Label.L0, left=left_1, right=1)
    SkipLinesIfValueEqual(2, left=special_effect, right=-1)
    ForceAnimation(character, animation__animation_id, unknown2=1.0)
    SkipLines(1)
    ForceAnimation(character, animation__animation_id, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfValueEqual(2, left=special_effect, right=-1)
    RotateToFaceEntity(character, PLAYER, animation=animation__animation_id)
    SkipLines(1)
    RotateToFaceEntity(character, PLAYER, animation=animation__animation_id, wait_for_completion=True)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    IfFlagDisabled(AND_1, flag)
    SkipLinesIfValueEqual(1, left=special_effect, right=-1)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfValueComparison(Label.L19, comparison_type=ComparisonType.Equal, left=animation_id, right=-1)
    DisableFlag(flag_1)
    ForceAnimation(character, animation_id, wait_for_completion=True, unknown2=1.0)
    Wait(seconds)
    Restart()

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(flag_1)
    Wait(seconds)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(90005742)
def Event_90005742(
    _,
    flag: uint,
    flag_1: uint,
    left: uint,
    character: uint,
    model_point: int,
    obj: uint,
    model_point_1: short,
    radius: float,
    animation: int,
    animation_id: int,
    special_effect: int,
    radius_1: float,
    flag_2: uint,
):
    """Event 90005742"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(MAIN, flag)
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    GotoIfUnsignedEqual(Label.L0, left=obj, right=0)
    MoveObjectToCharacter(obj, character=character, model_point=model_point_1)
    WaitFramesAfterCutscene(frames=1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=obj, radius=radius)
    GotoIfConditionTrue(Label.L9, input_condition=AND_1)
    IfEntityWithinDistance(AND_15, entity=PLAYER, other_entity=obj, radius=radius_1)
    IfEntityWithinDistance(AND_15, entity=PLAYER, other_entity=character, radius=radius_1)
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    RotateToFaceEntity(PLAYER, obj, wait_for_completion=True)
    RotateToFaceEntity(PLAYER, obj, animation=90006)
    Goto(Label.L8)

    # --- Label 0 --- #
    DefineLabel(0)
    RotateToFaceEntity(PLAYER, character, wait_for_completion=True)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
    GotoIfConditionTrue(Label.L9, input_condition=AND_1)
    RotateToFaceEntity(PLAYER, character, animation=90006)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    WaitFramesAfterCutscene(frames=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 9900)
    IfFlagDisabled(OR_2, flag)
    IfTimeElapsed(OR_2, seconds=2.0)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(OR_1, input_condition=OR_2)
    SkipLinesIfValueEqual(3, left=model_point, right=0)
    SkipLinesIfUnsignedEqual(2, left=obj, right=0)
    IfEntityWithinDistance(OR_1, entity=PLAYER, other_entity=obj, radius=radius)
    SkipLines(1)
    IfEntityWithinDistance(OR_1, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfFinishedConditionTrue(Label.L20, input_condition=AND_2)
    GotoIfFinishedConditionTrue(Label.L19, input_condition=OR_2)

    # --- Label 9 --- #
    DefineLabel(9)
    EnableFlag(flag_1)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    EnableFlag(left)
    SkipLinesIfValueEqual(1, left=model_point, right=0)
    Move(
        PLAYER,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        short_move=True,
    )
    SkipLinesIfValueEqual(2, left=special_effect, right=-1)
    RotateToFaceEntity(PLAYER, character, animation=animation)
    SkipLines(1)
    RotateToFaceEntity(PLAYER, character, animation=animation, wait_for_completion=True)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    WaitFramesAfterCutscene(frames=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_3, PLAYER, 9900)
    IfFlagEnabled(AND_15, flag_2)
    IfFlagDisabled(OR_3, flag)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfConditionTrue(OR_3, input_condition=AND_15)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L20, input_condition=AND_3)
    GotoIfValueComparison(Label.L18, comparison_type=ComparisonType.Equal, left=animation_id, right=-1)
    GotoIfFinishedConditionTrue(Label.L20, input_condition=AND_15)
    GotoIfValueComparison(Label.L10, comparison_type=ComparisonType.Equal, left=special_effect, right=-1)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, PLAYER, 9900)
    IfCharacterHasSpecialEffect(OR_4, PLAYER, special_effect)
    IfConditionTrue(OR_4, input_condition=AND_4)
    IfConditionTrue(MAIN, input_condition=OR_4)
    GotoIfFinishedConditionTrue(Label.L20, input_condition=AND_4)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableFlag(flag_1)
    ForceAnimation(PLAYER, animation_id, wait_for_completion=True, unknown2=1.0)
    Restart()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableFlag(flag_1)
    Restart()

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(flag)
    ForceAnimation(PLAYER, 0, unknown2=1.0)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(90005743)
def Event_90005743(
    _,
    flag: uint,
    flag_1: uint,
    left: uint,
    character: uint,
    animation__animation_id: int,
    left_1: uint,
    animation_id: int,
    special_effect: int,
    seconds: float,
    flag_2: uint,
):
    """Event 90005743"""
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfFlagEnabled(AND_1, left)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag_1)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    DisableFlag(left)
    GotoIfUnsignedEqual(Label.L0, left=left_1, right=1)
    SkipLinesIfValueEqual(2, left=special_effect, right=-1)
    ForceAnimation(character, animation__animation_id, unknown2=1.0)
    SkipLines(1)
    ForceAnimation(character, animation__animation_id, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfValueEqual(2, left=special_effect, right=-1)
    RotateToFaceEntity(character, PLAYER, animation=animation__animation_id)
    SkipLines(1)
    RotateToFaceEntity(character, PLAYER, animation=animation__animation_id, wait_for_completion=True)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    IfFlagDisabled(AND_1, flag)
    SkipLinesIfValueEqual(1, left=special_effect, right=-1)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfFlagEnabled(AND_15, flag_2)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfValueComparison(Label.L19, comparison_type=ComparisonType.Equal, left=animation_id, right=-1)
    GotoIfFinishedConditionTrue(Label.L20, input_condition=AND_15)
    DisableFlag(flag_1)
    ForceAnimation(character, animation_id, wait_for_completion=True, unknown2=1.0)
    Wait(seconds)
    Restart()

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(flag_1)
    Wait(seconds)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@NeverRestart(90005750)
def Event_90005750(
    _,
    obj: uint,
    action_button_id: int,
    item_lot_param_id: int,
    first_flag: uint,
    last_flag: uint,
    flag: uint,
    model_point: int,
):
    """Event 90005750"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, flag)
    IfFlagRangeAnyDisabled(AND_1, flag_range=(first_flag, last_flag))
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfValueEqual(2, left=model_point, right=0)
    CreateObjectVFX(obj, vfx_id=90, model_point=model_point)
    SkipLines(1)
    CreateObjectVFX(obj, vfx_id=90, model_point=6101)
    IfFlagDisabled(OR_2, flag)
    IfFlagRangeAllEnabled(OR_2, flag_range=(first_flag, last_flag))
    IfActionButtonParamActivated(OR_1, action_button_id=action_button_id, entity=obj)
    IfConditionTrue(OR_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    DeleteObjectVFX(obj)
    AwardItemLot(item_lot_param_id, host_only=True)
    EzstateAIRequest(PLAYER, command_id=60070, command_slot=0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(obj)
    Restart()


@RestartOnRest(90005751)
def Event_90005751(_, attacked_entity: uint, model_point: int, vfx_id: int):
    """Event 90005751"""
    EndIfPlayerNotInOwnWorld()
    IfAttackedWithDamageType(AND_1, attacked_entity=attacked_entity, attacker=20000)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateTemporaryVFX(
        vfx_id=vfx_id,
        anchor_entity=attacked_entity,
        model_point=model_point,
        anchor_type=CoordEntityType.Object,
    )
    Restart()


@NeverRestart(90005752)
def Event_90005752(_, obj: uint, vfx_id: int, model_point: int, seconds: float):
    """Event 90005752"""
    DisableNetworkSync()
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    IfAttackedWithDamageType(AND_2, attacked_entity=obj, attacker=20000)
    IfTimeElapsed(OR_1, seconds=seconds)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    RestartIfFinishedConditionTrue(input_condition=AND_2)
    DeleteObjectVFX(obj)

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_3)
    IfAttackedWithDamageType(AND_3, attacked_entity=obj, attacker=20000)
    IfConditionTrue(MAIN, input_condition=AND_3)
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=model_point)
    Restart()


@RestartOnRest(90005760)
def Event_90005760(_, flag: uint, character: uint, region: uint, flag_1: uint):
    """Event 90005760"""
    EndIfFlagEnabled(flag)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, 9000)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 20000, unknown2=1.0)
    End()


@RestartOnRest(90005770)
def Event_90005770(_, flag: uint):
    """Event 90005770"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(MAIN, flag)
    EnableNetworkFlag(flag)


@RestartOnRest(90005771)
def Event_90005771(_, other_entity: uint, flag: uint):
    """Event 90005771"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(flag)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=other_entity, radius=3.0)
    EnableFlag(flag)
    IfEntityBeyondDistance(MAIN, entity=PLAYER, other_entity=other_entity, radius=3.0)
    Restart()


@RestartOnRest(90005772)
def Event_90005772(_, character: uint):
    """Event 90005772"""
    DisableBackread(character)
    DisableCharacter(character)


@NeverRestart(90005773)
def Event_90005773(_, flag: uint):
    """Event 90005773"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(flag)
    IfFlagEnabled(MAIN, flag)
    SaveRequest()
    Restart()


@NeverRestart(90005774)
def Event_90005774(_, flag: uint, item_lot_param_id: int, flag_1: uint):
    """Event 90005774"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag_1)
    IfTimeElapsed(AND_2, seconds=2.0)
    IfFlagEnabled(AND_2, flag)
    AwaitConditionTrue(AND_2)
    SkipLinesIfPlayerNotInOwnWorld(1)
    AwardItemLot(item_lot_param_id, host_only=True)
    End()


@RestartOnRest(90005775)
def Event_90005775(_, unk_0_4: int, flag: uint, unk_4_8: float):
    """Event 90005775"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(MAIN, flag)
    Unknown_2003_78(unk_0_4=unk_0_4, unk_4_8=unk_4_8)


@NeverRestart(90005780)
def Event_90005780(
    _,
    flag: uint,
    summon_flag: uint,
    dismissal_flag: uint,
    character: uint,
    sign_type: int,
    region: uint,
    right: uint,
    unknown: uchar,
    right_1: int,
):
    """Event 90005780"""
    SkipLinesIfPlayerNotInOwnWorld(1)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    Unknown_2003_82(character=character)
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(dismissal_flag)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_1, right)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterBackreadEnabled(AND_1, character)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=10.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    PlaceSummonSign(
        sign_type=sign_type,
        character=character,
        region=region,
        summon_flag=summon_flag,
        dismissal_flag=dismissal_flag,
        unknown=unknown,
    )
    EndIfValueEqual(left=0, right=right_1)


@NeverRestart(90005781)
def Event_90005781(_, flag: uint, flag_1: uint, flag_2: uint, character: uint):
    """Event 90005781"""
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_2)
    IfFlagEnabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableAI(character)
    SetBackreadStateAlternate(character, True)
    IfFlagEnabled(AND_1, flag_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetBackreadStateAlternate(character, False)


@NeverRestart(90005782)
def Event_90005782(_, flag: uint, region: uint, character: uint, target_entity: uint, region_1: uint, animation: int):
    """Event 90005782"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    SetEventPoint(character, region=region_1, reaction_range=0.0)
    IfCharacterInsideRegion(MAIN, character=character, region=region_1)
    SkipLinesIfValueEqual(2, left=animation, right=0)
    RotateToFaceEntity(character, target_entity, animation=animation, wait_for_completion=True)
    SkipLines(1)
    RotateToFaceEntity(character, target_entity, animation=60060, wait_for_completion=True)
    IfTimeElapsed(OR_4, seconds=3.0)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfCharacterInsideRegion(OR_5, character=character, region=region)
    IfConditionTrue(MAIN, input_condition=OR_5)
    RestartIfFinishedConditionTrue(input_condition=OR_4)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@NeverRestart(90005784)
def Event_90005784(_, flag: uint, flag_1: uint, character: uint, region: uint, region_1: uint, animation: int):
    """Event 90005784"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    SetEventPoint(character, region=region_1, reaction_range=0.0)
    IfCharacterInsideRegion(MAIN, character=character, region=region_1)
    SkipLinesIfValueEqual(2, left=animation, right=0)
    RotateToFaceEntity(character, region, animation=animation, wait_for_completion=True)
    SkipLines(1)
    RotateToFaceEntity(character, region, animation=60060, wait_for_completion=True)
    IfTimeElapsed(OR_4, seconds=3.0)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfCharacterInsideRegion(OR_5, character=character, region=region)
    IfConditionTrue(MAIN, input_condition=OR_5)
    RestartIfFinishedConditionTrue(input_condition=OR_4)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(90005783)
def Event_90005783(
    _,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    character__unk_0_4: uint,
    other_entity: uint,
    region: uint,
    left: int,
):
    """Event 90005783"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfPlayerInOwnWorld(AND_2)
    IfFlagEnabled(AND_2, flag_1)
    IfHasAIStatus(
        AND_2,
        character__unk_0_4,
        ai_status=AIStatusType.Battle,
        target_comparison_type=ComparisonType.NotEqual,
    )
    SkipLinesIfUnsignedNotEqual(2, left=region, right=0)
    IfEntityBeyondDistance(AND_2, entity=PLAYER, other_entity=other_entity, radius=75.0)
    SkipLines(1)
    IfCharacterOutsideRegion(AND_2, character=PLAYER, region=region)
    IfPlayerInOwnWorld(AND_3)
    IfFlagEnabled(AND_3, flag_1)
    SkipLinesIfValueEqual(5, left=left, right=2)
    SkipLinesIfValueEqual(2, left=left, right=1)
    IfEntityBeyondDistance(AND_3, entity=PLAYER, other_entity=other_entity, radius=180.0)
    SkipLines(3)
    IfEntityBeyondDistance(AND_3, entity=PLAYER, other_entity=other_entity, radius=360.0)
    SkipLines(1)
    IfEntityBeyondDistance(AND_3, entity=PLAYER, other_entity=other_entity, radius=720.0)
    IfConditionTrue(OR_10, input_condition=AND_1)
    IfConditionTrue(OR_10, input_condition=AND_2)
    IfConditionTrue(OR_10, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_10)
    IfFlagEnabled(AND_11, flag)
    IfFlagEnabled(AND_11, flag_2)
    EndIfConditionTrue(input_condition=AND_11)
    Unknown_2003_79(unk_0_4=character__unk_0_4)
    End()


@RestartOnRest(90005785)
def Event_90005785(
    _,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    unk_0_4: uint,
    other_entity: uint,
    region: uint,
    radius: float,
):
    """Event 90005785"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfPlayerInOwnWorld(AND_2)
    IfFlagEnabled(AND_2, flag_1)
    SkipLinesIfUnsignedNotEqual(2, left=region, right=0)
    IfEntityBeyondDistance(AND_2, entity=PLAYER, other_entity=other_entity, radius=radius)
    SkipLines(1)
    IfCharacterOutsideRegion(AND_2, character=PLAYER, region=region)
    IfConditionTrue(OR_10, input_condition=AND_1)
    IfConditionTrue(OR_10, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_10)
    IfFlagEnabled(AND_11, flag)
    IfFlagEnabled(AND_11, flag_2)
    EndIfConditionTrue(input_condition=AND_11)
    Unknown_2003_79(unk_0_4=unk_0_4)
    End()


@NeverRestart(90005790)
def Event_90005790(
    _,
    right: uint,
    flag: uint,
    summon_flag: uint,
    dismissal_flag: uint,
    character: uint,
    sign_type: int,
    region: uint,
    region_1: uint,
    seconds: float,
    right_1: uint,
    unknown: uchar,
    right_2: int,
):
    """Event 90005790"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    EndIfFlagEnabled(right)
    EndIfFlagEnabled(flag)
    SkipLinesIfPlayerNotInOwnWorld(1)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    EndIfFlagEnabled(dismissal_flag)
    IfPlayerInOwnWorld(AND_1)
    IfFlagDisabled(AND_1, right)
    IfFlagDisabled(AND_1, flag)
    IfFlagDisabled(AND_1, summon_flag)
    SkipLinesIfUnsignedEqual(1, left=0, right=right_1)
    IfFlagEnabled(AND_1, right_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region_1)
    IfFlagDisabled(AND_1, 9000)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(seconds)
    PlaceSummonSign(
        sign_type=sign_type,
        character=character,
        region=region,
        summon_flag=summon_flag,
        dismissal_flag=dismissal_flag,
        unknown=unknown,
    )
    Wait(1.0)
    Restart()
    EndIfValueEqual(left=0, right=right_2)


@NeverRestart(90005791)
def Event_90005791(_, flag: uint, flag_1: uint, flag_2: uint, character: uint):
    """Event 90005791"""
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_2)
    IfFlagEnabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableBackread(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Unknown102)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableAI(character)
    SetBackreadStateAlternate(character, True)
    IfFlagEnabled(AND_1, flag_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetBackreadStateAlternate(character, False)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Unknown102)


@RestartOnRest(90005792)
def Event_90005792(_, flag: uint, flag_1: uint, flag_2: uint, character: uint, item_lot_param_id: int, seconds: float):
    """Event 90005792"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterDrawGroupEnabled(AND_1, character=character)
    IfFlagEnabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(seconds)
    EnableFlag(flag)
    EndIfPlayerNotInOwnWorld()
    EndIfValueEqual(left=item_lot_param_id, right=0)
    AwardItemLot(item_lot_param_id, host_only=True)
    End()
    IfFlagEnabled(OR_1, flag_2)


@RestartOnRest(90005793)
def Event_90005793(
    _,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    character__unk_0_4: uint,
    other_entity: uint,
    region: uint,
    left: int,
):
    """Event 90005793"""
    EndIfFlagEnabled(flag)
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, flag)
    IfPlayerInOwnWorld(AND_2)
    IfFlagEnabled(AND_2, flag_1)
    IfHasAIStatus(
        AND_2,
        character__unk_0_4,
        ai_status=AIStatusType.Battle,
        target_comparison_type=ComparisonType.NotEqual,
    )
    SkipLinesIfUnsignedNotEqual(2, left=region, right=0)
    IfEntityBeyondDistance(AND_2, entity=PLAYER, other_entity=other_entity, radius=110.0)
    SkipLines(1)
    IfCharacterOutsideRegion(AND_2, character=PLAYER, region=region)
    IfPlayerInOwnWorld(AND_3)
    IfFlagEnabled(AND_3, flag_1)
    SkipLinesIfValueEqual(5, left=left, right=2)
    SkipLinesIfValueEqual(2, left=left, right=1)
    IfEntityBeyondDistance(AND_3, entity=PLAYER, other_entity=other_entity, radius=180.0)
    SkipLines(3)
    IfEntityBeyondDistance(AND_3, entity=PLAYER, other_entity=other_entity, radius=360.0)
    SkipLines(1)
    IfEntityBeyondDistance(AND_3, entity=PLAYER, other_entity=other_entity, radius=720.0)
    IfConditionTrue(OR_10, input_condition=AND_1)
    IfConditionTrue(OR_10, input_condition=AND_2)
    IfConditionTrue(OR_10, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_10)
    EndIfFlagEnabled(flag)
    Unknown_2003_79(unk_0_4=character__unk_0_4)
    End()
    IfFlagDisabled(OR_11, flag_2)


@RestartOnRest(90005795)
def Event_90005795(
    _,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
    message: int,
    action_button_id: int,
    obj: uint,
    model_point: int,
):
    """Event 90005795"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    DeleteObjectVFX(obj)
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag_2)
    IfPlayerInOwnWorld(AND_1)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateObjectVFX(obj, vfx_id=100, model_point=model_point)
    IfTryingToCreateSession(OR_2)
    IfTryingToJoinSession(OR_2)
    IfConditionTrue(OR_3, input_condition=OR_2)
    IfActionButtonParamActivated(OR_3, action_button_id=action_button_id, entity=obj)
    IfFlagDisabled(OR_3, flag_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    RestartIfFinishedConditionTrue(input_condition=OR_2)
    RestartIfFlagDisabled(flag_2)
    DisplayDialogAndSetFlags(
        message=message,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=obj,
        display_distance=2.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    RestartIfFlagDisabled(left_flag)
    EnableFlag(flag_1)
    AddSpecialEffect(PLAYER, 15)
    Wait(20.0)
    Restart()


@RestartOnRest(90005796)
def Event_90005796(_, flag: uint, character: uint, banner_type: uchar, entity_id: uint):
    """Event 90005796"""
    DisableNetworkSync()
    EndIfPlayerInOwnWorld()
    EndIfFlagEnabled(flag)
    IfCharacterDrawGroupEnabled(AND_1, character=character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayBanner(banner_type)
    SkipLinesIfUnsignedEqual(1, left=entity_id, right=0)
    Unknown_2003_77(entity_id=entity_id)
    Unknown_2003_74(unk_0_4=1)


@RestartOnRest(90005797)
def Event_90005797(_, flag: uint, character: uint, banner_type: uchar, entity_id: uint, special_effect_id: int):
    """Event 90005797"""
    DisableNetworkSync()
    EndIfPlayerInOwnWorld()
    EndIfFlagEnabled(flag)
    IfCharacterDrawGroupEnabled(AND_1, character=character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    DisplayBanner(banner_type)
    AddSpecialEffect(20000, special_effect_id)
    SkipLinesIfUnsignedEqual(1, left=entity_id, right=0)
    Unknown_2003_77(entity_id=entity_id)
    Unknown_2003_74(unk_0_4=1)


@RestartOnRest(9005800)
def Event_9005800(
    _,
    flag: uint,
    entity: uint,
    region: uint,
    flag_1: uint,
    character: uint,
    action_button_id: int,
    left: uint,
    region_1: uint,
):
    """Event 9005800"""
    GotoIfFlagEnabled(Label.L10, flag=flag)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=left, right=0)
    GotoIfFlagEnabled(Label.L0, flag=left)
    SkipLinesIfUnsignedEqual(1, left=region_1, right=0)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=region_1)
    IfFlagEnabled(OR_1, left)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    RestartIfFlagEnabled(flag)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    IfPlayerInOwnWorld(AND_3)
    IfFlagDisabled(AND_3, flag)
    IfActionButtonParamActivated(AND_3, action_button_id=action_button_id, entity=entity)
    IfFlagEnabled(OR_3, flag)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    RestartIfFlagEnabled(flag)
    UnknownSound_2010_11(unk_0_4=5.0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=PLAYER, special_effect=4250)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    SkipLines(1)
    RotateToFaceEntity(PLAYER, region, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    IfTimeElapsed(OR_4, seconds=3.0)
    IfCharacterInsideRegion(OR_5, character=PLAYER, region=region)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfConditionTrue(AND_4, input_condition=OR_5)
    IfPlayerInOwnWorld(AND_4)
    IfFlagDisabled(AND_4, flag)
    IfConditionTrue(OR_6, input_condition=AND_4)
    IfFlagEnabled(OR_6, flag)
    IfConditionTrue(MAIN, input_condition=OR_6)
    RestartIfFlagEnabled(flag)
    RestartIfFinishedConditionTrue(input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(flag_1)
    EndIfPlayerNotInOwnWorld()
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_10)
    IfFlagEnabled(AND_10, flag)
    IfFailedToCreateSession(OR_10)
    IfMultiplayerState(OR_10, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_10, input_condition=OR_10)
    IfActionButtonParamActivated(AND_10, action_button_id=10000, entity=entity)
    IfConditionTrue(MAIN, input_condition=AND_10)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@RestartOnRest(9005801)
def Event_9005801(_, flag: uint, entity: uint, region: uint, flag_1: uint, flag_2: uint, action_button_id: int):
    """Event 9005801"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfFlagDisabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    IfCharacterWhitePhantom(AND_1, PLAYER)
    IfActionButtonParamActivated(AND_1, action_button_id=action_button_id, entity=entity)
    IfConditionTrue(MAIN, input_condition=AND_1)
    UnknownSound_2010_11(unk_0_4=5.0)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    IfCharacterWhitePhantom(AND_2, PLAYER)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfTimeElapsed(OR_1, seconds=3.0)
    IfConditionTrue(OR_2, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_2)
    RestartIfFinishedConditionTrue(input_condition=OR_1)
    EnableFlag(flag_2)
    Restart()


@RestartOnRest(9005810)
def Event_9005810(_, flag: uint, grace_flag: uint, character: uint, obj: uint, unknown: float):
    """Event 9005810"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableObject(obj)
    Wait(1.0)
    IfFlagEnabled(MAIN, flag)
    CreateTemporaryVFX(vfx_id=1060, anchor_entity=obj, model_point=200, anchor_type=CoordEntityType.Object)
    Wait(0.5)
    EnableCharacter(character)
    EnableObject(obj)

    # --- Label 0 --- #
    DefineLabel(0)
    RegisterGrace(grace_flag=grace_flag, obj=obj, reaction_distance=5.0, reaction_angle=180.0, unknown=unknown)


@RestartOnRest(9005811)
def Event_9005811(_, flag: uint, obj: uint, model_point: int, right: uint):
    """Event 9005811"""
    DisableNetworkSync()
    DisableObject(obj)
    DeleteObjectVFX(obj)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown18)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagDisabled(AND_1, flag)
    IfCharacterWhitePhantom(OR_2, PLAYER)
    IfCharacterType(OR_2, PLAYER, character_type=CharacterType.Unknown17)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfFlagDisabled(AND_2, flag)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_3, right)
    IfFlagDisabled(AND_3, flag)
    IfFailedToCreateSession(OR_4)
    IfMultiplayerState(OR_4, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_4, input_condition=OR_4)
    IfFlagEnabled(AND_4, flag)
    IfCharacterWhitePhantom(AND_7, PLAYER)
    IfConditionFalse(AND_4, input_condition=AND_7)
    IfFailedToCreateSession(OR_5)
    IfMultiplayerState(OR_5, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_5, input_condition=OR_5)
    IfFlagEnabled(AND_5, flag)
    IfCharacterWhitePhantom(AND_5, PLAYER)
    IfEntityBeyondDistance(AND_5, entity=PLAYER, other_entity=obj, radius=1.0)
    IfConditionTrue(OR_8, input_condition=AND_1)
    IfConditionTrue(OR_8, input_condition=AND_2)
    IfConditionTrue(OR_8, input_condition=AND_3)
    IfConditionTrue(OR_8, input_condition=AND_4)
    IfConditionTrue(OR_8, input_condition=AND_5)
    IfConditionTrue(MAIN, input_condition=OR_8)
    EnableObject(obj)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=101, model_point=model_point)
    IfCharacterType(OR_11, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_11, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_11, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_11, PLAYER, character_type=CharacterType.Unknown18)
    IfConditionTrue(AND_11, input_condition=OR_11)
    IfFlagDisabled(AND_11, flag)
    IfCharacterWhitePhantom(OR_12, PLAYER)
    IfCharacterType(OR_12, PLAYER, character_type=CharacterType.Unknown17)
    IfConditionTrue(AND_12, input_condition=OR_12)
    IfFlagDisabled(AND_12, flag)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_13, right)
    IfFlagDisabled(AND_13, flag)
    IfFailedToCreateSession(OR_14)
    IfMultiplayerState(OR_14, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_14, input_condition=OR_14)
    IfFlagEnabled(AND_14, flag)
    IfCharacterWhitePhantom(OR_7, PLAYER)
    IfConditionFalse(AND_14, input_condition=OR_7)
    IfFailedToCreateSession(OR_15)
    IfMultiplayerState(OR_15, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_15, input_condition=OR_15)
    IfFlagEnabled(AND_15, flag)
    IfCharacterWhitePhantom(AND_15, PLAYER)
    IfEntityBeyondDistance(AND_15, entity=PLAYER, other_entity=obj, radius=1.0)
    IfConditionFalse(AND_9, input_condition=AND_11)
    IfConditionFalse(AND_9, input_condition=AND_12)
    IfConditionFalse(AND_9, input_condition=AND_13)
    IfConditionFalse(AND_9, input_condition=AND_14)
    IfConditionFalse(AND_9, input_condition=AND_15)
    IfConditionTrue(MAIN, input_condition=AND_9)
    Restart()


@RestartOnRest(9005812)
def Event_9005812(_, flag: uint, obj: uint, model_point: int, right: uint, model_point_1: int):
    """Event 9005812"""
    DisableNetworkSync()
    DisableObject(obj)
    DeleteObjectVFX(obj)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_1, right)
    IfFlagDisabled(AND_1, flag)
    IfCharacterWhitePhantom(OR_3, PLAYER)
    IfCharacterType(OR_3, PLAYER, character_type=CharacterType.Unknown17)
    IfConditionTrue(AND_3, input_condition=OR_3)
    IfCharacterType(OR_4, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_4, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_4, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_4, PLAYER, character_type=CharacterType.Unknown18)
    IfConditionTrue(AND_4, input_condition=OR_4)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(OR_5, input_condition=AND_3)
    IfConditionTrue(OR_5, input_condition=AND_4)
    IfConditionTrue(MAIN, input_condition=OR_5)
    EnableObject(obj)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=101, model_point=model_point)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_11, right)
    IfFlagDisabled(AND_11, flag)
    IfCharacterWhitePhantom(OR_13, PLAYER)
    IfCharacterType(OR_13, PLAYER, character_type=CharacterType.Unknown17)
    IfConditionTrue(AND_13, input_condition=OR_13)
    IfCharacterType(OR_14, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_14, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_14, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_14, PLAYER, character_type=CharacterType.Unknown18)
    IfConditionTrue(AND_14, input_condition=OR_14)
    IfConditionFalse(AND_15, input_condition=AND_11)
    IfConditionFalse(AND_15, input_condition=AND_13)
    IfConditionFalse(AND_15, input_condition=AND_14)
    IfConditionTrue(MAIN, input_condition=AND_15)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFailedToCreateSession(OR_2)
    IfMultiplayerState(OR_2, state=MultiplayerState.Unknown6)
    IfFlagEnabled(OR_3, 9982)
    IfConditionTrue(OR_5, input_condition=OR_2)
    IfConditionTrue(OR_5, input_condition=OR_3)
    IfConditionTrue(MAIN, input_condition=OR_5)
    IfFailedToCreateSession(OR_12)
    IfMultiplayerState(OR_12, state=MultiplayerState.Unknown6)
    IfFlagEnabled(OR_13, 9982)
    IfConditionFalse(AND_15, input_condition=OR_12)
    IfConditionFalse(AND_15, input_condition=OR_13)
    IfConditionTrue(MAIN, input_condition=AND_15)
    Restart()
    CreateObjectVFX(obj, vfx_id=101, model_point=model_point_1)


@RestartOnRest(9005813)
def Event_9005813(_, flag: uint, obj: uint, model_point: int, right: uint, model_point_1: int):
    """Event 9005813"""
    DisableNetworkSync()
    DisableObject(obj)
    DeleteObjectVFX(obj)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_1, right)
    IfFlagDisabled(AND_1, flag)
    IfCharacterWhitePhantom(OR_3, PLAYER)
    IfCharacterType(OR_3, PLAYER, character_type=CharacterType.Unknown17)
    IfConditionTrue(AND_3, input_condition=OR_3)
    IfCharacterType(OR_4, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_4, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_4, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_4, PLAYER, character_type=CharacterType.Unknown18)
    IfConditionTrue(AND_4, input_condition=OR_4)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(OR_5, input_condition=AND_3)
    IfConditionTrue(OR_5, input_condition=AND_4)
    IfConditionTrue(MAIN, input_condition=OR_5)
    EnableObject(obj)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=101, model_point=model_point)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_11, right)
    IfFlagDisabled(AND_11, flag)
    IfCharacterWhitePhantom(OR_13, PLAYER)
    IfCharacterType(OR_13, PLAYER, character_type=CharacterType.Unknown17)
    IfConditionTrue(AND_13, input_condition=OR_13)
    IfCharacterType(OR_14, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_14, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_14, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_14, PLAYER, character_type=CharacterType.Unknown18)
    IfConditionTrue(AND_14, input_condition=OR_14)
    IfConditionFalse(AND_15, input_condition=AND_11)
    IfConditionFalse(AND_15, input_condition=AND_13)
    IfConditionFalse(AND_15, input_condition=AND_14)
    IfConditionTrue(MAIN, input_condition=AND_15)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFailedToCreateSession(OR_2)
    IfMultiplayerState(OR_2, state=MultiplayerState.Unknown6)
    IfTryingToJoinSession(OR_2)
    IfTryingToCreateSession(OR_2)
    IfConditionTrue(OR_5, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_5)
    EnableObject(obj)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=101, model_point=model_point_1)
    IfFailedToCreateSession(OR_12)
    IfMultiplayerState(OR_12, state=MultiplayerState.Unknown6)
    IfTryingToCreateSession(OR_12)
    IfTryingToJoinSession(OR_12)
    IfConditionFalse(AND_15, input_condition=OR_12)
    IfConditionTrue(MAIN, input_condition=AND_15)
    Restart()


@RestartOnRest(9005822)
def Event_9005822(
    _,
    flag: uint,
    unk_0_4: int,
    flag_1: uint,
    flag_2: uint,
    right: uint,
    flag_3: uint,
    left: int,
    left_1: int,
):
    """Event 9005822"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableFlag(flag_1)
    IfFlagEnabled(AND_1, flag_1)
    SkipLinesIfPlayerInOwnWorld(1)
    IfFlagEnabled(AND_1, flag_2)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_1, right)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFrames(frames=1)
    SkipLinesIfFlagEnabled(1, flag_3)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=0)
    IfFlagEnabled(OR_2, flag_3)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    WaitFrames(frames=1)
    SkipLinesIfValueEqual(0, left=left, right=0)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=1)
    IfFlagEnabled(OR_3, flag)
    IfConditionTrue(MAIN, input_condition=OR_3)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfValueEqual(2, left=left_1, right=1)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=-1)
    End()
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=-2)


@RestartOnRest(9005823)
def Event_9005823(
    _,
    flag: uint,
    unk_0_4: int,
    flag_1: uint,
    flag_2: uint,
    right: uint,
    flag_3: uint,
    flag_4: uint,
    left: int,
    left_1: int,
):
    """Event 9005823"""
    DisableNetworkSync()
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableFlag(flag_1)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(AND_1, flag_1)
    SkipLinesIfPlayerInOwnWorld(1)
    IfFlagEnabled(AND_1, flag_2)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_1, right)
    IfConditionTrue(MAIN, input_condition=AND_1)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=0)
    IfFlagEnabled(OR_2, flag_3)
    IfFlagEnabled(OR_2, flag_4)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    GotoIfFlagEnabled(Label.L2, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_4)
    WaitFrames(frames=1)
    SkipLinesIfValueEqual(0, left=left, right=1)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=1)
    IfFlagEnabled(OR_2, flag_4)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    GotoIfFlagEnabled(Label.L2, flag=flag)

    # --- Label 1 --- #
    DefineLabel(1)
    UnknownSound_2010_8(sound_id=90003003)
    IfFlagEnabled(OR_3, flag)
    IfConditionTrue(MAIN, input_condition=OR_3)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfValueEqual(2, left=left_1, right=1)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=-1)
    End()
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=-2)


@RestartOnRest(90005830)
def Event_90005830(_, flag: uint, region: uint):
    """Event 90005830"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(OR_1, flag)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    RestartIfFlagEnabled(flag)
    AddSpecialEffect(PLAYER, 4250)
    Wait(3.0)
    Restart()


@RestartOnRest(9005840)
def Event_9005840(_, flag: uint, left: uint, character: uint):
    """Event 9005840"""
    EndIfFlagEnabled(flag)
    IfHealthValueLessThanOrEqual(MAIN, character, value=0)
    Wait(4.0)
    PlaySoundEffect(character, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, character)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.HollowArenaLoss)
    EnableFlag(flag)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    EnableFlag(left)


@RestartOnRest(9005845)
def Event_9005845(_, flag: uint, character: uint):
    """Event 9005845"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    GotoIfFlagEnabled(Label.L1, flag=11000801)
    IfPlayerInOwnWorld(AND_1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=11000800, radius=20.0)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(11000801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 11002805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=11002800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(11005800)
    SetNetworkUpdateRate(11005800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(11000800)


@RestartOnRest(90005860)
def Event_90005860(
    _,
    flag: uint,
    left: uint,
    character: uint,
    left_1: uint,
    item_lot__item_lot_param_id: int,
    seconds: float,
):
    """Event 90005860"""
    SkipLinesIfValueEqual(1, left=item_lot__item_lot_param_id, right=0)
    Unknown_2004_76(flag=flag, item_lot=item_lot__item_lot_param_id)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    EndIfPlayerNotInOwnWorld()
    EndIfValueEqual(left=item_lot__item_lot_param_id, right=0)
    Wait(1.0)
    AwardItemLot(item_lot__item_lot_param_id, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfHealthValueLessThanOrEqual(MAIN, character, value=0)
    Wait(2.0)
    PlaySoundEffect(character, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, character)
    SkipLinesIfUnsignedEqual(6, left=left_1, right=3)
    SkipLinesIfUnsignedEqual(4, left=left_1, right=2)
    SkipLinesIfUnsignedEqual(2, left=left_1, right=1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.DutyFulfilled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.Unknown)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.HollowArenaLoss)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.HollowArenaWin)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    EnableFlag(left)
    EndIfPlayerNotInOwnWorld()
    EndIfValueEqual(left=item_lot__item_lot_param_id, right=0)
    Wait(5.0)
    AwardItemLot(item_lot__item_lot_param_id, host_only=True)
    End()
    Wait(seconds)


@RestartOnRest(90005861)
def Event_90005861(
    _,
    flag: uint,
    left: uint,
    character: uint,
    left_1: uint,
    item_lot__item_lot_param_id: int,
    text: int,
    seconds: float,
):
    """Event 90005861"""
    SkipLinesIfValueEqual(1, left=item_lot__item_lot_param_id, right=0)
    Unknown_2004_76(flag=flag, item_lot=item_lot__item_lot_param_id)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    EndIfPlayerNotInOwnWorld()
    EndIfValueEqual(left=item_lot__item_lot_param_id, right=0)
    Wait(1.0)
    AwardItemLot(item_lot__item_lot_param_id, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfHealthValueLessThanOrEqual(MAIN, character, value=0)
    Wait(2.0)
    PlaySoundEffect(character, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, character)
    SkipLinesIfUnsignedEqual(6, left=left_1, right=3)
    SkipLinesIfUnsignedEqual(4, left=left_1, right=2)
    SkipLinesIfUnsignedEqual(2, left=left_1, right=1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.DutyFulfilled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.Unknown)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.HollowArenaLoss)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.HollowArenaWin)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    EnableFlag(left)
    EndIfPlayerNotInOwnWorld()
    EndIfValueEqual(left=item_lot__item_lot_param_id, right=0)
    Wait(5.0)
    AwardItemLot(item_lot__item_lot_param_id, host_only=True)
    Wait(2.0)
    DisplayBattlefieldMessage(text)
    End()
    Wait(seconds)


@NeverRestart(90005870)
def Event_90005870(_, character: uint, name: int, unk_4_8: uint):
    """Event 90005870"""
    DisableNetworkSync()
    IfHasAIStatus(AND_1, character, ai_status=AIStatusType.Battle)
    IfUnknownCondition_33(AND_1, unk_4_8=unk_4_8, unk_8_9=True)
    IfFlagDisabled(AND_1, 9000)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfFlagDisabled(Label.L0, flag=9290)
    GotoIfFlagDisabled(Label.L1, flag=9291)
    Wait(5.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(9290)
    Wait(1.0)
    EnableBossHealthBar(character, name=name)
    SkipLinesIfPlayerNotInOwnWorld(2)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Unknown102)
    IfHasAIStatus(AND_2, character, ai_status=AIStatusType.Battle)
    IfUnknownCondition_33(AND_2, unk_4_8=unk_4_8, unk_8_9=True)
    IfConditionFalse(OR_2, input_condition=AND_2)
    IfCharacterDead(OR_2, character)
    IfFlagEnabled(OR_2, 9000)
    IfConditionTrue(MAIN, input_condition=OR_2)
    IfCharacterDead(OR_3, character)
    SkipLinesIfConditionFalse(2, OR_3)
    Wait(3.0)
    SkipLines(2)
    SkipLinesIfFlagEnabled(1, 9000)
    Wait(1.0)
    DisableBossHealthBar(character, name=name)
    SkipLinesIfPlayerNotInOwnWorld(2)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Unknown102)
    DisableFlag(9290)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(9291)
    Wait(1.0)
    EnableBossHealthBar(character, name=name, bar_slot=1)
    SkipLinesIfPlayerNotInOwnWorld(2)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Unknown102)
    IfHasAIStatus(AND_12, character, ai_status=AIStatusType.Battle)
    IfUnknownCondition_33(AND_12, unk_4_8=unk_4_8, unk_8_9=True)
    IfConditionFalse(OR_12, input_condition=AND_12)
    IfCharacterDead(OR_12, character)
    IfFlagEnabled(OR_12, 9000)
    IfConditionTrue(MAIN, input_condition=OR_12)
    IfCharacterDead(OR_13, character)
    SkipLinesIfConditionFalse(2, OR_13)
    Wait(3.0)
    SkipLines(2)
    SkipLinesIfFlagEnabled(1, 9000)
    Wait(1.0)
    DisableBossHealthBar(character, name=name, bar_slot=1)
    SkipLinesIfPlayerNotInOwnWorld(2)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Unknown102)
    DisableFlag(9291)
    Restart()


@NeverRestart(90005871)
def Event_90005871(_, character: uint, name: int, unk_4_8: uint, character_1: uint):
    """Event 90005871"""
    DisableNetworkSync()
    IfHasAIStatus(AND_1, character, ai_status=AIStatusType.Battle)
    IfUnknownCondition_33(AND_1, unk_4_8=unk_4_8, unk_8_9=True)
    IfFlagDisabled(AND_1, 9000)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfFlagDisabled(Label.L0, flag=9290)
    GotoIfFlagDisabled(Label.L1, flag=9291)
    Wait(5.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(9290)
    Wait(1.0)
    EnableBossHealthBar(character, name=name)
    SkipLinesIfPlayerNotInOwnWorld(4)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Unknown102)
    SetNetworkUpdateAuthority(character_1, authority_level=UpdateAuthority.Unknown8192)
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Unknown102)
    IfHasAIStatus(AND_2, character, ai_status=AIStatusType.Battle)
    IfUnknownCondition_33(AND_2, unk_4_8=unk_4_8, unk_8_9=True)
    IfConditionFalse(OR_2, input_condition=AND_2)
    IfCharacterDead(OR_2, character)
    IfFlagEnabled(OR_2, 9000)
    IfConditionTrue(MAIN, input_condition=OR_2)
    IfCharacterDead(OR_3, character)
    SkipLinesIfConditionFalse(2, OR_3)
    Wait(3.0)
    SkipLines(2)
    SkipLinesIfFlagEnabled(1, 9000)
    Wait(1.0)
    DisableBossHealthBar(character, name=name)
    SkipLinesIfPlayerNotInOwnWorld(4)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Unknown102)
    SetNetworkUpdateAuthority(character_1, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateRate(character_1, is_fixed=False, update_rate=CharacterUpdateRate.Unknown102)
    DisableFlag(9290)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(9291)
    Wait(1.0)
    EnableBossHealthBar(character, name=name, bar_slot=1)
    SkipLinesIfPlayerNotInOwnWorld(4)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Unknown102)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Unknown102)
    IfHasAIStatus(AND_12, character, ai_status=AIStatusType.Battle)
    IfUnknownCondition_33(AND_12, unk_4_8=unk_4_8, unk_8_9=True)
    IfConditionFalse(OR_12, input_condition=AND_12)
    IfCharacterDead(OR_12, character)
    IfFlagEnabled(OR_12, 9000)
    IfConditionTrue(MAIN, input_condition=OR_12)
    IfCharacterDead(OR_13, character)
    SkipLinesIfConditionFalse(2, OR_13)
    Wait(3.0)
    SkipLines(2)
    SkipLinesIfFlagEnabled(1, 9000)
    Wait(1.0)
    DisableBossHealthBar(character, name=name, bar_slot=1)
    SkipLinesIfPlayerNotInOwnWorld(4)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Unknown102)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Unknown102)
    DisableFlag(9291)
    Restart()


@NeverRestart(90005872)
def Event_90005872(_, character: uint, entity_id__unk_4_8: uint, right: uint):
    """Event 90005872"""
    DisableNetworkSync()
    SkipLinesIfUnsignedEqual(2, left=0, right=right)
    IfFlagEnabled(AND_1, right)
    SkipLines(1)
    IfHealthLessThanOrEqual(AND_1, character, value=0.550000011920929)
    IfUnknownCondition_33(AND_1, unk_4_8=entity_id__unk_4_8, unk_8_9=True)
    IfConditionTrue(MAIN, input_condition=AND_1)
    UnknownSound_2010_12(entity_id=entity_id__unk_4_8, unk_4_8=1)
    IfCharacterDead(OR_2, character)
    IfUnknownCondition_33(OR_2, unk_4_8=entity_id__unk_4_8, unk_8_9=False)
    IfConditionTrue(MAIN, input_condition=OR_2)
    UnknownSound_2010_12(entity_id=entity_id__unk_4_8, unk_4_8=0)
    Wait(0.30000001192092896)
    Restart()


@RestartOnRest(90005880)
def Event_90005880(
    _,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    character: uint,
    item_lot_param_id: int,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
):
    """Event 90005880"""
    EndIfFlagEnabled(flag)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(flag_1)
    IfCharacterDead(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(3.0)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.DutyFulfilled)
    UnknownMap_12(unk_0_4=10.0)
    AwardItemLot(item_lot_param_id, host_only=True)
    EnableNetworkFlag(flag)
    Wait(5.0)
    AddSpecialEffect(20000, 8870)
    Wait(2.0)
    EnableFlag(flag_2)
    EnableFlag(9295)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)
    End()


@RestartOnRest(90005881)
def Event_90005881(
    _,
    flag: uint,
    flag_1: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
    message: int,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start__region: uint,
):
    """Event 90005881"""
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_1)
    IfTryingToJoinSession(AND_2)
    IfConditionFalse(AND_1, input_condition=AND_2)
    IfLeavingSession(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9230, entity=anchor_entity)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialogAndSetFlags(
        message=message,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=anchor_entity,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    RestartIfFlagEnabled(cancel_flag__right_flag)
    IfTryingToCreateSession(OR_3)
    IfTryingToJoinSession(OR_3)
    RestartIfConditionTrue(input_condition=OR_3)
    EnableNetworkFlag(flag_1)
    AddSpecialEffect(PLAYER, 514)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 60450, unknown2=1.0)
    Wait(1.5)
    Unknown_2004_74(
        character=PLAYER,
        unknown1=1,
        region=player_start__region,
        unknown2=-1,
        character_2=PLAYER,
        unknown3=1,
        unknown4=1,
    )
    EnableFlag(9021)
    End()
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start__region)


@RestartOnRest(90005882)
def Event_90005882(
    _,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    character: uint,
    flag_3: uint,
    character_1: uint,
    obj: uint,
    owner_entity: uint,
    source_entity: uint,
    name: int,
    animation_id: int,
    animation_id_1: int,
):
    """Event 90005882"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    DisableObject(obj)
    EndIfFlagDisabled(flag_1)
    EndIfPlayerNotInOwnWorld()
    WaitFrames(frames=1)
    EnableFlag(1099002100)
    EnableFlag(flag_2)
    AddSpecialEffect(PLAYER, 190)
    UnknownMap_11(unk_0_4=0, unk_4_8=0.0)
    Unknown_2003_68(unknown1=7, unknown2=-1.0, unknown3=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=100,
        behavior_id=100500,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableAI(character_1)
    SkipLinesIfValueEqual(2, left=-1, right=animation_id)
    ForceAnimation(character, animation_id, unknown2=1.0)
    SkipLines(2)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableHealthBar(character)
    DisableNetworkFlag(flag_1)
    AddSpecialEffect(PLAYER, 514)
    EnableObject(obj)
    CreateObjectVFX(obj, vfx_id=200, model_point=806700)
    ForceAnimation(PLAYER, 60451, unknown2=1.0)
    Wait(1.0)
    AddSpecialEffect(20000, 8870)
    IfEntityBeyondDistance(OR_1, entity=PLAYER, other_entity=obj, radius=12.0)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=PLAYER)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableFlag(1099002100)
    SkipLinesIfValueNotEqual(2, left=-1, right=animation_id)
    EnableCharacter(character)
    EnableAnimations(character)
    SkipLinesIfValueEqual(1, left=-1, right=animation_id_1)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    EnableAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableFlag(flag_3)
    Wait(1.0)
    EnableBossHealthBar(character, name=name)


@RestartOnRest(90005883)
def Event_90005883(_, flag: uint, flag_1: uint, entity: uint):
    """Event 90005883"""
    ForceAnimation(entity, 0, loop=True, unknown2=1.0)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    ForceAnimation(entity, 10, loop=True, unknown2=1.0)
    EndIfFlagEnabled(flag_1)
    IfLeavingSession(AND_1)
    IfTryingToJoinSession(AND_2)
    IfConditionFalse(AND_1, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFrames(frames=1)
    ForceAnimation(entity, 1, loop=True, unknown2=1.0)
    IfLeavingSession(AND_11)
    IfTryingToJoinSession(AND_12)
    IfConditionFalse(AND_11, input_condition=AND_12)
    IfConditionFalse(MAIN, input_condition=AND_11)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(90005884)
def Event_90005884(_, flag: uint, flag_1: uint, character: uint, obj: uint):
    """Event 90005884"""
    AddSpecialEffect(character, 9531)
    DisableAI(character)
    DisableAnimations(character)
    DisableObject(obj)
    EndIfFlagDisabled(flag)
    EndIfFlagDisabled(flag_1)
    EndIfPlayerNotInOwnWorld()
    WaitFrames(frames=1)
    AddSpecialEffect(character, 9532)
    EnableAnimations(character)
    EnableObject(obj)


@RestartOnRest(90005885)
def Event_90005885(_, flag: uint, unk_0_4: int, flag_1: uint, flag_2: uint, left: int, left_1: int):
    """Event 90005885"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFrames(frames=1)
    SkipLinesIfValueEqual(2, left=0, right=unk_0_4)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=0)
    SkipLines(1)
    UnknownSound_2010_10(unk_0_4=921100, unk_4_8=0)
    IfFlagEnabled(OR_2, flag_2)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    WaitFrames(frames=1)
    SkipLinesIfValueEqual(4, left=left, right=1)
    SkipLinesIfValueEqual(2, left=0, right=unk_0_4)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=1)
    SkipLines(1)
    UnknownSound_2010_10(unk_0_4=925000, unk_4_8=1)
    IfFlagEnabled(OR_3, flag)
    IfConditionTrue(MAIN, input_condition=OR_3)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfValueEqual(5, left=left_1, right=1)
    SkipLinesIfValueEqual(2, left=0, right=unk_0_4)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=-1)
    SkipLines(1)
    UnknownSound_2010_10(unk_0_4=925000, unk_4_8=-1)
    End()
    SkipLinesIfValueEqual(2, left=0, right=unk_0_4)
    UnknownSound_2010_10(unk_0_4=unk_0_4, unk_4_8=-2)
    SkipLines(1)
    UnknownSound_2010_10(unk_0_4=925000, unk_4_8=-2)


@RestartOnRest(91005600)
def Event_91005600(_, flag: uint, obj: uint, model_point: int):
    """Event 91005600"""
    DisableNetworkSync()
    DisableObject(obj)
    DeleteObjectVFX(obj)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfFailedToCreateSession(OR_1)
    IfMultiplayerState(OR_1, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_4, input_condition=AND_1)
    IfFlagEnabled(OR_4, 9982)
    IfConditionTrue(MAIN, input_condition=OR_4)
    EnableObject(obj)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=101, model_point=model_point)
    IfTryingToCreateSession(OR_5)
    IfTryingToJoinSession(OR_5)
    IfFailedToCreateSession(OR_5)
    IfMultiplayerState(OR_5, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_5, input_condition=OR_5)
    IfConditionFalse(AND_8, input_condition=AND_5)
    IfFlagDisabled(AND_8, 9982)
    IfConditionTrue(MAIN, input_condition=AND_8)
    Restart()
    IfFlagEnabled(MAIN, flag)


@RestartOnRest(90005100)
def Event_90005100(
    _,
    flag: uint,
    flag_1: uint,
    obj: uint,
    source_flag: uint,
    value: uint,
    flag_2: uint,
    flag_3: uint,
    flag_4: uint,
    flag_5: uint,
    flag_6: uint,
    flag_7: uint,
    flag_8: uint,
    flag_9: uint,
    flag_10: uint,
    flag_11: uint,
):
    """Event 90005100"""
    SkipLinesIfFlagEnabled(2, 9000)
    DeleteObjectVFX(obj, erase_root=False)
    WaitFrames(frames=1)
    DeleteObjectVFX(obj)
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, 9000)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    CreateObjectVFX(obj, vfx_id=100, model_point=6400)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=0)
    EnableFlag(flag_2)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=1)
    EnableFlag(flag_3)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=2)
    EnableFlag(flag_4)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=3)
    EnableFlag(flag_5)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=4)
    EnableFlag(flag_6)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=5)
    EnableFlag(flag_7)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=6)
    EnableFlag(flag_8)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=7)
    EnableFlag(flag_9)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=8)
    EnableFlag(flag_10)
    Goto(Label.L6)
    EnableFlag(flag_11)
    Goto(Label.L6)

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfPlayerNotInOwnWorld(Label.L5)
    GotoIfFlagEnabled(Label.L5, flag=69080)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 100680)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableFlag(710510)
    DisplayTutorialMessage(tutorial_param_id=1510, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9108, flag=710510, bit_count=1)
    EnableFlag(69080)

    # --- Label 5 --- #
    DefineLabel(5)
    End()
    DeleteObjectVFX(obj, erase_root=False)
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagDisabled(Label.L3, flag=flag)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    DisableFlag(flag_4)
    DisableFlag(flag_5)
    DisableFlag(flag_6)
    DisableFlag(flag_7)
    DisableFlag(flag_8)
    DisableFlag(flag_9)
    DisableFlag(flag_10)
    DisableFlag(flag_11)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    IfEventValueGreaterThan(AND_10, flag=source_flag, bit_count=4, value=value)
    EndIfConditionTrue(input_condition=AND_10)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, 9000)
    IfFlagEnabled(OR_1, flag)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    IfEventValueGreaterThan(AND_11, flag=source_flag, bit_count=4, value=value)
    RestartIfConditionTrue(input_condition=AND_11)
    CreateObjectVFX(obj, vfx_id=100, model_point=6400)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=0)
    EnableFlag(flag_2)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=0,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_2)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=1)
    EnableFlag(flag_3)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=1,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_3)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=2)
    EnableFlag(flag_4)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_4)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=3)
    EnableFlag(flag_5)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_5)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=4)
    EnableFlag(flag_6)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=4,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_6)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=5)
    EnableFlag(flag_7)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=5,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_7)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=6)
    EnableFlag(flag_7)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=6,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_7)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=7)
    EnableFlag(flag_7)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=7,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_7)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=8)
    EnableFlag(flag_7)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=8,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_7)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=9)
    EnableFlag(flag_7)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=9,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_7)
    IfEventValueNotEqual(OR_2, flag=source_flag, bit_count=4, value=value)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(90005101)
def Event_90005101(
    _,
    flag: uint,
    flag_1: uint,
    obj: uint,
    source_flag: uint,
    value: uint,
    flag_2: uint,
    flag_3: uint,
    flag_4: uint,
    flag_5: uint,
    flag_6: uint,
    flag_7: uint,
    flag_8: uint,
    flag_9: uint,
    flag_10: uint,
    flag_11: uint,
):
    """Event 90005101"""
    SkipLinesIfFlagEnabled(2, 9000)
    DeleteObjectVFX(obj, erase_root=False)
    WaitFrames(frames=1)
    DeleteObjectVFX(obj)
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, 9000)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    CreateObjectVFX(obj, vfx_id=100, model_point=6401)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=0)
    EnableFlag(flag_2)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=1)
    EnableFlag(flag_3)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=2)
    EnableFlag(flag_4)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=3)
    EnableFlag(flag_5)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=4)
    EnableFlag(flag_6)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=5)
    EnableFlag(flag_7)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=6)
    EnableFlag(flag_8)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=7)
    EnableFlag(flag_9)
    Goto(Label.L6)
    SkipLinesIfUnsignedNotEqual(2, left=value, right=8)
    EnableFlag(flag_10)
    Goto(Label.L6)
    EnableFlag(flag_11)
    Goto(Label.L6)

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfPlayerNotInOwnWorld(Label.L5)
    GotoIfFlagEnabled(Label.L5, flag=710510)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, PLAYER, 100680)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableFlag(710510)
    DisplayTutorialMessage(tutorial_param_id=1510, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9108, flag=710510, bit_count=1)

    # --- Label 5 --- #
    DefineLabel(5)
    End()
    DeleteObjectVFX(obj, erase_root=False)
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagDisabled(Label.L3, flag=flag)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    DisableFlag(flag_4)
    DisableFlag(flag_5)
    DisableFlag(flag_6)
    DisableFlag(flag_7)
    DisableFlag(flag_8)
    DisableFlag(flag_9)
    DisableFlag(flag_10)
    DisableFlag(flag_11)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    IfEventValueGreaterThan(AND_10, flag=source_flag, bit_count=4, value=value)
    EndIfConditionTrue(input_condition=AND_10)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, 9000)
    IfFlagEnabled(OR_1, flag)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    IfEventValueGreaterThan(AND_11, flag=source_flag, bit_count=4, value=value)
    RestartIfConditionTrue(input_condition=AND_11)
    CreateObjectVFX(obj, vfx_id=100, model_point=6401)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=0)
    EnableFlag(flag_2)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=0,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_2)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=1)
    EnableFlag(flag_3)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=1,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_3)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=2)
    EnableFlag(flag_4)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_4)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=3)
    EnableFlag(flag_5)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_5)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=4)
    EnableFlag(flag_6)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=4,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_6)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=5)
    EnableFlag(flag_7)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=5,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_7)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=6)
    EnableFlag(flag_7)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=6,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_7)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=7)
    EnableFlag(flag_7)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=7,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_7)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=8)
    EnableFlag(flag_7)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=8,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_7)
    SkipLinesIfUnsignedNotEqual(3, left=value, right=9)
    EnableFlag(flag_7)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=4,
        operand=9,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Assign,
    )
    SkipLines(1)
    DisableFlag(flag_7)
    IfEventValueNotEqual(OR_2, flag=source_flag, bit_count=4, value=value)
    IfFlagEnabled(OR_2, flag)
    IfConditionTrue(MAIN, input_condition=OR_2)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(90005110)
def Event_90005110(
    _,
    flag: uint,
    flag_1: uint,
    obj: uint,
    item_lot_param_id: int,
    item: int,
    model_point: int,
    action_button_id: int,
    animation_id: int,
    left: int,
):
    """Event 90005110"""
    EndIfFlagEnabled(flag)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(flag_1)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=100, model_point=model_point)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=action_button_id, entity=obj)
    IfConditionTrue(MAIN, input_condition=AND_1)
    RotateToFaceEntity(PLAYER, obj, wait_for_completion=True)
    ForceAnimation(PLAYER, animation_id, unknown2=1.0)
    DeleteObjectVFX(obj)
    Wait(4.0)
    DisplayBanner(BannerType.Unknown26)
    AwardItemLot(item_lot_param_id, host_only=True)
    RemoveGoodFromPlayer(item=item, quantity=1)
    EnableFlag(flag)
    End()
    EndIfValueEqual(left=left, right=0)


@RestartOnRest(9005910)
def Event_9005910(_, obj: uint, first_flag: uint, last_flag: uint, right: int):
    """Event 9005910"""
    DeleteObjectVFX(obj)
    IfFlagRangeAllDisabled(AND_1, flag_range=(first_flag, last_flag))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    IfFlagRangeAllEnabled(AND_2, flag_range=(first_flag, last_flag))
    GotoIfConditionFalse(Label.L2, input_condition=AND_2)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfValueLessThan(2, left=3, right=right)
    CreateObjectVFX(obj, vfx_id=201, model_point=62)
    SkipLines(1)
    CreateObjectVFX(obj, vfx_id=201, model_point=63)
    IfFlagRangeAnyEnabled(MAIN, flag_range=(first_flag, last_flag))
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    CreateObjectVFX(obj, vfx_id=201, model_point=61)
    IfFlagRangeAllEnabled(MAIN, flag_range=(first_flag, last_flag))
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    DeleteObjectVFX(obj)
    End()


@RestartOnRest(9005911)
def Event_9005911(_, obj: uint):
    """Event 9005911"""
    CreateObjectVFX(obj, vfx_id=201, model_point=40)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=obj, radius=3.0)
    DeleteObjectVFX(obj)


@RestartOnRest(9005912)
def Event_9005912(_, flag: uint, text: int):
    """Event 9005912"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(MAIN, flag)
    DisplayUnknownMessage_13(text=text)


@RestartOnRest(9005920)
def Event_9005920(
    _,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
    character_5: uint,
    character_6: uint,
    character_7: uint,
    character_8: uint,
    character_9: uint,
):
    """Event 9005920"""
    SkipLinesIfFlagEnabled(3, 9800)
    DisableCharacter(character)
    DisableAnimations(character)
    SkipLines(2)
    EnableCharacter(character)
    EnableAnimations(character)
    SkipLinesIfFlagEnabled(3, 9801)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    SkipLines(2)
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    SkipLinesIfFlagEnabled(3, 9802)
    DisableCharacter(character_2)
    DisableAnimations(character_2)
    SkipLines(2)
    EnableCharacter(character_2)
    EnableAnimations(character_2)
    SkipLinesIfFlagEnabled(3, 9803)
    DisableCharacter(character_3)
    DisableAnimations(character_3)
    SkipLines(2)
    EnableCharacter(character_3)
    EnableAnimations(character_3)
    SkipLinesIfFlagEnabled(3, 9804)
    DisableCharacter(character_4)
    DisableAnimations(character_4)
    SkipLines(2)
    EnableCharacter(character_4)
    EnableAnimations(character_4)
    SkipLinesIfFlagEnabled(3, 9805)
    DisableCharacter(character_5)
    DisableAnimations(character_5)
    SkipLines(2)
    EnableCharacter(character_5)
    EnableAnimations(character_5)
    SkipLinesIfFlagEnabled(3, 9806)
    DisableCharacter(character_6)
    DisableAnimations(character_6)
    SkipLines(2)
    EnableCharacter(character_6)
    EnableAnimations(character_6)
    SkipLinesIfFlagEnabled(3, 9807)
    DisableCharacter(character_7)
    DisableAnimations(character_7)
    SkipLines(2)
    EnableCharacter(character_7)
    EnableAnimations(character_7)
    SkipLinesIfFlagEnabled(3, 9808)
    DisableCharacter(character_8)
    DisableAnimations(character_8)
    SkipLines(2)
    EnableCharacter(character_8)
    EnableAnimations(character_8)
    SkipLinesIfFlagEnabled(3, 9809)
    DisableCharacter(character_9)
    DisableAnimations(character_9)
    SkipLines(2)
    EnableCharacter(character_9)
    EnableAnimations(character_9)


@RestartOnRest(90005920)
def Event_90005920(_, flag: uint, obj: uint, obj_act_id: uint):
    """Event 90005920"""
    EndIfFlagEnabled(flag)
    CreateObjectVFX(obj, vfx_id=100, model_point=6150)
    IfObjectActivated(AND_1, obj_act_id=obj_act_id)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    Wait(0.30000001192092896)
    DeleteObjectVFX(obj)


@RestartOnRest(9005990)
def Event_9005990(_, seconds: float):
    """Event 9005990"""
    Wait(seconds)
