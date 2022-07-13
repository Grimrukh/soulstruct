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
    RegisterGrace(grace_flag=1034500000, obj=1034501950, unknown=5.0)
    RunCommonEvent(0, 9005810, args=(1034500703, 1034500001, 1034500951, 1034501951, 5.0), arg_types="IIIIf")
    RunCommonEvent(
        0,
        90005100,
        args=(76247, 76247, 1034501981, 77230, 0, 78230, 78231, 78232, 78233, 78234, 78235, 78236, 78237, 78238, 78239),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 900055278, args=(1034500739, 1034501739, 1506, 9320, 30050, 0, 0, 0), arg_types="IIiiiiii")
    RunCommonEvent(0, 900055278, args=(1034500739, 1034501701, 1506, 9320, 30050, 0, 0, 0), arg_types="IIiiiiii")
    RunCommonEvent(0, 900055278, args=(1034500739, 1034501702, 1506, 9320, 30050, 0, 0, 0), arg_types="IIiiiiii")
    Event_1034503600(0, region=1034502500, flag=1034500738)
    Event_1034502610()
    Event_1034502620()
    RunCommonEvent(0, 90005870, args=(1034500800, 904502601, 25), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1034500800, 0, 1034500800, 1, 0, 0.0), arg_types="IIIIif")
    Event_1034502800()
    Event_1034502801()
    Event_1034502804()
    Event_1034502802()
    Event_1034502803()
    RunCommonEvent(0, 90005300, args=(1035510200, 1034500200, 40200, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005525, args=(1034500620, 1034501620), arg_types="II")
    RunCommonEvent(0, 90005525, args=(1034500621, 1034501621), arg_types="II")
    Event_1034502580()
    Event_1034502510()
    RunCommonEvent(
        0,
        90005501,
        args=(1034500510, 1034500511, 0, 1034501510, 1034501511, 1034501512, 1034500512),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005704, args=(1034500705, 1034509258, 3460, 1034502711, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005703,
        args=(1034500705, 3461, 3462, 1034502711, 1034509258, 3460, 3463, -1),
        arg_types="IIIIIIIi",
    )
    RunCommonEvent(0, 90005702, args=(1034500705, 3463, 3460, 3463), arg_types="IIII")
    Event_1034503705(0, character=1034500705)
    Event_1034503706()
    Event_1034503707()
    Event_1034500730(0, character=1034500710, obj=1034501710)
    RunCommonEvent(0, 90005704, args=(1034500710, 3743, 3740, 1034509401, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005707,
        args=(1034500710, 3741, 3742, 1034509401, 1034500738, 3740, 3743, 0, 20003, 1034502742, 1034502743),
        arg_types="IIIIIIIiiII",
    )
    RunCommonEvent(0, 90005709, args=(1034500710, 905, 603000), arg_types="Iii")
    RunCommonEvent(0, 90005709, args=(1034500710, 960, 603050), arg_types="Iii")
    RunCommonEvent(0, 90005708, args=(1034500710, 3740, 0), arg_types="III")
    Event_1034500731()
    Event_1034500732(0, character=1034500710)
    Event_1034500733(0, character=1034500710)
    Event_1034500734()
    Event_1034500735()
    Event_1034500710(0, character=1034500720)
    Event_1034500700(0, character=1034500740)
    Event_1034500701(
        0,
        character=1034500741,
        character_1=1034500742,
        character_2=1034500743,
        character_3=1034500744,
        character_4=1034500745
    )
    RunCommonEvent(0, 90005702, args=(1034500741, 3603, 3600, 3603), arg_types="IIII")
    Event_1034500702(0, character=1034500741)
    Event_1034500715(0, character=1034500700)
    Event_1034500716(0, character=1034500701)
    RunCommonEvent(0, 90005704, args=(1034500701, 3561, 3560, 1034509301, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005707,
        args=(1034500701, 3561, 3562, 1034509301, 3563, 3560, 3563, 0, 90201, 1034502722, 1034502723),
        arg_types="IIIIIIIiiII",
    )
    RunCommonEvent(0, 90005709, args=(1034500701, 905, 603001), arg_types="Iii")
    RunCommonEvent(0, 90005709, args=(1034500701, 200, 603051), arg_types="Iii")
    Event_1034500717(0, character=1034500703)
    Event_1034500718(0, value=2)
    Event_1034500719()
    RunCommonEvent(0, 90005773, args=(1034509347,))
    Event_1034500712(
        0,
        character=1034500704,
        character_1=1034500715,
        character_2=1034500716,
        character_3=1034500717,
        character_4=1034500718
    )
    Event_1034500713(0, character=1034500719)
    Event_1034500714(0, character=1034500725)
    RunCommonEvent(0, 90005750, args=(1034501700, 4110, 101480, 400148, 400148, 3569, 0), arg_types="IiiIIIi")
    Event_1034503740()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1034500700)
    DisableBackread(1034500701)
    DisableBackread(1034500703)
    DisableBackread(1034500704)
    DisableBackread(1034500705)
    DisableBackread(1034500710)
    DisableBackread(1034500715)
    DisableBackread(1034500716)
    DisableBackread(1034500717)
    DisableBackread(1034500718)
    DisableBackread(1034500719)
    DisableBackread(1034500720)
    DisableBackread(1034500725)
    DisableBackread(1034500740)
    DisableBackread(1034500741)
    DisableBackread(1034500742)
    DisableBackread(1034500743)
    DisableBackread(1034500744)
    DisableBackread(1034500745)
    EnableObjectInvulnerability(1034501710)
    Event_1034500519()


@RestartOnRest(1034502340)
def Event_1034502340(_, character: uint):
    """Event 1034502340"""
    Kill(character, award_souls=True)


@NeverRestart(1034502580)
def Event_1034502580():
    """Event 1034502580"""
    RegisterLadder(start_climbing_flag=1034500580, stop_climbing_flag=1034500581, obj=1034501580)


@RestartOnRest(1034502510)
def Event_1034502510():
    """Event 1034502510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1034500510,
            1034500511,
            0,
            1034501510,
            1034501511,
            1034503511,
            1034501512,
            1034503512,
            1034502511,
            1034502512,
            1034500512,
            1034500513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(1034500519)
def Event_1034500519():
    """Event 1034500519"""
    EndIfThisEventSlotFlagEnabled()
    DisableFlag(1034500510)
    DisableThisSlotFlag()


@RestartOnRest(1034503600)
def Event_1034503600(_, region: uint, flag: uint):
    """Event 1034503600"""
    DisableNetworkSync()
    IfCharacterInsideRegion(AND_2, character=20000, region=region)
    IfFlagEnabled(AND_2, flag)
    IfConditionTrue(MAIN, input_condition=AND_2)
    AddSpecialEffect(20000, 9621)
    Wait(0.10000000149011612)

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterOutsideRegion(OR_3, character=20000, region=region)
    IfFlagDisabled(OR_3, flag)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Wait(0.10000000149011612)
    CancelSpecialEffect(20000, 9621)
    Restart()


@RestartOnRest(1034502610)
def Event_1034502610():
    """Event 1034502610"""
    DisableObject(1034501610)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1034500737)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 1034500738)
    IfFlagDisabled(AND_1, 1034500737)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfFlagEnabled(3, 1034500736)
    SetRespawnPoint(respawn_point=1034502610)
    SaveRequest()
    EnableFlag(1034500736)
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    AddSpecialEffect(PLAYER, 514)
    DisableCharacter(1034505610)
    EnableObject(1034501610)
    IfFlagDisabled(OR_1, 1034500738)
    IfFlagEnabled(OR_1, 1034500737)
    IfConditionTrue(MAIN, input_condition=OR_1)
    AddSpecialEffect(PLAYER, 4281)
    AddSpecialEffect(PLAYER, 4283)
    CancelSpecialEffect(PLAYER, 514)
    EnableCharacter(1034505610)
    DisableObject(1034501610)


@RestartOnRest(1034502620)
def Event_1034502620():
    """Event 1034502620"""
    EndIfFlagDisabled(3617)
    IfFlagEnabled(AND_1, 3617)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableCharacter(1034505610)
    Wait(1.0)
    Restart()


@RestartOnRest(1034502800)
def Event_1034502800():
    """Event 1034502800"""
    EndIfFlagEnabled(1034500800)
    AddSpecialEffect(1034500800, 10247)


@RestartOnRest(1034502801)
def Event_1034502801():
    """Event 1034502801"""
    EndIfFlagEnabled(1034500800)
    EndIfCharacterHasSpecialEffect(character=1034500800, special_effect=10207)
    EnableImmortality(1034500800)
    IfHealthRatioLessThan(OR_1, 1034500800, value=0.5)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Wait(0.5)
    IfHealthRatioLessThan(OR_2, 1034500800, value=0.5)
    SkipLinesIfConditionTrue(1, OR_2)
    Restart()
    EnableInvincibility(1034500800)
    ReplanAI(1034500800)
    ForceAnimation(1034500800, 20009, unknown2=1.0)
    EndIfCharacterHasSpecialEffect(character=1034500800, special_effect=10207)
    Wait(1.0)
    Restart()


@RestartOnRest(1034502802)
def Event_1034502802():
    """Event 1034502802"""
    EndIfFlagEnabled(1034500800)
    IfFlagEnabled(MAIN, 1034420800)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableCharacter(1034500800)
    EnableFlag(1034500800)


@RestartOnRest(1034502803)
def Event_1034502803():
    """Event 1034502803"""
    DisableNetworkSync()
    EndIfFlagEnabled(1034500800)
    IfCharacterInsideRegion(MAIN, character=1034500800, region=1034502800)
    AddSpecialEffect(1034500800, 10285)
    Wait(1.0)
    Restart()


@RestartOnRest(1034502804)
def Event_1034502804():
    """Event 1034502804"""
    EndIfFlagEnabled(1034500800)
    IfHealthRatioLessThan(AND_1, 1034500800, value=0.5)
    IfCharacterHasSpecialEffect(AND_1, 1034500800, 10207)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(4.699999809265137)
    EnableFlag(1034500800)
    DisableCharacter(1034500800)


@RestartOnRest(1034500700)
def Event_1034500700(_, character: uint):
    """Event 1034500700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    DisableAnimations(character)
    GotoIfFlagEnabled(Label.L9, flag=3609)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3609)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    EnableBackread(character)
    EnableCharacter(character)
    EnableImmortality(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3609)
    Restart()


@RestartOnRest(1034500701)
def Event_1034500701(_, character: uint, character_1: uint, character_2: uint, character_3: uint, character_4: uint):
    """Event 1034500701"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L17, flag=3617)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_3)
    DisableCharacter(character_4)
    DisableBackread(character_4)
    IfFlagEnabled(MAIN, 3617)
    Restart()

    # --- Label 17 --- #
    DefineLabel(17)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    ForceAnimation(character_1, 30001, unknown2=1.0)
    EnableBackread(character_2)
    EnableCharacter(character_2)
    ForceAnimation(character_2, 30002, unknown2=1.0)
    EnableBackread(character_3)
    EnableCharacter(character_3)
    ForceAnimation(character_3, 30002, unknown2=1.0)
    EnableBackread(character_4)
    EnableCharacter(character_4)
    ForceAnimation(character_4, 30001, unknown2=1.0)
    GotoIfFlagEnabled(Label.L0, flag=3600)
    GotoIfFlagEnabled(Label.L1, flag=3601)
    GotoIfFlagEnabled(Label.L2, flag=3602)
    GotoIfFlagEnabled(Label.L3, flag=3603)

    # --- Label 0 --- #
    DefineLabel(0)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetCharacterTalkRange(character=character, distance=100.0)
    AddSpecialEffect(character, 9627)
    ForceAnimation(character, 930013, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3617)
    Restart()


@RestartOnRest(1034500702)
def Event_1034500702(_, character: uint):
    """Event 1034500702"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 3603)
    IfFlagEnabled(AND_1, 3617)
    EndIfConditionTrue(input_condition=AND_1)
    IfHasAIStatus(MAIN, character, ai_status=AIStatusType.Battle)
    EnableFlag(1034502700)
    AddSpecialEffect(character, 9644)


@RestartOnRest(1034503705)
def Event_1034503705(_, character: uint):
    """Event 1034503705"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3460)
    DisableFlag(1034509253)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(OR_1, 3465)
    IfFlagEnabled(OR_1, 3466)
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_2, 3465)
    IfFlagEnabled(OR_2, 3466)
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagDisabled(Label.L1, flag=1034509256)
    GotoIfFlagEnabled(Label.L1, flag=3460)
    GotoIfFlagEnabled(Label.L2, flag=3461)
    GotoIfFlagEnabled(Label.L4, flag=3463)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SkipLinesIfFlagDisabled(3, 1034509256)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableFlag(1034509258)
    ForceAnimation(character, 90100, unknown2=1.0)
    SkipLinesIfFlagEnabled(3, 1034509256)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(1034509258)
    ForceAnimation(character, 90103, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(AND_15, 3465)
    IfFlagDisabled(AND_15, 3466)
    AwaitConditionTrue(AND_15)
    Restart()


@RestartOnRest(1034503706)
def Event_1034503706():
    """Event 1034503706"""
    EndIfFlagEnabled(3463)
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfHealthValueEqual(AND_1, 1034500705, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetBackreadStateAlternate(1034500705, True)
    IfTimeElapsed(AND_2, seconds=20.0)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SetBackreadStateAlternate(1034500705, False)


@RestartOnRest(1034503707)
def Event_1034503707():
    """Event 1034503707"""
    EndIfFlagEnabled(1034509256)
    SetTeamType(1034500705, TeamType.NoTeam)
    AwaitFlagEnabled(flag=1034509256)
    SetTeamType(1034500705, TeamType.FriendlyNPC)
    DisableNetworkConnectedFlagRange(flag_range=(3460, 3463))
    EnableNetworkFlag(3460)
    End()


@RestartOnRest(1034500710)
def Event_1034500710(_, character: uint):
    """Event 1034500710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    DisableAnimations(character)
    GotoIfFlagEnabled(Label.L6, flag=3766)
    DisableCharacter(character)
    DisableBackread(character)
    EnableImmortality(character)
    IfFlagEnabled(MAIN, 3766)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930017, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3766)
    Restart()


@RestartOnRest(1034500712)
def Event_1034500712(_, character: uint, character_1: uint, character_2: uint, character_3: uint, character_4: uint):
    """Event 1034500712"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableCharacter(character_3)
    EnableCharacter(character_4)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    EnableBackread(character_3)
    EnableBackread(character_4)
    EnableImmortality(character)
    EnableImmortality(character_1)
    EnableImmortality(character_2)
    EnableImmortality(character_3)
    EnableImmortality(character_4)
    ForceAnimation(character, 930002, unknown2=1.0)
    ForceAnimation(character_1, 930010, unknown2=1.0)
    ForceAnimation(character_2, 90101, unknown2=1.0)
    ForceAnimation(character_3, 90101, unknown2=1.0)
    ForceAnimation(character_4, 90101, unknown2=1.0)
    End()


@RestartOnRest(1034500713)
def Event_1034500713(_, character: uint):
    """Event 1034500713"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L10, flag=4230)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 4230)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    IfFlagDisabled(MAIN, 4230)
    Restart()


@RestartOnRest(1034500714)
def Event_1034500714(_, character: uint):
    """Event 1034500714"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L11, flag=4251)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 4251)
    Restart()

    # --- Label 11 --- #
    DefineLabel(11)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    IfFlagDisabled(MAIN, 4251)
    Restart()


@RestartOnRest(1034500715)
def Event_1034500715(_, character: uint):
    """Event 1034500715"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    DisableAnimations(character)
    GotoIfFlagEnabled(Label.L6, flag=3566)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3566)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3566)
    Restart()


@RestartOnRest(1034500716)
def Event_1034500716(_, character: uint):
    """Event 1034500716"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3560)
    DisableFlag(1034509302)
    SkipLinesIfFlagDisabled(2, 1034509346)
    SkipLinesIfFlagDisabled(1, 1034509328)
    IncrementEventValue(1034509339, bit_count=3, max_value=7)
    SkipLinesIfFlagDisabled(2, 1034509346)
    SkipLinesIfFlagDisabled(1, 1034509336)
    IncrementEventValue(1034509342, bit_count=3, max_value=7)
    DisableFlag(1034509346)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L7, flag=3567)
    GotoIfFlagEnabled(Label.L8, flag=3568)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagRangeAnyEnabled(MAIN, flag_range=(3567, 3568))
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)

    # --- Label 8 --- #
    DefineLabel(8)
    GotoIfFlagEnabled(Label.L0, flag=3560)
    GotoIfFlagEnabled(Label.L1, flag=3561)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagRangeAllDisabled(MAIN, flag_range=(3567, 3568))
    Restart()


@RestartOnRest(1034500717)
def Event_1034500717(_, character: uint):
    """Event 1034500717"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L9, flag=3569)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3569)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3569)
    Restart()


@RestartOnRest(1034500718)
def Event_1034500718(_, value: int):
    """Event 1034500718"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1034509345)
    IfTrueFlagCountGreaterThanOrEqual(MAIN, FlagType.Absolute, flag_range=(130000, 130100), value=value)
    EnableFlag(1034509345)


@RestartOnRest(1034500719)
def Event_1034500719():
    """Event 1034500719"""
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(MAIN, 1034502726)
    SkipLinesIfFlagEnabled(1, 120790)
    IfFlagEnabled(OR_1, 120790)
    SkipLinesIfFlagEnabled(1, 120800)
    IfFlagEnabled(OR_1, 120800)
    SkipLinesIfFlagEnabled(1, 120810)
    IfFlagEnabled(OR_1, 120810)
    SkipLinesIfFlagEnabled(1, 120820)
    IfFlagEnabled(OR_1, 120820)
    SkipLinesIfFlagEnabled(1, 120830)
    IfFlagEnabled(OR_1, 120830)
    SkipLinesIfFlagEnabled(1, 120840)
    IfFlagEnabled(OR_1, 120840)
    IfFlagEnabled(OR_1, 6000)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(1034502726)
    Restart()


@RestartOnRest(1034500730)
def Event_1034500730(_, character: uint, obj: uint):
    """Event 1034500730"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3740)
    DisableFlag(1034509403)
    SkipLinesIfFlagDisabled(1, 1034509429)
    EnableNetworkFlag(1034502745)
    DisableNetworkFlag(1034502748)
    IfFlagEnabled(AND_15, 1051369358)
    IfFlagEnabled(AND_15, 9410)
    IfFlagDisabled(AND_15, 9412)
    SkipLinesIfConditionFalse(1, AND_15)
    EnableNetworkFlag(1034502748)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(AND_1, 3747)
    IfFlagDisabled(AND_1, 1034502748)
    GotoIfConditionTrue(Label.L7, input_condition=AND_1)
    GotoIfFlagEnabled(Label.L8, flag=3748)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObjectInvulnerability(obj)
    IfFlagEnabled(AND_2, 3747)
    IfFlagDisabled(AND_2, 1034502748)
    IfFlagEnabled(OR_2, 3748)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfFlagEnabled(Label.L0, flag=3740)
    GotoIfFlagEnabled(Label.L1, flag=3741)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    GotoIfFlagEnabled(Label.L19, flag=1034509416)
    GotoIfFlagDisabled(Label.L19, flag=1034509418)
    SetTeamType(character, TeamType.NoTeam)

    # --- Label 19 --- #
    DefineLabel(19)
    ForceAnimation(character, 930000, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(AND_4, 3747)
    IfFlagDisabled(AND_4, 1034502748)
    IfConditionFalse(MAIN, input_condition=AND_4)
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    GotoIfFlagEnabled(Label.L0, flag=3740)
    GotoIfFlagEnabled(Label.L1, flag=3741)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    EnableImmortality(character)
    SkipLinesIfFlagEnabled(2, 1034509429)
    ForceAnimation(character, 930004, unknown2=1.0)
    SkipLines(1)
    ForceAnimation(character, 930000, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3748)
    Restart()


@RestartOnRest(1034500731)
def Event_1034500731():
    """Event 1034500731"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1034509419)
    IfEntityWithinDistance(MAIN, entity=20000, other_entity=1034500710, radius=10.0)
    EnableFlag(1034509419)
    EnableFlag(3758)


@RestartOnRest(1034500732)
def Event_1034500732(_, character: uint):
    """Event 1034500732"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1034509410)
    IfFlagEnabled(MAIN, 1034509410)
    SkipLinesIfFlagEnabled(1, 9130)
    EnableFlag(1034509412)
    EnableFlag(3618)
    EnableFlag(3778)
    EnableFlag(3578)
    SetTeamType(character, TeamType.NoTeam)
    EnableNetworkFlag(1034500738)
    BanishPhantoms(unknown=0)


@RestartOnRest(1034500733)
def Event_1034500733(_, character: uint):
    """Event 1034500733"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1034509416)
    GotoIfFlagDisabled(Label.L0, flag=1034509417)
    Wait(0.10000000149011612)
    EnableFlag(1034509416)
    EnableFlag(3758)

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(MAIN, 1034509416)
    EnableFlag(3618)
    EnableFlag(3778)
    EnableFlag(3578)
    SetTeamType(character, TeamType.FriendlyNPC)
    DisableNetworkFlag(1034500738)
    EnableNetworkFlag(1034500739)


@RestartOnRest(1034500734)
def Event_1034500734():
    """Event 1034500734"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1034509417)
    IfFlagEnabled(OR_1, 1034509205)
    IfFlagDisabled(OR_1, 1034509412)
    IfFlagEnabled(AND_1, 1034509306)
    IfFlagEnabled(AND_1, 1034509358)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1034509417)


@RestartOnRest(1034500735)
def Event_1034500735():
    """Event 1034500735"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1034509424)
    IfFlagEnabled(MAIN, 1034509424)
    EnableFlag(3578)


@RestartOnRest(1034503740)
def Event_1034503740():
    """Event 1034503740"""
    EndIfPlayerNotInOwnWorld()
    IfEntityWithinDistance(OR_1, entity=PLAYER, other_entity=1034500711, radius=3.0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(12012713)
    IfEntityBeyondDistance(AND_1, entity=PLAYER, other_entity=1034500711, radius=3.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(12012713)
    Restart()
