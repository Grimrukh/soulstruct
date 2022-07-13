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
    RegisterGrace(grace_flag=31190000, obj=31191950, unknown=5.0)
    Event_31192800()
    Event_31192810()
    Event_31192849()
    Event_31192830()
    Event_31192811()
    Event_31192850()
    Event_31192860()
    Event_31192899()
    Event_31192861()
    Event_31192862()
    Event_31192880()
    Event_31192863(0, character=31190381, flag=31192870)
    Event_31192863(1, character=31190382, flag=31192871)
    RunCommonEvent(0, 900005610, args=(31191200, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005261, args=(31190200, 31192200, 3.0, 0.0, 0), arg_types="IIffi")
    Event_31192210(0, 31190210, 31192210, 2.0, 0.0, 0)
    Event_31192210(1, 31190211, 31192210, 2.0, 0.0, 0)
    Event_31192210(2, 31190212, 31192210, 2.0, 0.0, 0)
    Event_31192210(3, 31190213, 31192210, 2.0, 1.0, 0)
    RunCommonEvent(0, 90005261, args=(31190217, 31192219, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31190219, 31192219, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31190220, 31192220, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31190300, 31192219, 3.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31190280, 31192218, 3.0, 0.0, 3001), arg_types="IIffi")
    RunCommonEvent(0, 90005525, args=(31190600, 31191600), arg_types="II")
    RunCommonEvent(0, 90005525, args=(31190601, 31191601), arg_types="II")
    RunCommonEvent(0, 90005525, args=(31190602, 31191602), arg_types="II")
    RunCommonEvent(0, 90005525, args=(31190603, 31191603), arg_types="II")
    RunCommonEvent(0, 90005525, args=(31190604, 31191604), arg_types="II")
    RunCommonEvent(0, 90005525, args=(31190605, 31191605), arg_types="II")
    RunCommonEvent(
        0,
        90005646,
        args=(31190800, 31192840, 31192841, 31191840, 31192840, 31, 19, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(
        0,
        90005646,
        args=(31190850, 31192890, 31192891, 31191890, 31192840, 31, 19, 0, 0),
        arg_types="IIIIIBBbb",
    )


@RestartOnRest(31192210)
def Event_31192210(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 31192210"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=character, radius=radius)
    IfFlagEnabled(AND_1, 31190603)
    IfFlagEnabled(AND_2, 31190603)
    IfAttackedWithDamageType(OR_2, attacked_entity=31190210, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=31190210, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31190210, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31190210, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31190210, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31190210, unk_8_12=260, unk_12_16=1)
    IfHasAIStatus(OR_2, 31190210, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(OR_5, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfHasAIStatus(OR_5, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(OR_5, input_condition=AND_2)
    IfConditionTrue(OR_5, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_5)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=OR_2)
    Wait(seconds)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    EnableAI(character)


@RestartOnRest(35002250)
def Event_35002250(
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
    """Event 35002250"""
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
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=region)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=31190210, attacker=0)
    IfHasAIStatus(OR_2, 31190210, ai_status=AIStatusType.Battle)
    IfUnknownCharacterCondition_34(OR_2, character=31190210, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31190210, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31190210, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31190210, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31190210, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_5, input_condition=AND_1)
    IfConditionTrue(OR_5, input_condition=AND_2)
    IfConditionTrue(OR_5, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_5)
    IfConditionTrue(AND_10, input_condition=OR_5)
    IfConditionTrue(MAIN, input_condition=AND_10)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_5)
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


@RestartOnRest(31190600)
def Event_31190600(_, flag: uint, obj: uint):
    """Event 31190600"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfPlayerInOwnWorld(AND_1)
    IfAttackedWithDamageType(AND_1, attacked_entity=obj, attacker=20000)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)
    ForceAnimation(obj, 1, wait_for_completion=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(obj)


@RestartOnRest(31192800)
def Event_31192800():
    """Event 31192800"""
    EndIfFlagEnabled(31190800)
    IfHealthValueLessThanOrEqual(MAIN, 31190800, value=0)
    Wait(4.0)
    PlaySoundEffect(31190800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 31190800)
    KillBossAndDisplayBanner(character=31190800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31190800)
    EnableFlag(9242)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61242)


@RestartOnRest(31192810)
def Event_31192810():
    """Event 31192810"""
    GotoIfFlagDisabled(Label.L0, flag=31190800)
    DisableCharacter(31190800)
    DisableAnimations(31190800)
    Kill(31190800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31190800)
    DisableAnimations(31190800)
    GotoIfFlagEnabled(Label.L1, flag=31190802)
    IfFlagEnabled(AND_1, 31192805)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31192800)
    IfAttackedWithDamageType(OR_1, attacked_entity=31190800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(31190800)
    EnableAnimations(31190800)
    SetNetworkUpdateRate(31190800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31190800, name=902100310)


@RestartOnRest(31192811)
def Event_31192811():
    """Event 31192811"""
    EndIfFlagEnabled(31190800)
    IfHealthRatioLessThanOrEqual(AND_1, 31190800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(31192802)


@RestartOnRest(31192830)
def Event_31192830():
    """Event 31192830"""
    DisableNetworkSync()
    EndIfFlagEnabled(31190800)
    IfCharacterHasSpecialEffect(AND_1, 20000, 416)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(20000, 14508)
    Wait(1.0)
    Restart()


@RestartOnRest(31192850)
def Event_31192850():
    """Event 31192850"""
    EndIfFlagEnabled(31190850)
    IfHealthValueLessThanOrEqual(MAIN, 31190850, value=0)
    Wait(4.0)
    PlaySoundEffect(31190850, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 31190850)
    KillBossAndDisplayBanner(character=31190850, banner_type=BannerType.DutyFulfilled)
    Kill(31195850)
    DisableSpawner(entity=31193821)
    DisableSpawner(entity=31193820)
    EnableFlag(31190850)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61249)
    EnableFlag(9249)


@RestartOnRest(31192860)
def Event_31192860():
    """Event 31192860"""
    GotoIfFlagDisabled(Label.L0, flag=31190850)
    DisableCharacter(31190850)
    DisableAnimations(31190850)
    Kill(31190850)
    DisableCharacter(31195850)
    DisableAnimations(31195850)
    Kill(31195850)
    DisableSpawner(entity=31193821)
    DisableSpawner(entity=31193820)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31190850)
    ForceAnimation(31190850, 68011, unknown2=1.0)
    DisableAI(31190380)
    ForceAnimation(31190380, 30000, unknown2=1.0)
    SetLockOnPoint(character=31190380, lock_on_model_point=220, state=False)
    IfFlagEnabled(AND_2, 31192855)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31192850)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ForceAnimation(31190850, 68012, unknown2=1.0)
    EnableAI(31190850)
    SetNetworkUpdateRate(31190850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31190850, name=137600)
    ForceAnimation(31190380, 20000, unknown2=1.0)
    EnableAI(31190380)
    Wait(3.0)
    SetLockOnPoint(character=31190380, lock_on_model_point=220, state=True)


@RestartOnRest(31192861)
def Event_31192861():
    """Event 31192861"""
    DisableNetworkSync()
    EndIfFlagEnabled(31190850)
    IfHealthRatioLessThanOrEqual(AND_1, 31190850, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(31192852)
    EndIfFlagEnabled(31190850)
    EnableSpawner(entity=31193821)
    EnableNetworkFlag(31192871)


@RestartOnRest(31192862)
def Event_31192862():
    """Event 31192862"""
    DisableNetworkSync()
    EndIfFlagEnabled(31190850)
    IfCharacterDead(MAIN, 31190380)
    EndIfFlagEnabled(31190850)
    EnableSpawner(entity=31193820)
    EnableNetworkFlag(31192870)


@RestartOnRest(31192863)
def Event_31192863(_, character: uint, flag: uint):
    """Event 31192863"""
    DisableNetworkSync()
    EndIfFlagEnabled(31190850)
    IfFlagEnabled(AND_1, flag)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(AND_2, input_condition=AND_1)
    IfLeavingSession(AND_3)
    IfConditionFalse(AND_2, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(31192875)
    Wait(3.0)
    IfCharacterHasSpecialEffect(OR_1, character, 7800)
    IfCharacterHasSpecialEffect(OR_1, character, 7801)
    IfCharacterHasSpecialEffect(OR_1, character, 7802)
    IfCharacterHasSpecialEffect(OR_1, character, 7820)
    IfCharacterHasSpecialEffect(OR_1, character, 7821)
    IfCharacterHasSpecialEffect(OR_1, character, 7822)
    SkipLinesIfConditionTrue(1, OR_1)
    Restart()
    IfPlayerInOwnWorld(AND_1)
    IfCharacterDead(AND_1, character)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfFlagEnabled(OR_1, 31192875)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(31192875)
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest(31192880)
def Event_31192880():
    """Event 31192880"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 31190605)
    IfFlagDisabled(AND_1, 31190850)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfFlagDisabled(OR_1, 31190800)
    EnableFlag(31190890)
    SkipLinesIfConditionFalse(1, OR_1)
    DisableFlag(31190890)
    IfFlagState(OR_2, FlagSetting.Change, FlagType.Absolute, 31190800)
    IfFlagState(OR_2, FlagSetting.Change, FlagType.Absolute, 31190850)
    IfFlagState(OR_2, FlagSetting.Change, FlagType.Absolute, 31190605)
    AwaitConditionTrue(OR_2)
    Wait(1.0)
    Restart()


@RestartOnRest(31192849)
def Event_31192849():
    """Event 31192849"""
    Event_31192845(
        0,
        flag=31190800,
        entity=31191800,
        region=31192800,
        flag_1=31192805,
        character=31195800,
        action_button_id=10000,
        left=0,
        region_1=0
    )
    RunCommonEvent(0, 9005801, args=(31190800, 31191800, 31192800, 31192805, 31192806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005813, args=(31190800, 31191800, 3, 0, 3), arg_types="IIiIi")
    RunCommonEvent(0, 9005822, args=(31190800, 921500, 31192805, 31192806, 0, 31192802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(31192899)
def Event_31192899():
    """Event 31192899"""
    Event_31192845(
        1,
        flag=31190850,
        entity=31191850,
        region=31192850,
        flag_1=31192855,
        character=31195850,
        action_button_id=10000,
        left=0,
        region_1=0
    )
    RunCommonEvent(0, 9005801, args=(31190850, 31191850, 31192850, 31192855, 31192856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005813, args=(31190850, 31191850, 3, 0, 3), arg_types="IIiIi")
    RunCommonEvent(0, 9005822, args=(31190850, 920100, 31192855, 31192856, 0, 31192852, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(31192845)
def Event_31192845(
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
    """Event 31192845"""
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
    BanishPhantoms(unknown=0)
    BanishInvaders(unknown=0)
    Restart()
