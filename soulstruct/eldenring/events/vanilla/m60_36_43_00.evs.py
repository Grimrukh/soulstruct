"""
linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1036430000, obj=1036431950, unknown=5.0)
    RegisterGrace(grace_flag=1036430001, obj=1036431951, unknown=5.0)
    Event_1036433700(0, character=1036430700, obj=1036431700)
    RunCommonEvent(0, 90005704, args=(1036430700, 4141, 4140, 1036439201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1036430700, 4141, 4142, 1036439201, 4141, 4140, 4144, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1036430700, 4143, 4140, 4144), arg_types="IIII")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1036430700)


@RestartOnRest(1036433700)
def Event_1036433700(_, character: uint, obj: uint):
    """Event 1036433700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 4140)
    DisableFlag(1036439203)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=4145)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagEnabled(OR_3, 4145)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4140)
    GotoIfFlagEnabled(Label.L2, flag=4141)
    GotoIfFlagEnabled(Label.L3, flag=4142)
    GotoIfFlagEnabled(Label.L4, flag=4143)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableObject(obj)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableObject(obj)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableObject(obj)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableObject(obj)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 4145)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()
