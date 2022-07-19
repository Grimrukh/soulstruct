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
from .entities.m60_51_39_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1051390000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005683(0, flag=62412, asset=Assets.AEG099_055_1000, vfx_id=209, flag_1=78494, flag_2=78494)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005250(0, 1051390204, 1051392204, 0.0, -1)
    CommonFunc_90005250(0, 1051390250, 1051392280, 0.0, -1)
    CommonFunc_90005250(0, 1051390251, 1051392251, 0.0, -1)
    CommonFunc_90005250(0, 1051390280, 1051392280, 0.0, -1)
    CommonFunc_90005250(0, 1051390400, 1051392400, 0.0, -1)
    CommonFunc_90005250(0, 1051390402, 1051392400, 0.0, -1)
    CommonFunc_90005250(0, 1051390431, 1051392401, 0.0, -1)
    CommonFunc_90005250(0, 1051390432, 1051392401, 0.0, -1)
    CommonFunc_90005250(0, 1051390433, 1051392401, 0.0, -1)
    CommonFunc_90005250(0, 1051390434, 1051392401, 0.0, -1)
    CommonFunc_90005250(0, 1051390435, 1051392401, 0.0, -1)
    CommonFunc_90005250(0, 1051390436, 1051392401, 0.0, -1)
    CommonFunc_90005250(0, 1051390437, 1051392401, 0.0, -1)
    CommonFunc_90005250(0, 1051390438, 1051392401, 0.0, -1)
    Event_1051392200(0, character=Characters.RadahnSoldier0)
    Event_1051392200(1, character=Characters.RadahnSoldier1)
    Event_1051392200(2, character=Characters.RadahnSoldier2)
    Event_1051392200(3, character=Characters.RadahnSoldier3)
    Event_1051392200(4, character=Characters.RadahnSoldier4)
    Event_1051392200(5, character=Characters.RadahnSoldier5)
    Event_1051392200(6, character=Characters.RadahnSoldier6)
    Event_1051392200(7, character=Characters.RadahnSoldier7)
    Event_1051392200(8, character=Characters.RadahnSoldier8)
    Event_1051392200(9, character=Characters.RadahnSoldier9)
    Event_1051392580(0, start_climbing_flag=1051390580, stop_climbing_flag=1051390851, asset=Assets.AEG030_001_2000)
    Event_1051392580(1, start_climbing_flag=1051390582, stop_climbing_flag=1051390853, asset=Assets.AEG030_608_2100)
    Event_1051392580(2, 1051390584, 1051390855, 1051391584)


@RestartOnRest(1051392200)
def Event_1051392200(_, character: uint):
    """Event 1051392200"""
    AddSpecialEffect(character, 8081)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    RemoveSpecialEffect(character, 8081)


@NeverRestart(1051392580)
def Event_1051392580(_, start_climbing_flag: uint, stop_climbing_flag: uint, asset: uint):
    """Event 1051392580"""
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, asset=asset)
