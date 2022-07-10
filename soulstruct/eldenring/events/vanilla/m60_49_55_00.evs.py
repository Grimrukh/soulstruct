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
    RegisterGrace(grace_flag=1049550000, obj=1049551950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76652, 76651, 1049551980, 77520, 1, 78520, 78521, 78522, 78523, 78524, 78525, 78526, 78527, 78528, 78529),
        arg_types="IIIIIIIIIIIIIII",
    )
    Event_1049552210(0, character=1049550205)
    Event_1049552210(1, character=1049550210)
    Event_1049552210(2, character=1049550211)
    Event_1049552200(0, attacker__character=1049555200, region=1049552200)
    Event_1049552500()
    Event_1049552550(0, character=1049550209, obj=1049551550)
    Event_1049552550(1, character=1049550203, obj=1049551551)
    Event_1049552550(2, character=1049550221, obj=1049551552)
    RunCommonEvent(0, 90005683, args=(62512, 1049551600, 211, 78594, 0), arg_types="IIiII")
    Event_1049552400(
        0,
        flag=1049550405,
        flag_1=1049552405,
        anchor_entity=1049550400,
        character=1049550410,
        left=1,
        item_lot_param_id=1049550700
    )
    Event_1049552401(0, flag=1049550405, flag_1=1049552405, character=1049550400, character_1=1049550410, left=1)
    Event_1049552410(0, character=1049550400)
    Event_1049552420(0, 1049550222, 30000, 20000, 0, 0.800000011920929, 0.0, 0, 0, 0, 0)
    RunCommonEvent(0, 90005706, args=(1049550710, 930023, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1049550700)
    DisableBackread(1049550710)


@RestartOnRest(1049552200)
def Event_1049552200(_, attacker__character: uint, region: uint):
    """Event 1049552200"""
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5650)
    AddSpecialEffect(attacker__character, 4802)
    EndIfFlagEnabled(1049552200)
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5650)
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
    EnableNetworkFlag(1049552200)
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5650)


@RestartOnRest(1049552210)
def Event_1049552210(_, character: uint):
    """Event 1049552210"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    DisableAI(character)
    ForceAnimation(character, 30012, loop=True, unknown2=1.0)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=260, unk_12_16=1)
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
    IfConditionTrue(OR_1, input_condition=AND_4)
    IfConditionTrue(OR_1, input_condition=AND_5)
    IfConditionTrue(OR_1, input_condition=AND_6)
    IfConditionTrue(OR_1, input_condition=AND_7)
    IfConditionTrue(OR_1, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    EnableAI(character)


@RestartOnRest(1049552400)
def Event_1049552400(
    _,
    flag: uint,
    flag_1: uint,
    anchor_entity: uint,
    character: uint,
    left: int,
    item_lot_param_id: int,
):
    """Event 1049552400"""
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
    AddSpecialEffect(character, 4305)
    Wait(3.0)
    DisableCharacter(character)
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfValueEqual(1, left=item_lot_param_id, right=0)
    AwardItemLot(item_lot_param_id, host_only=True)
    EnableNetworkFlag(flag)


@RestartOnRest(1049552401)
def Event_1049552401(_, flag: uint, flag_1: uint, character: uint, character_1: uint, left: int):
    """Event 1049552401"""
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
    Wait(0.800000011920929)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=character,
    )
    Wait(0.5)
    AddSpecialEffect(character, 4305)
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
    TriggerAISound(ai_sound_param_id=6410, anchor_entity=1049552400, unk_8_12=1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(flag_1)


@RestartOnRest(1049552410)
def Event_1049552410(_, character: uint):
    """Event 1049552410"""
    EndIfFlagEnabled(1049540405)
    DisableGravity(character)
    DisableAI(character)
    ForceAnimation(character, 30006, loop=True, unknown2=1.0)


@RestartOnRest(1049552420)
def Event_1049552420(
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
    """Event 1049552420"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    EndIfFlagEnabled(1049550405)
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
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(OR_2, attacked_entity=1049550400, attacker=0)
    IfUnknownCharacterCondition_34(OR_3, character=1049550400, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_3, character=1049550400, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_3, character=1049550400, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_3, character=1049550400, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_3, character=1049550400, unk_8_12=260, unk_12_16=1)
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


@RestartOnRest(1049552500)
def Event_1049552500():
    """Event 1049552500"""
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=1049552500)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    TriggerAISound(ai_sound_param_id=6410, anchor_entity=1049552501, unk_8_12=1)


@RestartOnRest(1049552550)
def Event_1049552550(_, character: uint, obj: uint):
    """Event 1049552550"""
    AttachObjectToCharacter(character=character, model_point=72, obj=obj)
