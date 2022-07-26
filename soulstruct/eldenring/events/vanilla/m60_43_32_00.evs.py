"""
West Weeping Peninsula (SE) (SE)

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
from .entities.m60_43_32_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_9005910(0, asset=1043321940, first_flag=1043320101, last_flag=1043320101, right=1)
    CommonFunc_9005911(0, asset=1043321941)
    CommonFunc_9005912(0, flag=1043320100, text=605055)
    CommonFunc_90005550(0, flag=1043320500, asset=1043321500, obj_act_id=43323500)
    Event_1043322215(0, character=Characters.Bat, region=1043322215)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(0, character=Characters.Rat0, region=1043322200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat1, region=1043322200, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=1043320202, radius=5.0, seconds=0.0, animation_id=3005)


@RestartOnRest(1043322215)
def Event_1043322215(_, character: uint, region: uint):
    """Event 1043322215"""
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    AddSpecialEffect(character, 8080)
