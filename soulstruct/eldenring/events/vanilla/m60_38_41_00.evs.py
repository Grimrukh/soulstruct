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
    RegisterGrace(grace_flag=1038410000, obj=1038411950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76206, 76202, 1038411980, 77200, 2, 78200, 78201, 78202, 78203, 78204, 78205, 78206, 78207, 78208, 78209),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005880,
        args=(1038410800, 1038410805, 1038412800, 1038410800, 30245, 60, 38, 41, 0, 1038412805),
        arg_types="IIIIiBBbbI",
    )
    RunCommonEvent(
        0,
        90005881,
        args=(1038410800, 1038410805, 1038412801, 1038412802, 20300, 1038411805, 60, 38, 41, 0, 1038412805),
        arg_types="IIIIiIBBbbI",
    )
    RunCommonEvent(
        0,
        90005882,
        args=(
            1038410800,
            1038410805,
            1038412800,
            1038410800,
            1038412806,
            1038415810,
            1038411800,
            1038410810,
            1038412810,
            900000520,
            -1,
            90005,
        ),
        arg_types="IIIIIIIIIiii",
    )
    RunCommonEvent(0, 90005883, args=(1038410800, 1038410805, 1038411805), arg_types="III")
    RunCommonEvent(0, 90005885, args=(1038410800, 0, 1038412806, 1038412807, 0, 1), arg_types="IiIIii")
    RunCommonEvent(0, 90005704, args=(1038410710, 3381, 3380, 1038419201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1038410710, 3381, 3382, 1038419201, 3381, 3380, 3384, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1038410710, 3383, 3380, 3384), arg_types="IIII")
    Event_1038413700(0, character=1038410710)
    RunCommonEvent(0, 90005706, args=(1038410720, 30018, 0), arg_types="IiI")
    RunCommonEvent(
        0,
        90005725,
        args=(4740, 4741, 4743, 1043339205, 1038410730, 1038400730, 1038416700),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005703, args=(1038410730, 4741, 4742, 1043339206, 4741, 4740, 4744, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1038410730, 4741, 4740, 1043339206, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1038410730, 4743, 4740, 4744), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1038400730, 4741, 4742, 1043339207, 4741, 4740, 4744, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1038400730, 4741, 4740, 1043339207, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005728, args=(1038400730, 1043332706, 1043332707), arg_types="III")
    RunCommonEvent(0, 90005727, args=(4741, 1038410730, 1038400730, 4740, 4743), arg_types="IIIII")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1038410700)
    DisableBackread(1038410710)
    DisableBackread(1038410720)
    DisableBackread(1038410730)
    DisableBackread(1038400730)


@RestartOnRest(1038413700)
def Event_1038413700(_, character: uint):
    """Event 1038413700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3380)
    DisableFlag(1038419202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L8, flag=3388)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3388)
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    GotoIfFlagEnabled(Label.L0, flag=3380)
    GotoIfFlagEnabled(Label.L1, flag=3381)
    GotoIfFlagEnabled(Label.L3, flag=3383)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    SetTeamType(character, TeamType.HostileNPC)
    AddSpecialEffect(character, 9628)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3388)
    Restart()


@RestartOnRest(1038413710)
def Event_1038413710(_, character: uint):
    """Event 1038413710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3680)
    DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3687)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3687)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100, unknown2=1.0)
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
    IfFlagEnabled(OR_4, 3687)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1038413711)
def Event_1038413711(_, character: uint, flag: uint, flag_1: uint):
    """Event 1038413711"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3683)
    IfFlagDisabled(AND_1, 3685)
    IfFlagDisabled(AND_1, 3686)
    IfFlagDisabled(AND_1, 3687)
    EndIfConditionTrue(input_condition=AND_1)
    GotoIfFlagDisabled(Label.L1, flag=3681)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(MAIN, 3681)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    IfCharacterHasSpecialEffect(AND_2, PLAYER, 9700)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=character, radius=5.0)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    EnableNetworkFlag(flag)
    DisableNetworkFlag(flag_1)
    DisableNetworkFlag(31002701)
    DisableNetworkFlag(31002707)
    DisableNetworkFlag(31002700)
    DisableNetworkFlag(31009205)
    SetTeamType(character, TeamType.FriendlyNPC)
    ClearTargetList(character)
    ReplanAI(character)
    End()


@RestartOnRest(1038413712)
def Event_1038413712():
    """Event 1038413712"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(31009206)
    EndIfFlagEnabled(1038419254)
    IfFlagDisabled(AND_1, 3685)
    IfFlagDisabled(AND_1, 3686)
    IfFlagDisabled(AND_1, 3687)
    EndIfConditionTrue(input_condition=AND_1)
    EnableFlag(1038419254)
    WaitFrames(frames=1)
    EnableFlag(3698)
    End()
