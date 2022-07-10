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
    RegisterGrace(grace_flag=76311, obj=1043531950, unknown=5.0)
    RegisterGrace(grace_flag=76312, obj=1043531951, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76314, 76312, 1043531981, 77300, 4, 78300, 78301, 78302, 78303, 78304, 78305, 78306, 78307, 78308, 78309),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005300, args=(1043530500, 1043530500, 40318, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(
        0,
        90005211,
        args=(1043530354, 30005, 20021, 1043532350, 3.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1043530355, 30005, 20021, 1043532350, 3.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1043530350, 30000, 20000, 1043532350, 3.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005870, args=(1043530800, 903100602, 10), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1043530800, 0, 1043530800, 0, 1043530400, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005760, args=(1043530800, 1043530800, 1043532400, 1043532708), arg_types="IIII")
    RunCommonEvent(0, 90005872, args=(1043530800, 10, 0), arg_types="III")
    RunCommonEvent(0, 90005702, args=(1043530700, 4763, 4760, 4763), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1043530700, 4761, 4762, 1043530702, 4761, 4760, 4763, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1043530700, 4761, 4760, 1043530702, 3), arg_types="IIIIi")
    Event_1043530700(0, character=1043530700, character_1=1043530701, obj=1043536700)
    RunCommonEvent(0, 90005770, args=(1043530701,))
    RunCommonEvent(0, 90005727, args=(4761, 1043530700, 1043530701, 4760, 4763), arg_types="IIIII")
    RunCommonEvent(0, 90005728, args=(1043530701, 1043532706, 1043532707), arg_types="III")
    RunCommonEvent(0, 90005703, args=(1043530701, 4761, 4762, 1043530702, 4761, 4760, 4763, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1043530701, 4761, 4760, 1043530702, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005771, args=(1043530951, 1043532710), arg_types="II")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1043530700)
    DisableBackread(1043530701)
    RunCommonEvent(
        0,
        90005211,
        args=(1043530202, 30016, 20016, 1043532203, 3.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005200, args=(1043530203, 30016, 20016, 1043532203, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1043530204, 30016, 20016, 1043532204, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1043530206, 30014, 20014, 1043532206, 8.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1043530207, 30014, 20014, 1043532206, 8.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005200, args=(1043530208, 30014, 20014, 1043532208, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(1043530218, 30014, 20014, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1043530219, 30014, 20014, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1043530221, 30014, 20014, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1043530222, 30014, 20014, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1043530228, 30014, 20014, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1043530229, 30014, 20014, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1043530209, 30014, 20014, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1043530210, 30014, 20014, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1043530211, 30014, 20014, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1043530214, 30014, 20014, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1043530215, 30014, 20014, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1043530216, 30014, 20014, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(1043530230, 30014, 20014, 1043532230, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1043530212, 30016, 20016, 1043532212, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")


@RestartOnRest(1043530700)
def Event_1043530700(_, character: uint, character_1: uint, obj: uint):
    """Event 1043530700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 4760)
    DisableFlag(1043539205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L4, flag=1043532709)
    DisableNetworkFlag(1043532708)
    IfFlagEnabled(OR_1, 1043530701)
    IfFlagEnabled(OR_1, 4761)
    IfFlagEnabled(OR_1, 4763)
    IfTimeOfDay(AND_1, earliest=(20, 0, 0), latest=(5, 30, 0))
    IfFlagDisabled(AND_1, 1043530800)
    IfConditionTrue(AND_1, input_condition=OR_1)
    GotoIfConditionFalse(Label.L4, input_condition=AND_1)
    EnableNetworkFlag(1043532708)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableNetworkFlag(1043532709)
    GotoIfFlagEnabled(Label.L0, flag=4760)
    GotoIfFlagEnabled(Label.L1, flag=4761)
    GotoIfFlagEnabled(Label.L3, flag=4763)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagDisabled(6, 1043532708)
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
    SkipLinesIfFlagDisabled(6, 1043532708)
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
