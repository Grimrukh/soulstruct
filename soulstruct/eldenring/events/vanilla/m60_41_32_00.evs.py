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
    RegisterGrace(grace_flag=1041320000, obj=1041321950, unknown=5.0)
    RunCommonEvent(0, 90005724, args=(1041320290, 1041320290, 70000, 0.0, 1, 1041325291), arg_types="IIifiI")
    RunCommonEvent(0, 90005722, args=(1041320290, 1041320291), arg_types="II")
    RunCommonEvent(0, 90005720, args=(1041320290, 1041320292, 10961, 181), arg_types="IIii")
    RunCommonEvent(0, 90005720, args=(1041320290, 1041320293, 10961, 182), arg_types="IIii")
    RunCommonEvent(0, 90005721, args=(1041320290, 1041320292), arg_types="II")
    RunCommonEvent(0, 90005721, args=(1041320290, 1041320293), arg_types="II")
    RunCommonEvent(0, 90005723, args=(1041320290,))
    RunCommonEvent(0, 90005920, args=(1041320900, 1041321900, 1041323900), arg_types="III")
    RunCommonEvent(0, 90005261, args=(1041329200, 1041322200, 5.0, 0.0, 1701), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1041329201, 1041322200, 5.0, 2.0, 1701), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1041329202, 1041322200, 5.0, 1.0, 1702), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1041329203, 1041322200, 5.0, 0.0, 1701), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1041329204, 1041322200, 5.0, 2.0, 1702), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1041329205, 1041322200, 5.0, 1.0, 1702), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1041329206, 1041322200, 5.0, 0.0, 1701), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005725,
        args=(4745, 4746, 4748, 1041329205, 1041320700, 1041320701, 1041326700),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005703, args=(1041320700, 4746, 4747, 1041329206, 4746, 4745, 4749, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1041320700, 4746, 4745, 1041329206, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1041320700, 4748, 4745, 4749), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1041320701, 4746, 4747, 1041329207, 4746, 4745, 4749, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1041320701, 4746, 4745, 1041329207, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005728, args=(1041320701, 1041322706, 1041322707), arg_types="III")
    RunCommonEvent(0, 90005727, args=(4746, 1041320700, 1041320701, 4745, 4748), arg_types="IIIII")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1041320700)
    DisableBackread(1041320701)


@RestartOnRest(1041320300)
def Event_1041320300():
    """Event 1041320300"""
    DropMandatoryTreasure(1041320360)
    IfPlayerInOwnWorld(AND_1)
    IfFlagDisabled(AND_1, 1041320321)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1041322350)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1041322320)


@RestartOnRest(1041320301)
def Event_1041320301():
    """Event 1041320301"""
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 1041322320)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=1041322350)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableCharacter(1041320350)
    DisableAnimations(1041320350)
    EnableFlag(1041320321)
    DisableFlag(1041322320)
