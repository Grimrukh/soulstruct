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
    RegisterGrace(grace_flag=1052560000, obj=1052561950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76510, 76520, 1052561980, 77500, 5, 78500, 78501, 78502, 78503, 78504, 78505, 78506, 78507, 78508, 78509),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005860, args=(1052560800, 0, 1052560800, 0, 30525, 0.0), arg_types="IIIIif")
    Event_1052562815(0, character=1052560800, name=904810601, unk_4_8=18)
    RunCommonEvent(0, 90005872, args=(1052560800, 18, 0), arg_types="III")
    RunCommonEvent(
        0,
        90005211,
        args=(1052560800, 30000, 20000, 1052562800, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(1052560211, 30001, 20001, 0, 0.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    Event_1052562820()
    Event_1052562821()
    Event_1052562830(0, 1052560801, 30001, 20020, 0, 0.0, 0.0, 0, 0, 0, 0)
    RunCommonEvent(0, 90005771, args=(1052560950, 1052562700), arg_types="II")


@NeverRestart(1052562815)
def Event_1052562815(_, character: uint, name: int, unk_4_8: uint):
    """Event 1052562815"""
    DisableNetworkSync()
    IfHasAIStatus(OR_15, character, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_15, 1052560801, ai_status=AIStatusType.Battle)
    IfConditionTrue(AND_1, input_condition=OR_15)
    IfUnknownCondition_33(AND_1, unk_4_8=unk_4_8, unk_8_9=True)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfFlagDisabled(Label.L0, flag=9290)
    GotoIfFlagDisabled(Label.L1, flag=9291)
    Wait(5.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(9290)
    Wait(1.0)
    EnableBossHealthBar(1052560803, name=name)
    IfHasAIStatus(OR_14, character, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_14, 1052560801, ai_status=AIStatusType.Battle)
    IfConditionTrue(AND_2, input_condition=OR_14)
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
    DisableBossHealthBar(1052560803, name=name)
    DisableFlag(9290)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(9291)
    Wait(1.0)
    EnableBossHealthBar(1052560803, name=name, bar_slot=1)
    IfHasAIStatus(OR_11, character, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_11, 1052560801, ai_status=AIStatusType.Battle)
    IfConditionTrue(AND_12, input_condition=OR_11)
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
    DisableBossHealthBar(1052560803, name=name, bar_slot=1)
    DisableFlag(9291)
    Restart()


@RestartOnRest(1052562820)
def Event_1052562820():
    """Event 1052562820"""
    AddSpecialEffect(1052560800, 17320)
    AddSpecialEffect(1052560801, 17321)
    AddSpecialEffect(1052560802, 17322)
    DisableHealthBar(1052560800)
    DisableHealthBar(1052560801)
    DisableHealthBar(1052560802)
    DisableHealthBar(1052560803)
    DisableGravity(1052560803)
    DisableAnimations(1052560803)
    ReferDamageToEntity(1052560800, target_entity=1052560803)
    ReferDamageToEntity(1052560801, target_entity=1052560803)
    ReferDamageToEntity(1052560802, target_entity=1052560803)


@RestartOnRest(1052562821)
def Event_1052562821():
    """Event 1052562821"""
    GotoIfFlagDisabled(Label.L0, flag=1052560800)
    DisableAnimations(1052560800)
    DisableAnimations(1052560801)
    DisableAnimations(1052560802)
    DisableAnimations(1052560803)
    Kill(1052560800)
    Kill(1052560801)
    Kill(1052560802)
    Kill(1052560803)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfHealthValueEqual(OR_1, 1052560800, value=0)
    IfHealthValueEqual(OR_1, 1052560801, value=0)
    IfHealthValueEqual(OR_1, 1052560802, value=0)
    IfHealthValueEqual(OR_1, 1052560803, value=0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Kill(1052560800)
    Kill(1052560801)
    Kill(1052560802)
    Kill(1052560803)


@RestartOnRest(1052562830)
def Event_1052562830(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    seconds: float,
    seconds_1: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 1052562830"""
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
    SkipLinesIfUnsignedEqual(1, left=0, right=region)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfCharacterHasSpecialEffect(OR_3, 1052560800, 17325)
    IfCharacterHasSpecialEffect(OR_3, 1052560801, 17326)
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
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    Wait(seconds_1)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    EnableAI(character)
    Move(
        character,
        destination=1052560800,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=1052560800,
    )
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    Wait(5.0)
    AddSpecialEffect(1052560800, 17327)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    Wait(5.0)
    AddSpecialEffect(1052560800, 17327)
    End()
    Wait(seconds)
