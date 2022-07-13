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
    RunCommonEvent(
        0,
        90005646,
        args=(30050800, 30052840, 30052841, 30051840, 30052840, 30, 5, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(
        0,
        90005646,
        args=(30050850, 30052890, 30052891, 30051890, 30052840, 30, 5, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RegisterGrace(grace_flag=300500, obj=30051950, unknown=5.0)
    Event_30052880()
    Event_30052800()
    Event_30052810()
    Event_30052849()
    Event_30052811()
    Event_30052850()
    Event_30052860()
    Event_30052899()
    Event_30052861()
    RunCommonEvent(0, 90005616, args=(30057030, 30052700), arg_types="II")
    RunCommonEvent(0, 90005650, args=(30050540, 30051540, 30051541, 30053541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30050540, 30051540), arg_types="II")
    Event_30052400()
    RunCommonEvent(0, 90005513, args=(30050542, 30051542, 30051543, 30053543, 27002, 0, 0), arg_types="IIIIiii")
    RunCommonEvent(0, 90005525, args=(30050570, 30051570), arg_types="II")
    Event_30052580()
    RunCommonEvent(
        0,
        90005620,
        args=(30050575, 30051575, 30051576, 0, 30052575, 30052576, 30052577),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(30050575, 30051578), arg_types="II")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005200, args=(30050800, 30001, 20001, 30052800, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(30050815, 30003, 20003, 30052800, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(30050816, 30003, 20003, 30052800, 0.6000000238418579, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(30050817, 30003, 20003, 30052800, 1.2000000476837158, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(30050200, 30003, 20003, 30052200, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30050202, 30003, 20003, 30052202, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_30052203(0, character=30050203)
    RunCommonEvent(
        0,
        90005200,
        args=(30050203, 30003, 20003, 30052202, 1.7000000476837158, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(30050201, 30003, 20003, 30052302, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30050204, 30003, 20003, 30052302, 4.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30050205, 30003, 20003, 30052205, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30050206, 30003, 20003, 30052205, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30050207, 30052207, 0.0, 3021), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(30050208, 30003, 20003, 30052208, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005200, args=(30050209, 30003, 20003, 30052209, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30050210, 30003, 20003, 30052209, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30050211, 30052211, 0.0, 3011), arg_types="IIfi")
    Event_30052203(1, character=30050212)
    RunCommonEvent(0, 90005200, args=(30050212, 30003, 20003, 30052212, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30050215, 30052215, 0.0, 3030), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30050213, 30003, 20003, 30052213, 4.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30050214, 30003, 20003, 30052214, 9.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(30050300, 30052450, 7.0, 0.0, 0), arg_types="IIffi")
    Event_30052302()
    Event_30052300(0, character=30050300, character_1=30050205)
    Event_30052300(1, character=30050300, character_1=30050206)
    Event_30052300(2, character=30050300, character_1=30050208)
    Event_30052350(0, character=30050300, character_1=30050205)
    Event_30052350(1, character=30050300, character_1=30050206)
    Event_30052350(2, character=30050300, character_1=30050208)
    RunCommonEvent(0, 90005250, args=(30050301, 30052301, 0.0, 3015), arg_types="IIfi")
    Event_30052301()
    Event_30052300(3, character=30050301, character_1=30050209)
    Event_30052300(4, character=30050301, character_1=30050210)
    Event_30052300(5, character=30050301, character_1=30050211)
    Event_30052350(3, character=30050301, character_1=30050209)
    Event_30052350(4, character=30050301, character_1=30050210)
    Event_30052350(5, character=30050301, character_1=30050211)
    RunCommonEvent(0, 90005250, args=(30050302, 30052302, 0.0, 3015), arg_types="IIfi")
    Event_30052300(6, character=30050302, character_1=30050201)
    Event_30052300(7, character=30050302, character_1=30050204)
    Event_30052350(6, character=30050302, character_1=30050201)
    Event_30052350(7, character=30050302, character_1=30050204)
    RunCommonEvent(0, 90005250, args=(30050400, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30050401, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30050402, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30050403, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30050404, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30050405, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30050406, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30050407, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30050408, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30050409, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30050410, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30050411, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30050412, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30050413, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30050414, 30052400, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30050450, 30001, 20001, 30052450, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_30052450(0, 30050451, 30001, 20001, 30052450, 8.0, 0, 0, 0, 0)
    RunCommonEvent(
        0,
        90005780,
        args=(30050850, 30052160, 30052161, 30050700, 20, 30052711, 11109649, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(30050850, 30052160, 30052161, 30050700), arg_types="IIII")
    RunCommonEvent(0, 90005782, args=(30052160, 30052855, 30050700, 30052855, 30052809, 0), arg_types="IIIIIi")


@NeverRestart(30052580)
def Event_30052580():
    """Event 30052580"""
    RegisterLadder(start_climbing_flag=30050580, stop_climbing_flag=30050581, obj=30051580)


@RestartOnRest(30052203)
def Event_30052203(_, character: uint):
    """Event 30052203"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 17210)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(30052300)
def Event_30052300(_, character: uint, character_1: uint):
    """Event 30052300"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHasSpecialEffect(MAIN, character, 14716)
    AddSpecialEffect(character_1, 14717)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(30052301)
def Event_30052301():
    """Event 30052301"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30052310)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=30050301, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(4.0)
    ChangePatrolBehavior(30050301, patrol_information_id=30053310)


@RestartOnRest(30052302)
def Event_30052302():
    """Event 30052302"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30052205)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=30050300, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    ForceAnimation(30050300, 3015, unknown2=1.0)


@RestartOnRest(30052350)
def Event_30052350(_, character: uint, character_1: uint):
    """Event 30052350"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterDead(AND_1, character)
    IfCharacterHasSpecialEffect(AND_1, character_1, 14717)
    IfCharacterDoesNotHaveSpecialEffect(OR_11, character_1, 5080)
    IfCharacterDoesNotHaveSpecialEffect(OR_11, character_1, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(0.800000011920929)
    CancelSpecialEffect(character_1, 5860)
    Kill(character_1, award_souls=True)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@NeverRestart(30052400)
def Event_30052400():
    """Event 30052400"""
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005675, args=(30052650, 30053500, 30051500, 30052650, 801202070, 4.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005675, args=(30052650, 30053500, 30051500, 30052650, 801202060, 4.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005675, args=(30052650, 30053500, 30051500, 30052650, 801202050, 4.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005675, args=(30052650, 30053500, 30051500, 30052650, 801202040, 4.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005675, args=(30052650, 30053500, 30051500, 30052650, 801202030, 4.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005675, args=(30052650, 30053500, 30051500, 30052650, 801202020, 4.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005675, args=(30052650, 30053500, 30051500, 30052650, 801202010, 4.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005675, args=(30052650, 30053500, 30051500, 30052650, 801202000, 4.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005675, args=(30052702, 30053502, 30051502, 30052650, 801202070, 2.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005675, args=(30052702, 30053502, 30051502, 30052650, 801202060, 2.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005675, args=(30052702, 30053502, 30051502, 30052650, 801202050, 2.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005675, args=(30052702, 30053502, 30051502, 30052650, 801202040, 2.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005675, args=(30052702, 30053502, 30051502, 30052650, 801202030, 2.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005675, args=(30052702, 30053502, 30051502, 30052650, 801202020, 2.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005675, args=(30052702, 30053502, 30051502, 30052650, 801202010, 2.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005675, args=(30052702, 30053502, 30051502, 30052650, 801202000, 2.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005675, args=(30052704, 30053504, 30051504, 30052650, 801202070, 0.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005675, args=(30052704, 30053504, 30051504, 30052650, 801202060, 0.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005675, args=(30052704, 30053504, 30051504, 30052650, 801202050, 0.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005675, args=(30052704, 30053504, 30051504, 30052650, 801202040, 0.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005675, args=(30052704, 30053504, 30051504, 30052650, 801202030, 0.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005675, args=(30052704, 30053504, 30051504, 30052650, 801202020, 0.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005675, args=(30052704, 30053504, 30051504, 30052650, 801202010, 0.0, 0), arg_types="IIIIifi")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005675, args=(30052704, 30053504, 30051504, 30052650, 801202000, 0.0, 0), arg_types="IIIIifi")


@RestartOnRest(30052450)
def Event_30052450(
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
    """Event 30052450"""
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
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=30052451)
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
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    IfCharacterInsideRegion(AND_4, character=PLAYER, region=30052451)
    SkipLinesIfConditionTrue(6, AND_4)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()
    Wait(2.5)
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


@RestartOnRest(30052800)
def Event_30052800():
    """Event 30052800"""
    EndIfFlagEnabled(30050800)
    IfHealthValueLessThanOrEqual(MAIN, 30050800, value=0)
    Kill(30055800)
    Wait(4.0)
    PlaySoundEffect(30050800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30050800)
    KillBossAndDisplayBanner(character=30050800, banner_type=BannerType.DutyFulfilled)
    EnableObjectActivation(30051670, obj_act_id=-1)
    Kill(30050816)
    Kill(30050815)
    Kill(30050817)
    EnableFlag(30050800)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61205)
    EnableFlag(9205)


@RestartOnRest(30052850)
def Event_30052850():
    """Event 30052850"""
    EndIfFlagEnabled(30050850)
    IfHealthValueLessThanOrEqual(MAIN, 30050850, value=0)
    Wait(4.0)
    PlaySoundEffect(30050850, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30050850)
    KillBossAndDisplayBanner(character=30050850, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30050850)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61221)
    EnableFlag(9221)


@RestartOnRest(30052810)
def Event_30052810():
    """Event 30052810"""
    GotoIfFlagDisabled(Label.L0, flag=30050800)
    DisableCharacter(30055800)
    DisableCharacter(30060815)
    DisableCharacter(30060816)
    DisableCharacter(30060817)
    DisableAnimations(30055800)
    DisableAnimations(30060815)
    DisableAnimations(30060816)
    DisableAnimations(30060817)
    Kill(30055800)
    Kill(30050816)
    Kill(30050815)
    Kill(30050817)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30050800)
    DisableObjectActivation(30051670, obj_act_id=-1)
    IfFlagEnabled(AND_2, 30052805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30052800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableAI(30050800)
    SetNetworkUpdateRate(30050800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30050800, name=903664301)


@RestartOnRest(30052811)
def Event_30052811():
    """Event 30052811"""
    EndIfFlagEnabled(30050800)
    IfHealthRatioLessThanOrEqual(AND_1, 30050800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30052802)


@NeverRestart(30052825)
def Event_30052825(_, flag: uint, region: uint, character: uint, target_entity: uint, region_1: uint, animation: int):
    """Event 30052825"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    SetEventPoint(character, region=region_1, reaction_range=0.0)
    IfTimeElapsed(OR_15, seconds=4.0)
    IfConditionTrue(OR_14, input_condition=OR_15)
    IfCharacterInsideRegion(OR_14, character=character, region=region_1)
    IfConditionTrue(MAIN, input_condition=OR_14)
    RestartIfFinishedConditionTrue(input_condition=OR_15)
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
    Wait(2.0)


@RestartOnRest(30052880)
def Event_30052880():
    """Event 30052880"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 30050570)
    IfFlagDisabled(AND_1, 30050850)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfFlagDisabled(OR_1, 30050800)
    EnableFlag(30050880)
    SkipLinesIfConditionFalse(1, OR_1)
    DisableFlag(30050880)
    IfFlagState(OR_2, FlagSetting.Change, FlagType.Absolute, 30050800)
    IfFlagState(OR_2, FlagSetting.Change, FlagType.Absolute, 30050850)
    IfFlagState(OR_2, FlagSetting.Change, FlagType.Absolute, 30050570)
    AwaitConditionTrue(OR_2)
    Restart()


@RestartOnRest(30052860)
def Event_30052860():
    """Event 30052860"""
    GotoIfFlagDisabled(Label.L0, flag=30050850)
    DisableCharacter(30050850)
    DisableAnimations(30050850)
    Kill(30050850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30050850)
    IfFlagEnabled(AND_2, 30052855)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30052855)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableAI(30050850)
    SetNetworkUpdateRate(30050850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30050850, name=902100301)


@RestartOnRest(30052861)
def Event_30052861():
    """Event 30052861"""
    EndIfFlagEnabled(30050850)
    IfHealthRatioLessThanOrEqual(AND_1, 30050850, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30052852)


@RestartOnRest(30052849)
def Event_30052849():
    """Event 30052849"""
    Event_30052870(
        0,
        flag=30050800,
        entity=30051800,
        region=30052800,
        flag_1=30052805,
        character=30055800,
        action_button_id=10000,
        left=0,
        region_1=0
    )
    RunCommonEvent(0, 9005801, args=(30050800, 30051800, 30052800, 30052805, 30052806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005813, args=(30050800, 30051800, 3, 0, 3), arg_types="IIiIi")
    RunCommonEvent(0, 9005822, args=(30050800, 930000, 30052805, 30052806, 0, 30052802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(30052899)
def Event_30052899():
    """Event 30052899"""
    Event_30052870(
        1,
        flag=30050850,
        entity=30051850,
        region=30052855,
        flag_1=30052855,
        character=30055850,
        action_button_id=10000,
        left=0,
        region_1=0
    )
    RunCommonEvent(0, 9005801, args=(30050850, 30051850, 30052855, 30052855, 30052856, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005813, args=(30050850, 30051850, 3, 0, 3), arg_types="IIiIi")
    RunCommonEvent(0, 9005822, args=(30050850, 921500, 30052855, 30052856, 0, 30052852, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(30052870)
def Event_30052870(
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
    """Event 30052870"""
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
