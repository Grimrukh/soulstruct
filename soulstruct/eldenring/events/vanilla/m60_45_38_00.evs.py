"""
linked:
0
72
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 90005704, args=(1045380700, 3581, 3580, 1045389201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1045380700, 3581, 3582, 1045389201, 3581, 3580, 3583, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1045380700, 3583, 3580, 3583), arg_types="IIII")
    Event_1045383700(0, 1045380700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1045380700)


@RestartOnRest(1045382390)
def Event_1045382390():
    """Event 1045382390"""
    DisableObject(1045381390)


@RestartOnRest(1045383700)
def Event_1045383700(_, character__obj: uint):
    """Event 1045383700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3580)
    IfFlagEnabled(AND_1, 1045389203)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1045389203)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    IfFlagEnabled(OR_1, 3585)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    IfFlagEnabled(OR_2, 3585)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3580)
    GotoIfFlagEnabled(Label.L2, flag=3581)
    GotoIfFlagEnabled(Label.L4, flag=3583)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character__obj)
    EnableBackread(character__obj)
    ForceAnimation(character__obj, 90100, unknown2=1.0)
    SetCharacterTalkRange(character=character__obj, distance=100.0)
    SkipLinesIfFlagDisabled(1, 1045389205)
    ForceAnimation(character__obj, 90101, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character__obj)
    EnableBackread(character__obj)
    SetTeamType(character__obj, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character__obj)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    DisableObject(character__obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_15, 3585)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()
