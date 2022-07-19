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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_41_37_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=1041378540)
    CommonFunc_90005300(0, flag=1041370200, character=Characters.Scarab, item_lot_param_id=40120, seconds=0.0, left=0)
    CommonFunc_90005300(
        0,
        flag=1041370340,
        character=Characters.GuardianGolem,
        item_lot_param_id=0,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005570(0, 60833, 91, 1041371520, 0, 1, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1041372340()
    CommonFunc_90005261(0, 1041370340, 1041372340, 5.0, 0.0, 1700)


@RestartOnRest(1041372340)
def Event_1041372340():
    """Event 1041372340"""
    if FlagEnabled(1041370340):
        return
    DisableHealthBar(Characters.GuardianGolem)
    AddSpecialEffect(Characters.GuardianGolem, 12189)
    Wait(3.0)
    RemoveSpecialEffect(Characters.GuardianGolem, 12189)
    EnableHealthBar(Characters.GuardianGolem)


@RestartOnRest(1041372670)
def Event_1041372670():
    """Event 1041372670"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1041370670):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9240, entity=Assets.AEG099_375_1001))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1041370670)
    DisplayDialog(text=90010, anchor_entity=0, display_distance=1.0, number_buttons=NumberButtons.OneButton)
