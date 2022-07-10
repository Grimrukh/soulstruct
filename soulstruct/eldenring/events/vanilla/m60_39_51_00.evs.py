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
    RegisterGrace(grace_flag=76303, obj=1039511950, unknown=3.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76314, 76303, 1039511980, 77300, 2, 78300, 78301, 78302, 78303, 78304, 78305, 78306, 78307, 78308, 78309),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005476, args=(1039510800, 1039510801), arg_types="II")
    Event_1039512451(0, character=1039510800, character_1=1039510801)
    RunCommonEvent(0, 90005871, args=(1039510800, 903150604, 10, 1039510801), arg_types="IiII")
    RunCommonEvent(0, 90005860, args=(1039510800, 0, 1039510800, 0, 1039510200, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005300, args=(1039510800, 1039510801, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005872, args=(1039510800, 10, 0), arg_types="III")
    RunCommonEvent(0, 90005300, args=(1039510500, 1039510500, 40304, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005703, args=(1039510700, 3941, 3942, 1039409251, 3941, 3940, 3943, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1039510700, 3941, 3940, 1039409251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1039510700, 3943, 3940, 3944), arg_types="IIII")
    Event_1039513700(0, character=1039510700)
    Event_1039513701(0, entity=1039510700)
    RunCommonEvent(0, 90005771, args=(1039510950, 1039512710), arg_types="II")
    RunCommonEvent(0, 90005771, args=(1039510950, 1039512711), arg_types="II")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1039510700)
    RunCommonEvent(0, 90005201, args=(1039510201, 30000, 20000, 12.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1039510202, 30001, 20001, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005261, args=(1039510300, 1039512300, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005201, args=(1039510406, 30001, 20001, 7.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1039510407, 30010, 20010, 18.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1039510408, 30010, 20010, 18.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005250, args=(1039510350, 1039512350, 0.0, 3003), arg_types="IIfi")
    RunCommonEvent(0, 90005201, args=(1039510363, 30000, 20000, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005250, args=(1039510361, 1039512361, 0.0, -1), arg_types="IIfi")


@RestartOnRest(1039512451)
def Event_1039512451(_, character: uint, character_1: uint):
    """Event 1039512451"""
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


@RestartOnRest(1039513700)
def Event_1039513700(_, character: uint):
    """Event 1039513700"""
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
    IfFlagDisabled(AND_5, 11109819)
    IfFlagDisabled(AND_5, 3957)
    GotoIfConditionTrue(Label.L5, input_condition=AND_5)
    IfFlagEnabled(AND_6, 3947)
    IfFlagDisabled(AND_6, 11109819)
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
    SkipLinesIfFlagEnabled(4, 3956)
    SkipLinesIfFlagEnabled(3, 1039519209)
    IfFlagEnabled(AND_6, 76303)
    IfFlagEnabled(AND_6, 9000)
    AwaitConditionTrue(AND_6)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    EnableNetworkFlag(1039519209)
    EnableNetworkFlag(3956)
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
    IfFlagDisabled(AND_15, 11109819)
    IfFlagDisabled(AND_15, 3957)
    IfConditionFalse(MAIN, input_condition=AND_15)
    Restart()


@RestartOnRest(1039513701)
def Event_1039513701(_, entity: uint):
    """Event 1039513701"""
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
