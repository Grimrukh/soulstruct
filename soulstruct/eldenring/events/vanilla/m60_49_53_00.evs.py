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
    RegisterGrace(grace_flag=1049530000, obj=1049531950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76510, 76501, 1049531980, 77500, 1, 78500, 78501, 78502, 78503, 78504, 78505, 78506, 78507, 78508, 78509),
        arg_types="IIIIIIIIIIIIIII",
    )
    RegisterGrace(grace_flag=1049530001, obj=1049531951, unknown=5.0)
    RunCommonEvent(0, 90005261, args=(1049530260, 1049532260, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1049530261, 1049532261, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1049530262, 1049532262, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1049530263, 1049532263, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 900005610, args=(1049531600, 100, 800, 0), arg_types="IiiI")
    Event_1049532200(0, character=1049535200)
    RunCommonEvent(0, 90005704, args=(1049530700, 3621, 3620, 1049539201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1049530700, 3621, 3622, 1049539201, 3621, 3620, 3624, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1049530700, 3623, 3620, 3624), arg_types="IIII")
    Event_1049533700(0, character=1049530700)
    Event_1049533701()
    Event_1049533702()
    Event_1049533703(0, character=1049530700)
    RunCommonEvent(0, 90005705, args=(1049530710,))
    Event_1049533705()
    Event_1049533710(0, 1049532710)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1049530700)
    DisableBackread(1049530710)


@RestartOnRest(1049532200)
def Event_1049532200(_, character: uint):
    """Event 1049532200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@RestartOnRest(1049533700)
def Event_1049533700(_, character: uint):
    """Event 1049533700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3620)
    DisableFlag(1043379255)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3631)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3631)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3620)
    GotoIfFlagEnabled(Label.L2, flag=3621)
    GotoIfFlagEnabled(Label.L3, flag=3622)
    GotoIfFlagEnabled(Label.L4, flag=3623)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90103, unknown2=1.0)
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
    IfFlagEnabled(OR_4, 3631)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1049533701)
def Event_1049533701():
    """Event 1049533701"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1049539210)
    EnableFlag(1049539210)
    SkipLinesIfFlagDisabled(2, 3621)
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3620)
    IfFlagEnabled(OR_1, 1043359259)
    IfFlagEnabled(OR_1, 1044389209)
    IfFlagEnabled(OR_1, 1035469209)
    IfFlagEnabled(OR_1, 1039529209)
    GotoIfConditionTrue(Label.L1, input_condition=OR_1)
    SkipLinesIfFlagDisabled(2, 3626)
    EnableFlag(1043359259)
    Goto(Label.L1)
    SkipLinesIfFlagDisabled(2, 3625)
    EnableFlag(1044389209)
    Goto(Label.L1)
    SkipLinesIfFlagDisabled(2, 3627)
    EnableFlag(1035469209)
    Goto(Label.L1)
    SkipLinesIfFlagDisabled(2, 3630)
    EnableFlag(1039529209)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    EnableFlag(3638)
    End()


@RestartOnRest(1049533702)
def Event_1049533702():
    """Event 1049533702"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 3623)
    IfFlagEnabled(AND_1, 3631)
    EndIfConditionTrue(input_condition=AND_1)
    IfFlagEnabled(MAIN, 3631)
    EndIfFlagDisabled(35000500)
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3623)
    SaveRequest()
    End()


@RestartOnRest(1049533703)
def Event_1049533703(_, character: uint):
    """Event 1049533703"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3623)
    IfCharacterDead(AND_1, character)
    IfFlagDisabled(AND_1, 3623)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1049539212)
    SetBackreadStateAlternate(character, True)
    IfCharacterDoesNotHaveSpecialEffect(OR_1, character, 9600)
    IfTimeElapsed(OR_1, seconds=60.0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SetBackreadStateAlternate(character, False)
    End()


@RestartOnRest(1049533705)
def Event_1049533705():
    """Event 1049533705"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(11109561)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1049532500)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(11109561)
    End()


@RestartOnRest(1049533710)
def Event_1049533710(_, flag: uint):
    """Event 1049533710"""
    EndIfPlayerNotInOwnWorld()
    DisableNetworkSync()
    DisableFlag(flag)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(flag)
    IfTryingToCreateSession(OR_2)
    IfTryingToJoinSession(OR_2)
    IfConditionFalse(MAIN, input_condition=OR_2)
    Restart()
