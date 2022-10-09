"""
Northwest Limgrave Coast (SE) (SE)

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_43_40_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005251(0, character=Characters.GuardianGolem, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005300(0, flag=1043400200, character=Characters.GuardianGolem, item_lot=0, seconds=0.0, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_1043402200()


@RestartOnRest(1043402200)
def Event_1043402200():
    """Event 1043402200"""
    if FlagEnabled(1043400200):
        return
    DisableHealthBar(Characters.GuardianGolem)
    AddSpecialEffect(Characters.GuardianGolem, 12189)
    Wait(3.0)
    RemoveSpecialEffect(Characters.GuardianGolem, 12189)
    EnableHealthBar(Characters.GuardianGolem)
