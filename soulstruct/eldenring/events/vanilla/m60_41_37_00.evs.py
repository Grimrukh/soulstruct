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
    RunCommonEvent(0, 900005610, args=(1041371680, 100, 800, 1041378540), arg_types="IiiI")
    RunCommonEvent(0, 90005300, args=(1041370200, 1041370200, 40120, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1041370340, 1041370340, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005570, args=(60833, 91, 1041371520, 0, 1, 0), arg_types="IiIiii")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1041372340()
    RunCommonEvent(0, 90005261, args=(1041370340, 1041372340, 5.0, 0.0, 1700), arg_types="IIffi")


@RestartOnRest(1041372340)
def Event_1041372340():
    """Event 1041372340"""
    EndIfFlagEnabled(1041370340)
    DisableHealthBar(1041370340)
    AddSpecialEffect(1041370340, 12189)
    Wait(3.0)
    CancelSpecialEffect(1041370340, 12189)
    EnableHealthBar(1041370340)


@RestartOnRest(1041372670)
def Event_1041372670():
    """Event 1041372670"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1041370670)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9240, entity=1041371670)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1041370670)
    DisplayDialog(text=90010, anchor_entity=0, display_distance=1.0, number_buttons=NumberButtons.OneButton)
