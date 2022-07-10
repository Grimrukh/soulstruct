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
    RegisterGrace(grace_flag=1051560000, obj=1051561950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76510, 76503, 1051561980, 77500, 2, 78500, 78501, 78502, 78503, 78504, 78505, 78506, 78507, 78508, 78509),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005300, args=(1051560210, 1051560210, 1051560700, 0.0, 0), arg_types="IIifi")
    Event_1051562200(0, character=1051565200)
    Event_1051562500()
    Event_1051562510()
    RunCommonEvent(0, 90005704, args=(1051560700, 3841, 3840, 1051569201, 1), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1051560700, 3841, 3842, 1051569201, 3841, 3840, 3844, -1), arg_types="IIIIIIIi")
    Event_1051563700(0, character=1051560700)
    Event_1051563701(0, 1051560700, 7.0)
    Event_1051563702(0, 10.0, 12.0, 20.0, 1051569206)
    Event_1051563703(0, entity=1051561702)
    Event_1051563704(0, character=1051560700)
    Event_1051563710(0, character=1051560705)
    RunCommonEvent(0, 90005704, args=(1051560705, 4181, 4180, 1051569251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1051560705, 4181, 4182, 1051569251, 4181, 4180, 4182, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1051560705, 4183, 4180, 4184), arg_types="IIII")
    Event_1051563715(0, character=1051560720)
    RunCommonEvent(0, 90005704, args=(1051560720, 4201, 4200, 1040529251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1051560720, 4201, 4202, 1040529251, 4201, 4200, 4203, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1051560720, 4203, 4200, 4204), arg_types="IIII")
    Event_1051563716(0, character=1051560710)
    Event_1051563717(0, character=1051560710)
    Event_1051563720(0, 1051560715, 1051562700, 155.0)
    RunCommonEvent(
        0,
        90005725,
        args=(4795, 4796, 4798, 1051569405, 1051560725, 1051560726, 1051566700),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005703, args=(1051560725, 4796, 4797, 1051569406, 4796, 4795, 4799, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1051560725, 4796, 4795, 1051569406, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1051560725, 4798, 4795, 4799), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1051560726, 4796, 4797, 1051569407, 4796, 4795, 4799, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1051560726, 4796, 4795, 1051569407, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005728, args=(1051560726, 1051562746, 1051562747), arg_types="III")
    RunCommonEvent(0, 90005727, args=(4796, 1051560725, 1051560726, 4795, 4798), arg_types="IIIII")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1051560700)
    DisableBackread(1051560705)
    DisableBackread(1051560710)
    DisableBackread(1051560715)
    DisableBackread(1051560720)
    DisableBackread(1051560725)
    DisableBackread(1051560726)


@RestartOnRest(1051562200)
def Event_1051562200(_, character: uint):
    """Event 1051562200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@RestartOnRest(1051562500)
def Event_1051562500():
    """Event 1051562500"""
    GotoIfFlagEnabled(Label.L0, flag=1051569206)
    DeleteObjectVFX(1051561500)
    CreateObjectVFX(1051561500, vfx_id=200, model_point=1520)
    AwaitFlagEnabled(flag=1051569206)
    DisplayDialog(text=30030, anchor_entity=0, display_distance=5.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(1051561500)
    DeleteObjectVFX(1051561500)
    PlaySoundEffect(1051561500, 1500, sound_type=SoundType.s_SFX)
    End()


@RestartOnRest(1051562510)
def Event_1051562510():
    """Event 1051562510"""
    DisableNetworkSync()
    EndIfFlagEnabled(1051569206)
    IfActionButtonParamActivated(OR_1, action_button_id=9320, entity=1051561500)
    IfFlagEnabled(OR_1, 1051569206)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(1051569206)
    DisplayDialog(text=30031, anchor_entity=1051561500)
    Wait(1.0)
    Restart()


@RestartOnRest(1051563700)
def Event_1051563700(_, character: uint):
    """Event 1051563700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3840)
    DisableFlag(1051569204)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3845)
    DisableCharacter(character)
    DisableBackread(character)
    SetCharacterTalkRange(character=character, distance=17.0)
    IfFlagEnabled(OR_3, 3845)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3840)
    GotoIfFlagEnabled(Label.L2, flag=3841)
    GotoIfFlagEnabled(Label.L3, flag=3842)
    GotoIfFlagEnabled(Label.L4, flag=3843)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 930000, unknown2=1.0)
    SetCharacterTalkRange(character=character, distance=30.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
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
    IfFlagEnabled(OR_4, 3845)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1051563701)
def Event_1051563701(_, character: uint, radius: float):
    """Event 1051563701"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1051569206)
    IfCharacterHasSpecialEffect(OR_1, 35000, 14200)
    IfCharacterHasSpecialEffect(OR_1, 35000, 14201)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterHasSpecialEffect(AND_1, 35000, 297000)
    IfFlagDisabled(AND_1, 3841)
    IfEntityWithinDistance(AND_1, entity=character, other_entity=35000, radius=radius)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1051562708)
    DisableAnimations(character)
    EnableImmortality(character)
    IfFlagEnabled(MAIN, 1051562709)
    ForceAnimation(character, 20002, unknown2=1.0)
    AddSpecialEffect(PLAYER, 9560)
    AddSpecialEffect(PLAYER, 236000)
    Wait(2.0)
    EnableFlag(1051569206)
    SkipLinesIfFlagEnabled(2, 60829)
    EnableFlag(60829)
    Unknown_2003_71(unk_0_4=72)
    Wait(8.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(1051563702)
def Event_1051563702(_, seconds: float, seconds_1: float, seconds_2: float, flag: uint):
    """Event 1051563702"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    EnableFlag(1051562702)
    IfFlagEnabled(MAIN, 1051562703)
    Wait(seconds)
    EndIfFlagEnabled(flag)
    EnableFlag(1051562704)
    IfFlagEnabled(MAIN, 1051562705)
    Wait(seconds_1)
    EndIfFlagEnabled(flag)
    EnableFlag(1051562706)
    IfFlagEnabled(MAIN, 1051562707)
    Wait(seconds_2)
    EndIfFlagEnabled(flag)
    DisableFlag(1051562702)
    DisableFlag(1051562703)
    DisableFlag(1051562704)
    DisableFlag(1051562705)
    DisableFlag(1051562706)
    DisableFlag(1051562707)
    Restart()


@RestartOnRest(1051563703)
def Event_1051563703(_, entity: uint):
    """Event 1051563703"""
    EndIfPlayerNotInOwnWorld()
    IfActionButtonParamActivated(MAIN, action_button_id=6590, entity=entity)
    DisplayDialog(text=30090, anchor_entity=0, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()


@RestartOnRest(1051563704)
def Event_1051563704(_, character: uint):
    """Event 1051563704"""
    EndIfPlayerNotInOwnWorld()
    DisableNetworkConnectedFlagRange(flag_range=(3840, 3844))
    EnableNetworkFlag(3840)
    SaveRequest()
    SetTeamType(character, TeamType.FriendlyNPC)
    ClearTargetList(character)
    ReplanAI(character)
    IfFlagDisabled(AND_1, 3840)
    IfFlagEnabled(AND_2, 1051569206)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFinishedConditionTrue(input_condition=AND_2)
    IfCharacterHasSpecialEffect(AND_6, character, 14200)
    IfTimeElapsed(AND_7, seconds=10.0)
    IfConditionTrue(OR_6, input_condition=AND_6)
    IfConditionTrue(OR_6, input_condition=AND_7)
    IfConditionTrue(MAIN, input_condition=OR_6)
    RestartIfFinishedConditionTrue(input_condition=AND_7)
    IfCharacterHasSpecialEffect(MAIN, character, 14201)
    Restart()


@RestartOnRest(1051563710)
def Event_1051563710(_, character: uint):
    """Event 1051563710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 4180)
    DisableFlag(1050389253)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4189)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 4189)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101, unknown2=1.0)
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
    IfFlagDisabled(MAIN, 4189)
    Restart()


@RestartOnRest(1051563715)
def Event_1051563715(_, character: uint):
    """Event 1051563715"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 4200)
    DisableFlag(1040529253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 4209)
    IfFlagEnabled(OR_1, 4211)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(OR_2, 4209)
    IfFlagEnabled(OR_2, 4211)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4200)
    GotoIfFlagEnabled(Label.L2, flag=4201)
    GotoIfFlagEnabled(Label.L4, flag=4203)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90102, unknown2=1.0)
    SkipLinesIfFlagDisabled(1, 4211)
    Move(character, destination=1051562710, destination_type=CoordEntityType.Region, short_move=True)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
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
    IfFlagEnabled(OR_15, 4209)
    IfFlagEnabled(OR_15, 4211)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()


@RestartOnRest(1051563716)
def Event_1051563716(_, character: uint):
    """Event 1051563716"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 4209)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagDisabled(AND_1, 4203)
    IfFlagDisabled(AND_2, 4217)
    IfFlagEnabled(AND_2, 4203)
    IfFlagEnabled(AND_2, 11009555)
    IfFlagDisabled(AND_2, 11059304)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930009, unknown2=1.0)
    DisableNetworkFlag(1040549254)
    DisableNetworkFlag(11009554)
    EnableNetworkFlag(1051569454)
    DisableNetworkFlag(11059304)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_10, 4209)
    IfConditionTrue(AND_10, input_condition=OR_10)
    IfFlagDisabled(AND_10, 4203)
    IfFlagDisabled(AND_11, 4217)
    IfFlagEnabled(AND_11, 4203)
    IfFlagEnabled(AND_11, 11009555)
    IfFlagDisabled(AND_11, 11059304)
    IfConditionTrue(OR_11, input_condition=AND_10)
    IfConditionTrue(OR_11, input_condition=AND_11)
    IfConditionFalse(MAIN, input_condition=OR_11)
    Restart()


@RestartOnRest(1051563717)
def Event_1051563717(_, character: uint):
    """Event 1051563717"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EnableImmortality(character)
    IfAttackedWithDamageType(MAIN, attacked_entity=character, attacker=PLAYER)
    EnableNetworkFlag(1040542710)
    ForceAnimation(character, 20014, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    End()


@RestartOnRest(1051563720)
def Event_1051563720(_, character: uint, region: uint, distance: float):
    """Event 1051563720"""
    WaitFrames(frames=1)
    DisableBackread(character)
    DisableCharacter(character)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(4100)
    EndIfFlagDisabled(4106)
    EndIfFlagEnabled(1051569301)
    EndIfFlagEnabled(1047589205)
    EnableBackread(character)
    EnableCharacter(character)
    Move(character, destination=region, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagEnabled(1, 1051562720)
    DisableFlag(1051569300)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=region)
    SetCharacterTalkRange(character=character, distance=distance)
    EnableFlag(1051569300)
    Wait(30.0)
    SetCharacterTalkRange(character=character, distance=17.0)
    End()
