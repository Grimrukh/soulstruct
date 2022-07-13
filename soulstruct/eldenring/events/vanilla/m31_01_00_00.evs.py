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
    RegisterGrace(grace_flag=31010000, obj=31011950, unknown=5.0)
    Event_31012800()
    Event_31012810()
    Event_31012849()
    Event_31012811()
    Event_31012830()
    RunCommonEvent(
        0,
        90005646,
        args=(31010800, 31012840, 31012841, 31011840, 31012840, 31, 1, 0, 0),
        arg_types="IIIIIBBbb",
    )
    Event_31012500()
    RunCommonEvent(0, 900005610, args=(31011200, 100, 800, 0), arg_types="IiiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(31010201, 31012201, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31010202, 31012201, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31012200(0, character=31010201, patrol_information_id=31013201)
    Event_31012200(1, character=31010202, patrol_information_id=31013202)
    Event_31012230(0, character=31010201)
    Event_31012230(1, character=31010202)
    Event_31012207(0, 31010207, 31012207, 2.0, 7.0, 0)
    Event_31012207(1, 31010208, 31012207, 2.0, 10.0, 0)
    Event_31012207(2, 31010209, 31012207, 2.0, 15.0, 0)
    RunCommonEvent(0, 90005261, args=(31010221, 31012221, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31010222, 31012221, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31012207(3, 31010300, 31012207, 3.0, 3.0, 0)
    Event_31012220(0, character=31010207)
    Event_31012220(1, character=31010208)
    Event_31012220(2, character=31010209)
    Event_31012220(3, 31010300)


@RestartOnRest(31012500)
def Event_31012500():
    """Event 31012500"""
    GotoIfFlagDisabled(Label.L0, flag=31010500)
    DisableObject(31011500)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31012500)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DestroyObject(31011500)
    EnableFlag(31010500)


@RestartOnRest(31012200)
def Event_31012200(_, character: uint, patrol_information_id: uint):
    """Event 31012200"""
    EndIfThisEventSlotFlagEnabled()
    IfHasAIStatus(OR_1, 31010207, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_1, 31010208, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_1, 31010209, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_1, 31010300, ai_status=AIStatusType.Battle)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableAI(character)
    AddSpecialEffect(character, 5000)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31012207)
def Event_31012207(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 31012207"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(OR_5, character=PLAYER, region=region)
    IfConditionTrue(OR_3, input_condition=OR_5)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_3)
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
    IfAttackedWithDamageType(OR_6, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=OR_6)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=OR_5)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(31012220)
def Event_31012220(_, character: uint):
    """Event 31012220"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=1.5)
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
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    EnableAI(character)


@RestartOnRest(31012230)
def Event_31012230(_, character: uint):
    """Event 31012230"""
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
    IfAttackedWithDamageType(OR_2, attacked_entity=31010201, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=31010202, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31012800)
def Event_31012800():
    """Event 31012800"""
    EndIfFlagEnabled(31010800)
    IfHealthValueLessThanOrEqual(MAIN, 31010800, value=0)
    Wait(4.0)
    PlaySoundEffect(31010800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 31010800)
    KillBossAndDisplayBanner(character=31010800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31010800)
    EnableFlag(9231)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61231)


@RestartOnRest(31012810)
def Event_31012810():
    """Event 31012810"""
    GotoIfFlagDisabled(Label.L0, flag=31010800)
    DisableCharacter(31010800)
    DisableAnimations(31010800)
    Kill(31010800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31010800)
    ForceAnimation(31010800, 30000, unknown2=1.0)
    GotoIfFlagEnabled(Label.L1, flag=31010801)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31012801)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=31010800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(31010801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 31012805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31012800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(31010800)
    ForceAnimation(31010800, 20000, unknown2=1.0)
    SetNetworkUpdateRate(31010800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31010800, name=904630310)


@RestartOnRest(31012811)
def Event_31012811():
    """Event 31012811"""
    EndIfFlagEnabled(31010800)
    IfHealthRatioLessThanOrEqual(AND_1, 31010800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(31012802)


@RestartOnRest(31012830)
def Event_31012830():
    """Event 31012830"""
    EndIfFlagEnabled(31010801)
    AddSpecialEffect(31010100, 9531)
    AwaitFlagEnabled(flag=31010801)
    AddSpecialEffect(31010100, 9532)


@RestartOnRest(31012849)
def Event_31012849():
    """Event 31012849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31010800, 31011800, 31012800, 31012805, 31015800, 10000, 31010801, 31012801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31010800, 31011800, 31012800, 31012805, 31012806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31010800, 31011800, 3, 31010801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(31010800, 931000, 31012805, 31012806, 0, 31012802, 0, 0), arg_types="IiIIIIii")
