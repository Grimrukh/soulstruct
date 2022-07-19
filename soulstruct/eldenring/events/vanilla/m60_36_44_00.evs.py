"""
East Liurnia (SW) (SW)

linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_36_44_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1036442203(0, character=1036440203)
    Event_1036442203(1, character=1036440204)
    Event_1036442203(2, character=1036440205)
    Event_1036442203(3, character=1036440206)
    CommonFunc_90005300(0, flag=1036440250, character=Characters.Scarab, item_lot_param_id=40202, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1036440260, character=1036440260, item_lot_param_id=1036440200, seconds=0.0, left=0)
    CommonFunc_90005920(0, flag=1036440600, asset=1036441600, obj_act_id=1036443600)
    CommonFunc_90005705(0, 1036440700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.FingerReader)
    CommonFunc_90005201(
        0,
        character=1036440210,
        animation_id=30002,
        animation_id_1=20002,
        radius=7.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, 1036440220, 1036442220, 10.0, 0.0, -1)
    CommonFunc_90005261(0, 1036440230, 1036442220, 10.0, 0.0, -1)
    CommonFunc_90005261(0, 1036440231, 1036442220, 10.0, 0.0, -1)
    CommonFunc_90005251(0, character=Characters.RayaLucariaSoldier0, radius=15.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, 1036440242, 15.0, 0.0, 0)


@RestartOnRest(1036442203)
def Event_1036442203(_, character: uint):
    """Event 1036442203"""
    Kill(character)
    End()
