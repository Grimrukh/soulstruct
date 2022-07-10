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
    RegisterGrace(grace_flag=1036490000, obj=1036491950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76209, 76208, 1036491980, 77210, 1, 78210, 78211, 78212, 78213, 78214, 78215, 78216, 78217, 78218, 78219),
        arg_types="IIIIIIIIIIIIIII",
    )
    RegisterGrace(grace_flag=1036490001, obj=1036491951, unknown=5.0)
    RunCommonEvent(0, 90005300, args=(1036490200, 1036490200, 40204, 0.0, 0), arg_types="IIifi")
    Event_1036492610()
    RunCommonEvent(0, 90005704, args=(1036490700, 3381, 3380, 1036499201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1036490700, 3381, 3382, 1036499201, 3381, 3380, 3384, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1036490700, 3383, 3380, 3384), arg_types="IIII")
    Event_1036493700(0, character=1036490700)
    RunCommonEvent(
        0,
        90005725,
        args=(4755, 4756, 4758, 1036499255, 1036490705, 1036490706, 1036496700),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005703, args=(1036490705, 4756, 4757, 1036499256, 4756, 4755, 4759, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1036490705, 4756, 4755, 1036499256, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1036490705, 4758, 4755, 4759), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1036490706, 4756, 4757, 1036499257, 4756, 4755, 4759, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1036490706, 4756, 4755, 1036499257, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005727, args=(4756, 1036490705, 1036490706, 4755, 4758), arg_types="IIIII")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1036490700)
    DisableBackread(1036490705)
    DisableBackread(1036490706)


@RestartOnRest(1036492610)
def Event_1036492610():
    """Event 1036492610"""
    IfObjectDestroyed(OR_1, 1036491620)
    IfObjectNotDestroyed(OR_2, 1036491610)
    IfObjectNotDestroyed(OR_2, 1036491610)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DestroyObject(1036491610, request_slot=0)
    DestroyObject(1036491611, request_slot=0)


@RestartOnRest(1036493700)
def Event_1036493700(_, character: uint):
    """Event 1036493700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3380)
    DisableFlag(1036499202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L11, flag=3391)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3391)
    Restart()

    # --- Label 11 --- #
    DefineLabel(11)
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
    SetTeamType(character, TeamType.HostileNPC)
    AddSpecialEffect(character, 9628)
    ForceAnimation(character, 90101, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3391)
    Restart()
