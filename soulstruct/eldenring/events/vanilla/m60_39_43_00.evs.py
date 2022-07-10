"""
linked:
0
82
166

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: N:\\GR\\data\\Param\\event\\m60.emevd
232: 
234: 
236: 
238: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 90005300, args=(1039430800, 1039430341, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005476, args=(1039430340, 1039430341), arg_types="II")
    RunCommonEvent(0, 90005477)
    Event_1039432340(0, character=1039430340, character_1=1039430341)
    RunCommonEvent(0, 90005860, args=(1039430800, 0, 1039430340, 0, 1039430400, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1039430340, 10, 0), arg_types="III")
    RunCommonEvent(0, 90005871, args=(1039430340, 903150602, 10, 1039430341), arg_types="IiII")
    RunCommonEvent(0, 90005706, args=(1039430700, 930023, 0), arg_types="IiI")
    RunCommonEvent(0, 90005300, args=(1039430310, 1039430310, 40252, 0.0, 0), arg_types="IIifi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1039430700)


@RestartOnRest(1039432340)
def Event_1039432340(_, character: uint, character_1: uint):
    """Event 1039432340"""
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
