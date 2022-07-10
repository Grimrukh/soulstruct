"""
linked:
0
72
138
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\m60.emevd
138: N:\\GR\\data\\Param\\event\\common_func.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1036410000, obj=1036411950, unknown=5.0)
    RunCommonEvent(0, 90005570, args=(60824, 54, 1036411500, 2, 1, 0), arg_types="IiIiii")
    Event_1036413700(0, character=1036410700, character_1=1036410705)
    Event_1036413701(0, character=1036410700)
    Event_1036413702(0, character=1036410700)
    RunCommonEvent(0, 90005704, args=(1036410700, 4101, 4100, 1036419201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1036410700, 4101, 4102, 1036419201, 4101, 4100, 4104, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1036410700, 4103, 4100, 4104), arg_types="IIII")
    RunCommonEvent(0, 90005750, args=(1036411700, 4350, 104100, 400410, 400410, 1036419215, 0), arg_types="IiiIIIi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1036410700)
    DisableBackread(1036410705)


@RestartOnRest(1036413700)
def Event_1036413700(_, character: uint, character_1: uint):
    """Event 1036413700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 4100)
    DisableFlag(1036419203)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    SetTeamType(character_1, TeamType.NoTeam)
    ForceAnimation(character_1, 30020, unknown2=1.0)
    GotoIfFlagEnabled(Label.L5, flag=4105)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 4105)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    SkipLinesIfFlagDisabled(4, 1051587800)
    DisableCharacter(character)
    DisableBackread(character)
    EnableFlag(1036419215)
    Goto(Label.L20)
    GotoIfFlagEnabled(Label.L1, flag=4100)
    GotoIfFlagEnabled(Label.L2, flag=4101)
    GotoIfFlagEnabled(Label.L3, flag=4102)
    GotoIfFlagEnabled(Label.L4, flag=4103)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 30020, unknown2=1.0)
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
    IfFlagEnabled(OR_4, 4105)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1036413701)
def Event_1036413701(_, character: uint):
    """Event 1036413701"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(4100)
    EndIfFlagDisabled(4105)
    IfFlagEnabled(MAIN, 1036419209)
    DisableAnimations(character)
    Wait(30.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(1036413702)
def Event_1036413702(_, character: uint):
    """Event 1036413702"""
    EndIfFlagEnabled(4101)
    EndIfFlagEnabled(4103)
    IfCharacterHasSpecialEffect(OR_1, character, 9644)
    IfFlagEnabled(OR_1, 4101)
    IfConditionTrue(MAIN, input_condition=OR_1)
    IfCharacterHasSpecialEffect(AND_1, character, 9644)
    IfFlagDisabled(AND_1, 4101)
    EndIfConditionTrue(input_condition=AND_1)
    ForceAnimation(character, 20022, unknown2=1.0)
    End()
