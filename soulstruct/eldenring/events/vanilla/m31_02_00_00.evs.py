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
    RegisterGrace(grace_flag=310200, obj=31021950, unknown=5.0)
    Event_31022800()
    Event_31022810()
    Event_31022811()
    Event_31022849()
    RunCommonEvent(0, 90005250, args=(31025800, 31022361, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 900005610, args=(31021200, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005646,
        args=(31020800, 31022840, 31022841, 31021840, 31022840, 31, 2, 0, 0),
        arg_types="IIIIIBBbb",
    )
    Event_31022900(0, tutorial_param_id=1580, flag=710580)
    Event_31022901(0, 1690, 710690, 31020040)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(31020200, 31022200, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31020201, 31022201, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31020205, 31022205, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31020206, 31022206, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31020207, 31022206, 2.0, 0.5, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31020211, 31022200, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31020212, 31022200, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31022211(0, character=31020211)
    Event_31022211(1, character=31020212)
    Event_31022223(0, 31020218, 30001, 20001, 31022218, 1.0, 0.800000011920929, 0, 0, 0, 0, 31020219, 31020220)
    Event_31022223(1, 31020219, 30001, 20001, 31022218, 1.0, 0.5, 0, 0, 0, 0, 31020218, 31020220)
    Event_31022223(2, 31020220, 30001, 20001, 31022218, 1.0, 0.0, 0, 0, 0, 0, 31020218, 31020219)
    RunCommonEvent(0, 90005261, args=(31020250, 31022250, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31022255()
    Event_31022256()
    RunCommonEvent(0, 90005261, args=(31020251, 31022251, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31022250(0, character=31020250)
    Event_31022250(0, character=31020260)
    Event_31022250(0, character=31020261)
    RunCommonEvent(0, 90005261, args=(31020260, 31022260, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31020261, 31022260, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31020266, 31022266, 2.0, 0.30000001192092896, 0), arg_types="IIffi")
    Event_31022260(0, character=31020250)
    Event_31022260(1, character=31020251)
    Event_31022260(2, character=31020260)
    Event_31022260(3, character=31020261)
    Event_31022260(4, character=31020262)
    Event_31022260(5, character=31020263)
    Event_31022260(6, character=31020264)
    Event_31022260(7, character=31020265)
    Event_31022260(8, character=31020266)
    RunCommonEvent(0, 90005211, args=(31020301, 30000, 20000, 31022300, 2.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31020302, 30000, 20000, 31022300, 2.0, 0.5, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31020303, 30000, 20000, 31022303, 2.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31020304, 30000, 20000, 31022304, 2.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(31020350, 31022350, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31020351, 31022350, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31020357, 31022357, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31020358, 31022358, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31020359, 31022358, 2.0, 0.0, 0), arg_types="IIffi")


@RestartOnRest(31022211)
def Event_31022211(_, character: uint):
    """Event 31022211"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31022212)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=31020211, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=31020212, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=31020211, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020211, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020211, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020211, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020211, unk_8_12=260, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020212, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020212, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020212, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020212, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020212, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31022223)
def Event_31022223(
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
    attacked_entity: uint,
):
    """Event 31022223"""
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
    IfAttackedWithDamageType(OR_2, attacked_entity=character_1, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacked_entity, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character_1, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character_1, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character_1, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character_1, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character_1, unk_8_12=260, unk_12_16=1)
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


@RestartOnRest(31022250)
def Event_31022250(_, character: uint):
    """Event 31022250"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=7.0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=31020250, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=31020260, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=31020261, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=31020250, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020250, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020250, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020250, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020250, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31022255)
def Event_31022255():
    """Event 31022255"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31022255)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31022256)
def Event_31022256():
    """Event 31022256"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(31020250)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31022256)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31022250)
    IfFlagEnabled(AND_1, 31022255)
    IfCharacterHasSpecialEffect(AND_4, 31020250, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 31020250, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 31020250, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 31020250, 90160)
    IfCharacterHasSpecialEffect(AND_5, 31020250, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 31020250, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 31020250, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 31020250, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 31020250, 90162)
    IfCharacterHasSpecialEffect(AND_6, 31020250, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 31020250, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 31020250, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 31020250, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 31020250, 90161)
    IfCharacterHasSpecialEffect(AND_7, 31020250, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 31020250, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 31020250, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 31020250, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 31020250, 90162)
    IfCharacterHasSpecialEffect(AND_8, 31020250, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 31020250, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 31020250, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 31020250, 90160)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfAttackedWithDamageType(OR_2, attacked_entity=31020250, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=31020250, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020250, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020250, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020250, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31020250, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(31020250)


@RestartOnRest(31022260)
def Event_31022260(_, character: uint):
    """Event 31022260"""
    AddSpecialEffect(character, 90000)


@RestartOnRest(31022800)
def Event_31022800():
    """Event 31022800"""
    EndIfFlagEnabled(31020800)
    IfHealthValueLessThanOrEqual(MAIN, 31020800, value=0)
    Wait(4.0)
    PlaySoundEffect(31020800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 31020800)
    KillBossAndDisplayBanner(character=31020800, banner_type=BannerType.DutyFulfilled)
    Kill(31025800)
    EnableFlag(31020800)
    EnableFlag(9230)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61230)


@RestartOnRest(31022810)
def Event_31022810():
    """Event 31022810"""
    GotoIfFlagDisabled(Label.L0, flag=31020800)
    DisableCharacter(31020800)
    DisableAnimations(31020800)
    Kill(31025800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31020800)
    IfFlagEnabled(AND_2, 31022805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31022800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(31020801)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(31020800)
    SetNetworkUpdateRate(31020800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31020800, name=904480311)


@RestartOnRest(31022811)
def Event_31022811():
    """Event 31022811"""
    EndIfFlagEnabled(31020800)
    IfHealthRatioLessThanOrEqual(AND_1, 31020800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(31022802)


@RestartOnRest(31022849)
def Event_31022849():
    """Event 31022849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31020800, 31021800, 31022800, 31022805, 31025800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31020800, 31021800, 31022800, 31022805, 31022806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31020800, 31021800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(31020800, 931000, 31022805, 31022806, 0, 31022802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(31022900)
def Event_31022900(_, tutorial_param_id: int, flag: uint):
    """Event 31022900"""
    EndIfPlayerNotInOwnWorld()
    IfPlayerHasGood(AND_1, 9500)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=False)


@RestartOnRest(31022901)
def Event_31022901(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 31022901"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag_1)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=False)
