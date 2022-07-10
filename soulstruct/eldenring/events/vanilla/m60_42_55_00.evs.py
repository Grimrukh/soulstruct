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
    RunCommonEvent(0, 9005810, args=(1042550800, 1042550000, 1042550950, 1042551950, 5.0), arg_types="IIIIf")
    RunCommonEvent(0, 90005870, args=(1042550800, 903560600, 27), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1042550800, 0, 1042550800, 0, 30325, 0.0), arg_types="IIIIif")
    RunCommonEvent(
        0,
        90005780,
        args=(1042550800, 1042552160, 1042552161, 1042550705, 20, 1042552700, 1042559207, 0, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(1042550800, 1042552160, 1042552161, 1042550705), arg_types="IIII")
    RunCommonEvent(
        0,
        90005783,
        args=(1042550800, 1042552160, 1042552161, 1042550705, 1042552700, 1041542701, 1),
        arg_types="IIIIIIi",
    )
    Event_1042553710(0, character=1042550700)
    RunCommonEvent(0, 90005704, args=(1042550700, 4181, 4180, 1042559201, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005703,
        args=(1042550700, 4181, 4182, 1042559201, 1059481190, 4180, 4184, -1),
        arg_types="IIIIIIIi",
    )
    RunCommonEvent(0, 90005702, args=(1042550700, 4183, 4180, 4184), arg_types="IIII")
    Event_1042553711()
    Event_1042553712()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1042550700)
    RunCommonEvent(0, 90005251, args=(1042550800, 50.0, 0.0, 0), arg_types="Iffi")


@RestartOnRest(1042553710)
def Event_1042553710(_, character: uint):
    """Event 1042553710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 4180)
    DisableFlag(1050389253)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4188)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 4188)
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
    IfFlagDisabled(MAIN, 4188)
    Restart()


@RestartOnRest(1042553711)
def Event_1042553711():
    """Event 1042553711"""
    EndIfFlagEnabled(1042550800)
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 1042552160)
    IfFlagEnabled(AND_1, 1042550800)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1042559204)
    End()


@RestartOnRest(1042553712)
def Event_1042553712():
    """Event 1042553712"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagRangeAllDisabled(flag_range=(1042559207, 1042559209))
    IfFlagRangeAnyEnabled(AND_1, flag_range=(4181, 4183))
    AwaitConditionTrue(AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1042559207, 1042559209))
    End()
