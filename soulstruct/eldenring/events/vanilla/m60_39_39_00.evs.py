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
    RunCommonEvent(0, 90005704, args=(1039390700, 3801, 3800, 1039399201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1039390700, 3801, 3802, 1039399201, 3801, 3800, 3803, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1039390700, 3803, 3800, 3803), arg_types="IIII")
    Event_1039393700(0, character__obj=1039390700)
    Event_1039393701()
    Event_1039393702(0, character=1039390700, obj=1039391700)
    RunCommonEvent(0, 90005300, args=(1039390200, 1039390200, 40206, 0.0, 0), arg_types="IIifi")
    Event_1039392200()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1039390700)


@RestartOnRest(1039392200)
def Event_1039392200():
    """Event 1039392200"""
    EndIfFlagEnabled(3803)
    DisableCharacter(1039390200)
    DisableAnimations(1039390200)


@RestartOnRest(1039393700)
def Event_1039393700(_, character__obj: uint):
    """Event 1039393700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3800)
    IfFlagEnabled(AND_1, 1039399203)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1039399203)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    IfFlagEnabled(OR_1, 3805)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    IfFlagEnabled(OR_2, 3805)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3800)
    GotoIfFlagEnabled(Label.L2, flag=3801)
    GotoIfFlagEnabled(Label.L4, flag=3803)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character__obj)
    EnableBackread(character__obj)
    ForceAnimation(character__obj, 90100, unknown2=1.0)
    Move(character__obj, destination=1039392700, destination_type=CoordEntityType.Region, short_move=True)
    DisableGravity(character__obj)
    EnableObjectInvulnerability(1039391700)
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
    IfFlagEnabled(OR_15, 3805)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()


@RestartOnRest(1039393701)
def Event_1039393701():
    """Event 1039393701"""
    IfFlagEnabled(AND_1, 1039399213)
    IfFlagEnabled(AND_1, 1039399218)
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    IfTrueFlagCountGreaterThanOrEqual(AND_2, FlagType.Absolute, flag_range=(120500, 120749), value=3)
    AwaitConditionTrue(AND_2)
    EnableNetworkFlag(1039399218)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1039393702)
def Event_1039393702(_, character: uint, obj: uint):
    """Event 1039393702"""
    IfFlagEnabled(AND_1, 3801)
    AwaitConditionTrue(AND_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 9624)
    IfCharacterBackreadEnabled(AND_1, character)
    IfPlayerInOwnWorld(AND_1)
    AwaitConditionTrue(AND_1)
    DisableObjectInvulnerability(obj)
    DestroyObject(obj, request_slot=0)
    EnableGravity(character)
    End()
