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
    RegisterGrace(grace_flag=31100000, obj=31101950, unknown=5.0)
    Event_31102800()
    Event_31102801()
    Event_31102802()
    Event_31102810()
    Event_31102811()
    Event_31102815()
    Event_31102849()
    Event_31102860()
    Event_31102830()
    RunCommonEvent(
        0,
        90005646,
        args=(31100800, 31102840, 31102841, 31101840, 31102840, 31, 10, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 900005610, args=(31101200, 100, 800, 0), arg_types="IiiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_31102255(0, character=31100252, patrol_information_id=31103252)
    Event_31102255(1, character=31100253, patrol_information_id=31103253)
    RunCommonEvent(0, 90005261, args=(31100270, 31102270, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31100350, 31102350, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31102360()
    RunCommonEvent(0, 90005261, args=(31100201, 31102201, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31100202, 31102201, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31100205, 31102205, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31100236, 31102236, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31100237, 31102236, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31100238, 31102238, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31102200(1, 31100238)


@RestartOnRest(31102200)
def Event_31102200(_, character: uint):
    """Event 31102200"""
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
    IfEntityWithinDistance(AND_1, entity=character, other_entity=PLAYER, radius=2.0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfHasAIStatus(OR_2, character, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31102250)
def Event_31102250(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 31102250"""
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
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_2)
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


@RestartOnRest(31102255)
def Event_31102255(_, character: uint, patrol_information_id: uint):
    """Event 31102255"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31102252)
    IfHasAIStatus(OR_3, character, ai_status=AIStatusType.Normal)
    IfHasAIStatus(OR_3, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(OR_3, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(OR_3, character, ai_status=AIStatusType.Unknown4)
    IfHasAIStatus(OR_3, character, ai_status=AIStatusType.Unknown5)
    IfHasAIStatus(OR_3, character, ai_status=AIStatusType.Unknown6)
    IfConditionTrue(AND_1, input_condition=OR_3)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    ClearTargetList(character)
    WaitFrames(frames=10)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)


@NeverRestart(31102360)
def Event_31102360():
    """Event 31102360"""
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31102365)
    IfHasAIStatus(OR_15, 31100350, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_15, 31100350, ai_status=AIStatusType.Unknown5)
    IfConditionTrue(MAIN, input_condition=OR_15)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNest(31102350, region=31102361)


@RestartOnRest(31102800)
def Event_31102800():
    """Event 31102800"""
    EndIfFlagEnabled(31100800)
    IfCharacterDead(AND_1, 31100800)
    IfCharacterDead(AND_1, 31100801)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(4.0)
    KillBossAndDisplayBanner(character=31100800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31100800)
    EnableFlag(9244)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61244)


@RestartOnRest(31102801)
def Event_31102801():
    """Event 31102801"""
    EndIfFlagEnabled(31100800)
    IfHealthValueLessThanOrEqual(MAIN, 31100800, value=0)
    Wait(4.0)
    PlaySoundEffect(31100800, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31102802)
def Event_31102802():
    """Event 31102802"""
    EndIfFlagEnabled(31100800)
    IfHealthValueLessThanOrEqual(MAIN, 31100801, value=0)
    Wait(4.0)
    PlaySoundEffect(31100801, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31102830)
def Event_31102830():
    """Event 31102830"""
    EndIfFlagEnabled(31100800)
    IfHealthLessThanOrEqual(MAIN, 31100800, value=0.8500000238418579)
    ChangePatrolBehavior(31100801, patrol_information_id=31103830)
    CancelSpecialEffect(31100801, 8085)
    AddSpecialEffect(31100801, 8090)
    SetAIParamID(0, ai_param_id=0)


@RestartOnRest(31102810)
def Event_31102810():
    """Event 31102810"""
    GotoIfFlagDisabled(Label.L0, flag=31100800)
    DisableCharacter(31100800)
    DisableCharacter(31100801)
    DisableAnimations(31100800)
    DisableAnimations(31100801)
    Kill(31100800)
    Kill(31100801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=31100801)
    IfAttackedWithDamageType(OR_1, attacked_entity=31100800, attacker=PLAYER)
    IfAttackedWithDamageType(OR_1, attacked_entity=31100801, attacker=PLAYER)
    IfHasAIStatus(OR_1, 31100800, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_1, 31100801, ai_status=AIStatusType.Battle)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31102805)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(31100801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfAttackedWithDamageType(OR_2, attacked_entity=31100800, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=31100801, attacker=PLAYER)
    IfHasAIStatus(OR_2, 31100800, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_2, 31100801, ai_status=AIStatusType.Battle)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31102805)
    IfFlagEnabled(AND_2, 31102805)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkUpdateRate(31100800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(31100801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31100800, name=903970311)
    EnableBossHealthBar(31100801, name=903970312, bar_slot=1)


@RestartOnRest(31102811)
def Event_31102811():
    """Event 31102811"""
    EndIfFlagEnabled(31100800)
    IfCharacterDead(OR_15, 31100800)
    IfCharacterDead(OR_15, 31100801)
    IfConditionTrue(MAIN, input_condition=OR_15)
    EnableFlag(31102842)


@RestartOnRest(31102815)
def Event_31102815():
    """Event 31102815"""
    GotoIfFlagEnabled(Label.L10, flag=31100800)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=31100801, right=0)
    GotoIfFlagEnabled(Label.L0, flag=31100801)
    IfFlagState(OR_1, FlagSetting.On, FlagType.RelativeToThisEventSlot, 31102810)
    IfFlagEnabled(OR_1, 31100801)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfFlagEnabled(OR_2, 31100800)
    IfConditionTrue(MAIN, input_condition=OR_2)
    RestartIfFlagEnabled(31100800)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    IfPlayerInOwnWorld(AND_3)
    IfFlagDisabled(AND_3, 31100800)
    IfActionButtonParamActivated(AND_3, action_button_id=10000, entity=31101800)
    IfFlagEnabled(OR_3, 31100800)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    RestartIfFlagEnabled(31100800)
    UnknownSound_2010_11(unk_0_4=5.0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=PLAYER, special_effect=4250)
    RotateToFaceEntity(PLAYER, 31102800, animation=60060, wait_for_completion=True)
    SkipLines(1)
    RotateToFaceEntity(PLAYER, 31102800, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=31102805)
    IfTimeElapsed(OR_4, seconds=3.0)
    IfCharacterInsideRegion(OR_5, character=PLAYER, region=31102800)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfConditionTrue(AND_4, input_condition=OR_5)
    IfPlayerInOwnWorld(AND_4)
    IfFlagDisabled(AND_4, 31100800)
    IfConditionTrue(OR_6, input_condition=AND_4)
    IfFlagEnabled(OR_6, 31100800)
    IfConditionTrue(MAIN, input_condition=OR_6)
    RestartIfFlagEnabled(31100800)
    RestartIfFinishedConditionTrue(input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    SkipLinesIfFlagEnabled(1, 31100801)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(31105800, authority_level=UpdateAuthority.Unknown8192)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(31105800)
    EnableNetworkFlag(31102805)
    EndIfPlayerNotInOwnWorld()
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_10)
    IfFlagEnabled(AND_10, 31100800)
    IfFailedToCreateSession(OR_10)
    IfMultiplayerState(OR_10, state=MultiplayerState.Unknown6)
    IfConditionTrue(AND_10, input_condition=OR_10)
    IfActionButtonParamActivated(AND_10, action_button_id=10000, entity=31101800)
    IfConditionTrue(MAIN, input_condition=AND_10)
    RotateToFaceEntity(PLAYER, 31102800, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@RestartOnRest(31102860)
def Event_31102860():
    """Event 31102860"""
    EndIfFlagEnabled(31100800)
    IfFlagEnabled(AND_1, 31102805)
    IfAttackedWithDamageType(OR_1, attacked_entity=31100800, attacker=PLAYER)
    IfHasAIStatus(OR_1, 31100800, ai_status=AIStatusType.Battle)
    IfUnknownCharacterCondition_34(OR_1, character=31100800, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=31100800, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=31100800, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=31100800, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=31100800, unk_8_12=260, unk_12_16=1)
    IfAttackedWithDamageType(OR_1, attacked_entity=31100801, attacker=PLAYER)
    IfHasAIStatus(OR_1, 31100801, ai_status=AIStatusType.Battle)
    IfUnknownCharacterCondition_34(OR_1, character=31100801, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=31100801, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=31100801, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=31100801, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=31100801, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31102805)
    IfPlayerInOwnWorld(AND_1)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(31102865)
    NotifyBossBattleStart()


@RestartOnRest(31102849)
def Event_31102849():
    """Event 31102849"""
    RunCommonEvent(0, 9005801, args=(31100800, 31101800, 31102800, 31102865, 31102806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31100800, 31101800, 3, 31100801), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(31100800, 931000, 31102805, 31102806, 31102810, 31102842, 0, 0),
        arg_types="IiIIIIii",
    )
