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
    RegisterGrace(grace_flag=1044390000, obj=1044391950, unknown=5.0)
    RunCommonEvent(0, 90005726, args=(4720, 4721, 4723, 1044399255, 1044390710, 1044396700), arg_types="IIIIII")
    RunCommonEvent(0, 90005703, args=(1044390710, 4721, 4722, 1044399256, 4721, 4720, 4724, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1044390710, 4721, 4720, 1044399256, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1044390710, 4723, 4720, 4724), arg_types="IIII")
    RunCommonEvent(0, 90005704, args=(1044390700, 4041, 4040, 1044399201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1044390700, 4041, 4042, 1044399201, 4041, 4040, 4043, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1044390700, 4043, 4040, 4043), arg_types="IIII")
    Event_1044390715(0, character=1044390700, character_1=1044390705, obj=1044391700)
    RunCommonEvent(0, 90005730, args=(1044399210, 20.0, 1044399214, 4045, 1044399213, 1044399212), arg_types="IfIIII")
    RunCommonEvent(0, 90005731, args=(1044399214, 1044390700, 10.0, 12.0), arg_types="IIff")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1044390700)
    DisableBackread(1044390705)
    DisableBackread(1044390710)
    DisableBackread(1044390711)
    RunCommonEvent(0, 90005261, args=(1044390200, 1044392200, 1.0, 1.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044390201, 1044392200, 1.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044390202, 1044392202, 1.0, 1.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044390203, 1044392202, 1.0, 1.5, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044390204, 1044392202, 1.0, 0.0, 1700), arg_types="IIffi")


@NeverRestart(1044393710)
def Event_1044393710(_, character__obj: uint):
    """Event 1044393710"""
    WaitFrames(frames=1)
    DisableFlag(1044399250)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 4000)
    IfFlagEnabled(AND_1, 1044392710)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1044392710)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=4000)
    GotoIfFlagEnabled(Label.L2, flag=4001)
    GotoIfFlagEnabled(Label.L4, flag=4003)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character__obj)
    EnableBackread(character__obj)
    ForceAnimation(character__obj, 30003, unknown2=1.0)
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
    IfFlagEnabled(MAIN, 1044399250)
    Restart()


@RestartOnRest(1044390715)
def Event_1044390715(_, character: uint, character_1: uint, obj: uint):
    """Event 1044390715"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    ForceAnimation(character_1, 90004, unknown2=1.0)
    EnableObject(obj)
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 4040)
    DisableFlag(1044399202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L5, flag=4045)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 4045)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L0, flag=4040)
    GotoIfFlagEnabled(Label.L1, flag=4041)
    GotoIfFlagEnabled(Label.L3, flag=4043)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90103, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 4045)
    Restart()
