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
    RegisterGrace(grace_flag=1036480000, obj=1036481950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76209, 76207, 1036481980, 77210, 0, 78210, 78211, 78212, 78213, 78214, 78215, 78216, 78217, 78218, 78219),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005261, args=(1036480200, 1036482200, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005300, args=(1036480800, 1036480341, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005476, args=(1036480340, 1036480341), arg_types="II")
    RunCommonEvent(0, 90005477)
    Event_1036482340(0, character=1036480340, character_1=1036480341)
    RunCommonEvent(0, 90005860, args=(1036480800, 0, 1036480340, 0, 1036480400, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1036480340, 10, 0), arg_types="III")
    RunCommonEvent(0, 90005871, args=(1036480340, 903150603, 10, 1036480341), arg_types="IiII")
    RunCommonEvent(0, 90005703, args=(1036480700, 3941, 3942, 1039409251, 3941, 3940, 3943, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1036480700, 3941, 3940, 1039409251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1036480700, 3943, 3940, 3944), arg_types="IIII")
    Event_1036483700(0, character=1036480700)
    Event_1036483701(0, entity=1036480700)
    RunCommonEvent(0, 90005705, args=(1036480710,))
    RunCommonEvent(0, 90005771, args=(1036480950, 1036482710), arg_types="II")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1036480700)
    DisableBackread(1036480710)


@RestartOnRest(1036482340)
def Event_1036482340(_, character: uint, character_1: uint):
    """Event 1036482340"""
    IfCharacterAlive(AND_1, character)
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    IfCharacterHasSpecialEffect(AND_2, character, 11825)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    IfCharacterBackreadEnabled(AND_3, character_1)
    IfConditionTrue(MAIN, input_condition=AND_3)
    AddSpecialEffect(character, 11825)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterBackreadDisabled(AND_4, character_1)
    IfConditionTrue(MAIN, input_condition=AND_4)
    AddSpecialEffect(character, 11826)
    Wait(1.0)
    Restart()


@RestartOnRest(1036483700)
def Event_1036483700(_, character: uint):
    """Event 1036483700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
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
    IfFlagDisabled(AND_5, 1039519209)
    IfFlagDisabled(AND_5, 11109819)
    IfFlagDisabled(AND_5, 3956)
    IfFlagDisabled(AND_5, 3957)
    GotoIfConditionTrue(Label.L5, input_condition=AND_5)
    IfFlagEnabled(AND_6, 3947)
    IfFlagDisabled(AND_6, 1039519209)
    IfFlagDisabled(AND_6, 11109819)
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
    SkipLinesIfFlagEnabled(4, 3955)
    SkipLinesIfFlagEnabled(3, 1036489213)
    IfFlagEnabled(AND_6, 76207)
    IfFlagEnabled(AND_6, 9000)
    AwaitConditionTrue(AND_6)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    EnableNetworkFlag(1036489213)
    EnableNetworkFlag(3955)
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
    IfFlagDisabled(AND_15, 1039519209)
    IfFlagDisabled(AND_15, 11109819)
    IfFlagDisabled(AND_15, 3956)
    IfFlagDisabled(AND_15, 3957)
    IfConditionFalse(MAIN, input_condition=AND_15)
    Restart()


@RestartOnRest(1036483701)
def Event_1036483701(_, entity: uint):
    """Event 1036483701"""
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
