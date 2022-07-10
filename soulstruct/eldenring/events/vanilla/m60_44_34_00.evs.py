"""
linked:
0
72
154
238

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\common_macro.emevd
238: N:\\GR\\data\\Param\\event\\m60.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1044340000, obj=1044341950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76161, 76157, 1044341980, 77110, 1, 78110, 78111, 78112, 78113, 78114, 78115, 78116, 78117, 78118, 78119),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005637, args=(31018600, 1044340620, 1044341620), arg_types="III")
    RunCommonEvent(
        0,
        90005636,
        args=(31018600, 1044340620, 1044341620, 4470, 1044342620, 1044342621, 1044342620, 1044343620, -1),
        arg_types="IIIiIIIIi",
    )
    Event_1044342502()
    Event_1044342200()
    Event_1044340650(
        0,
        tutorial_param_id=1520,
        flag=710520,
        tutorial_param_id_1=1770,
        flag_1=710770,
        flag_2=69090,
        flag_3=69370
    )
    Event_1044342300(0, character=1044340300, obj=1044341300, region=1044342300)
    Event_1044342300(1, character=1044340301, obj=1044341302, region=1044342301)
    Event_1044342300(2, character=1044340302, obj=1044341301, region=1044342301)
    Event_1044342203(0, character=1044340203)
    RunCommonEvent(0, 90005250, args=(1044340203, 1044342280, 0.0, -1), arg_types="IIfi")
    Event_1044342280()
    RunCommonEvent(0, 90005261, args=(1044340270, 1044342270, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044340271, 1044342270, 5.0, 1.5, -1), arg_types="IIffi")
    Event_1044342230(0, character=1044340230)
    Event_1044342230(1, character=1044340231)
    Event_1044342230(2, character=1044340232)
    Event_1044342230(3, character=1044340240)
    RunCommonEvent(0, 90005251, args=(1044340252, 8.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1044340250, 1044342600, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005630, args=(61443400, 1044341500, 127), arg_types="IIi")
    Event_1044343700(0, character=1044340700, character_1=1044340701, character_2=1044340702, obj=1044346700)
    Event_1044343702(0, character=1044340700)
    Event_1044343704(0, character=1044340700)
    Event_1044343701(0, character=1044340700)
    RunCommonEvent(
        0,
        90005700,
        args=(1044340700, 4741, 4742, 1044349249, 0.6499999761581421, 4740, 4743, 0),
        arg_types="IIIIfIIi",
    )
    RunCommonEvent(0, 90005701, args=(1044340700, 4741, 4742, 1044349249, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1044340700, 4743, 4740, 4743), arg_types="IIII")
    Event_1044343703()
    RunCommonEvent(
        0,
        90005700,
        args=(1044340701, 1044349246, 1044349246, 1044349247, 0.6499999761581421, 1044349246, 1044349246, 0),
        arg_types="IIIIfIIi",
    )
    RunCommonEvent(0, 90005701, args=(1044340701, 4741, 4742, 1044349249, 3), arg_types="IIIIi")
    RunCommonEvent(0, 1044343705, args=(1044340700, 1044340701), arg_types="II")
    Event_1044343706(
        0,
        character=1044340700,
        first_flag=4740,
        flag=4741,
        flag_1=4742,
        last_flag=4743,
        character_1=1044340701,
        flag_2=1044349246
    )
    Event_1044343707(0, flag=4740, flag_1=1041369201, flag_2=1044349226)
    RunCommonEvent(0, 90005704, args=(1044340710, 3601, 3600, 1044349251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1044340710, 3601, 3602, 1044349251, 3603, 3600, 3603, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1044340710, 3603, 3600, 3604), arg_types="IIII")
    Event_1044343710(0, 1044340710)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1044340710)


@RestartOnRest(1044342502)
def Event_1044342502():
    """Event 1044342502"""
    RegisterLadder(start_climbing_flag=44340580, stop_climbing_flag=44340851, obj=1044341580)
    RegisterLadder(start_climbing_flag=44340582, stop_climbing_flag=44340853, obj=1044341582)
    RegisterLadder(start_climbing_flag=44340584, stop_climbing_flag=44340855, obj=1044341584)


@RestartOnRest(1044342200)
def Event_1044342200():
    """Event 1044342200"""
    DisableObject(1044346200)


@RestartOnRest(1044342203)
def Event_1044342203(_, character: uint):
    """Event 1044342203"""
    IfCharacterDead(AND_1, character)
    EndIfConditionTrue(input_condition=AND_1)
    AddSpecialEffect(character, 8089)
    SetTeamType(character, TeamType.CoopNPC)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=1044342281)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SetTeamType(character, TeamType.Enemy2)
    End()


@RestartOnRest(1044342230)
def Event_1044342230(_, character: uint):
    """Event 1044342230"""
    Kill(character)
    End()


@RestartOnRest(1044342280)
def Event_1044342280():
    """Event 1044342280"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterDead(MAIN, 1044345280)
    TriggerAISound(ai_sound_param_id=4132, anchor_entity=1044340280, unk_8_12=2)
    TriggerAISound(ai_sound_param_id=4132, anchor_entity=1044340281, unk_8_12=2)
    TriggerAISound(ai_sound_param_id=4132, anchor_entity=1044340282, unk_8_12=2)
    TriggerAISound(ai_sound_param_id=4132, anchor_entity=1044340283, unk_8_12=2)
    End()


@RestartOnRest(1044342300)
def Event_1044342300(_, character: uint, obj: uint, region: uint):
    """Event 1044342300"""
    DisableCharacter(character)
    DisableObject(obj)
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    IfCharacterDead(AND_10, character)
    EndIfConditionTrue(input_condition=AND_10)
    EnableObject(obj)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=obj, attacker=20000)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_2)
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
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_4)
    IfConditionTrue(OR_3, input_condition=AND_5)
    IfConditionTrue(OR_3, input_condition=AND_6)
    IfConditionTrue(OR_3, input_condition=AND_7)
    IfConditionTrue(OR_3, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_3)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    CreateTemporaryVFX(vfx_id=641012, anchor_entity=character, model_point=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    DisableObject(obj)
    Wait(0.30000001192092896)
    EnableCharacter(character)


@RestartOnRest(1044340650)
def Event_1044340650(
    _,
    tutorial_param_id: int,
    flag: uint,
    tutorial_param_id_1: int,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1044340650"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfPlayerHasGood(AND_1, 130)
    IfInsideMap(AND_1, game_map=EAST_WEEPING_PENINSULA_NW_SW)
    IfPlayerDoesNotHaveGood(AND_1, 9109)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 100690)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_2)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9109, flag=flag, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9137, flag=flag_1, bit_count=1)
    EnableFlag(flag_2)
    EnableFlag(flag_3)


@RestartOnRest(1044343700)
def Event_1044343700(_, character: uint, character_1: uint, character_2: uint, obj: uint):
    """Event 1044343700"""
    WaitFrames(frames=1)
    DisableFlag(1044349200)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    IfFlagEnabled(AND_10, 4740)
    IfFlagEnabled(AND_10, 1041369248)
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(1041369248)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableObject(obj)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    IfFlagEnabled(OR_1, 4745)
    IfFlagEnabled(OR_1, 4746)
    IfFlagEnabled(OR_1, 4747)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagEnabled(AND_1, 1044349221)
    GotoIfConditionFalse(Label.L20, input_condition=AND_1)
    GotoIfFlagEnabled(Label.L1, flag=4740)
    GotoIfFlagEnabled(Label.L2, flag=4741)
    GotoIfFlagEnabled(Label.L4, flag=4743)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableObject(obj)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    SkipLinesIfFlagDisabled(1, 4980)
    ForceAnimation(character, 30001, unknown2=1.0)
    SkipLinesIfFlagRangeAllDisabled(1, (4982, 4983))
    ForceAnimation(character, 30002, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableObject(obj)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    SkipLinesIfFlagDisabled(1, 4980)
    ForceAnimation(character, 30001, unknown2=1.0)
    SkipLinesIfFlagRangeAllDisabled(2, (4982, 4983))
    ForceAnimation(character, 30002, unknown2=1.0)
    DisableAI(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfFlagDisabled(Label.L20, flag=1044349222)
    DropMandatoryTreasure(character)
    DropMandatoryTreasure(character_1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    EnableObject(obj)
    DisableBackread(character)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(MAIN, 1044349200)
    Restart()


@NeverRestart(1044343701)
def Event_1044343701(_, character: uint):
    """Event 1044343701"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(4743)
    EndIfFlagDisabled(1044349221)
    IfCharacterDead(MAIN, character)
    EnableNetworkFlag(1044349222)
    End()


@NeverRestart(1044343702)
def Event_1044343702(_, character: uint):
    """Event 1044343702"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(OR_1, 4745)
    IfFlagEnabled(OR_1, 4746)
    IfFlagEnabled(OR_1, 4747)
    IfFlagEnabled(OR_2, 4740)
    IfFlagEnabled(OR_2, 4741)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_1, input_condition=OR_2)
    EndIfConditionFalse(input_condition=AND_1)
    GotoIfFlagEnabled(Label.L0, flag=4980)
    GotoIfFlagRangeAnyEnabled(Label.L10, flag_range=(4982, 4983))

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterHasSpecialEffect(OR_5, character, 9601)
    IfCharacterHasSpecialEffect(OR_5, character, 9603)
    IfConditionTrue(MAIN, input_condition=OR_5)
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=9601)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=9603)

    # --- Label 1 --- #
    DefineLabel(1)
    IfEntityWithinDistance(OR_6, entity=20000, other_entity=character, radius=4.0)
    IfCharacterDoesNotHaveSpecialEffect(OR_6, character, 9601)
    IfConditionTrue(MAIN, input_condition=OR_6)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9601)
    ForceAnimation(character, 20004, unknown2=1.0)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, character, 9601)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    IfEntityBeyondDistance(OR_7, entity=20000, other_entity=character, radius=6.0)
    IfCharacterDoesNotHaveSpecialEffect(OR_7, character, 9603)
    IfConditionTrue(MAIN, input_condition=OR_7)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9603)
    ForceAnimation(character, 20010, unknown2=1.0)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, character, 9603)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    IfCharacterHasSpecialEffect(OR_10, character, 9603)
    IfConditionTrue(MAIN, input_condition=OR_10)
    GotoIfCharacterHasSpecialEffect(Label.L11, character=character, special_effect=9603)

    # --- Label 11 --- #
    DefineLabel(11)
    IfEntityBeyondDistance(OR_11, entity=20000, other_entity=character, radius=6.0)
    IfCharacterDoesNotHaveSpecialEffect(OR_11, character, 9603)
    IfConditionTrue(MAIN, input_condition=OR_11)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=9603)
    ForceAnimation(character, 20011, unknown2=1.0)
    DisableAI(character)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, character, 9603)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    Restart()


@RestartOnRest(1044343703)
def Event_1044343703():
    """Event 1044343703"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1044349229)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=1044340700, radius=7.5)
    EnableNetworkFlag(1044349229)
    End()


@RestartOnRest(1044343704)
def Event_1044343704(_, character: uint):
    """Event 1044343704"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(OR_1, 4745)
    IfFlagEnabled(OR_1, 4746)
    IfFlagEnabled(OR_1, 4747)
    IfFlagEnabled(OR_2, 4740)
    IfFlagEnabled(OR_2, 4741)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_1, input_condition=OR_2)
    EndIfConditionFalse(input_condition=AND_1)
    GotoIfCharacterHasSpecialEffect(Label.L0, character=character, special_effect=9602)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, character, 9602)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableAI(character)
    IfCharacterHasSpecialEffect(MAIN, character, 9602)
    Restart()


@RestartOnRest(1044343705)
def Event_1044343705(_, character: uint, attacked_entity: uint):
    """Event 1044343705"""
    EndIfPlayerNotInOwnWorld()
    IfAttackedWithDamageType(OR_1, attacked_entity=attacked_entity, attacker=20000)
    IfAttackedWithDamageType(OR_1, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagDisabled(AND_1, 1041362709)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1041362708)
    EndIfFlagEnabled(4741)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9601)
    ForceAnimation(character, 20004, unknown2=1.0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9602)
    ForceAnimation(character, 20006, unknown2=1.0)


@NeverRestart(1044343706)
def Event_1044343706(
    _,
    character: uint,
    first_flag: uint,
    flag: uint,
    flag_1: uint,
    last_flag: uint,
    character_1: uint,
    flag_2: uint,
):
    """Event 1044343706"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(first_flag)
    DisableNetworkFlag(flag_2)
    IfFlagEnabled(OR_1, flag)
    IfFlagEnabled(OR_1, flag_1)
    IfAttackedWithDamageType(AND_1, attacked_entity=character, attacker=20000)
    IfHealthValueLessThan(AND_1, character, value=1)
    IfConditionTrue(OR_2, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfFlagEnabled(OR_3, flag_2)
    IfAttackedWithDamageType(AND_3, attacked_entity=character_1, attacker=20000)
    IfHealthValueLessThan(AND_3, character_1, value=1)
    IfConditionTrue(OR_4, input_condition=OR_3)
    IfConditionTrue(OR_4, input_condition=AND_3)
    IfConditionTrue(OR_5, input_condition=OR_2)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfConditionTrue(MAIN, input_condition=OR_5)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=OR_4)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNetworkFlag(flag_2)
    SetTeamType(character_1, TeamType.HostileNPC)
    Goto(Label.L10)

    # --- Label 5 --- #
    DefineLabel(5)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAI(character)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    SaveRequest()
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    WaitFrames(frames=1)
    DisableNetworkFlag(flag_2)
    IfFlagEnabled(MAIN, flag_2)
    DisableNetworkFlag(flag_2)
    End()


@RestartOnRest(1044343707)
def Event_1044343707(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 1044343707"""
    IfFlagDisabled(OR_1, flag)
    IfFlagEnabled(OR_1, flag_1)
    SkipLinesIfConditionFalse(2, OR_1)
    DisableNetworkFlag(flag_2)
    End()
    EnableNetworkFlag(flag_2)
    IfFlagDisabled(OR_2, flag)
    IfFlagEnabled(OR_2, flag_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    DisableNetworkFlag(flag_2)
    End()


@RestartOnRest(1044343710)
def Event_1044343710(_, character: uint):
    """Event 1044343710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3600)
    DisableFlag(1044349252)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L7, flag=3607)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3607)
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfFlagEnabled(Label.L0, flag=3600)
    GotoIfFlagEnabled(Label.L1, flag=3601)
    GotoIfFlagEnabled(Label.L2, flag=3602)
    GotoIfFlagEnabled(Label.L3, flag=3603)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3607)
    Restart()
