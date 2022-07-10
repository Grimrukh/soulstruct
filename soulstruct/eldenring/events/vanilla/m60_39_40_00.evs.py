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
    RegisterGrace(grace_flag=1039400000, obj=1039401950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76206, 76200, 1039401980, 77200, 0, 78200, 78201, 78202, 78203, 78204, 78205, 78206, 78207, 78208, 78209),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 900005610, args=(1039401680, 100, 800, 0), arg_types="IiiI")
    Event_1039400700(0, character=1039400701)
    RunCommonEvent(0, 90005702, args=(1039400701, 3383, 3380, 3383), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1039400701, 3381, 3382, 1039409201, 3381, 3380, 3383, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1039400701, 3381, 3380, 1039409201, 3), arg_types="IIIIi")
    Event_1039400701()
    RunCommonEvent(0, 90005703, args=(1039400710, 3941, 3942, 1039409251, 3941, 3940, 3943, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1039400710, 3941, 3940, 1039409251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1039400710, 3943, 3940, 3944), arg_types="IIII")
    Event_1039403710(0, character=1039400710)
    Event_1039403711(0, 1039400710)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1039400701)
    DisableBackread(1039400710)
    RunCommonEvent(0, 90005261, args=(1039400210, 1039402210, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039400211, 1039402211, 5.0, 0.5, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039400212, 1039402211, 5.0, 1.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039400213, 1039402211, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1039400220, 30001, 20001, 1039402220, 0.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )


@RestartOnRest(1039400700)
def Event_1039400700(_, character: uint):
    """Event 1039400700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3380)
    DisableFlag(1039409202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L7, flag=3387)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3387)
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
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
    IfFlagDisabled(MAIN, 3387)
    Restart()


@RestartOnRest(1039400701)
def Event_1039400701():
    """Event 1039400701"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1045349259)
    IfFlagEnabled(MAIN, 1039409206)
    EnableFlag(3418)


@RestartOnRest(1039403710)
def Event_1039403710(_, character: uint):
    """Event 1039403710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    DisableFlag(1039409250)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    IfFlagEnabled(AND_1, 3940)
    IfFlagEnabled(AND_1, 1043379353)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1043379353)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(AND_5, 3947)
    IfFlagDisabled(AND_5, 1036489213)
    IfFlagDisabled(AND_5, 1039519209)
    IfFlagDisabled(AND_5, 11109819)
    IfFlagDisabled(AND_5, 3955)
    IfFlagDisabled(AND_5, 3956)
    IfFlagDisabled(AND_5, 3957)
    GotoIfConditionTrue(Label.L5, input_condition=AND_5)
    IfFlagEnabled(AND_6, 3947)
    IfFlagDisabled(AND_6, 1036489213)
    IfFlagDisabled(AND_6, 1039519209)
    IfFlagDisabled(AND_6, 11109819)
    IfFlagDisabled(AND_6, 3955)
    IfFlagDisabled(AND_6, 3956)
    IfFlagDisabled(AND_6, 3957)
    IfConditionTrue(MAIN, input_condition=AND_6)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3940)
    GotoIfFlagEnabled(Label.L2, flag=3941)
    GotoIfFlagEnabled(Label.L3, flag=3942)
    GotoIfFlagEnabled(Label.L4, flag=3943)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(4, 3954)
    SkipLinesIfFlagEnabled(3, 1039409264)
    IfFlagEnabled(AND_6, 76200)
    IfFlagEnabled(AND_6, 9000)
    AwaitConditionTrue(AND_6)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    EnableNetworkFlag(1039409264)
    EnableNetworkFlag(3954)
    Goto(Label.L20)

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
    IfFlagEnabled(AND_15, 3947)
    IfFlagDisabled(AND_15, 1036489213)
    IfFlagDisabled(AND_15, 1039519209)
    IfFlagDisabled(AND_15, 11109819)
    IfFlagDisabled(AND_15, 3955)
    IfFlagDisabled(AND_15, 3956)
    IfFlagDisabled(AND_15, 3957)
    IfConditionFalse(MAIN, input_condition=AND_15)
    Restart()


@RestartOnRest(1039403711)
def Event_1039403711(_, entity: uint):
    """Event 1039403711"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(OR_1, 3943)
    IfFlagDisabled(OR_1, 3947)
    IfFlagEnabled(OR_1, 1039409259)
    EndIfConditionTrue(input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=entity, other_entity=20000, radius=4.0)
    IfCharacterHasSpecialEffect(AND_1, 20000, 9690)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1039402710)
    End()
