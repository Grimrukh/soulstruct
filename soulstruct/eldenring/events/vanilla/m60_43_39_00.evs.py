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
    RegisterGrace(grace_flag=1043390000, obj=1043391950, unknown=5.0)
    RunCommonEvent(0, 900005610, args=(1043391680, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(1043391682, 100, 800, 1043398540), arg_types="IiiI")
    RunCommonEvent(0, 90005460, args=(1043390250,))
    RunCommonEvent(0, 90005461, args=(1043390250,))
    RunCommonEvent(0, 90005462, args=(1043390250,))
    RunCommonEvent(0, 90005460, args=(1043390251,))
    RunCommonEvent(0, 90005461, args=(1043390251,))
    RunCommonEvent(0, 90005462, args=(1043390251,))
    RunCommonEvent(0, 90005460, args=(1043390252,))
    RunCommonEvent(0, 90005461, args=(1043390252,))
    RunCommonEvent(0, 90005462, args=(1043390252,))
    RunCommonEvent(0, 90005460, args=(1043390253,))
    RunCommonEvent(0, 90005461, args=(1043390253,))
    RunCommonEvent(0, 90005462, args=(1043390253,))
    RunCommonEvent(0, 90005460, args=(1043390254,))
    RunCommonEvent(0, 90005461, args=(1043390254,))
    RunCommonEvent(0, 90005462, args=(1043390254,))
    Event_1043392600(0, attacked_entity=1043391610, region=1043392610)
    Event_1043392600(1, attacked_entity=1043391611, region=1043392611)
    RunCommonEvent(0, 90005683, args=(62104, 1043391684, 210, 78192, 78192), arg_types="IIiII")
    Event_1043393700(0, character=1043390700, character_1=1043390701, character_2=1043390702, obj=1043396700)
    Event_1043393703(0, character=1043390700)
    Event_1043393705(0, character=1043390700)
    Event_1043393702(0, character=1043390700)
    RunCommonEvent(
        0,
        90005700,
        args=(1043390700, 4741, 4742, 1043399249, 0.6499999761581421, 4740, 4743, 0),
        arg_types="IIIIfIIi",
    )
    RunCommonEvent(0, 90005701, args=(1043390700, 4741, 4742, 1043399249, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1043390700, 4743, 4740, 4743), arg_types="IIII")
    Event_1043393704()
    RunCommonEvent(
        0,
        90005700,
        args=(1043390701, 1043399246, 1043399246, 1043399247, 0.6499999761581421, 1043399246, 1043399246, 0),
        arg_types="IIIIfIIi",
    )
    RunCommonEvent(0, 90005701, args=(1043390701, 4741, 4742, 1043399249, 3), arg_types="IIIIi")
    RunCommonEvent(0, 1043393706, args=(1043390700, 1043390701), arg_types="II")
    Event_1043393707(
        0,
        character=1043390700,
        first_flag=4740,
        flag=4741,
        flag_1=4742,
        last_flag=4743,
        character_1=1043390701,
        flag_2=1043399246
    )
    RunCommonEvent(0, 90005706, args=(1043370720, 930025, 0), arg_types="IiI")
    RunCommonEvent(
        0,
        90005703,
        args=(1043390710, 3661, 3662, 1043399301, 1043399314, 3660, 3663, -1),
        arg_types="IIIIIIIi",
    )
    RunCommonEvent(0, 90005704, args=(1043390710, 1043399314, 3660, 1043399301, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1043390710, 3663, 3660, 3663), arg_types="IIII")
    Event_1043393720(0, character=1043390710)
    Event_1043393721()
    Event_1043393722()
    Event_1043390724()
    Event_1043393750(0, character=1043390705)
    Event_1043392390()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1043392200()
    RunCommonEvent(0, 90005261, args=(1043390220, 1043392220, 3.0, 0.0, 3010), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(1043390220, 5.0, 0.0, -1), arg_types="Iffi")


@RestartOnRest(1043392600)
def Event_1043392600(_, attacked_entity: uint, region: uint):
    """Event 1043392600"""
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacked_entity, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    PlaySoundEffect(attacked_entity, 810000099, sound_type=SoundType.Unknown14)
    ForceAnimation(attacked_entity, 1, unknown2=1.0)
    TriggerAISound(ai_sound_param_id=7000, anchor_entity=region, unk_8_12=1)
    Wait(2.0)
    TriggerAISound(ai_sound_param_id=7000, anchor_entity=region, unk_8_12=1)
    Wait(1.0)
    Restart()


@RestartOnRest(1043392200)
def Event_1043392200():
    """Event 1043392200"""
    DropMandatoryTreasure(1043395200)


@RestartOnRest(1043392390)
def Event_1043392390():
    """Event 1043392390"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=1042372800)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1043392390)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=1043392391)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=1043392392)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=1043392393)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=1043392394)
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    CancelSpecialEffect(PLAYER, 4211)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 4211)
    Wait(1.0)
    Restart()


@RestartOnRest(1043392670)
def Event_1043392670(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1043392670"""
    EndIfTryingToCreateSession()
    IfPlayerHasGood(AND_1, 130)
    IfPlayerDoesNotHaveGood(AND_1, 9109)
    IfLeavingSession(AND_1)
    IfInsideMap(AND_1, game_map=WEST_LIMGRAVE_NE_NE)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 100690)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=False)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9109, flag=flag_1, bit_count=1)


@RestartOnRest(1043392671)
def Event_1043392671(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1043392671"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag)
    IfLeavingSession(AND_1)
    IfInsideMap(AND_1, game_map=WEST_LIMGRAVE_NE_NE)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9120, flag=flag_1, bit_count=1)


@RestartOnRest(1043393700)
def Event_1043393700(_, character: uint, character_1: uint, character_2: uint, obj: uint):
    """Event 1043393700"""
    WaitFrames(frames=1)
    DisableFlag(1043399200)
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
    IfFlagEnabled(AND_1, 1043399221)
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
    GotoIfFlagDisabled(Label.L20, flag=1043399222)
    DropMandatoryTreasure(character)
    DropMandatoryTreasure(character_1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    EnableObject(obj)
    DisableBackread(character)
    DisableBackread(character_1)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(MAIN, 1043399200)
    Restart()


@NeverRestart(1043393702)
def Event_1043393702(_, character: uint):
    """Event 1043393702"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(4743)
    EndIfFlagDisabled(1043399221)
    IfCharacterDead(MAIN, character)
    EnableNetworkFlag(1043399222)
    End()


@NeverRestart(1043393703)
def Event_1043393703(_, character: uint):
    """Event 1043393703"""
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


@RestartOnRest(1043393704)
def Event_1043393704():
    """Event 1043393704"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043399229)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=1043390700, radius=7.5)
    EnableNetworkFlag(1043399229)
    End()


@RestartOnRest(1043393705)
def Event_1043393705(_, character: uint):
    """Event 1043393705"""
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


@RestartOnRest(1043393706)
def Event_1043393706(_, character: uint, attacked_entity: uint):
    """Event 1043393706"""
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


@NeverRestart(1043393707)
def Event_1043393707(
    _,
    character: uint,
    first_flag: uint,
    flag: uint,
    flag_1: uint,
    last_flag: uint,
    character_1: uint,
    flag_2: uint,
):
    """Event 1043393707"""
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


@RestartOnRest(1043343700)
def Event_1043343700(_, character: uint):
    """Event 1043343700"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30023, unknown2=1.0)
    End()


@RestartOnRest(1043343701)
def Event_1043343701(_, character: uint):
    """Event 1043343701"""
    GotoIfFlagEnabled(Label.L1, flag=30110800)
    IfFlagEnabled(MAIN, 30110800)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(1043343702)
def Event_1043343702():
    """Event 1043343702"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043399356)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=30111950, radius=15.0)
    IfFlagEnabled(AND_1, 1043399355)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1043399356)
    End()


@RestartOnRest(1043393720)
def Event_1043393720(_, character: uint):
    """Event 1043393720"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3660)
    DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3665)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3665)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    SkipLinesIfFlagDisabled(2, 1043399311)
    Move(character, destination=1043392700, destination_type=CoordEntityType.Region, short_move=True)
    GotoIfFlagEnabled(Label.L1, flag=3660)
    GotoIfFlagEnabled(Label.L2, flag=3661)
    GotoIfFlagEnabled(Label.L4, flag=3663)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    SkipLinesIfFlagEnabled(1, 1043399311)
    ForceAnimation(character, 930018, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3665)
    Restart()


@RestartOnRest(1043393721)
def Event_1043393721():
    """Event 1043393721"""
    WaitFrames(frames=1)
    EndIfFlagDisabled(3660)
    EnableImmortality(1043390710)
    DisableHealthBar(1043390710)
    AwaitFlagEnabled(flag=1043399311)
    DisableImmortality(1043390710)
    EnableHealthBar(1043390710)
    End()


@RestartOnRest(1043393722)
def Event_1043393722():
    """Event 1043393722"""
    EndIfFlagDisabled(3665)
    DisableNetworkFlag(1043392712)
    DisableNetworkFlag(1043392713)
    IfFlagEnabled(AND_1, 3665)
    IfFlagDisabled(AND_1, 1043399305)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=1043390710, radius=30.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1043392712)
    Wait(20.0)
    Restart()


@RestartOnRest(1043390724)
def Event_1043390724():
    """Event 1043390724"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043399311)
    EnableFlag(1043399314)
    IfFlagEnabled(MAIN, 1043399311)
    DisableFlag(1043399314)
    End()


@RestartOnRest(1043393750)
def Event_1043393750(_, character: uint):
    """Event 1043393750"""
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableBackread(character)
