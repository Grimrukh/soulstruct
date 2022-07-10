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
    RegisterGrace(grace_flag=1048410000, obj=1048411950, unknown=5.0)
    RunCommonEvent(0, 90005300, args=(1048410290, 1048410290, 40412, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005760, args=(1048410800, 1048410800, 1048412300, 1048412708), arg_types="IIII")
    RunCommonEvent(0, 90005870, args=(1048410800, 903100603, 10), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1048410800, 0, 1048410800, 0, 1048410800, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1048410800, 10, 0), arg_types="III")
    RunCommonEvent(0, 90005702, args=(1048410700, 4793, 4790, 4793), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1048410700, 4791, 4792, 1048410702, 4791, 4790, 4793, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1048410700, 4791, 4790, 1048410702, 3), arg_types="IIIIi")
    Event_1048410700(0, character=1048410700, character_1=1048410701, obj=1048416700)
    RunCommonEvent(0, 90005770, args=(1048410701,))
    RunCommonEvent(0, 90005727, args=(4791, 1048410700, 1048410701, 4790, 4793), arg_types="IIIII")
    RunCommonEvent(0, 90005728, args=(1048410701, 1048412706, 1048412707), arg_types="III")
    RunCommonEvent(0, 90005703, args=(1048410701, 4791, 4792, 1048410702, 4791, 4790, 4793, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1048410701, 4791, 4790, 1048410702, 3), arg_types="IIIIi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1048410700)
    DisableBackread(1048410701)


@RestartOnRest(1048410700)
def Event_1048410700(_, character: uint, character_1: uint, obj: uint):
    """Event 1048410700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 4790)
    DisableFlag(1048419205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L4, flag=1048412709)
    DisableNetworkFlag(1048412708)
    IfFlagEnabled(OR_1, 1048410701)
    IfFlagEnabled(OR_1, 4791)
    IfFlagEnabled(OR_1, 4793)
    IfTimeOfDay(AND_1, earliest=(20, 0, 0), latest=(5, 30, 0))
    IfFlagDisabled(AND_1, 1048410800)
    IfConditionTrue(AND_1, input_condition=OR_1)
    GotoIfConditionFalse(Label.L4, input_condition=AND_1)
    EnableNetworkFlag(1048412708)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableNetworkFlag(1048412709)
    GotoIfFlagEnabled(Label.L0, flag=4790)
    GotoIfFlagEnabled(Label.L1, flag=4791)
    GotoIfFlagEnabled(Label.L3, flag=4793)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagDisabled(6, 1048412708)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableObject(obj)
    Goto(Label.L20)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930003, unknown2=1.0)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagDisabled(6, 1048412708)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableObject(obj)
    Goto(Label.L20)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetTeamType(character_1, TeamType.HostileNPC)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableObject(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()
