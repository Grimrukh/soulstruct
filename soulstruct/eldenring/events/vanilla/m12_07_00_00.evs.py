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
    RegisterGrace(grace_flag=71270, obj=12071950, unknown=5.0)
    RegisterGrace(grace_flag=71271, obj=12071951, unknown=5.0)
    RunCommonEvent(0, 900005610, args=(12071680, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005501,
        args=(12070525, 12071525, 4, 12071525, 1045371526, 12071527, 12070527),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(12070515, 12071515, 7, 12071515, 12071516, 12071517, 12070516),
        arg_types="IIIIIII",
    )
    Event_12070510()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(12070700)
    DisableBackread(12070701)
    Event_12070519()
    RunCommonEvent(0, 90005250, args=(12070250, 12072250, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12070251, 12072250, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12070252, 12072250, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12070253, 12072250, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12070254, 12072250, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12070255, 12072250, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12070256, 12072250, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(
        0,
        90005211,
        args=(12070271, 30001, 20001, 12072271, 2.0, 1.7999999523162842, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(12070272, 30001, 20001, 12072271, 2.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(12070273, 30001, 20001, 12072271, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(12070274, 30001, 20001, 12072271, 2.0, 1.2000000476837158, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(12070275, 30001, 20001, 12072271, 2.0, 1.399999976158142, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(12070276, 30001, 20001, 12072271, 2.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(12070300, 30001, 20001, 12072300, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(12070301, 30001, 20001, 12072300, 10.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(12070310, 30001, 20001, 12072310, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(12070311, 30001, 20001, 12072310, 10.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(12070312, 30001, 20001, 12072310, 10.0, 0.8999999761581421, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(12070313, 30001, 20001, 12072310, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(12070320, 12072300, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(12070321, 30001, 20001, 12072320, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(12070322, 30001, 20001, 12072320, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005200, args=(12070340, 30000, 20000, 12072340, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(12070341, 30000, 20000, 12072340, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(12070342, 30000, 20000, 12072340, 4.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(12070343, 30000, 20000, 12072340, 4.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005251, args=(12070345, 5.0, 0.0, 3003), arg_types="Iffi")
    RunCommonEvent(0, 90005200, args=(12070355, 30000, 20000, 12072355, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(12070356, 30000, 20000, 12072355, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(12070357, 30000, 20000, 12072355, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(12070358, 30000, 20000, 12072355, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005251, args=(12070380, 60.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005200, args=(12070385, 30000, 20000, 12072340, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(12070382, 12072382, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005300, args=(12070402, 12070402, 40652, 1.5, 0), arg_types="IIifi")
    Event_12073700(0, 12070700, 12070701)


@NeverRestart(12070510)
def Event_12070510():
    """Event 12070510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            12070525,
            12070526,
            4,
            12071525,
            1045371526,
            1045373526,
            12071527,
            12073527,
            1045372526,
            12072527,
            12070527,
            12070528,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            12070515,
            12071515,
            7,
            12071515,
            12071516,
            12073516,
            12071517,
            12073517,
            12072516,
            12072517,
            12070516,
            12072517,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(12070519)
def Event_12070519():
    """Event 12070519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(12070525)
    DisableFlag(12070515)


@RestartOnRest(12073700)
def Event_12073700(_, character: uint, character_1: uint):
    """Event 12073700"""
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)


@RestartOnRest(12073701)
def Event_12073701():
    """Event 12073701"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3503)
    IfFlagEnabled(AND_1, 3506)
    IfFlagDisabled(AND_1, 12079006)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12072700)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(12079005)
    End()


@RestartOnRest(12073702)
def Event_12073702():
    """Event 12073702"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3503)
    IfFlagEnabled(AND_1, 3506)
    IfFlagDisabled(AND_1, 12079008)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12072701)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(12079007)
    End()
